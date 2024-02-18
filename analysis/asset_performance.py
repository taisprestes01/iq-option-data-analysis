import pandas as pd
import os
import matplotlib.pyplot as plt

# Folder where CSV files are located
data_folder = 'output'

# Initialize a dictionary to store asset performance
asset_performance = {}

# Process CSV files and calculate asset performance
for file_name in os.listdir(data_folder):
    if file_name.endswith('.csv'):
        df = pd.read_csv(os.path.join(data_folder, file_name))
        for asset in df['active']:
            if asset not in asset_performance:
                asset_performance[asset] = {'wins': 0, 'losses': 0}
            wins = len(df[(df['win'] == 'win') & (df['active'] == asset)])
            losses = len(df[(df['win'] == 'loss') & (df['active'] == asset)])
            asset_performance[asset]['wins'] += wins
            asset_performance[asset]['losses'] += losses

# Create a bar chart to show asset performance
assets = list(asset_performance.keys())
wins = [asset_performance[asset]['wins'] for asset in assets]
losses = [asset_performance[asset]['losses'] for asset in assets]

plt.figure(figsize=(12, 6))
plt.bar(assets, wins, label='Wins', color='green')
plt.bar(assets, losses, label='Losses', color='red', bottom=wins)
plt.xlabel('Assets')
plt.ylabel('Number of Operations')
plt.title('Asset Performance')
plt.xticks(rotation=45, ha='right')
plt.legend()

plt.tight_layout()
plt.show()
