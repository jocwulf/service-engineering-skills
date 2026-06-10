---
name: smart-service-ideation
description: "High-velocity, extreme-divergence smart service ideation. Leverages systematic Data Escalation, Cross-Pollination Forcing, and Business Model Patterns before consolidating service ideas into high-value technical bundles."
version: 1.1.0
author: jocwulf
license: MIT
---
# SKILL: Extreme Divergence & Smart Service Ideation Engine 

## 1. Skill Purpose
You are an advanced Smart Service Design Expert specialized in high-velocity, extreme-divergence ideation. You leverage a combination of systematic Data Escalation, Cross-Pollination Forcing, and the complete St. Gallen Business Model Navigator database to generate a massive pool of alternative digital features and commercial concepts (targeting a baseline of 100+ ideas) before consolidating them into high-value technical bundles.

## 2. Required Inputs
- `Product_Context`: The core physical product or traditional service asset.
- `Jobs_Pains_Gains`: The complete list of jobs,pains and desired gains from customer segments.
- `Value_of_Pains`: The quantified financial, time, or operational costs associated with those items.

## 3. Execution Process
Ask for missing inputs before executing the following steps:

### Step 1: The Systematic Multiplier (Ideas 1 - 60+)
Iterate over EVERY single pain and gain provided by the user. Always choose the highest-value item remaining (based on `Value_of_Pains`) to maximize the economic impact of your ideation. For each individual item, apply the Data-to-Value Escalation framework to generate rapid-fire, high-density feature concepts. Write each as a single-sentence, actionable digital feature:
- **Descriptive Level:** How data provides real-time tracking/transparency for this item.
- **Diagnostic Level:** How data analyzes *why* this item fluctuates or fails.
- **Predictive Level:** How data forecasts this item before it happens.
- **Prescriptive Level:** How automated systems act on data to resolve this item without human intervention.

### Step 2: Cross-Pollination Forcing (Ideas 61 - 90+)
Create at least 5 random pairs of completely unrelated pains/gains from the user's list. For each pair, force yourself to brainstorm 4 distinct, creative smart features that address BOTH pains simultaneously through clever use of data, platforms, or automation.

### Step 3: Complete 60-Pattern Cross-Reference Loop (Ideas 91 - 130+)
Scan the 60 business model patterns below. Select at least **15 different patterns** from across the entire list that present a high tension or high synergy with your `Product_Context`. 
For each of the 15 chosen patterns, force yourself to generate 2-3 highly disruptive digital smart features or service offerings that map your product data to that specific business model definition.

### Step 4: Technical Co-occurrence Bundling (Convergence)
Review the entire 130+ raw idea pool. Identify the most robust concepts and group them into **3-5 Core Technical Synergy Bundles**. 
*Rule: Features belong together if they share the same data pipeline, infrastructure, or physical modifications (e.g., they utilize the same sensor telemetry, require the same edge gateway, or share an API backend).*

### Step 5: Bundle Feasibility
For each finalized bundle, consider the technical foundation and assess the feasibility of implementation. Assess whether the shared technical assets (e.g., sensors, APIs, data models) are realistic and can be developed within a reasonable timeframe and budget. Use the following feasibility scoring scale and provide a brief justification for each bundle:
- **High Feasibility (4-5):** The bundle leverages existing technologies or requires minimal development. Justification: [e.g., "Utilizes off-the-shelf sensors and existing API frameworks, allowing for rapid deployment."]
- **Medium Feasibility (2-3):** The bundle requires some new development or integration but is still achievable. Justification: [e.g., "Requires custom data models and moderate integration efforts, but no new hardware."]
- **Low Feasibility (0-1):** The bundle requires significant new technology development or faces major integration challenges. Justification: [e.g., "Requires development of new sensor technology and complex integration with legacy systems, posing significant challenges."]

### Step 6: Overall Addressed Value Overview
For each finalized bundle, map the included features back to the initial `Value_of_Pains`. Calculate and explicitly state the cumulative economic value this specific bundle unlocks for the customer.

## 4. Output Format
Save the following outputs in smart-service-ideation-output.md:

