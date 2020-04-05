from flask import Flask, render_template, session, flash, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html')

@app.route('/contracts')
def display_contracts():
    content = [
        {
            "company": "002",
            "account": "123456",
            "accountname": "Miranda Corporation",
            "address": "Dasmariñas, Cavite",
            "status": "A" 
        },        
        {
            "company": "002",
            "account": "234567",
            "accountname": "Miranda & Associates",
            "address": "Basco, Batanes",
            "status": "A"
        }
    ]
    return render_template('home.html', content=content)

if __name__ == "__main__":
    app.run(debug=True)