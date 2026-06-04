import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

item_ids = []
types = []
descriptions = []
agents = []
potential_values = []

with open("value_of_pains.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        item_ids.append(row["Item ID"])
        types.append(row["Type (Pain/Gain)"])
        descriptions.append(row["Description"])
        agents.append(row["Agent (Customer/Provider)"])
        potential_values.append(float(row["Potential Value (Annual)"]))

colors = [
    "#e07070" if t.strip().lower() == "pain" else "#5cb85c"
    for t in types
]
edge_colors = [
    "#a03030" if t.strip().lower() == "pain" else "#2d7a2d"
    for t in types
]

short_labels = [
    f"{item_ids[i]}\n({agents[i][:4]})"
    for i in range(len(item_ids))
]

fig, ax = plt.subplots(figsize=(max(10, len(item_ids) * 1.3), 7))

x = range(len(item_ids))
bar_width = 0.55

bars = ax.bar(
    list(x),
    potential_values,
    width=bar_width,
    color=colors,
    edgecolor=edge_colors,
    linewidth=1.2,
    zorder=3,
)

for bar, val in zip(bars, potential_values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + max(potential_values) * 0.015,
        f"{int(val):,} €",
        ha="center",
        va="bottom",
        fontsize=8.5,
        fontweight="bold",
        color="#333333",
    )

ax.set_xticks(list(x))
ax.set_xticklabels(short_labels, fontsize=9)
ax.set_ylabel("Annual Potential Value (€)", fontsize=11)
ax.set_title(
    "Value of Pains & Gains — Baseline Potential Values\n"
    "Frequency × Impact per Item",
    fontsize=12,
    fontweight="bold",
    pad=14,
)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{int(v):,} €"))
ax.grid(axis="y", linestyle="--", alpha=0.4, zorder=0)
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor="#e07070", edgecolor="#a03030", label="Pain ($VP_{pot}$)"),
    Patch(facecolor="#5cb85c", edgecolor="#2d7a2d", label="Gain ($VG_{pot}$)"),
]
ax.legend(handles=legend_elements, fontsize=10, loc="upper right")

total_pain = sum(v for v, t in zip(potential_values, types) if t.strip().lower() == "pain")
total_gain = sum(v for v, t in zip(potential_values, types) if t.strip().lower() == "gain")
total = total_pain + total_gain

ax.annotate(
    f"Total Pain: {total_pain:,.0f} €\nTotal Gain: {total_gain:,.0f} €\nTotal: {total:,.0f} €",
    xy=(0.98, 0.97),
    xycoords="axes fraction",
    ha="right",
    va="top",
    fontsize=10,
    fontweight="bold",
    color="#1b365d",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#f5f5f5", edgecolor="#555555", linewidth=1.2),
)

plt.tight_layout()
plt.savefig("value_of_pains.png", dpi=150, bbox_inches="tight")
print(f"Chart saved. Total Pain Potential: {total_pain:,.0f} €  |  Total Gain Potential: {total_gain:,.0f} €  |  Total: {total:,.0f} €")