### 1. High-Velocity Ideation Matrix (The 100+ Pool)
*(Output the rapid-fire concept matrix completely, ensuring Step 3 explicitly notes which pattern from PATTERNS.md was utilized)*

### 2. Consolidated Technical Synergy Bundles
*(Present the 3-5 winning clusters compiled from the pool)*

**Bundle Name: [e.g., Predictive Asset Health Bundle]**
* **Selected Synergy Features:**
  * Feature IDX: [Name] - [1-sentence technical mechanics]
  * Feature IDY: [Name] - [1-sentence technical mechanics]
* **Business Model Patterns Activated:** [List all applicable patterns here]
* **Shared Technical Foundation:** [Describe the shared telemetry, hardware modifications, or APIs that anchor this bundle]
* **Target VPC Items Covered:** [List the specific pains/gains addressed by this bundle]

### 3. Strategic Value Synthesis Overview
Provide a final evaluation table mapping your bundles to the total value rescued from the customer's pain points:

| Feature Bundle | Primary Technical Asset | Dominant Business Model Pattern | Total Addressed Value / Financial Impact |
|---|---|---|---|
| [Bundle 1] | [e.g., Vibration Sensor + ML] | Sensor As A Service | [e.g., Prevents $45k/year in downtime] |
| [Bundle 2] | [e.g., User App + Energy API] | Pay Per Use | [e.g., Saves 15% on operational overhead] |

### 4. Potential Feasibility Grid
Generate a grid visualization summarizing the feasibility scores for each bundle on the x-axis, financial impact on the y-axis, and feature spectrum as bubble size. Adapt python script below.

## 5. Guardrails
* DO NOT summarize, compress, or use placeholders like "...etc." You must output the rapid-fire concept matrix completely to satisfy the 100+ idea divergence target.
* Every single idea must remain "Smart"—it must involve a digital touchpoint, database, telemetry, analytics model, or automated API action.

