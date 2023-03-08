import urllib.parse
import requests


def format_for_url(text: str) -> str:
    """
    convert to url format

    :param text: str to convert
    :return: str url compatible
    """
    return urllib.parse.quote_plus(text)


def http_request(url: str) -> object:
    """
    do a get http request

    :param url: str url to reach
    :return: object response from url
    """
    return requests.get(url)


def is_valid_number(text: str) -> bool:
    """
    str is convertible in int True if not False

    :param text: str to convert
    :return: bool
    """
    try:
        int(text)
        return True
    except ValueError:
        return False


def create_query_url(base_url: str, api_key: str, query: str, number_of_result: str) -> str:
    """
    create an url for GIPHY API

    :param base_url: str domain to reach
    :param api_key: str needed for use GIPHY API
    :param query: str user query
    :param number_of_result: str user wanted results
    :return: str complete url ready to use GIPHY API
    """
    return f"{base_url}api_key={api_key}&q={query}&limit={number_of_result}" \
           f"&offset=0&rating=g&lang=en"
