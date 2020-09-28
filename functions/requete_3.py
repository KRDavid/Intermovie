import pandas as pd

def requete():
    #fichier title
    data_title = pd.read_csv('./data/RAW/title.basics.tsv', sep="\t")
    data_title = data_title.drop(["titleType","primaryTitle","isAdult","startYear","endYear","runtimeMinutes"], axis = 1)
    data_title.set_index('tconst', inplace  = True)
    data_title_clean = data_title.dropna()
    del data_title

    #fichier ratings
    data_ratings = pd.read_csv('./data/RAW/title.ratings.tsv', sep="\t")
    data_ratings = data_ratings.drop(["numVotes"], axis = 1)
    data_ratings.set_index('tconst', inplace  = True)
    data_ratings_clean = data_ratings.dropna()
    del data_ratings

    #fusion des dataframes
    df_intermediaire = data_title_clean.join(data_ratings_clean)
    df_intermediaire = df_intermediaire.reset_index()
    df_intermediaire = df_intermediaire.drop(["tconst"], axis = 1)
    df_intermediaire = df_intermediaire.dropna()
    del data_title_clean
    del data_ratings_clean

    #calcul moyenne
    df_cat = pd.DataFrame
    df_cat = df_intermediaire["genres"].str.split(",", expand=True)
    df_intermediaire = df_intermediaire.join(df_cat).drop(["genres"], axis=1)
    del df_cat
    df_moy1 = df_intermediaire.groupby([0])["averageRating"].mean()
    df_moy2 = df_intermediaire.groupby([1])["averageRating"].mean()
    df_moy3 = df_intermediaire.groupby([2])["averageRating"].mean()
    df_moy = pd.concat([df_moy1, df_moy2, df_moy3], axis = 1, keys = ["moy1", "moy2", "moy3"])
    del df_intermediaire
    del df_moy1
    del df_moy2
    del df_moy3
    df_moy['moy'] = df_moy[['moy1', 'moy2', 'moy3']].mean(axis=1)
    df_moy = df_moy.drop(["moy1", "moy2", "moy3"], axis = 1)

    #convertion en csv
    df_moy.to_csv('./data/OUTPUT/csv_req_3.csv')
    del df_moy