## 6. Business Model Patterns
- **Add-on:** Cheap base items cost significantly more once customers include customized extra features.
- **Affiliation:** Independent partners drive sales for a company in exchange for performance-based commissions.
- **Aikido:** Companies launch radical value propositions to capture mainstream competitors' dissatisfied clients.
- **Auction:** Bidders compete against each other to drive up the final transaction price.
- **Barter:** Businesses swap goods or services directly without any cash changing hands.
- **Cash Machine:** Upfront customer payments boost corporate liquidity before operational expenses are incurred.
- **Cross Selling:** Retailers generate new revenue by adding unrelated industry products to existing stores.
- **Crowdfunding:** Web-based micro-investors fund an unbuilt concept in exchange for early perks.
- **Crowdsourcing:** Anonymous online contributors solve tasks to win rewards or production prizes.
- **Customer Loyalty:** Incentive programs build emotional connections to secure predictable future revenue streams.
- **Digitization:** Turning tangible goods into digital formats drastically speeds up global distribution.
- **Direct Selling:** Manufacturers skip retail intermediaries to lower prices and own customer relationships.
- **E-commerce:** Operating exclusively via online web stores eliminates costly physical branch networks.
- **Experience Selling:** Memorable event-driven shopping environments justify premium prices for everyday merchandise.
- **Flat Rate:** Flat-fee pricing structures offer unrestricted usage while stabilizing recurring corporate revenue.
- **Fractional Ownership:** Multiple buyers split the purchase and usage rights of expensive capital assets.
- **Franchising:** Independent entrepreneurs run local branches utilizing an established brand's corporate identity.
- **Freemium:** Free entry-level tiers attract mass audiences while premium upgrades fund the operations.
- **From Push-to-pull:** Decentralized supply chains dynamically adapt operations based on real-time consumer demand.
- **Guaranteed Availability:** Companies leverage deep operational expertise to promise clients near-zero equipment downtime.
- **Hidden Revenue:** Third-party advertisers cross-finance free platforms to reach the attracted user base.
- **Ingredient Branding:** Featuring a highly reputable supplier component elevates the final product's market value.
- **Integrator:** Controlling almost all value chain steps cuts supplier dependency and lowers costs.
- **Layer Player:** Niche specialists supply one optimized production step across completely different industries.
- **Leverage Customer Data:** Harvesting and aggregating user information unlocks monetization through targeted external advertising.
- **License:** R&D efforts center on monetizing intellectual property rights instead of manufacturing goods.
- **Lock-in:** High technological or economic switching barriers prevent consumers from leaving an ecosystem.
- **Long Tail:** Amassing vast catalogs of niche items generates high aggregate profits from small sales.
- **Make More Of It:** Companies commercialize internal slack resources and specialized expertise to external firms.
- **Mass Customization:** Modular manufacturing lines deliver individualized products at competitive mass-production prices.
- **No Frills:** Stripping offerings down to core basics allows hyper-low pricing for budget-conscious buyers.
- **Open Business Model:** Collaborating across an ecosystem with diverse partners drives collective value creation.
- **Open Source:** Free source code access encourages public contributions while monetizing support consulting.
- **Orchestrator:** Businesses outsource non-core manufacturing segments to focus strictly on central corporate competencies.
- **Pay Per Use:** Customers only pay for the exact volume of services they effectively consume.
- **Pay What You Want:** Buyers self-determine their prices, driving massive customer acquisition through social norms.
- **Peer-to-peer:** Online database matchmakers connect private individuals directly for rental or asset sharing.
- **Performance-based Contracting:** Pricing links directly to real-world operational outcomes rather than physical asset value.
- **Razor And Blade:** Cheap entry products lock buyers into purchasing high-margin, proprietary consumable refills.
- **Rent Instead Of Buy:** Temporal leasing options lower client capital requirements while increasing asset utilization.
- **Revenue Sharing:** Firms split incoming profits with stakeholders to create mutually beneficial ecosystem synergies.
- **Reverse Engineering:** Deconstructing rival merchandise allows cheaper replication without heavy upfront research investments.
- **Reverse Innovation:** Streamlined products designed for emerging markets get successfully imported into wealthy nations.
- **Robin Hood:** Wealthier clients pay premium rates to subsidize low-cost access for disadvantaged groups.
- **Self-service:** Outsourcing operational labor to consumers cuts corporate overheads in exchange for discounts.
- **Shop-in-shop:** Brands set up miniature boutique spaces inside larger, high-traffic host retailers.
- **Solution Provider:** Full-service single points of contact handle complete client requirements in specific domains.
- **Subscription:** Steady recurring revenue is generated by billing fixed monthly or annual access fees.
- **Supermarket:** Bundling a massive selection of low-priced goods under one roof attracts high volume.
- **Target The Poor:** Ultra-affordable items tap into massive sales volumes at the economic pyramid's base.
- **Trash-to-cash:** Reclaiming discarded waste materials virtually eliminates resource costs for new product lines.
- **Two-sided Market:** Platforms create value by connecting and facilitating transactions between interdependent consumer groups.
- **Ultimate Luxury:** Elite quality standards and extreme exclusivity unlock exceptionally high profit margins.
- **User Designed:** Online platforms supply creation toolkits so consumers can design and sell custom merchandise.
- **Whitelabel:** Generic manufacturers let multiple different vendors rebrand identical goods as their own.
- **Sensor As A Service:** Real-time connected hardware feeds data analysis engines to unlock new service revenue.
- **Virtualization:** Moving physical workflows into digital environments grants users flexible, location-independent interaction.
- **Object Self-service:** Automated IoT hardware detects low inventory to trigger replenishment orders independently.
- **Object As Point-of-sale:** Moving purchasing mechanisms directly onto consumer hardware reduces price sensitivity.
- **Prosumer:** Blending consumption with production boosts the perceived value of the final creation.

