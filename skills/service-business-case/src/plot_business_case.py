
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from typing import Dict, List, Any

# ==============================================================================
# --- USER INPUT CONFIGURATION ---
# Please adjust the values below based on the user's input during the SKILL.md
# interaction. This dictionary serves as the direct data input for the analysis.
# ==============================================================================

FINANCIAL_DATA_INPUT = {
    "service_name": "Example Smart Service",  # Default or user-provided name
    "target_price": 100.0,  # Value-based price per unit/customer/year
    "tam": 100000,          # Total Addressable Market (potential customers/units)
    "adoption_curve": [2.0, 5.0, 10.0, 15.0, 20.0], # Adoption rate (%) for Years 1-5
    "capex_costs": {
        "Software & Platform Development": 50000.0,
        "Hardware Engineering": 10000.0,
        "IT Integration & Setup": 5000.0,
    },
    "fixed_opex_costs": {
        # Annual costs for Years 0-5
        "R&D & Platform Maintenance": [10000.0, 12000.0, 13000.0, 14000.0, 15000.0, 16000.0],
        "Sales & Marketing": [5000.0, 6000.0, 7000.0, 8000.0, 9000.0, 10000.0],
        "Overhead & Admin": [15000.0, 16000.0, 17000.0, 18000.0, 19000.0, 20000.0],
    },
    "variable_opex_per_user": {
        "Cloud Hosting & Data Storage": 5.0,
        "Connectivity": 2.0,
        "Hardware / Consumables": 10.0, # Per unit cost, if any
        "Customer Support": 3.0,
    },
    "tax_rate": 0.25,        # Corporate tax rate (e.g., 0.25 for 25%)
    "discount_rate_wacc": 0.12 # Discount rate / WACC (e.g., 0.12 for 12%)
}

# ==============================================================================
# --- FINANCIAL MODELING FUNCTIONS ---
# These functions implement the logic from assets/financial_formulas.md
# ==============================================================================

def calculate_simplified_fcff(df_financials, tax_rate, discount_rate_wacc):
    """Calculates Simplified FCFF, NPV, IRR, and Payback Period."""
    
    # --- Core Metrics ---
    df_financials['Active Users'] = df_financials['Year'].apply(lambda y: 0 if y == 0 else int(FINANCIAL_DATA_INPUT['tam'] * (FINANCIAL_DATA_INPUT['adoption_curve'][y-1] / 100)))
    df_financials['Revenue'] = df_financials['Active Users'] * FINANCIAL_DATA_INPUT['target_price']
    
    df_financials['Fixed OPEX'] = df_financials['Year'].apply(lambda y: FINANCIAL_DATA_INPUT['fixed_opex_costs'][key][y] for key in FINANCIAL_DATA_INPUT['fixed_opex_costs'])
    df_financials['Variable OPEX'] = df_financials['Active Users'] * sum(FINANCIAL_DATA_INPUT['variable_opex_per_user'][key] for key in FINANCIAL_DATA_INPUT['variable_opex_per_user'])
    df_financials['Total OPEX'] = df_financials['Fixed OPEX'] + df_financials['Variable OPEX']
    
    df_financials['CAPEX'] = df_financials['Year'].apply(lambda y: sum(FINANCIAL_DATA_INPUT['capex_costs'][key] for key in FINANCIAL_DATA_INPUT['capex_costs']) if y == 0 else 0)
    
    # --- Simplified FCFF Calculation ---
    df_financials['EBIT'] = df_financials['Revenue'] - df_financials['Total OPEX']
    df_financials['Taxes'] = df_financials['EBIT'].apply(lambda x: max(0, x * tax_rate)) # No negative taxes
    df_financials['FCFF'] = df_financials['EBIT'] - df_financials['Taxes'] - df_financials['CAPEX']
    
    df_financials['Cumulative FCFF'] = df_financials['FCFF'].cumsum()

    # --- KPI Calculations ---
    # NPV
    df_financials['Discount Factor'] = (1 + discount_rate_wacc)**(-df_financials['Year'])
    df_financials['Discounted FCFF'] = df_financials['FCFF'] * df_financials['Discount Factor']
    npv = df_financials['Discounted FCFF'].sum()

    # IRR
    # Requires FCFF values, use numpy's irr for non-annual cash flows if needed,
    # but for annual cash flows, direct calculation or numpy's irr is fine.
    # We use a simple list of FCFFs for numpy.irr
    fcff_values = df_financials['FCFF'].tolist()
    if all(x <= 0 for x in fcff_values[1:]) and fcff_values[0] < 0: # Check if IRR is possible
        irr = np.nan 
    else:
        # Use a common approximation for IRR calculation
        try:
            irr = np.irr(fcff_values) * 100 # IRR is annual percentage
        except Exception: # Catch cases where IRR might not be calculable (e.g. all zeros)
            irr = np.nan 

    # Payback Period (in Months)
    payback_months = np.nan
    if npv >= 0: # Only calculate if NPV is non-negative
        for i in range(len(df_financials) - 1):
            if df_financials['Cumulative FCFF'].iloc[i] < 0 and df_financials['Cumulative FCFF'].iloc[i+1] >= 0:
                # Linear interpolation
                cum_fcff_prev = df_financials['Cumulative FCFF'].iloc[i]
                cum_fcff_curr = df_financials['Cumulative FCFF'].iloc[i+1]
                fcff_next_year = df_financials['FCFF'].iloc[i+1]
                
                if fcff_next_year > 0: # Ensure we are not dividing by zero or negative
                    fraction_of_year = abs(cum_fcff_prev) / fcff_next_year
                    payback_years = (i + 1) + fraction_of_year # i+1 because index i is year 0, i+1 is year 1
                    payback_months = payback_years * 12
                    break
    
    return npv, irr, payback_months

