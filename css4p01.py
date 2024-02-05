import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt



# Read the movie data from a CSV file
data = pd.read_csv("movie_dataset.csv")


# Check for missing values
missing_values = data.isnull().sum()
print("Missing values in each column:\n", missing_values)


# Print the first 5 rows of the data
print("\nFirst 5 rows of the data:\n", data.head())


# Describe the numerical columns of the data
print("\nDescriptive statistics of numerical columns:\n", data.describe())


# Find the highest rated movie
highest_rated_movie = data.iloc[data['Rating'].idxmax()]
print("\nHighest rated movie:")
print(highest_rated_movie)


# Calculate the average revenue of all movies
average_revenue = data['Revenue (Millions)'].mean()
print("\nAverage revenue of all movies:", average_revenue)


# Calculate the average revenue of movies from 2015 to 2017
average_revenue_2015_2017 = data[data.Year.between(2015, 2017)]['Revenue (Millions)'].mean()
print("\nAverage revenue of movies from 2015 to 2017:", average_revenue_2015_2017)


# Count movies released in 2016
num_movies_2016 = len(data[data.Year == 2016])
print("\nNumber of movies released in 2016:", num_movies_2016)


# Count movies directed by Christopher Nolan
num_movies_by_nolan = len(data[data['Director'] == 'Christopher Nolan'])
print("\nNumber of movies directed by Christopher Nolan:", num_movies_by_nolan)


# Count movies with a rating of at least 8.0
num_high_rated_movies = len(data[data.Rating >= 8])
print("\nNumber of movies with a rating of at least 8.0:", num_high_rated_movies)


# Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan = data[data['Director'] == 'Christopher Nolan'].Rating.median()
print("\nMedian rating of movies directed by Christopher Nolan:", median_rating_nolan)


# Find the year with the highest average rating
year_highest_rating = data.groupby('Year')['Rating'].mean().idxmax()
print("\nYear with the highest average rating:", year_highest_rating)


# Calculate the percentage increase in the number of movies between 2006 and 2016
starting_value = len(data[data.Year == 2006])
end_value = len(data[data.Year == 2016])
percentage_increase = ((end_value - starting_value) / starting_value) * 100
print("\nPercentage increase in number of movies from 2006 to 2016:", percentage_increase)


# Find the most common actor
from statistics import mode
names = []
for i in data.Actors:
    for x in i.split(","):
        names.append(x)
most_common_actor = mode(names)
print("\nMost common actor:", most_common_actor)


# Analyze unique genres
data["Genre"] = data["Genre"].apply(lambda x: x.split(","))
genre = data.Genre.explode()
genre_counts = genre.value_counts()
most_common_genre = genre_counts.idxmax()
print("\nMost common genre:", most_common_genre)


# Analyze correlations
numerical_data = data.select_dtypes(include=['int64', 'float64'])
sns.heatmap(numerical_data.corr(numeric_only=True), annot=True)

# Plot specific correlations
sns.scatterplot(data=data, x="Votes", y="Revenue (Millions)")
plt.show()


# Observations and advice
# ... (You can add your observations and advice here based on the analysis)


# Pairplot for further exploration
sns.pairplot(data)
plt.show()

