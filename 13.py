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
