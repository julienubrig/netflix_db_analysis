import pandas as pd

# Détermination du nombre de séries
def count_shows(df):
    nb_shows = len(df)
    return nb_shows


# Détermination de la répartition films/séries
def repartition_films_series(df):
    pourc_films = round(len(df[df['type'] == 'Movie']) / len(df) * 100, 2)
    pourc_series = round(len(df[df['type'] == 'TV Show']) / len(df) * 100, 2)

    return pourc_films, pourc_series


# Détermination des ajouts par année
def repartition_ajouts_par_annee(df):
    df_films_par_annee = df.groupby('Année')['Année'].count()
    return df_films_par_annee


# Détermination du top 5 des séries
def top5_series(df):
    df['categories'] = df['categories'].str.strip()
    categories_count = df['categories'].value_counts().head(5)
    return categories_count


# Détermination du top 5 des comédiens les plus plébiscités aux Etats-Unis
def top5_acteurs(df_casting, df_countries):
    df_wip = pd.merge(df_casting, df_countries, on='show_id')
    df_wip = df_wip[df_wip['countries'] == 'United States']
    df_wip['casting'] = df_wip['casting'].str.strip()
    casting_count = df_wip['casting'].value_counts().head(5)
    return casting_count


# Détermination de la répartition des jours d'ajouts
def repartition_jours_semaine(df):
    return df['Jour de la semaine'].value_counts()


# Détermination du top 5 des pays où sont produits les documentaires
def top5_pays_documentaires(df_categories, df_countries):
    df_pays_documentaires = df_categories.merge(df_countries, on='show_id')
    df_pays_documentaires_only = df_pays_documentaires[df_pays_documentaires['categories'] == 'Documentaries']
    top5_pays_docu = df_pays_documentaires_only.value_counts('countries').head(5)
    return top5_pays_docu


# Détermination du nombre moyen de saisons par série
def moy_saisons(df):
    df_wip = df.copy()
    moy_saisons = round(df_wip['seasons (TV Shows)'].mean(),2)
    return moy_saisons


# Détermination de la distribution des films selon leur durée
def distri_films(df):
    df_wip = df.copy()
    df_wip_movies = df_wip[df_wip['type'] == 'Movie']
    distri_films = df_wip_movies['duration (movies)'].quantile([0,0.25,0.50,0.75,1])
    return distri_films


# Détermination du nombre de séries avec thématique sur la drogue
def series_drogue(df):
    df_wip = df.copy()
    df_series_drogue = df_wip[df_wip['description'].str.contains('drug')]
    nb_series_drogue = len(df_series_drogue)
    return nb_series_drogue