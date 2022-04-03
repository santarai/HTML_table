from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Dorje', 'last_name' : 'Tamang'},
        {'first_name' : 'Jabez', 'last_name' : 'Sarki'},
        {'first_name' : 'Mani', 'last_name' : 'Sotang'},
        {'first_name' : 'KB', 'last_name' : 'Magar'}
    ]
    return render_template("index.html",users=users)



if __name__=="__main__":
    app.run(debug=True)