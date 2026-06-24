📘 Netflix Dataset Analysis

Overview

This project analyzes the Netflix Movies and TV Shows dataset (Kaggle) to extract insights about:
  Film vs TV Show distribution
  Most common categories
  Most frequent actors (US productions)
  Countries producing the most documentaries
  Film duration distribution
  Trends over time (year, weekday)
  Topic‑based filtering

The workflow is split into three modules:
  main.py — runs the full pipeline
  data_loading_cleaning.py — import & preprocessing
  data_analysis.py — analytical functions

Project Structure
  Code
  ├── main.py
  ├── data_loading_cleaning.py
  ├── data_analysis.py
  ├── netflix_titles.csv
  └── README.md
    
Installation
  pip install pandas
    
Download the Kaggle dataset and place it as:
  netflix_titles.csv

Usage
  Run the full analysis:
  python main.py
  The script loads the dataset, cleans it, generates exploded DataFrames (countries, categories, casting), and prints all results.

Data Processing

  Cleaning
    Converts date_added to datetime
    Extracts film duration (minutes)
    Extracts number of seasons for TV shows
    Creates Year, Month, Day of the week

  Exploded DataFrames
    countries_df → one row per country
    categories_df → one row per category
    casting_df → one row per actor

Analysis
  Total number of titles
  Film vs TV Show ratio
  Titles added per year
  Top 5 categories
  Top 5 actors in US productions
  Additions by weekday
  Top 5 documentary‑producing countries
  Average number of seasons
  Film duration quantiles
  Number of drug‑related series

Example Output
  Total titles: 8807
  Movies: 69.6% / TV Shows: 30.4%
  Top categories: International Movies, Dramas, Comedies...
  Top actors (US): Robert De Niro, Tom Hanks...
  Top documentary countries: United States, India...
  Average seasons: 1.7
  Film duration quantiles: 40–240 min
  Drug‑related series: 37

Author
  Julien Ubrig  
  Python Developer & Data Analyst — Strasbourg, France
