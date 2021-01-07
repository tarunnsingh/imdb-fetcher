## :memo: IMDB CHART FETCHER

Gets you the information of top movies from IMDB.

### :pushpin: Tested URLs

1. https://www.imdb.com/india/top-rated-indian-movies
2. https://www.imdb.com/india/top-rated-tamil-movies
3. https://www.imdb.com/india/top-rated-telugu-movies

## :bookmark: Steps to RUN Locally. (Tested on Pyhton 3.6.0 and PIP 9.0.1)

- Clone the repo, and browse in it.
- Create a Virtual Environment. `py -m venv env`.
- Activate the Environment. `env\Scripts\activte.bat` or `env\Scripts\Activte.ps1` (if using Powershell)
- Install modules. `pip install -r requirements.txt`
- Run the script and Add the url (any one from above 3) as first argument. Add second argument which is the count (1, 2, 3 ...). **Sample Request**:

`python imdb_chart_fetcher.py 'https://www.imdb.com/india/top-rated-indian-movies' 3`

> OR run the SHELL Script:
> `imdb_chart_fetcher.sh 'https://www.imdb.com/india/top-rated-indian-movies' 3`

This returns the following response.

```json
[
  {
    "title": "Pather Panchali",
    "movie_release_year": "1955",
    "imdb_rating": "8.6",
    "summary": "Impoverished priest Harihar Ray, dreaming of a better life for himself and his family, leaves his rural Bengal village in search of work.",
    "duration": "2h 5min",
    "genre": "Drama"
  },
  {
    "title": "Hanky Panky",
    "movie_release_year": "1979",
    "imdb_rating": "8.6",
    "summary": "A man's simple lie to secure his job escalates into more complex lies when his orthodox boss gets suspicious.",
    "duration": "2h 24min",
    "genre": "Comedy, Romance"
  },
  {
    "title": "Raatchasan",
    "movie_release_year": "2018",
    "imdb_rating": "8.7",
    "summary": "A sub-inspector sets out in pursuit of a mysterious serial killer who targets teen school girls and murders them brutally.",
    "duration": "2h 50min",
    "genre": "Action, Crime, Thriller"
  }
]
```

## Additional Notes:

The Script is configured to save the Latest JSON response inside `movie_reccords` folder as a CSV file.

## Thanks! :star:
