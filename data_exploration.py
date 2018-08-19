import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('transfers.csv')

# Find Top 5 Leagues by turnover in selling players
league_from = data.groupby(['League_from'])['Transfer_fee'].sum()
top5sell_league = league_from.sort_values(ascending=False).head(5)

# Find Top 5 Leagues by turnover in buying players
league_to = data.groupby(['League_to'])['Transfer_fee'].sum()
top5buy_league = league_to.sort_values(ascending=False).head(5)

# Profits?
diff_league = top5sell_league - top5buy_league
diff_league = diff_league.sort_values(ascending=False)

# Summary
league_summary = pd.concat([top5sell_league, top5buy_league], axis=1)
league_summary = league_summary.assign(diff=diff_league)
new_columns = league_summary.columns.values
new_columns[[0, 1]] = ['sell', 'buy']
league_summary.columns = new_columns

# Analyzing clubs
# Sellers
club_from_sum = data.groupby(['Team_from'])['Transfer_fee'].sum()
club_from_count = data.groupby(['Team_from'])['Transfer_fee'].count()
club_from_mean_price = (club_from_sum/1000000) / club_from_count

# Buyers
club_to_sum = data.groupby(['Team_to'])['Transfer_fee'].sum()
club_to_count = data.groupby(['Team_to'])['Transfer_fee'].count()
club_to_mean_price = (club_to_sum/1000000) / club_to_count

# Profits?
diff_club = club_from_sum - club_to_sum
diff_club = diff_club.sort_values(ascending=False)
diff_club = diff_club.dropna()

# Summary Top and Bottom 15 for clubs
# Total sum of sales
club_from_sum = club_from_sum.sort_values(ascending=False)
club_from_sum.head(15)
club_from_sum.tail(15)

# Mean price of a sale
club_from_mean_price = club_from_mean_price.sort_values(ascending=False)
club_from_mean_price.head(15)
club_from_mean_price.tail(15)

# Total sum of buys
club_to_sum = club_to_sum.sort_values(ascending=False)
club_to_sum.head(15)
club_to_sum.tail(15)

# Mean price of a buy
club_to_mean_price = club_to_mean_price.sort_values(ascending=False)
club_to_mean_price.head(15)
club_to_mean_price.tail(15)

# Profits / Loses
diff_club.head(15)
diff_club.tail(15)

# Visualize
visual = diff_club.head(15)
visual = visual/1000000
millions = np.array(visual.values).tolist()
teams = np.array(visual.index.values).tolist()
ind = np.arange(len(teams))
plt.bar(ind, millions)
plt.xticks(ind, teams, rotation=90)
plt.show()
