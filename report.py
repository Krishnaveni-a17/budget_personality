# report.py
# Builds the formatted spending report.
# Prints to terminal AND saves as .txt file.

import os


def build_bar(percentage, width=20):
    """
    Builds a visual bar from a percentage.
    Example: 40% with width 20 → ████████░░░░░░░░░░░░
    """
    filled = int((percentage / 100) * width)
    empty  = width - filled
    return "█" * filled + "░" * empty


def generate_nudge(personality_name, percentages, grouped):
    """
    Generates a personalised savings tip based on personality.
    Shows how much the user would save with a 20% cut.
    """
    total = sum(grouped.values())

    if "Comfort" in personality_name:
        food_amount = grouped.get("Food", 0)
        saving      = round(food_amount * 0.20 * 12, 2)
        return (f"If you cut Food spending by 20%, "
                f"you save ₹{saving:.2f} extra per year.")

    elif "Impulse" in personality_name:
        shop_amount = grouped.get("Shopping", 0)
        saving      = round(shop_amount * 0.20 * 12, 2)
        return (f"If you cut Shopping by 20%, "
                f"you save ₹{saving:.2f} extra per year.")

    elif "Homebody" in personality_name:
        return "Try allocating ₹500/month toward an experience — travel, hobby, or skill."

    elif "Balanced" in personality_name:
        saving = round(total * 0.10 * 12, 2)
        return (f"You're already balanced! Investing 10% "
                f"could grow to ₹{saving:.2f} saved per year.")

    else:
        return "Try tracking for one more month to see your clearest pattern."


def generate_report(expenses, grouped, percentages, personality):
    """
    Builds complete report as a string.
    Prints to terminal and saves to reports/spending_report.txt
    """
    name, description = personality

    lines = []
    lines.append("════════════════════════════════════════════")
    lines.append("      💸 SPENDING PERSONALITY REPORT")
    lines.append("════════════════════════════════════════════")
    lines.append("")

    # Category breakdown with bar chart
    for category, pct in percentages.items():
        amount = grouped[category]
        bar    = build_bar(pct)
        lines.append(
            f"  {category:15} ₹{amount:>8.2f}   ({pct:.1f}%)  {bar}"
        )

    lines.append("")
    lines.append("────────────────────────────────────────────")
    lines.append("  🧠 YOUR SPENDING PERSONALITY:")
    lines.append("")
    lines.append(f"  {name}")
    lines.append(f"  {description}")
    lines.append("")

    # Savings nudge
    nudge = generate_nudge(name, percentages, grouped)
    lines.append("  💡 NUDGE:")
    lines.append(f"  {nudge}")
    lines.append("")
    lines.append("════════════════════════════════════════════")

    # Assemble into one string
    report_text = "\n".join(lines)

    # Print to terminal
    print("\n" + report_text)

    # Save to file
    os.makedirs("reports", exist_ok=True)
    filename = "reports/spending_report.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_text)

    print(f"\n  Report saved to {filename}")
    return report_text