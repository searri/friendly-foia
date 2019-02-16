from flask import Flask, render_template, request
import Dictionaries
app = Flask(__name__)

pageHead = '''
<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
    <meta charset="utf-8">
    <title>Friendly FOIA</title>
    <link rel="stylesheet" href="static/css/main.css">
    <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
</head>

<body>
'''
pageTail = '''
</body>

</html>
'''

@app.route('/')
def home():
    return render_template('landingpage.html')

@app.route('/findagency', methods=['POST'])
def findagency():
    agency = request.form['agency']
    components = Dictionaries.getComponents(agency)
    formOptions = ''
    compKeys = list(components.keys())
    for i in compKeys:
        one = '<option value ="' + components.get(i) + '">'
        three = '</option>'
        string = one + i + three
        formOptions = formOptions + string

    submitBtn = '''
    <input type="submit" value="SUBMIT DEPARTMENT">
    </form>
    </div
    '''
    
    return (pageHead + 
            '<h1>Need to submit a FOIA Request?</h1><h2>Friendly FOIA is here to help!</h2><div style="text-align: center"><form action="/submitform" method="POST"><select name="component">' + 
            formOptions +
            submitBtn + 
            pageTail
    )

@app.route('/submitform', methods=['POST'])
def submitform():
    return render_template('landingpage.html')

if __name__ == '__main__':
    app.run(debug=True)
