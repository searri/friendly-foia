from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('landingpage.html')

@app.route('/findagency', methods=['POST'])
def findagency():
    agency = request.form['agency']
    print(agency)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
