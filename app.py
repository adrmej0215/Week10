from flask import Flask, render_template

app = Flask(__name__)

def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

#homepage
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/marvel")
def marvel():
    return render_template("marvel.html")
@app.route("/dc")
def dc():
    return render_template("dc.html")

@app.route("/hello/<name>")
def hello(name):
    ListOfNames = [name, "Peter", "Steve", "Tony"]
    return render_template("name.html", Sname = name, nameList=ListOfNames)

@app.route("/profHomepage")
def profHomepage():
    x = readDetails("templates/aboutMeProf.txt")
    return render_template("profHomepage.html", aboutMe=x)

#add option to run directly
if __name__ == "__main__":
    app.run(debug=True) 
    