import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "StudentsPerformance .csv"
df = pd.read_csv(file_path)

# === 1. Data Cleaning & Preparation ==
# Rename columns for easier access
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Create avverage exam score
df["average_score"] = df [["math_score", "reading_score", "writing_score"]].mean(axis = 1)

# Classify education levels
lower_edu_levels = ["some high school", "high school"]
df["low_parent_edu"] = df["parental_level_of_education"].isin(lower_edu_levels)

# == 2. Compare average scores by test prep ===
prep_comparison = df.groupby("test_preparation_course")["average_score"].mean().reset_index()

# == 3
low_edu_df = df[df["low_parent_edu"] == True]
low_edu_comparison = low_edu_df.groupby("test_preparation_course")["average_score"].mean().reset_index()

# == 4
plt.figure(figsize=(7, 5))
sns.barplot(data=prep_comparison, x="test_preparation_course", y="average_score", palette="Blues_d")
plt.title("Average Exam Score vs. Test Preparation Course")
plt.xlabel("Test Preparation Course")
plt.ylabel("Average Score")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()