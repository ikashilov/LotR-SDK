"""
This module provides a simple Python wrapper for The One API, a RESTful web service that provides data about The Lord of the Rings universe.

Usage:

    from lord_of_the_rings import LordOfTheRings

    # Create a new instance of the API wrapper with your access token
    lotr = LordOfTheRings('your_access_token')

    # Call API methods to retrieve data
    movies = lotr.movies_list()
    movie = lotr.movie('movie_id')
    quotes = lotr.movie_quotes('movie_id')

API documentation: https://the-one-api.dev/documentation
"""

import requests
from typing import List, Optional, Union

BASE_URL = 'https://the-one-api.dev/v2'


class LordOfTheRings:

    def __init__(self, token):
        """Initializes a new instance of the MyAPI client.

         Args:
             token (str): The access token to use for LotR API. Read here: https://the-one-api.dev/documentation
         """
        self.base_url = BASE_URL
        self.token = token
        self.session = requests.session()
        self.session.headers = {'authorization': f'Bearer {token}'}

    def _request(self, path: str, limit: Optional[int] = None, page: Optional[int] = None, offset: Optional[int] = None,
                 sort: Optional[str] = '', filters: Optional[Union[str, List[str]]] = None) -> requests.Response:
        """Send a request to the LotR API endpoint.

        Args:
            path (str): The endpoint path.
            limit (int, optional): The maximum number of results to return. Defaults to ''.
            page (int, optional): The page number of results to return. Defaults to ''.
            offset (int, optional): The number of results to skip. Defaults to ''.
            sort (str, optional): The field to sort the results by. Defaults to ''.
            filters (Union[str, List[str]], optional): The filters to apply to the results.
                If a string is passed, it is included in the query string without modification.
                If a list is passed, each element is included in the query string with a '&' separator.
                Defaults to None.

        Returns:
            requests.Response: The response object returned by the API.
        """
        params = self.add_optional_params(limit, page, offset, sort, filters)
        url = f'{self.base_url}/{path}{params}'
        return self.session.get(url)

    @staticmethod
    def add_optional_params(limit: Optional[int] = None, page: Optional[int] = None, offset: Optional[int] = None,
                            sort: Optional[str] = '', filters: Optional[Union[str, List[str]]] = None) -> str:
        """Constructs a query string from optional parameters.

        Args:
            limit (int, optional): The maximum number of results to return. Defaults to None.
            page (int, optional): The page number of results to return. Required parameter.
            offset (int, optional): The number of results to skip. Defaults to ''.
            sort (str, optional): The field to sort the results by. Defaults to ''.
            filters (Union[str, List[str]], optional): The filters to apply to the results.
                If a string is passed, it is included in the query string without modification.
                If a list is passed, each element is included in the query string with a '&' separator.
                Defaults to None.

        Returns:
            str: The constructed query string.
        """

        params = ''
        if limit:
            params += f'limit={limit}&'
        if page:
            params += f'page={page}&'
        if offset:
            params += f'offset={offset}&'
        if sort:
            params += f'sort={sort}&'
        if filters:
            if isinstance(filters, list):
                params += '&'.join(filters)
            else:
                params += filters

        if params and params[-1] == '&':
            params = params[:-1]

        return f'?{params}' if params else ''

    def movies_list(self, *args, **kwargs) -> requests.Response:
        """Returns a list of all movies in the API.

        Args:
            *args: Additional positional arguments to pass to the underlying HTTP request.
            **kwargs: Additional keyword arguments to pass to the underlying HTTP request.

        Returns:
            requests.Response: The HTTP response object.
        """
        return self._request('movie', *args, **kwargs)

    def movie(self, movie_id: str, *args, **kwargs) -> requests.Response:
        """Returns details for a specific movie.

        Args:
            movie_id (str): The ID of the movie to retrieve.
            *args: Additional positional arguments to pass to the underlying HTTP request.
            **kwargs: Additional keyword arguments to pass to the underlying HTTP request.

        Returns:
            requests.Response: The HTTP response object.
        """
        return self._request(f'movie/{movie_id}', *args, **kwargs)

    def movie_quotes(self, movie_id: str, *args, **kwargs) -> requests.Response:
        """Returns a list of quotes for a specific movie.

        Args:
            movie_id (str): The ID of the movie to retrieve quotes for.
            *args: Additional positional arguments to pass to the underlying HTTP request.
            **kwargs: Additional keyword arguments to pass to the underlying HTTP request.

        Returns:
            requests.Response: The HTTP response object.
        """
        return self._request(f'movie/{movie_id}/quote', *args, **kwargs)
