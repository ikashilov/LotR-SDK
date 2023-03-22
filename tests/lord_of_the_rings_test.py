import unittest
from unittest.mock import MagicMock, patch
from src.lord_of_the_rings.lord_of_the_rings import LordOfTheRings


class TestLordOfTheRings(unittest.TestCase):
    def setUp(self):
        self.token = 'my_token'
        self.headers = {'authorization': f'Bearer {self.token}'}

    @patch('requests.session')
    def test_init(self, mock_session):
        session = MagicMock()
        mock_session.return_value = session

        api = LordOfTheRings(token=self.token)

        self.assertEqual(api.token, self.token)
        self.assertEqual(api.session, session)
        self.assertEqual(api.session.headers, self.headers)

    @patch.object(LordOfTheRings, '_request')
    def test_movies_list(self, mock_request):
        api = LordOfTheRings(token=self.token)

        api.movies_list()

        mock_request.assert_called_once_with('movie')

    @patch.object(LordOfTheRings, '_request')
    def test_movie(self, mock_request):
        api = LordOfTheRings(token=self.token)
        movie_id = '123'

        api.movie(movie_id)

        mock_request.assert_called_once_with(f'movie/{movie_id}')

    @patch.object(LordOfTheRings, '_request')
    def test_movie_quotes(self, mock_request):
        api = LordOfTheRings(token=self.token)
        movie_id = '123'

        api.movie_quotes(movie_id)

        mock_request.assert_called_once_with(f'movie/{movie_id}/quote')

    def test_add_optional_params(self):
        api = LordOfTheRings(token=self.token)

        # Test with all string parameters provided
        limit = 10
        page = 2
        offset = 20
        sort = 'name:asc'
        filters = 'budgetInMillions<100'
        expected_params = f'?limit={limit}&page={page}&offset={offset}&sort={sort}&{filters}'
        result_params = api.add_optional_params(limit=limit, page=page, offset=offset, sort=sort, filters=filters)
        self.assertEqual(result_params, expected_params)

        # Test with no parameters provided
        expected_params = ''
        result_params = api.add_optional_params()
        self.assertEqual(result_params, expected_params)

        # Test with some parameters provided
        limit = 10
        sort = 'name:desc'
        expected_params = f'?limit={limit}&sort={sort}'
        result_params = api.add_optional_params(limit=limit, sort=sort)
        self.assertEqual(result_params, expected_params)

        # Test with 'filters' as a list parameter provided
        filters = ['runtimeInMinutes>=160', 'academyAwardWins>0']
        expected_params = f'?{filters[0]}&{filters[1]}'
        result_params = api.add_optional_params(filters=filters)
        self.assertEqual(result_params, expected_params)
