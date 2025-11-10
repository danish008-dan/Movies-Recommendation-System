# Importing required libraries
import numpy as np                # For numerical operations
import pandas as pd               # For data manipulation


import warnings
warnings.filterwarnings('ignore')


# Defining column names for the dataset
col_name = ['user_id', 'item_id', 'rating', 'timestamp']

# Reading the movie rating dataset (user_id, movie_id, rating, timestamp)
df = pd.read_csv('u.data', sep='\t', names=col_name)
print(df.head())

# Reading movie titles dataset
movie_title = pd.read_csv('Movie_Id_Titles (1)')

# Merging both datasets on 'item_id' (common column)
df = pd.merge(df, movie_title, on='item_id')
print(df.head())

# Calculating the average rating for each movie
ratings = pd.DataFrame(df.groupby('title')['rating'].mean().sort_values(ascending=False))
print(ratings.head())

# Adding a new column 'no_of_ratings' showing how many users rated each movie
ratings['no_of_ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
print(ratings.head())

# Creating a pivot table where:
# Rows = user IDs, Columns = movie titles, Values = ratings
mm = df.pivot_table(index='user_id', columns='title', values='rating')
print(mm.head())

# Extracting user ratings for two specific movies
starwars_rate = mm['Star Wars (1977)']
liar_rate = mm['Liar Liar (1997)']

# Finding correlation between Star Wars and all other movies
same_as_starwars = mm.corrwith(starwars_rate)

# Finding correlation between Liar Liar and all other movies
same_as_liar = mm.corrwith(liar_rate)

# Creating a DataFrame for Star Wars correlations
corr_starwars = pd.DataFrame(same_as_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)

# Adding the number of ratings to the correlation data
corr_starwars = corr_starwars.join(ratings['no_of_ratings'])

# Displaying movies with more than 100 ratings similar to Star Wars, sorted by correlation
print(corr_starwars[corr_starwars['no_of_ratings'] > 100]
      .sort_values('Correlation', ascending=False)
      .head(10))

# Creating a DataFrame for Liar Liar correlations
corr_liar = pd.DataFrame(same_as_liar, columns=['Correlation'])
corr_liar.dropna(inplace=True)

# Adding the number of ratings to the Liar Liar correlation data
corr_liar = corr_liar.join(ratings['no_of_ratings'])

# Displaying movies with more than 100 ratings similar to Liar Liar, sorted by correlation
print(corr_liar[corr_liar['no_of_ratings'] > 100]
      .sort_values('Correlation', ascending=False)
      .head(10))