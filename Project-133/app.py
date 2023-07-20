# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Shanmukha" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def Father():

    name = "Sateesh"
    age = "42"

    return render_template('index.html', name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def Mother():

    name = "Vani"
    age = "39"

    return render_template('index.html', name = name , age = age)

# define the route to siblings webpage
@app.route("/brother")
def Brother():

    name = "Gunina"
    age = "5"

    return render_template('index.html', name = name , age = age)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
