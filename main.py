from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/')
def index():
    lista={"betillo","betillo","antoi"}
    grupo="IDGS-803"
    #PARA LLEBVAR VARIABLE A FRONT inicializas la variable y la pones a un lado del archivo
    return render_template("index.html",grupo=grupo,lista=lista)
@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")
@app.route('/ejemplo2')
def ejemplo2():
    return render_template("ejemplo2.html")
@app.route("/OperaBas")
def Operas():
    return render_template("OperaBas.html")

@app.route("/Resultado", methods=["GET","POST"])
def Resultado():
    if request.method=="POST":
        num1=request.form.get("N1")
        num2=request.form.get("N2")
        resultado=int(num2)+int(num1)
        return render_template("OperaBas.html",resultado=resultado)

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

@app.route("/form1")
def form1():
    return '''
    <form>
    <label>nombre</label>
    <input type="text" name="nombre" placeholder="nombre">
    </form>
    '''

if __name__=='__main__':
    app.run(debug=True)

