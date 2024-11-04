from flask import Flask, render_template, request, redirect, url_for

from package.function import add
app = Flask(__name__)
                                 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/hello')
def hello():
    return "Hello, Flask!" + str(add(4, 5))

@app.route("/traitement", methods=["POST", "GET"])
def traitement():
    if request.method == "POST":
        donnees = request.form
        nom = donnees.get('nom')
        mdp = donnees.get('mdp')
        if nom == 'admin' and mdp == '1234':
            return render_template("traitement.html", nom_utilisateur=nom, admin=True)
        elif nom == 'alfred':
            return render_template("traitement.html", nom_utilisateur=nom, admin=False)
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)
