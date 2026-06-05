# Financial Formulas for Simplified Business Case

To maintain simplicity, this business case ignores Working Capital changes ($\Delta$NWC), Depreciation (and consequently Amortization), and Interest Rates. All capital investments are treated as immediate cash outflows. 

Strictly use the following definitions for all calculations.

## 1. Market & Revenue
For each Year $t$ (from 0 to 5):
*   **Active Users ($U_t$)**: $TAM \times AdoptionRate_t$ (Note: $U_0 = 0$)
*   **Revenue ($R_t$)**: $U_t \times V_P$

## 2. Cost Aggregation
Calculate costs based on the elicited fixed and variable positions:

**CAPEX ($C_t$)**: Usually occurs in Year 0, but may have entries in other years.
*   $C_t = SoftwareDev_t + HardwareEng_t + Integration_t$

**OPEX ($O_t$)**: Calculated yearly based on fixed costs and active users.
*   $FixedOPEX_t = Maintenance_t + SalesMarketing_t + Overhead_t$
*   $VariableOPEX\_PerUser = CloudCost + ConnectivityCost + HardwareUnitCost + SupportCost$
*   $VariableOPEX_t = U_t \times VariableOPEX\_PerUser$
*   $O_t = FixedOPEX_t + VariableOPEX_t$

## 3. Simplified Free Cash Flow to Firm (FCFF)
Since we ignore depreciation and interest:
*   **EBIT ($E_t$)**: $R_t - O_t$
*   **Taxes ($Tax_t$)**: If $E_t > 0$, then $Tax_t = E_t \times TaxRate$. If $E_t \le 0$, then $Tax_t = 0$ (ignoring tax loss carryforwards for simplicity).
*   **Simplified FCFF ($FCFF_t$)**: $E_t - Tax_t - C_t$

## 4. Key Performance Indicators (KPIs)

### Net Present Value (NPV)
Discount the FCFF using the WACC ($r$):
$NPV = \sum_{t=0}^{5} \frac{FCFF_t}{(1 + r)^t}$

### Internal Rate of Return (IRR)
The rate $r^*$ at which $NPV = 0$. (Calculate programmatically/iteratively; if FCFF is never positive, state "N/A").

### Payback Period (in Months)
Identify the exact point where Cumulative FCFF turns positive.
Let Year $Y$ be the last year with a negative Cumulative FCFF.
Let $Abs(CumFCFF_Y)$ be the absolute value of the cumulative deficit at the end of Year $Y$.
Let $FCFF_{Y+1}$ be the cash flow in the year the project turns positive.

$Payback\_Years = Y + \frac{Abs(CumFCFF_Y)}{FCFF_{Y+1}}$
**Payback in Months** = $Payback\_Years \times 12$

## 5. Sensitivity Analysis Rules
Calculate two alternative scenarios by adjusting the Base Case inputs:
*   **Best Case**: Increase $AdoptionRate_t$ by 20% (multiply by 1.2). Decrease $C_t$, $FixedOPEX_t$, and $VariableOPEX\_PerUser$ by 20% (multiply by 0.8).
*   **Worst Case**: Decrease $AdoptionRate_t$ by 20% (multiply by 0.8). Increase $C_t$, $FixedOPEX_t$, and $VariableOPEX\_PerUser$ by 20% (multiply by 1.2).
Recalculate NPV, IRR, and Payback Period for both.