#Lab 13
#1
from flask import Flask, request
app = Flask(__name__)
@app.route('/prime')
def prime():
    args = request.args
    number = int(args.get("number"))
    import math
    k = int(math.sqrt(number))
    for i in range(2, k + 2):
        if number % i == 0:
            Prime_number = False
            break
        if i == k + 1:
            Prime_number = True

    response = {
        "Number" : number,
        "isPrime" : Prime_number
    }
    return response
if __name__ == '__main__':
    app.run(use_reloader = True, host = '127.0.0.1', port = 5000)

#2
import mysql.connector
from flask import Flask, request
import json

app = Flask(__name__)
@app.route('/airport/<icao>')
def airport(icao):
    cursor = connection.cursor()
    cursor.execute("SELECT name, municipality FROM airport WHERE ident ='"+ icao +"'")
    result = cursor.fetchall()
    for row in result:
        response = {
            "ICAO" : icao,
            "Name" : row[0],
            "Location" : row[1]
        }
        return response

connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='20220822Metropolia',
        autocommit=True
    )

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
