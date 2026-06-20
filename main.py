import data_loading_cleaning
import data_analysis

# Importation du csv et création du DataFrame
df = data_loading_cleaning.import_csv('netflix_titles.csv')

# Cleaning du DataFrame
cleaned_df = data_loading_cleaning.clean_df(df)

print(cleaned_df)