# ==============================================================================
# --- CHART GENERATION ---
# ==============================================================================

def generate_charts(data_input=FINANCIAL_DATA_INPUT, output_path="business_case_charts.png"):
    """Generates financial charts based on the provided data."""
    
    # Create DataFrame from input data
    years = np.arange(6) # Years 0 to 5
    df_financials = pd.DataFrame({'Year': years})
    
    # Calculate core metrics and KPIs
    npv, irr, payback_months = calculate_simplified_fcff(df_financials, data_input['tax_rate'], data_input['discount_rate_wacc'])
    
    # --- Prepare Data for Chart 2 ---
    # Ensure costs are plotted correctly relative to Revenue and EBIT
    # EBIT is already calculated, so we plot Revenue and then stack costs below EBIT
    
    # --- Chart 1: Cumulative FCFF & Payback Period ---
    fig, axes = plt.subplots(2, 1, figsize=(12, 12))
    ax1 = axes[0]
    
    ax1.plot(df_financials['Year'], df_financials['Cumulative FCFF'], marker='o', markersize=8, linestyle='-', color='#1f77b4', linewidth=2.5, label='Cumulative FCFF')
    ax1.axhline(0, color='#d62728', linestyle='--', linewidth=1.5, alpha=0.8)
    
    # Highlight Payback Period (Zero Crossing)
    if not np.isnan(payback_months):
        # Find the year index where payback occurs
        for i in range(len(df_financials) - 1):
            if df_financials['Cumulative FCFF'].iloc[i] < 0 and df_financials['Cumulative FCFF'].iloc[i+1] >= 0:
                payback_year_float = i + 1 + (abs(df_financials['Cumulative FCFF'].iloc[i]) / df_financials['FCFF'].iloc[i+1])
                ax1.plot(payback_year_float, 0, marker='X', color='#d62728', markersize=12, label=f'Payback ({payback_months:.0f} Months)')
                ax1.annotate(f'Payback: ~{payback_months:.0f} Months', 
                             xy=(payback_year_float, 0), 
                             xytext=(payback_year_float - 0.7, ax1.get_ylim()[1] * 0.5), # Adjust text position dynamically
                             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
                             fontsize=11, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1))
                break
    else:
        ax1.annotate('Payback not reached in projection', 
                     xy=(df_financials['Year'].iloc[-1], df_financials['Cumulative FCFF'].iloc[-1]), 
                     xytext=(df_financials['Year'].iloc[-1]-1.5, ax1.get_ylim()[1] * 0.5),
                     fontsize=11, color='red', fontweight='bold')

    ax1.set_title('Cumulative Free Cash Flow to Firm (FCFF) & Payback Period', fontsize=14, fontweight='bold', pad=15)
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Amount ($)', fontsize=12)
    ax1.set_xticks(years) # Ensure ticks are at integer years
    ax1.legend(loc='upper left')

    # --- Chart 2: Financial Breakdown ---
    ax2 = axes[1]
    width = 0.5 # Width of the bars

    revenue_val = df_financials['Revenue'].values
    # Ensure costs are positive for plotting, and EBIT is plotted separately
    fixed_opex_val = df_financials['Fixed OPEX'].values
    var_opex_val = df_financials['Variable OPEX'].values
    capex_val = df_financials['CAPEX'].values
    taxes_val = df_financials['Taxes'].values
    ebit_val = df_financials['EBIT'].values

    # Base for stacking: CAPEX first (Year 0 only, else 0)
    stack_base_capex = np.where(years == 0, capex_val, 0)
    
    # Plot Revenue bar (upwards)
    ax2.bar(years, revenue_val, width, label='Revenue', color='#2ca02c')
    
    # Stack costs downwards from Revenue, starting with CAPEX
    ax2.bar(years, stack_base_capex, width, label='CAPEX', color='#d62728', bottom=revenue_val)
    ax2.bar(years, fixed_opex_val, width, label='Fixed OPEX', color='#ff7f0e', bottom=revenue_val + stack_base_capex)
    ax2.bar(years, var_opex_val, width, label='Variable OPEX', color='#ffbb78', bottom=revenue_val + stack_base_capex + fixed_opex_val)
    ax2.bar(years, taxes_val, width, label='Taxes', color='#9467bd', bottom=revenue_val + stack_base_capex + fixed_opex_val + var_opex_val)

    # Overlay EBIT line
    ax2.plot(years, ebit_val, marker='D', markersize=8, color='black', label='EBIT', linewidth=2, linestyle=':')

    ax2.axhline(0, color='black', linewidth=1.2)
    ax2.set_title('Financial Breakdown: Revenue vs. Cost Structure', fontsize=14, fontweight='bold', pad=15)
    ax2.set_xlabel('Year', fontsize=12)
    ax2.set_ylabel('Amount ($)', fontsize=12)
    ax2.set_xticks(years) # Ensure ticks are at integer years
    
    # Adjust legend position to prevent overlap
    ax2.legend(loc='upper left', bbox_to_anchor=(-0.1, 1.15), title="Legend", title_fontsize='11', fontsize='10')

    # Layout adjustment and save
    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to make room for the title and legend
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Success: Business case charts saved to '{output_path}'")


if __name__ == "__main__":
    # This block is for direct execution and testing.
    # In an agentic workflow, the agent would populate 'financial_data'
    # and then call generate_charts(data_input=populated_data)
    
    # Example of how the agent would populate data (this part is normally handled by SKILL.md logic)
    # For demonstration, we use the default FINANCIAL_DATA_INPUT here
    print("Running chart generation with example data...")
    generate_charts(data_input=FINANCIAL_DATA_INPUT, output_path="business_case_charts.png")
    print("Example data run complete.")