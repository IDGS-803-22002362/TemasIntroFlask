from flask import Flask

app=Flask(__name__)
@app.route('/')
def index():
    return "hola mami"
@app.route('/hola')
def hola():
    return("hola")
@app.route("/user/<string:user>")
def user(user):
    return f"hola {user}"
@app.route("/edad/<int:edad>")
def felicitacion(edad):
    return f"feliz cumple {edad}"

@app.route("/edad/<int:edad>/nombre/<string:nombre>")
def felicitaciones(edad,nombre):
    return f"feliz cumple numero {edad} amigo {nombre}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "la suma es {}".format(n1+n2)
@app.route("/default")
@app.route("/default/<string:nom>")
def func(nom="pepe"):
    return "el nombre de Nom es"+nom

if __name__=='__main__':
    app.run(debug=True)

