import pandas as pd

def requete():
    #fichier title
    data_title1 = pd.read_csv('./data/CURATED/title.basics/movie.csv', sep = ',')
    data_title2 = pd.read_csv('./data/CURATED/title.basics/tvMovie.csv', sep = ',')
    data_title = pd.concat([data_title1, data_title2], axis = 0)
    del data_title1
    del data_title2
    data_title = data_title.drop(["titleType","primaryTitle","isAdult","startYear","endYear","runtimeMinutes","genres"], axis = 1)
    data_title.set_index('tconst', inplace  = True)
    data_title_clean = data_title.dropna()
    del data_title

    #fichier ratings
    data_ratings = pd.read_csv('./data/RAW/title.ratings.tsv', sep="\t")
    data_ratings = data_ratings.drop(["numVotes"], axis = 1)
    data_ratings.set_index('tconst', inplace  = True)
    data_ratings_clean = data_ratings.dropna()
    del data_ratings

    #fichier natio
    data_natio = pd.read_csv('./data/CURATED/title.akas/US.csv', sep=",")
    data_natio = data_natio.dropna()
    data_natio = data_natio.drop(["ordering", "region", "title", "language", "types", "attributes", "isOriginalTitle"], axis=1)
    data_natio_clean = data_natio.set_index('titleId')
    del data_natio

    #fusion des dataframe
    data_natio_clean = data_natio_clean.join(data_title_clean)
    data_final = data_natio_clean.join(data_ratings_clean).reset_index()
    data_final.drop_duplicates(keep = 'first', inplace=True)
    del data_natio_clean

    #convertion en csv
    data_final = data_final.dropna()
    data_final.to_csv("./data/OUTPUT/csv_req_2.csv")
    del data_final