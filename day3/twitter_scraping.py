import nest_asyncio
import twint
nest_asyncio.apply()

def twitter_twint(search_word: str) -> DataFrame:
    """
    Returns the search result from twitter

    :param search_word: str - word to be searched in twitter
    :return: dataframe - raw search rseult from twitter
    """
    try:
        c = twint.Config()
        c.Search = "depression"
        c.Since = "2021-01-01"
        c.Until = "2021-12-31"
        c.Lang = "en"
    except Exception as e:
        print(e)


if __name__ == "__main__":
    pass
