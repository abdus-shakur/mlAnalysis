import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import logging

logging.basicConfig(filename="./console.log", level=logging.DEBUG, filemode="w",
                    format="%(asctime)s %(levelname)s %(module)s %(lineno)d %(funcName)s %(message)s")
logger = logging.getLogger(__name__)

# Set options for data visualization
pd.set_option('display.max_rows', 10)  # Set maximum number of rows to display
pd.set_option('display.max_columns', None)  # Set maximum number of columns to display (None means display all)
pd.set_option('display.float_format', '{:.2f}'.format)  # Set floating-point number format to display two decimal places

df = pd.read_csv("C:/Users/SHA/PycharmProjects/scrapyProject/iplT20/data/final-2/IPL_*_beststrikeratestournament_2024_04_02.csv")
logger.debug(df.describe())
min_matches = 2
df[f'Atleast {min_matches} Match'] = df['Matches'] > min_matches
logger.debug(df.keys)
true_count = sum(df[f'Atleast {min_matches} Match'])
false_count = len(df[f'Atleast {min_matches} Match']) - true_count

matches = df['Matches'].drop_duplicates()
match_data = {'count': [], 'label': []}
for match in matches:
    match_data['label'].append(match)
    df[f'Match {match}'] = df['Matches'] = match
    match_data['count'].append(sum(df[f'Match {match}']))

# plt.pie([true_count, false_count], labels=["Yes", "No"], autopct='%1.1f%%', startangle=90)
# plt.title(f"Played more than {min_matches} Match")
# plt.show()

plt.pie(match_data['count'], labels=match_data['label'], autopct='%1.1f%%', startangle=45)
plt.title(f"Number of Matches played to Player Percentage")
plt.show()
