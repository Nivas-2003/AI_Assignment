import pandas as pd

# ============================================================
# Sleep Reflex Agent - Sleep Duration Analysis
# ============================================================

# Load dataset
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent

file_path = (
    project_folder
    / "dataset"
    / "Sleep_health_and_lifestyle_dataset.csv"
)

df = pd.read_csv(file_path)

print("\n========================================")
print("SLEEP DURATION vs SLEEP QUALITY")
print("========================================")

# Group records by sleep duration
duration_analysis = (
    df.groupby("Sleep Duration")["Quality of Sleep"]
    .agg(["count", "mean", "min", "max"])
    .reset_index()
)

print(duration_analysis.to_string(index=False))


# ============================================================
# Average quality for different sleep-duration ranges
# ============================================================

print("\n========================================")
print("SLEEP DURATION RANGES")
print("========================================")

def classify_duration(hours):
    if hours < 6:
        return "Less than 6 hours"
    elif hours < 7:
        return "6 to <7 hours"
    elif hours < 8:
        return "7 to <8 hours"
    elif hours <= 9:
        return "8 to 9 hours"
    else:
        return "More than 9 hours"


df["Duration Range"] = df["Sleep Duration"].apply(classify_duration)

range_analysis = (
    df.groupby("Duration Range", observed=True)["Quality of Sleep"]
    .agg(["count", "mean", "min", "max"])
    .reset_index()
)

print(range_analysis.to_string(index=False))


# ============================================================
# Overall statistics
# ============================================================

print("\n========================================")
print("OVERALL SLEEP STATISTICS")
print("========================================")

print(f"Average Sleep Duration : {df['Sleep Duration'].mean():.2f} hours")
print(f"Average Sleep Quality  : {df['Quality of Sleep'].mean():.2f} / 10")
print(f"Minimum Sleep Duration : {df['Sleep Duration'].min():.2f} hours")
print(f"Maximum Sleep Duration : {df['Sleep Duration'].max():.2f} hours")
print(f"Minimum Sleep Quality  : {df['Quality of Sleep'].min()} / 10")
print(f"Maximum Sleep Quality  : {df['Quality of Sleep'].max()} / 10")