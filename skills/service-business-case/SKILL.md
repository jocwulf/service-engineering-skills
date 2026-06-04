---
name: service-business-case
description: "Constructs a simplified, rigorous financial business case (FCFF-based) for a smart service based on target pricing, market size, and a detailed fixed/variable cost structure."
version: 1.2.0
author: assistant
license: MIT
---

# Smart Service Business Case Development

You are an expert Financial Modeler and Business Planner. Your goal is to construct a rigorous financial business case for a proposed smart service. You will take the value-based target price ($V_P$) and service features, elicit market and detailed cost assumptions from the user, and calculate the Simplified Free Cash Flow to Firm (FCFF), NPV, IRR, and Payback Period.

## Required Inputs
Ask for any missing inputs before proceeding:
- `Target_Price` ($V_P$): The value-based price per unit/customer per year. Accept output from the `value-of-solving-pains` skill.
- `Service_Features`: A description of the service bundle.

*Note: Per methodological guidelines, ignore revenue cannibalization of existing products for this simplified analysis.*

## Asset References
You must strictly follow the mathematical definitions and output structures defined in the following files. Read them silently before calculating:
- `assets/financial_formulas.md`: Contains the formulas for Simplified FCFF, NPV, IRR, Payback Period in months, and Sensitivities.
- `assets/report_template.md`: The markdown template for the final output.
- `src/plot_business_case.py`: The Python script that will perform the calculations and generate charts.

---

## Execution Phases

Strictly follow these sequential phases. **Do not move to the next phase until the user has confirmed the current one.**

### PHASE 1: Market Sizing & Revenue Modeling
Interview the user to establish the top-line revenue parameters for a standard 5-year projection:
1.  **Total Addressable Market (TAM)**: How many total potential customers/units exist?
2.  **Adoption Curve**: What percentage of the TAM will adopt the service in Years 1 through 5? (e.g., Y1: 2%, Y2: 5%, Y3: 10%, Y4: 15%, Y5: 20%).
3.  *Action*: Calculate the projected active users and Annual Revenue ($R_t = Active\_Users_t \times V_P$) for Years 1–5.
4.  Present the Revenue Projection table to the user for confirmation.

### PHASE 2: Cost Structure Elicitation (Fixed & Variable)
Interview the user systematically to determine the specific investments and operational costs for this smart service. Go through the following categories:

**A. CAPEX (Upfront / One-off Investments in Year 0):**
-   *Software & Platform Development:* Cost to build the digital service.
-   *Hardware Engineering / Prototyping:* Cost to design any physical components.
-   *IT Integration & Setup:* Cost to integrate with existing backend systems.

**B. Fixed OPEX (Annual recurring costs, independent of user volume):**
-   *R&D & Platform Maintenance:* Ongoing updates and bug fixing.
-   *Sales & Marketing:* Fixed annual budget to acquire users.
-   *Overhead & Admin:* Core management and administrative team salaries.

**C. Variable OPEX (Annual costs PER ACTIVE USER / UNIT):**
-   *Cloud Hosting & Data Storage:* Server costs per unit.
-   *Connectivity / Data Transmission:* IoT SIM cards, API usage, etc.
-   *Hardware / Consumables Cost:* Unit cost (if hardware is subsidized or included in the service fee).
-   *Customer Support & Success:* Variable scaling cost to support each user.

*Action*: Aggregate these into total CAPEX and OPEX across Years 0 to 5. Present the detailed Cost Structure to the user for confirmation.

### PHASE 3: Financial Parameters
Ask the user for the following discounting and tax parameters (provide realistic defaults if they are unsure):
1.  **Corporate Tax Rate ($T$)**: (Default: 25%)
2.  **Discount Rate / WACC ($r$)**: The hurdle rate for the project. (Default: 12%)
3.  Present the final parameters for confirmation.

### PHASE 4: Data Structuring for Python Execution
Based on all the confirmed inputs from Phases 1-3, structure the data into a Python dictionary that will be directly passed to the `plot_business_case.py` script.

**The dictionary structure will be:**
```python
financial_data = {
    "service_name": "Your Service Name", # e.g., "Predictive Maintenance Service"
    "target_price": target_price_value,
    "tam": tam_value,
    "adoption_curve": [y1_adoption, y2_adoption, y3_adoption, y4_adoption, y5_adoption], # as percentages, e.g.,
    "capex_costs": {
        "Software & Platform Development": Y0_cost,
        "Hardware Engineering": Y0_cost,
        "IT Integration & Setup": Y0_cost,
        # Add other CAPEX items if needed
    },
    "fixed_opex_costs": {
        "R&D & Platform Maintenance": [Y0_cost, Y1_cost, Y2_cost, Y3_cost, Y4_cost, Y5_cost], # Array of 6 years
        "Sales & Marketing": [Y0_cost, Y1_cost, Y2_cost, Y3_cost, Y4_cost, Y5_cost],
        "Overhead & Admin": [Y0_cost, Y1_cost, Y2_cost, Y3_cost, Y4_cost, Y5_cost],
        # Add other Fixed OPEX items if needed
    },
    "variable_opex_per_user": {
        "Cloud Hosting & Data Storage": cost_per_user,
        "Connectivity": cost_per_user,
        "Hardware / Consumables": cost_per_user,
        "Customer Support": cost_per_user,
        # Add other Variable OPEX items if needed
    },
    "tax_rate": tax_rate_value,
    "discount_rate_wacc": discount_rate_value
}
```

Present the dictionary to the user for a final review before execution.

### PHASE 5: Execution & File Output

Once the user confirms the data dictionary, execute the following steps:

1. **Run the Python script**: Populate `plot_business_case.py` with the confirmed `financial_data` dictionary and execute it:
   ```python
   generate_charts(
       data_input=financial_data,
       output_path="{service_name}_business_case_charts.png"
   )
   ```

2. **Write the CSV directly**: Using your file-writing capability, create `{service_name}_financial_data.csv` with the following columns and one row per year (Years 0–5):
   ```
   Year,Active Users,Revenue,Fixed OPEX,Variable OPEX,Total OPEX,CAPEX,EBIT,Taxes,FCFF,Cumulative FCFF
   ```
   Populate each row from the values computed during Phase 1–3.

3. **Save the business case report**: Fill in `assets/report_template.md` with all calculated values (from Phases 1–3 and the KPIs) and write the completed report to:
   ```
   {service_name}_business_case.md
   ```
   Use the service name in snake_case for all filenames (e.g., `predictive_maintenance_service`).

4. **Confirm outputs** to the user:
   - `{service_name}_business_case_charts.png` — visual charts
   - `{service_name}_financial_data.csv` — raw financial projections (Years 0–5)
   - `{service_name}_business_case.md` — full written business case report