Movie Recommendation System

A Python-based Movie Recommendation System that suggests movies similar to a given one using collaborative filtering based on user ratings. The system leverages statistical correlation between movie ratings to find similar films and identify user preferences.

🧠 Overview

This project analyzes movie rating data to recommend movies similar to those a user likes. It uses the MovieLens dataset, performs data cleaning, merging, aggregation, and computes Pearson correlation between movie rating vectors to identify relationships between films.

⚙️ Features

📊 Data analysis and visualization of movie ratings

🎥 Recommend similar movies based on user preferences

📈 Uses correlation to find similar rating patterns

💡 Works with real-world MovieLens dataset

🧩 Easy to modify for personalized recommendation engines

🧰 Technologies Used

Python 3.x

NumPy – for numerical computation

Pandas – for data manipulation and analysis

📁 Project Structure
Movie_Recommendation_System/
│
├── Movie_Recommendation_System.py    # Main program script
├── u.data                            # Dataset: user_id, item_id, rating, timestamp
├── Movie_Id_Titles (1).csv           # Dataset: movie_id and movie titles
└── README.md                         # Project documentation

🧩 How It Works

Load the dataset

Reads user ratings and movie titles from CSV files.

Merges them into a single DataFrame based on item_id.

Compute statistics

Calculates average ratings per movie.

Counts the number of ratings each movie received.

Create a pivot table

Rows: user IDs

Columns: movie titles

Values: ratings

Find movie correlations

Measures how similar each movie’s ratings are to another (e.g., Star Wars (1977)).

Filters results to show only movies with a significant number of ratings.

🚀 Example Output
Top movies similar to Star Wars (1977):

                       Correlation  no_of_ratings
Star Wars (1977)          1.000000            583
Empire Strikes Back       0.748193            368
Return of the Jedi        0.680987            507
Raiders of the Lost Ark   0.654321            420
...

🧪 How to Run
1️⃣ Clone the repository
git clone https://github.com/<your-username>/movies-recommendation-system.git
cd movies-recommendation-system

2️⃣ Install dependencies
pip install pandas numpy

3️⃣ Run the script
python Movie_Recommendation_System.py

📊 Dataset

This project uses the MovieLens 100k dataset, which contains:

100,000 ratings from 943 users on 1,682 movies.

Each user has rated at least 20 movies.

Dataset source: MovieLens Dataset

🧭 Future Improvements

Add a user interface (web or command-line based)

Implement content-based filtering (using genres, keywords, etc.)

Integrate with TMDB API for richer metadata

Use machine learning models (e.g., SVD, KNN, or neural collaborative filtering)
