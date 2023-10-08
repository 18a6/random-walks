import pandas as pd

melbourne_path_file = 'input/melbourne-housing-snapshot/melb_data.csv'

melbourne_data = pd.read_csv(melbourne_path_file)
melbourne_data.describe()

print(melbourne_data.head())
