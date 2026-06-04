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
OUTPUT_PATH = "potential-feasibility-grid.png"
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
