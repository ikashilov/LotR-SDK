# Python Wrapper for The One API - Lord of the Rings
This module provides a simple Python wrapper for The One API, a RESTful web service that provides data about The Lord of the Rings universe.

## Installation
You can install the module using pip:

```bash
pip install -i https://test.pypi.org/simple/ lord-of-the-rings==0.1.1
```

## Usage
To use this module, you will need an access token for The One API. You can get one by registering at https://the-one-api.dev/signup.

Once you have your access token, you can create a new instance of the API wrapper:

Usage
To use the API wrapper, import the LordOfTheRings class from the module and create a new instance with your API access token:

```python
from lord_of_the_rings import LordOfTheRings
lotr = LordOfTheRings('your_access_token')
```

### Retrieving Data
The wrapper provides several methods for retrieving data from The One API. Here are some examples:

#### Retrieving a List of Movies
```python
movies = lotr.movies_list()
```

#### Retrieving Information About a Specific Movie
```python
movie_id = '5cd95395de30eff6ebccde5c'
movie = lotr.movie(movie_id)
```

#### Retrieving Quotes from a Specific Movie (only working for the LotR trilogy)
```python
movie_id = '5cd95395de30eff6ebccde5c'
quotes = lotr.movie_quotes(movie_id)
```

#### Optional Parameters
The API methods accept several optional parameters, such as limit, page, offset, sort, and filters. Here's an example of how to use these parameters:

```python
movies = lotr.movies_list(limit=10, page=2, sort='name:desc')
```
For more information please visit: https://the-one-api.dev/documentation#filtering

## API Documentation
For more information about The One API, check out the official documentation at https://the-one-api.dev/documentation.

## Testing
To run the tests, navigate to the root directory of the module in your terminal and run the following command:
```python
 python3 -m unittest tests/*
```

## Contribution
If you'd like to contribute to this module, feel free to fork the repository and submit a pull request with your changes. Please make sure to write tests for any new functionality you add, and to run the existing tests to ensure that everything still works as expected. We appreciate any and all contributions!
