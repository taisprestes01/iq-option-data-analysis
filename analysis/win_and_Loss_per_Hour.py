import pandas as pd
import os
import matplotlib.pyplot as plt

# Folder where CSV files are located
data_folder = 'output'

# Initialize lists to store hours, wins, and losses
hours = []
wins = []
losses = []

# Process CSV files and calculate wins and losses for each period
for file_name in os.listdir(data_folder):
    if file_name.endswith('.csv'):
        df = pd.read_csv(os.path.join(data_folder, file_name))
        for index, row in df.iterrows():
            created_hour = row['created'].split()[1][:5]  # Extract creation time (assuming the format is HH:MM)
            expired_hour = row['expired'].split()[1][:5]  # Extract expiration time (assuming the format is HH:MM)
            win_or_loss = row['win']  # Here we use "loss" based on your dataset

            # If the operation is a win
            if win_or_loss == 'win':
                wins.append((created_hour, expired_hour))
            # If the operation is a loss
            elif win_or_loss == 'loss':
                losses.append((created_hour, expired_hour))

# Extract unique hours
unique_hours = list(set(hours))

# Count wins and losses per hour
win_counts = [wins.count(hour) for hour in unique_hours]
loss_counts = [losses.count(hour) for hour in unique_hours]

# Create a stacked bar chart
plt.figure(figsize=(12, 6))
plt.bar(unique_hours, win_counts, label='Win', color='green')
plt.bar(unique_hours, loss_counts, label='Loss', color='red', bottom=win_counts)
plt.xlabel('Hour')
plt.ylabel('Operation Count')
plt.title('Distribution of Win and Loss Operations per Hour (Created and Expired)')
plt.xticks(rotation=45, ha='right')
plt.legend()

plt.tight_layout()
plt.show()
