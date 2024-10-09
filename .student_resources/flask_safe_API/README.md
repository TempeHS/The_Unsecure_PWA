# API

API is the acronym for application programming interface — a software intermediary that allows two applications to talk to each other. APIs are an accessible way to extract and share data within and across organizations.

> [!NOTE]
> The [W3C defines API's as best pratice](https://www.w3.org/TR/dwbp/#accessAPIs) in making data available.

This example, safe API, is a basic implementation for a random movie generator. The API will randomly select a film for its database and return it as JSON. An API argument call can return whether the movie was liked or disliked. A new movie can also be added to the database through the POST method with a JSON file to the API.

To allow cross origins, you need to install the flask CORS library.

> [!IMPORTANT]
> This is an example of how to create a secure API in a development environment. A secure public API would have the following additional features:
>
>   - HTTPS encryption
>   - A CSP policy that enforces HTTPS for all communication
>   - API rate limits, for example, [Flask Limiter](https://flask-limiter.readthedocs.io/en/stable/)
>   - Detailed logging of all POST and GET requests for security analysis

```bash
    pip install flask_cors
```

| API Call | Result |
| --- | --- |
| [http://127.0.0.1:1000/](http://127.0.0.1:1000/ ) | A random movie is selected from the database and returned to the user as a JSON file with a response code 200. |
| [http://127.0.0.1:1000/?dislike="123"](http://127.0.0.1:1000/?dislike="123") | A database entry is created recording a like for film_id "123" if the id exists and a response code 200 returned to the user. |
| [http://127.0.0.1:1000/?like="456"](http://127.0.0.1:1000/?like="456") | A database entry is created recording a dislike for film_id "456" if the id exists and a response code 200 returned to the user. |
| [http://127.0.0.1:1000/add_film](http://127.0.0.1:1000/add_film) | If the submitted JSON is correctly constructed and validated, then a film entry will be added to the films database, and a response code 201 returned to the user. |

## Helpful Links  

- [Open Movie Database](https://www.omdbapi.com/) an example API interface.
- [Create a Python Flask API in 12 minutes](https://www.youtube.com/watch?v=zsYIw6RXjfM) a video tutorial.
- [Postman](https://www.postman.com/), an app to test your API.
- An alternative to [Postman](https://www.postman.com/) is to run the [index.html](/index.html) file from a local folder. The webpage allows you to test a POST, GET or HEAD request to the API and confirm the response. It is a handy utility if you are not able to install Postman.
