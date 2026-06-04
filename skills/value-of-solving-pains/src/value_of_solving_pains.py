import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

pain_ids = []
pain_labels = []
effective_values = []
potential_values = []

with open("value_of_solving_pains.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        pain_ids.append(row["Pain ID"])
        pain_labels.append(row["Pain Description"])
        effective_values.append(float(row["Effective Value (Annual)"]))
        potential_values.append(float(row["Potential Value (Annual)"]))

short_labels = [
    "P1\nSync Rework",
    "P2\nPitch Rejection",
    "P3\nCollab Friction",
    "P4\nAnalysis Paralysis",
    "P5\nProductivity",
    "P6\nBlindspots",
    "P7\nNo Ext. View",
    "P8\nCapacity",
]

fig, ax = plt.subplots(figsize=(13, 7))

x = range(len(pain_ids))
bar_width = 0.38

bars_pot = ax.bar(
    [i - bar_width / 2 for i in x],
    potential_values,
    width=bar_width,
    color="#c8d8e8",
    edgecolor="#4a7aab",
    linewidth=1.2,
    label="Potential Value ($VC_{pot}$)",
    zorder=3,
)
bars_eff = ax.bar(
    [i + bar_width / 2 for i in x],
    effective_values,
    width=bar_width,
    color="#1b365d",
    edgecolor="#0d1f38",
    linewidth=1.2,
    label="Effective Value ($VC_{C}$)",
    zorder=3,
)

for bar, val in zip(bars_eff, effective_values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 250,
        f"{int(val):,} €",
        ha="center",
        va="bottom",
        fontsize=8.5,
        fontweight="bold",
        color="#1b365d",
    )

ax.set_xticks(list(x))
ax.set_xticklabels(short_labels, fontsize=9)
ax.set_ylabel("Annual Value (€)", fontsize=11)
ax.set_title(
    "Value of Solving Pains — Skills Collection for Service Engineering\n"
    "Customer Segment: Corporate Product Managers & Cross-Functional Innovation Teams",
    fontsize=12,
    fontweight="bold",
    pad=14,
)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{int(v):,} €"))
ax.grid(axis="y", linestyle="--", alpha=0.4, zorder=0)
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(fontsize=10, loc="upper left")

total_vc = sum(effective_values)
ax.annotate(
    f"Total $V_C$ = {total_vc:,.0f} €",
    xy=(0.98, 0.97),
    xycoords="axes fraction",
    ha="right",
    va="top",
    fontsize=11,
    fontweight="bold",
    color="#1b365d",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#e8f0f8", edgecolor="#1b365d", linewidth=1.2),
)

plt.tight_layout()
plt.savefig("value_of_solving_pains.png", dpi=150, bbox_inches="tight")
print(f"Chart saved. Total Customer Value (V_C): {total_vc:,.0f} €")
