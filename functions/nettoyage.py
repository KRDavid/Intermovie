import pandas as pd

def nettoyage_title_basics():
    #fichier title
    data_title1 = pd.read_csv('./data/CURATED/title.basics/movie.csv', sep = ',')
    data_title2 = pd.read_csv('./data/CURATED/title.basics/tvMovie.csv', sep = ',')
    data_title = pd.concat([data_title1, data_title2], axis = 0)

    data_title = data_title.drop(["titleType","primaryTitle","isAdult","startYear","endYear","runtimeMinutes","genres"], axis = 1)
    data_title.set_index('tconst', inplace  = True)
    data_title_clean = data_title.dropna()
    
    return data_title_clean

def lecture_title_basics():
    #fichier title
    data_title = pd.read_csv('./data/RAW/title.basics.tsv', sep="\t")
    data_title = data_title.drop(["titleType","primaryTitle","isAdult","startYear","endYear","runtimeMinutes"], axis = 1)
    data_title.set_index('tconst', inplace  = True)
    data_title_clean = data_title.dropna()
    
    return data_title_clean

def nettoyage_name_basics():
    #fichier noms
    data_noms = pd.read_csv('./data/RAW/name.basics.tsv', sep="\t")
    data_noms = data_noms.drop(["birthYear", "deathYear"], axis = 1)
    data_noms = data_noms.dropna()
    data_noms = data_noms[["nconst", "primaryName"]][data_noms['primaryProfession'].str.contains('actor|actress', regex=True)]
    data_noms_clean = data_noms.set_index('nconst')
    
    return data_noms_clean

def nettoyage_title_principals():
    #fichier films
    data_films1 = pd.read_csv('./data/CURATED/title.principals/actor.csv', sep=",")
    data_films2 = pd.read_csv('./data/CURATED/title.principals/actress.csv', sep=",")
    data_films = pd.concat([data_films1, data_films2], axis=0)
    
    data_films = data_films.dropna()
    data_films = data_films.drop(["ordering", "job", "characters"], axis = 1)
    data_films_clean = data_films[["tconst", "nconst"]][data_films['nconst'].str.contains('n')]
    
    return data_films_clean

def nettoyage_title_ratings():
    #fichier ratings
    data_ratings = pd.read_csv('./data/RAW/title.ratings.tsv', sep="\t")
    data_ratings = data_ratings.drop(["numVotes"], axis = 1)
    data_ratings.set_index('tconst', inplace  = True)
    data_ratings_clean = data_ratings.dropna()
    
    return data_ratings_clean

def nettoyage_title_akas():
    #fichier natio
    data_natio = pd.read_csv('./data/CURATED/title.akas/US.csv', sep=",")
    data_natio = data_natio.dropna()
    data_natio = data_natio.drop(["ordering", "region", "title", "language", "types", "attributes", "isOriginalTitle"], axis=1)
    data_natio_clean = data_natio.set_index('titleId')

    return data_natio_clean