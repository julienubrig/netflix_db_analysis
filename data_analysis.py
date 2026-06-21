import pandas as pd

# Détermination du nombre de séries
def count_tv_shows(df):
    nb_tv_shows = len(df[df['type'] == 'TV Show'])
    return nb_tv_shows


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


# Détermination du top 5 des comédiens les plus plébiscités
def top5_acteurs(df):
    df['casting'] = df['casting'].str.strip()
    casting_count = df['casting'].value_counts().head(5)
    return casting_count


# Détermination de la réparition des jours d'ajouts
def repartition_jours_semaine(df):
    return df['Jour de la semaine'].value_counts()