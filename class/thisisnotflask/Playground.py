from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def get_name():
    return render_template('index.html')

@app.route('/greet', methods = ['POST'])
def greet():
    typedName = request.form['name']
    print(typedName)
    return render_template('hello.html', name=typedName)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)