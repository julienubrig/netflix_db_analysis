import pandas as pd

# 1) Importation du csv et création du DataFrame
def import_csv(file):
    data = pd.read_csv(file, encoding='latin-1')
    df = pd.DataFrame(data)
    df_wip = df.copy()
    return df_wip

# 2) Cleaning du DataFrame
def clean_df(df_wip):
    # Vérification du contenu des colonnes
    # print(df_wip.info())

    # Sélection des colonnes utiles
    df_wip = df_wip[['show_id','type','title','director','cast','country','date_added','release_year','rating','duration','listed_in','description']]

    # Vérification de la colonne show_id (ni valeur nulle, ni doublon)
    # print(df_wip.info())
    # print(df_wip.duplicated().sum())

    # Mise en place de l'index sur show_id
    df_wip.set_index('show_id', inplace=True)

    # Vérification des types des colonnes
    # df_wip.info()
    # print(df_wip['date_added'])

    # Conversion de 'date_added' : str -> date (avec suppression des espace en début de chaîne)
    df_wip['date_added'] = pd.to_datetime(df_wip['date_added'].str.strip(), format='%B %d, %Y')

    # Vérification des valeurs uniques de la colonne 'type'
    # print(df_wip['type'].value_counts())

    # Vérification du format de la colonne 'duration' en fonction du 'type'
    # print(df_wip.groupby('type')['duration'].apply(list))

    # Création d'une colonne indiquant la durée en minute des films 
    df_wip['duration (movies)'] = df_wip.loc[df_wip['type'] == 'Movie', 'duration'].str.split(' ').str[0].astype(float)
    # Création d'une colonne indiquant le nombre de saisons des séries 
    df_wip['seasons (TV Shows)'] = df_wip.loc[df_wip['type'] == 'TV Show', 'duration'].str.split(' ').str[0].astype(float)
    # Suppression de la colonne 'duration'
    df_wip = df_wip[['type','title','director','cast','country','date_added','release_year','rating','duration (movies)','seasons (TV Shows)','listed_in','description']]

    # Suppression des colonnes explosées du DataFrame principal
    df_wip = df_wip[['type','title','director','date_added','release_year','rating','duration (movies)','seasons (TV Shows)','description']]

    # Création de colonnes Année, Mois et Jour de la semaine
    df_wip['Année'] = df_wip['date_added'].dt.year.astype('Int64')
    df_wip['Mois'] = df_wip['date_added'].dt.month.astype('Int64')
    df_wip['Jour de la semaine'] = df_wip['date_added'].dt.day_name()

    return df_wip

# Création de DataFrames
def countries_df(df_wip):
    # Séparation des pays pour les lignes contenant plusieurs pays
    df_wip['countries'] = df_wip['country'].str.split(',').to_list()
    # Création d'un DataFrame avec une ligne par pays
    countries_exploded = df_wip.explode('countries')[['countries']]
    countries_exploded.name = 'countries'
    return countries_exploded

def categories_df(df_wip):
    # Séparation des catégories pour les lignes contenant plusieurs catégories
    df_wip['categories'] = df_wip['listed_in'].str.split(',').to_list()
    # Création d'un DataFrame avec une ligne par catégorie
    categories_exploded = df_wip.explode('categories')[['categories']]
    return categories_exploded

def casting_df(df_wip):
    # Séparation des acteurs
    df_wip['casting'] = df_wip['cast'].str.split(',').to_list()
    # Création d'un DataFrame avec une ligne par acteur
    cast_list = df_wip.explode('casting')[['casting']]
    return cast_list