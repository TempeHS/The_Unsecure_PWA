from flask import Flask
from flask import request
from flask import jsonify
import database_management as dbHandler
from flask_cors import CORS, cross_origin
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


api = Flask(__name__)
cors = CORS(api)
api.config["CORS_HEADERS"] = "Content-Type"
limiter = Limiter(
    get_remote_address,
    app=api,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)


@api.route("/", methods=["GET"])
@limiter.limit("1/second", override_defaults=False)
def get_film():
    film = dbHandler.get_random_film()
    # For security data is validated on entry
    if request.args.get("like") and request.args.get("like").isdigit():
        film_id = request.args.get("like")
        api.logger.critical(
            f"You have liked the film id={film_id}"
        )  # debugging statement only
        dbHandler.record_like(film_id)
    # For security data is validated on entry
    if request.args.get("dislike") and request.args.get("dislike").isdigit():
        film_id = request.args.get("dislike")
        api.logger.critical(
            f"You have disliked the film id={film_id}"
        )  # debugging statement only
        dbHandler.record_dislike(film_id)
    return jsonify(film), 200


@api.route("/add_film", methods=["POST", "HEAD"])
@limiter.limit("1/second", override_defaults=False)
def add_film():
    data = request.get_json()
    info = dict(request.headers)
    api.logger.critical(f"User {info}")
    api.logger.critical(f"Has added the movie {data}")
    dbHandler.add_film(data)
    return data, 201


if __name__ == "__main__":
    api.run(debug=True, host="0.0.0.0", port=1000)
