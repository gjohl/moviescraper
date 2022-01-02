from imdb import IMDb
import pandas as pd

from utils.constants import NOMINEES_FPATH


['localized title', 'cast', 'genres', 'runtimes', 'countries', 'country codes', 'language codes',
 'color info', 'aspect ratio', 'sound mix', 'certificates', 'original air date', 'rating', 'votes',
 'cover url', 'imdbID', 'plot outline', 'languages', 'title', 'year', 'kind', 'original title',
 'director', 'writer', 'producer', 'composer', 'cinematographer', 'editor', 'editorial department',
 'production design', 'art direction', 'costume designer', 'production manager', 'assistant director',
 'art department', 'sound crew', 'visual effects', 'camera and electrical department', 'casting department',
 'costume department', 'location management', 'music department', 'transportation department',
 'miscellaneous crew', 'thanks', 'akas', 'production companies', 'distributors', 'other companies',
 'plot', 'synopsis', 'canonical title', 'long imdb title', 'long imdb canonical title', 'smart canonical title',
 'smart long imdb canonical title', 'full-size cover url']


def get_imdb_info(movie_title):
    """
    Search imdb for the given movie title and get interesting info.

    Parameters
    ----------
    movie_title: str
        The title of the movie to query.

    Returns
    -------
    dict
    """
    ia = IMDb()

    # Find the movie
    movies = ia.search_movie(movie_title)
    movie_id = movies[0].movieID
    movie = ia.get_movie(movie_id)

    # Find supplementary info
    metascore = ia.get_movie_critic_reviews(movie_id).get('data', {'metascore': 0}).get('metascore', 0)
    vote_details = ia.get_movie_vote_details(movie_id).get('data', {})
    certifications_by_country = movie.get('certificates', ['United Kingdom:Unknown'])
    certification = [k for k in certifications_by_country if 'United Kingdom' in k][0].split(':')[-1]

    res_dict = {
        'plot_outline': movie.get('plot outline', ''),
        'genres': movie.get('genres', []),
        'runtimes': int(movie.get('runtimes', [0])[0]),
        'rating': movie.get('rating', 0),
        'metascore': metascore,
        'votes': movie.get('votes', 0),
        'director': movie.get('director', [{'name': ''}])[0]['name'],
        'cover_url': movie.get('full-size cover url', ''),
        'vote_details': vote_details,
        'certification': certification
    }

    return res_dict


def get_nominees_by_year(year):
    """
    Get the list of nominees released in a given year.

    Parameters
    ----------
    year: int
        The year to query

    Returns
    -------
    list of str
        The list of movie titles nominated in the given year
    """
    df = pd.read_csv(NOMINEES_FPATH)
    return df.query("year == @year")['title'].tolist()
