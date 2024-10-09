from flask import Flask
from flask import request
from flask import jsonify
import database_management as dbHandler
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def get_film():
	film = dbHandler.get_random_film()
	# For security data is validated on entry
	if request.args.get("like") and request.args.get("like").isdigit():
		film_id = request.args.get("like")
		app.logger.info(f"You have liked the film id={film_id}") #debugging statement only
		dbHandler.record_like(film_id)
	# For security data is validated on entry
	if request.args.get("dislike") and request.args.get("dislike").isdigit():
		film_id = request.args.get("dislike")
		app.logger.critical(f"You have disliked the film id={film_id}") #debugging statement only
		dbHandler.record_dislike(film_id)
	return jsonify(film), 200


@app.route('/add_film', methods=['POST', 'HEAD'])
def add_film():
	data = request.get_json()
	info = dict(request.headers)
	app.logger.critical(f"User {info}")
	app.logger.critical(f"Has added the movie {data}")
	dbHandler.add_film(data)
	return data, 201

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=1000)

