import pandas as pd

from utils.constants import WINNERS_FPATH


def get_random_movie(path=WINNERS_FPATH, unwatched=True):
    """
    Return the title of a movie at random. Optionally only return unwatched movies.

    Parameters
    ----------
    path: str
        Full filepath to spreadsheet containing movies
    unwatched: bool
        Whether to filter to return unwatched movies only.

    Returns
    -------
    dict
        Randomly selected movie.
        Keys are 'year', 'title'
    """
    df = pd.read_csv(path)
    df['watched'] = df['watched'].fillna(0).astype(int)
    if unwatched:
        df = df.query("watched == 0")

    random_row = df[['year', 'title']].sample()

    return random_row.to_dict(orient='records')[0]
