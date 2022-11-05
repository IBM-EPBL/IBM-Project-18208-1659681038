from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register",methods = ['GET',"POST"])
def register():
    if request.method == 'POST':
        uname = request.form['name']
        email = request.form['email_id']
        pwd = request.form['password']
        cpwd = request.form['confirm_pwd']
        if pwd != cpwd:
            return render_template('register.html',pwd_error = "Password does not match!")
        else:
            return render_template("login.html")
    else:
        return render_template('register.html')

@app.route("/login",methods = ['GET',"POST"])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
