import pandas as pd
from getDataHistory import getHistory
from datetime import datetime
import os

trade_history = getHistory('login', 'password', 300, 'REAL')

def object_to_save(trade_history):
    data = {}
    for operation in trade_history['msg']['result']['closed_options']:
        date = datetime.fromtimestamp(operation['created']).date()
        if date not in data:
            data[date] = []

        id = operation['id'][0]
        active = operation['active']
        active_id = operation['active_id']
        amount = operation['amount']
        win_amount = operation['win_amount']
        exp_value = operation['exp_value']
        expired = str(datetime.fromtimestamp(operation['expired']))
        created = str(datetime.fromtimestamp(operation['created']))
        created_millisecond = operation['created_millisecond']
        count = operation['count']
        win = operation['win']
        option_type = operation['option_type']

        data[date].append([id, active, active_id, amount, win_amount, exp_value, expired, created, created_millisecond, count, win, option_type])

    return data

def save_data_to_csv(data, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for date, operations in data.items():
        file_name = os.path.join(output_folder, f'iq_option_data_{date}.csv')
        df = pd.DataFrame(operations, columns=['id', 'active', 'active_id', 'amount', 'win_amount', 'exp_value', 'expired', 'created', 'created_millisecond', 'count', 'win', 'option_type'])
        df.to_csv(file_name, index=False)

output_folder = 'output'
data = object_to_save(trade_history)
save_data_to_csv(data, output_folder)
