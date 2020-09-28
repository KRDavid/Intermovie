import pandas as pd


def requete():
    #fichier title
    data_title1 = pd.read_csv('./data/CURATED/title.basics/movie.csv', sep = ',')
    data_title2 = pd.read_csv('./data/CURATED/title.basics/tvMovie.csv', sep = ',')
    data_title = pd.concat([data_title1, data_title2], axis = 0)
    del data_title1
    del data_title2
    data_title = data_title.drop(["titleType","originalTitle","isAdult","startYear","endYear","runtimeMinutes","genres"], axis = 1)
    data_title.set_index('tconst', inplace  = True)
    data_title_clean = data_title.dropna()
    del data_title

    #fichier noms
    data_noms = pd.read_csv('./data/RAW/name.basics.tsv', sep="\t")
    data_noms = data_noms.drop(["birthYear", "deathYear"], axis = 1)
    data_noms = data_noms.dropna()
    data_noms = data_noms[["nconst", "primaryName"]][data_noms['primaryProfession'].str.contains('actor|actress', regex=True)]
    data_noms_clean = data_noms.set_index('nconst')
    del data_noms

    #fichier films
    data_films1 = pd.read_csv('./data/CURATED/title.principals/actor.csv', sep=",")
    data_films2 = pd.read_csv('./data/CURATED/title.principals/actress.csv', sep=",")
    data_films = pd.concat([data_films1, data_films2], axis=0)
    del data_films1
    del data_films2
    data_films = data_films.dropna()
    data_films = data_films.drop(["ordering", "job", "characters"], axis = 1)
    data_films_clean = data_films[["tconst", "nconst"]][data_films['nconst'].str.contains('n')]
    del data_films

    #fichier ratings
    data_ratings = pd.read_csv('./data/RAW/title.ratings.tsv', sep="\t")
    data_ratings = data_ratings.drop(["numVotes"], axis = 1)
    data_ratings.set_index('tconst', inplace  = True)
    data_ratings_clean = data_ratings.dropna()
    del data_ratings

    #fusion des dataframes
    data_films_clean.set_index('tconst', inplace  = True)
    data_films_with_title = data_films_clean.join(data_title_clean)
    data_films_with_title = data_films_with_title.join(data_ratings_clean).reset_index().drop(["tconst"], axis = 1)
    del data_films_clean
    del data_title_clean
    del data_ratings_clean
    data_films_with_title.set_index('nconst', inplace  = True)
    data_final = data_films_with_title.join(data_noms_clean).reset_index().drop(["nconst"], axis = 1)
    del data_films_with_title
    del data_noms_clean

    #calcul de la moyenne
    data_final = data_final.dropna()
    data_final = data_final.groupby(["primaryName"]).mean()

    #conversion en csv
    data_final.to_csv('./data/OUTPUT/csv_req_4.csv')
    del data_final