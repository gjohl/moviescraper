import re
import pandas as pd

from data.webpage_text import WINNERS_TEXT, NOMINEES_TEXT
from utils.constants import WINNERS_FPATH, NOMINEES_FPATH


def get_best_picture_winners(text=WINNERS_TEXT):
    """
    Return a list of Best Picture Oscar Winners by Year.

    This munges data from the imdb list and saves the result to a CSV file.

    Parameters
    ----------
    text: str
        The page text copied from the imdb website.

    Returns
    -------
    df: pd.DataFrame
        Columns: year, title
    """
    regexp = re.compile(r'^[0-9]+\.')

    text_list = text.split('\n')
    filtered_list = [k for k in text_list if regexp.search(k)]
    pruned_list = [k.split('. ')[1].replace('(I) ', '') for k in filtered_list]
    title_list = [k[:-7] for k in pruned_list]
    year_list = [k[-5:-1] for k in pruned_list]

    df = pd.DataFrame({'year': year_list, 'title': title_list})
    df.to_csv(WINNERS_FPATH, index=False)
    return df


def get_best_picture_nominees(text=NOMINEES_TEXT):
    """
    Return a list of Best Picture Oscar nominees by Year.

    This munges data from the imdb list and saves the result to a CSV file.

    Parameters
    ----------
    text: str
        The page text copied from the imdb website.

    Returns
    -------
    df: pd.DataFrame
        Columns: year, title
    """
    regexp = re.compile(r'^[0-9]+\.')

    text_list = text.split('\n')
    filtered_list = [k.split('\t')[0] for k in text_list if regexp.search(k)]
    pruned_list = [re.split(r'\d+\. ', k)[1].replace('(I) ', '').replace('(II) ', '') for k in filtered_list]

    title_list = [re.split(r'\(\d{4}\)', k)[0].strip() for k in pruned_list]
    year_list = [k.split('(')[-1][:-1] for k in pruned_list]

    df = pd.DataFrame({'year': year_list, 'title': title_list})
    df.to_csv(NOMINEES_FPATH, index=False)
    return df
