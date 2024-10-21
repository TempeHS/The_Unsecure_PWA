# API

API is the acronym for application programming interface — a software intermediary that allows two applications to talk to each other. APIs are an accessible way to extract and share data within and across organizations.

> [!NOTE]
> The [W3C defines API's as best pratice](https://www.w3.org/TR/dwbp/#accessAPIs) in making data available.

This safe API example is a incomplete implementation for a random movie generator. The API will randomly select a film for its database and return it as JSON. An API argument call can return whether the movie was liked or disliked by users to create a voting system. A new movie can also be added to the database through the POST method with a JSON file to the API.

| API Call | Result |
| --- | --- |
| [http://127.0.0.1:1000/](http://127.0.0.1:1000/ ) | A random movie is selected from the database and returned to the user as a JSON file with a response code 200. |
| [http://127.0.0.1:1000/?dislike=123](http://127.0.0.1:1000/?dislike=123) | A database entry is created recording a like for film_id "123" if the id exists and a response code 200 returned to the user. |
| [http://127.0.0.1:1000/?like=456](http://127.0.0.1:1000/?like=456) | A database entry is created recording a dislike for film_id "456" if the id exists and a response code 200 returned to the user. |
| [http://127.0.0.1:1000/add_film](http://127.0.0.1:1000/add_film) | If the submitted JSON is correctly constructed and validated, then a film entry will be added to the films database, and a response code 201 returned to the user. |

Because this API is intended to be a public access and it will be accessed by other websites the API needs to allow cross origins, to do this install and configure the [Flask CORS](https://pypi.org/project/Flask-Cors/) library as per the documentation. The library also allows you to limited CORS to specific domains if your API is not intended as a public access API.

```bash
    pip install flask_cors
```

Allowing open cross origin introduces vulnerabilities of DoS and excessive demand affecting availability and response times. As a countermeasure the API needs rate limiting, to do this install and configure [Flask Limiter](https://flask-limiter.readthedocs.io/en/stable/) library as per the documentation.

```bash
    pip install Flask-Limiter
```

> [!IMPORTANT]
> This example API is assumed to be in a development environment. A safe and secure public API would have the following additional features:
>
>   - Authentication and authorisation, for example, [Authentication with Flask](https://www.youtube.com/watch?v=71EU8gnZqZQ).
>   - HTTPS encryption.
>   - A [Content Security Policy (CSP)](../content_security_policy/README.md) that enforces HTTPS for all communication
>   - Detailed [logging](..\defensive_data_handling\README.md#Logging) of all HEAD, POST, and GET requests for security analysis.
>   - Detailed and explicit [defensive data handling](../defensive_data_handling) practices.

## Helpful Links  

- [Open Movie Database](https://www.omdbapi.com/) an example API interface.
- [Create a Python Flask API in 12 minutes](https://www.youtube.com/watch?v=zsYIw6RXjfM) a basic video tutorial.
- [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client), a VSCode extension to test your API.
- The [index.html](index.html) file serves as both a front-end javascript code sample for making API requests but also a simple API testing tool. The webpage allows you to test a POST, GET or HEAD request to your API and confirm the response.
- [Postman](https://www.postman.com/), a alternative local app to test your API.