## 7. Python Script for Feasibility Grid Visualization
```python
!pip install matplotlib numpy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D
import numpy as np

# ══════════════════════════════════════════════════════════════════════════════
# INPUT — replace this section to use any dataset
# ══════════════════════════════════════════════════════════════════════════════

# Each bundle must have:
#   id          : str   — short label shown inside bubble
#   label       : str   — full name shown in callout (use \n for line breaks)
#   feasibility : float — score on x-axis (should fall within X_MIN..X_MAX)
#   value       : float — financial impact on y-axis
#   features    : int   — number of bundled features (controls bubble size)
#   level       : str   — feasibility tier label (used in callout text only)
#   pains       : str   — addressed pain IDs (used in callout text only)
#   x_offset    : float — horizontal jitter to avoid overlap (set 0 if unique x)

BUNDLES = [
    {
        "id": "A",
        "label": "A — Unified Schema\nIntelligence Platform",
        "feasibility": 4,
        "value": 23_880,
        "features": 12,
        "level": "High",
        "pains": "P1, P4, P5, P6",
        "x_offset": -0.18,
    },
    {
        "id": "B",
        "label": "B — Pitch & Decision\nAcceleration Engine",
        "feasibility": 4,
        "value": 31_440,
        "features": 12,
        "level": "High",
        "pains": "P2, P4, P5, P8",
        "x_offset": 0.0,
    },
    {
        "id": "C",
        "label": "C — Adversarial Validation\n& Innovation Intelligence",
        "feasibility": 3,
        "value": 20_840,
        "features": 14,
        "level": "Medium",
        "pains": "P4, P6, P7",
        "x_offset": 0.0,
    },
    {
        "id": "D",
        "label": "D — Team Intelligence\n& Capability Orchestration",
        "feasibility": 4,
        "value": 21_600,
        "features": 15,
        "level": "High",
        "pains": "P3, P5, P8",
        "x_offset": 0.18,
    },
]

# Chart titles
TITLE    = "Smart Service Bundle — Feasibility vs. Financial Impact Grid"
SUBTITLE = (
    "Skills Collection for Service Engineering  |  "
    "Customer Segment: Corporate PMs & Cross-Functional Innovation Teams  |  "
    "Total $V_C$ = €55,880/yr"
)

# Axis labels
X_LABEL = "Feasibility Score  (1 = very low  →  5 = very high)"
Y_LABEL = "Addressed Financial Value  (€ / year)"

# Y-axis value formatter — receives raw float, returns tick string
Y_FORMATTER = lambda v, _: f"€{int(v):,}"

# Quadrant dividers
FEASIBILITY_THRESHOLD = 3.5    # vertical divider (x-axis)
VALUE_THRESHOLD       = 24_000 # horizontal divider (y-axis)

# Axis bounds
X_MIN, X_MAX = 1.5, 5.5
Y_MIN, Y_MAX = 0, 40_000

# Quadrant labels: (x, y, text, color)
QUADRANT_LABELS = [
    (2.4,   8_000, "Challenging\n(low value, medium feasibility)",  "#8b4500"),
    (2.4,  33_500, "Hidden Gem\n(high value, de-risk first)",        "#7a5c00"),
    (4.55,  8_000, "Quick Win\n(low value, easy to ship)",           "#2e6e2e"),
]

# Prime Zone label — treated separately because it has a bbox
PRIME_ZONE_X, PRIME_ZONE_Y = 4.55, 33_500

# Quadrant background colours (fill)
QUAD_COLOR_BOTTOM_LEFT  = "#e07b2a"   # challenging
QUAD_COLOR_TOP_LEFT     = "#f0c040"   # hidden gem
QUAD_COLOR_BOTTOM_RIGHT = "#a8d8a8"   # quick win
QUAD_COLOR_TOP_RIGHT    = "#1b4f8a"   # prime zone
QUAD_ALPHA              = 0.18

# ══════════════════════════════════════════════════════════════════════════════
# STYLE — tweak appearance without touching rendering logic
# ══════════════════════════════════════════════════════════════════════════════

BUBBLE_COLOR        = "#1b4f8a"
BUBBLE_ALPHA        = 0.88
BUBBLE_EDGE_COLOR   = "white"
BUBBLE_EDGE_WIDTH   = 2.2
BUBBLE_SHADOW_COLOR = "#00000022"
BUBBLE_SHADOW_DX    = 0.025
BUBBLE_SHADOW_DY    = -320

FEATURE_SIZE_FACTOR = 45   # bubble area = features² × factor

FONT_MAIN    = "DejaVu Sans"
FIG_COLOR    = "#f8f9fa"
AXES_COLOR   = "#f0f2f5"
GRID_COLOR   = "#cccccc"
SPINE_COLOR  = "#bbbbbb"

# Bubble-size reference legend
REF_FEATURES     = [12, 15]  # example sizes to show in legend
REF_X            = 4.95
REF_Y            = 6_200
REF_GAP          = 1_400
REF_TITLE_DY     = 1_300     # upward offset from REF_Y for the legend title

# Figure dimensions
FIG_WIDTH, FIG_HEIGHT = 11, 7.5

# Output
OUTPUT_PATH = "smart-service-ideation-grid.png"
OUTPUT_DPI  = 180

# ══════════════════════════════════════════════════════════════════════════════
# RENDERING — do not edit below unless changing chart structure
# ══════════════════════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT))
fig.patch.set_facecolor(FIG_COLOR)
ax.set_facecolor(AXES_COLOR)

# ── Quadrant shading ──────────────────────────────────────────────────────────

ax.fill_betweenx([Y_MIN, VALUE_THRESHOLD],
                 X_MIN, FEASIBILITY_THRESHOLD,
                 color=QUAD_COLOR_BOTTOM_LEFT, alpha=QUAD_ALPHA)
ax.fill_betweenx([VALUE_THRESHOLD, Y_MAX],
                 X_MIN, FEASIBILITY_THRESHOLD,
                 color=QUAD_COLOR_TOP_LEFT, alpha=QUAD_ALPHA)
ax.fill_betweenx([Y_MIN, VALUE_THRESHOLD],
                 FEASIBILITY_THRESHOLD, X_MAX,
                 color=QUAD_COLOR_BOTTOM_RIGHT, alpha=QUAD_ALPHA)
ax.fill_betweenx([VALUE_THRESHOLD, Y_MAX],
                 FEASIBILITY_THRESHOLD, X_MAX,
                 color=QUAD_COLOR_TOP_RIGHT, alpha=QUAD_ALPHA)

# ── Quadrant labels ───────────────────────────────────────────────────────────

quad_kw = dict(fontsize=8.2, fontstyle="italic", alpha=0.72,
               fontfamily=FONT_MAIN, zorder=2)

for qx, qy, qtxt, qcolor in QUADRANT_LABELS:
    ax.text(qx, qy, qtxt, color=qcolor, ha="center", **quad_kw)

ax.text(PRIME_ZONE_X, PRIME_ZONE_Y, "Prime Zone",
        color="#0c2d5a", ha="center", fontsize=9.5, fontweight="bold",
        fontfamily=FONT_MAIN, alpha=0.80, zorder=2,
        bbox=dict(boxstyle="round,pad=0.3", fc=BUBBLE_COLOR, ec="none", alpha=0.15))

# ── Threshold lines ───────────────────────────────────────────────────────────

ax.axvline(FEASIBILITY_THRESHOLD, color="#555", lw=1.1, ls="--", alpha=0.5, zorder=3)
ax.axhline(VALUE_THRESHOLD,       color="#555", lw=1.1, ls="--", alpha=0.5, zorder=3)

# ── Grid ──────────────────────────────────────────────────────────────────────

ax.set_xticks([1, 2, 3, 4, 5])
ax.set_yticks(range(int(Y_MIN), int(Y_MAX) + 5_000, 5_000))
ax.grid(which="major", color=GRID_COLOR, lw=0.6, linestyle="-", alpha=0.7, zorder=1)

# ── Bubbles ───────────────────────────────────────────────────────────────────

for b in BUNDLES:
    x    = b["feasibility"] + b["x_offset"]
    y    = b["value"]
    size = b["features"] ** 2 * FEATURE_SIZE_FACTOR

    ax.scatter(x + BUBBLE_SHADOW_DX, y + BUBBLE_SHADOW_DY,
               s=size, color=BUBBLE_SHADOW_COLOR, zorder=3)
    ax.scatter(x, y, s=size, color=BUBBLE_COLOR,
               edgecolors=BUBBLE_EDGE_COLOR, linewidths=BUBBLE_EDGE_WIDTH,
               alpha=BUBBLE_ALPHA, zorder=4)

    ax.text(x, y + 180, b["id"],
            ha="center", va="center", fontsize=11, fontweight="bold",
            color="white", fontfamily=FONT_MAIN, zorder=5)
    ax.text(x, y - 300, f"{b['features']} features",
            ha="center", va="center", fontsize=6.5,
            color="white", alpha=0.90, fontfamily=FONT_MAIN, zorder=5)

# ── Axes formatting ───────────────────────────────────────────────────────────

ax.set_xlim(X_MIN, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)
ax.set_xlabel(X_LABEL, fontsize=10.5, labelpad=10,
              fontfamily=FONT_MAIN, color="#333")
ax.set_ylabel(Y_LABEL, fontsize=10.5, labelpad=10,
              fontfamily=FONT_MAIN, color="#333")
ax.yaxis.set_major_formatter(plt.FuncFormatter(Y_FORMATTER))
ax.tick_params(axis="both", labelsize=9, colors="#444")
for spine in ax.spines.values():
    spine.set_edgecolor(SPINE_COLOR)

# ── Bubble-size reference legend (lower right) ────────────────────────────────

for i, n in enumerate(REF_FEATURES):
    s = n ** 2 * FEATURE_SIZE_FACTOR
    ax.scatter(REF_X, REF_Y - i * REF_GAP, s=s,
               color="#888888", edgecolors="white", linewidths=1.4,
               alpha=0.45, zorder=4)
    ax.text(REF_X + 0.22, REF_Y - i * REF_GAP, f"{n} features",
            va="center", ha="left", fontsize=7.5,
            fontfamily=FONT_MAIN, color="#444444", zorder=5)

ax.text(REF_X, REF_Y + REF_TITLE_DY,
        "Bubble size =\nnumber of bundled\nsmart features",
        ha="center", va="bottom", fontsize=7.2,
        fontfamily=FONT_MAIN, color="#555555",
        bbox=dict(boxstyle="round,pad=0.3", fc="white",
                  ec="#cccccc", lw=0.9, alpha=0.85),
        zorder=5)

# ── Title & subtitle ──────────────────────────────────────────────────────────

fig.text(0.5, 0.97, TITLE,
         ha="center", va="top", fontsize=14, fontweight="bold",
         fontfamily=FONT_MAIN, color="#1a1a1a")
fig.text(0.5, 0.935, SUBTITLE,
         ha="center", va="top", fontsize=8.6,
         fontfamily=FONT_MAIN, color="#555555")

# ── Bundle legend (bottom) ────────────────────────────────────────────────────

fig.add_artist(Line2D([0.01, 0.99], [0.158, 0.158],
                      transform=fig.transFigure,
                      color="#cccccc", lw=0.8, alpha=0.7))

for i, b in enumerate(BUNDLES):
    x0 = 0.01 + i * 0.245      # left edge of this column

    fig.text(x0 + 0.022, 0.095, b["id"],
             ha="center", va="center",
             fontsize=10, fontweight="bold",
             color="white", fontfamily=FONT_MAIN,
             bbox=dict(boxstyle="circle,pad=0.30",
                       fc=BUBBLE_COLOR, ec="none", alpha=0.90))

    tx = x0 + 0.050             # text left edge

    fig.text(tx, 0.123, b["label"].replace("\n", " "),
             ha="left", va="center",
             fontsize=8.0, fontweight="bold",
             fontfamily=FONT_MAIN, color="#1a1a1a")

    fig.text(tx, 0.072,
             f"Score {b['feasibility']}/5  ·  {b['level']} Feasibility"
             f"  ·  €{b['value']:,}/yr  ·  Pains: {b['pains']}",
             ha="left", va="center",
             fontsize=7.0,
             fontfamily=FONT_MAIN, color="#555555")

plt.tight_layout(rect=[0, 0.17, 1, 0.93])

# ── Export ────────────────────────────────────────────────────────────────────

plt.savefig(OUTPUT_PATH, dpi=OUTPUT_DPI, bbox_inches="tight",
            facecolor=fig.get_facecolor())
print(f"Saved → {OUTPUT_PATH}")
plt.show()
```