from flask import Flask, request 
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello anonymous person"

@app.route('/hello/<name>')
def greet(name):
    return f"Hello there, {name}"

@app.route('/date')
def date():
    day = request.args.get('day', '')
    month = request.args.get('month','')
    year = request.args.get('year','')

    today = datetime.date.today()
    currentYear = today.year

    if year < currentYear and # other expressions to ensure valid input.
        try:
            return (f"Date is {year}-{month}-{day}")
        except ValueError:
            return ('Enter a valid date')
        

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)


