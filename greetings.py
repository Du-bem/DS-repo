def say_hello():
    print('Cześć!')

if __name__ == '__main__':          # <-- If code isn't top-level, it shouldn't run on main
    say_hello()

animal = ['goat', 'cat', 'pig', 'dog', 'snail']
if animal[0] == 'goat':
    print('Is')
else:
    pass



"""# Define timer in seconds
start_time = time.time()
time_limit = 60
"""

# import numpy as np
import pandas as pd

# sorting
homelessness = pd.read_csv("homelessness.csv")
homelessness_ind_st = homelessness.sort_values(by=["individuals", "state"], ascending=[False, True])
# print(homelessness_ind_st.head(5))

# sorting rows by categorical variables
canu = ["California", "Arizona", "Nevada", "Utah"]
mojave_desert_homelessness = homelessness[homelessness["state"].isin(canu)]
# print(mojave_desert_homelessness)

# Create column for homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"]/homelessness["state_pop"]
# Subset for values > 20 and sort in descending order
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]
high_homelessness_srt = high_homelessness.sort_values(by="individuals", ascending=False)
result = high_homelessness_srt[["state", "indiv_per_10k"]]
# print(result)


# SUMMARY STATISTICS (Numeric variables)
def iqr(v):
    return v.quantile(0.75) - v.quantile(0.25)

# Print the iqr and median of 3 columns in sales
sales = pd.read_csv("walmart.csv")
sales_iqr_med = sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, "median"])
# print(sales_iqr_med)

# Create a df that contains the sales data on department 1 of store 1
sales_1_1 = sales.query('store == 1 and department == 1')
# print(len(sales.query('store == 1 and department == 1')))

sales_1_1 = sales_1_1.sort_values('date')
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()
# print(sales_1_1[['date', 'weekly_sales', 'cum_weekly_sales', 'cum_max_sales']])

# SUMMARY STATISTICS (Categorical variables)
# Dropping duplicates
store_types = sales.drop_duplicates(subset=["store", "type"])
# print(store_types.head(5))
store_depts = sales.drop_duplicates(subset=["store", "department"])
# print(store_depts.head(5))
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset="date")
# print(holiday_dates["date"].head())

# Counting categorical variables
store_counts = store_types["type"].value_counts()       # no. of stores
# print(store_counts)
store_props = store_types["type"].value_counts(normalize=True)      # proportion of stores
# print(store_props)
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
# print(dept_counts_sorted.head())
dept_props_sorted = store_depts["department"].value_counts(normalize=True, sort=True)
# print(dept_props_sorted.head())

# GROUPED SUMMARY STATISTICS
# aggregate weekly_sales: get stats of each store type
sales_stats = sales.groupby("type")["weekly_sales"].agg(['min', 'max', 'mean', 'median'])
# print(sales_stats.head(4))
# aggregate unemployment and fuel price: get stats of each store type
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg(['min', 'max', 'mean', 'median'])
# print(unemp_fuel_stats.head(4))

# PIVOT TABLES
# Pivot for mean and median weekly_sales by store type and holiday
mean_med_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday", aggfunc=["mean", "median"])
# print(mean_med_sales_by_type_holiday.head(4))

# Pivot for mean weekly_sales by dept and type; fill missing values; sum all rows and columns
mean_sales_by_dept_type = sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value="None", margins=True)
# print(meanemissions__sales_by_dept_type.tail(4))

# EXPLICIT INDEXES
temperatures = pd.read_csv("temperatures.csv")
# setting indexes
temperatures_ind = temperatures.set_index("city")
# print(temperatures_ind.head(4))
# resetting indexes: False keeps values; True drops values
# print(temperatures_ind.reset_index(drop=False).head(4))

# subsetting with .loc comparison
cities = ["Moscow", "Saint Petersburg"]
# print(temperatures[temperatures["city"].isin(cities)].tail(4))
# print(temperatures_ind.loc[cities].tail(4))

# multi-level indexes
temperatures_indx = temperatures.set_index(["country", "city"])
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]
# print(temperatures_indx.loc[rows_to_keep].tail(4))

# sorting by index values
# print(temperatures_indx.sort_index(level=["country", "city"], ascending=[True, False]).head(4))

# SLICING/SUBSETTING WITH .LOC/.ILOC
# Use .loc on temperatures_indx to slice temps from Lahore to Moscow
temperatures_srt = temperatures_indx.sort_index()
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")].tail(3))
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")].head(3))
print(temperatures_srt.loc[:, "date":"avg_temp_c"].head(3))
print(temperatures_srt.loc[("India", "Hyderabad"):("Pakistan", "Baghdad"), "date":"avg_temp_c"].head(3))
x = 1j
print('foo' if (256).bit_length() > 8 else 'bar')

import math

claim = "Pluto is a planet"
words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(day, month, year)
print('/'.join([day, month, year]))

planet = "Pluto"
galaxy = "Milky Way"
print("{} is a dwarf planet in the {} galaxy.".format(planet, galaxy))

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))

# DICTIONARY COMPREHENSION
big_six = ["Man United", "Liverpool", "Arsenal", "Chelsea", "Man City", "Tottenham"]
big_six_initial = {club: club[0] for club in big_six}
big_six_final = {club: club[-1] for club in big_six}
print(big_six_initial,
      big_six_final)

for club, final in big_six_final.items():
    print("{} ends in a \"{}\"".format(club.ljust(10), final.upper()))        # rjust = right justified

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    "">>> word_search(doc_list, 'casino')
    "">>> [0]""
    """
    indices = []
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalize = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalize:
            indices.append(i)
    return indices


doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville", "Casino"]
print(word_search(doc_list, 'casino'))

print(f"pi to four significant figures = {(math.pi):.4}")   # "pi to four significant figures = {:.4}".format(math.pi)


