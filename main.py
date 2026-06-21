import data_loading_cleaning
import data_analysis

# Importation du csv et création du DataFrame
df = data_loading_cleaning.import_csv('netflix_titles.csv')

# Cleaning et création des DataFrames
cleaned_df = data_loading_cleaning.clean_df(df)
countries_df = data_loading_cleaning.countries_df(df)
categories_df = data_loading_cleaning.categories_df(df)
casting_df = data_loading_cleaning.casting_df(df)

# Analyse des données

# 1) Compter le nombre de séries
nb_series = data_analysis.count_tv_shows(cleaned_df)
print(f"Nombre de séries dans le Dataset : {nb_series}")
print()

# 2) Déterminer la répartition Films/Séries
pourc_films, pourc_series = data_analysis.repartition_films_series(cleaned_df)
print(f"Répartition films/séries : Films : {pourc_films} % / Séries : {pourc_series} %")
print()

# 3) Répartition des ajouts en fonction de l'année
df_films_par_annee = data_analysis.repartition_ajouts_par_annee(cleaned_df)
print("Répartition des films par année :")
for films, annee in df_films_par_annee.items():
    print(f"{films} : {annee}")
print()

# 4) Top 5 des catégories de séries 
top5_series = data_analysis.top5_series(categories_df)
print("Top 5 des catégories :")
for category, count in top5_series.items():
    print(f"{category} : {count}")
print()

# 5) Top 5 des comédiens les plus plébiscités
top5_acteurs = data_analysis.top5_acteurs(casting_df)
print("Top 5 des acteurs :")
for acteur, count in top5_acteurs.items():
    print(f"{acteur} apparaît dans {count} films et/ou séries")
print()

# Répartition des ajouts selon le jour de la semaine
# print(cleaned_df)
repartition_ajouts_jours_semaine = data_analysis.repartition_jours_semaine(cleaned_df)
print("Répartition des ajouts par jour de la semaine :")
for day, count in repartition_ajouts_jours_semaine.items():
    pourc_ajout = round(count / len(cleaned_df) * 100, 2)
    print(f"{day} : {pourc_ajout} % des ajouts")
print()
