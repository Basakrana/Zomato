--importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

--Create dataframe

df = pd.read_csv("Zomato data .csv")
df.head()

---Data cleaning

def rating(value):
    value = str(value).split("/")
    value = value[0]
    return float(value)

df['rate'] = df['rate'].apply(rating)
df.head()

---objectives

plt.figure(figsize = (4,4))
sns.countplot(x = df['listed_in(type)'],legend = False , hue = df['listed_in(type)'],palette = 'Set1')
plt.title('Tota Number of Resturants')
plt.xlabel('Types of returant')
plt.ylabel('Numbers of Resturant')
plt.show()

plt.figure(figsize = (4,3))
grouped_data = df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result,color = "purple",marker=".")
plt.title('Number of votes by resturants')
plt.xlabel('Resturant types')
plt.ylabel('Total votes');

plt.figure(figsize = (5,3))
plt.hist(df['rate'],bins = 10, color = 'cyan',edgecolor = 'black')
plt.title('Rate distribution')
plt.xlabel('Ratings')
plt.ylabel('Number of ratings')

plt.figure(figsize = (10,4))
cd = df['approx_cost(for two people)']
sns.countplot(x = cd,legend = False,hue = cd, palette ='Set1')
plt.title('Cost per Couple')
plt.xlabel('Avg cost for two people')
plt.ylabel('number of people');

plt.figure(figsize = (4,3))
sns.boxplot(x='online_order',y = 'rate',data = df,showfliers = False,legend = False, hue = 'online_order',palette = 'cool');

plt.figure(figsize = (4,4))
pivot_table = df.pivot_table(index = 'listed_in(type)', columns = 'online_order',aggfunc = 'size', fill_value = 0)
sns.heatmap(pivot_table,annot = True,cmap = "YlGn",fmt = 'd')
plt.ylabel('Resturat type');
