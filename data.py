# import os
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import plotly.express as px
# import os
# os.makedirs("plots", exist_ok=True)


# # Create output directory
# os.makedirs("plots", exist_ok=True)

# # Load dataset
# df = pd.read_csv("heart.csv")  # Make sure this file is in the same folder

# # Set Seaborn style
# sns.set(style="whitegrid", font_scale=1.2)
# palette = sns.color_palette("husl", 8)  # Vibrant colors

# # ----- 1. Histogram: Age Distribution -----
# plt.figure(figsize=(10, 6))
# sns.histplot(df['age'], kde=True, bins=20, color=palette[0], edgecolor='black')
# plt.title('Age Distribution of Patients', fontsize=18, fontweight='bold')
# plt.xlabel('Age', fontsize=14)
# plt.ylabel('Count', fontsize=14)
# plt.grid(True, linestyle='--', linewidth=0.5)
# plt.tight_layout()
# plt.savefig('plots/age_distribution.png', dpi=300, bbox_inches='tight')
# plt.show()

# # ----- 2. Count Plot: Chest Pain Type vs Heart Disease -----
# plt.figure(figsize=(10, 6))
# sns.countplot(data=df, x='cp', hue='target', palette='cool')
# plt.title('Chest Pain Type vs Heart Disease', fontsize=18, fontweight='bold')
# plt.xlabel('Chest Pain Type', fontsize=14)
# plt.ylabel('Count', fontsize=14)
# plt.legend(title='Heart Disease (1=Yes, 0=No)')
# plt.tight_layout()
# plt.savefig('plots/cp_vs_target.png', dpi=300, bbox_inches='tight')
# plt.show()

# # ----- 3. Box Plot: Cholesterol by Heart Disease -----
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=df, x='target', y='chol', palette='Set3')
# plt.title('Cholesterol Levels by Heart Disease', fontsize=18, fontweight='bold')
# plt.xlabel('Heart Disease', fontsize=14)
# plt.ylabel('Cholesterol', fontsize=14)
# plt.tight_layout()
# plt.savefig('plots/chol_by_target.png', dpi=300, bbox_inches='tight')
# plt.show()

# # ----- 4. Correlation Heatmap -----
# plt.figure(figsize=(12, 8))
# sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm', square=True)
# plt.title('Correlation Heatmap', fontsize=18, fontweight='bold')
# plt.tight_layout()
# plt.savefig('plots/correlation_heatmap.png', dpi=300, bbox_inches='tight')
# plt.show()

# # ----- 5. Pair Plot of Selected Features -----
# pair_plot = sns.pairplot(df[['age', 'trestbps', 'chol', 'thalach', 'target']], hue='target', palette='husl')
# pair_plot.fig.suptitle("Pairwise Relationships", y=1.02, fontsize=18)
# pair_plot.savefig("plots/pairplot.png", dpi=300, bbox_inches='tight')
# plt.show()

# # ----- 6. Plotly Scatter: Age vs Max Heart Rate -----
# fig = px.scatter(df, x='age', y='thalach', color='target',
#                  title='Age vs Max Heart Rate (Target Colored)',
#                  labels={'thalach': 'Max Heart Rate', 'target': 'Heart Disease'},
#                  template='plotly_dark')

# fig.update_traces(marker=dict(size=10, opacity=0.7, line=dict(width=1, color='DarkSlateGrey')))
# fig.write_html("plots/age_vs_thalach.html")
# fig.show()

import os
import kagglehub

# Download the entire dataset
dataset_path = kagglehub.dataset_download("vipoooool/new-plant-diseases-dataset")

# Construct the path to the 'test' subdirectory
test_path = os.path.join(dataset_path, "test")

print(f"Path to the 'test' directory: {test_path}")

# You can now use the 'test_path' variable to access your test data