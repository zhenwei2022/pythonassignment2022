import requests
import math
import mysql.connector
from geopy import distance

app = Flask(__name__)
cors = CORS(app)


@app.route('/game_setup')
def game_setup():
    args = request.args
    player_name = args.get("player")
    location = args.get("city")
    destination = args.get("destination")
    distance = args.get("distance")
    response = [{
        "name": player_name,
        "location": location,
        "destination": destination,
        "distance": distance
    }]
    return response


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
