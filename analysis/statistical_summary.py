import pandas as pd
import os
import matplotlib.pyplot as plt

# Folder where CSV files are located
data_folder = 'output'

# Initialize lists to store success rates and dates
success_rates = []
dates = []

# Process CSV files and calculate success rates for each file
for file_name in os.listdir(data_folder):
    if file_name.endswith('.csv'):
        df = pd.read_csv(os.path.join(data_folder, file_name))
        total_operations = len(df)
        winning_operations = len(df[df['win'] == 'win'])
        losing_operations = len(df[df['win'] == 'lose'])
        success_rate = (winning_operations / total_operations) * 100
        success_rates.append(success_rate)
        dates.append(file_name.replace('iq_option_data_', '').replace('.csv', ''))

# Create a bar chart to display success rates by date
plt.figure(figsize=(12, 6))
plt.bar(dates, success_rates)
plt.xlabel('Date')
plt.ylabel('Success Rate (%)')
plt.title('Operation Success Rate (Including Losses) by Date')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()
