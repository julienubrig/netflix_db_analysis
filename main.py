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
nb_shows = data_analysis.count_shows(cleaned_df)
print(f"Nombre de shows dans le Dataset : {nb_shows}")
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

# 5) Top 5 des comédiens les plus plébiscités aux Etats-Unis
top5_acteurs = data_analysis.top5_acteurs(casting_df, countries_df)
print("Top 5 des acteurs :")
for acteur, count in top5_acteurs.items():
    print(f"{acteur} apparaît dans {count} films et/ou séries")
print()

# Répartition des ajouts selon le jour de la semaine
repartition_ajouts_jours_semaine = data_analysis.repartition_jours_semaine(cleaned_df)
print("Répartition des ajouts par jour de la semaine :")
for day, count in repartition_ajouts_jours_semaine.items():
    pourc_ajout = round(count / len(cleaned_df) * 100, 2)
    print(f"{day} : {pourc_ajout} % des ajouts")
print()


# Pays dans lesquels sont produits le plus de documentaires
top5_pays_documentaires = data_analysis.top5_pays_documentaires(categories_df, countries_df)
print("Top 5 des pays où sont produits les documentaires :")
for country, count in top5_pays_documentaires.items():
    print(f"{country} : {count}")
print()


# Nombre moyen de saisons par série
df_moy_saisons_series = data_analysis.moy_saisons(cleaned_df)
print(f"Nombre moyen de saisons par série : {df_moy_saisons_series}")
print()


# Distribution des films
distri_films = data_analysis.distri_films(cleaned_df)
print("Distribution des films par durée :")
print(distri_films)
print()


# Nombre de série avec thématique drogue
series_drogue = data_analysis.series_drogue(cleaned_df)
print(f"Nombre de séries ayant la drogue en thématique : {series_drogue}")