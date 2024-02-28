from flask import Flask, request
app = Flask(__name__)

# method 1
@app.route('/login', method=['Get','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
# method 2
@app.get('/login')
def login_get():
    return show_the_login_form()
@app.post('/login'):
def login_post():
    return do_the_login()
