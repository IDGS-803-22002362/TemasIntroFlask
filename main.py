from flask import Flask, render_template, request
from flask import g
from flask_wtf.csrf import CSRFProtect  #PROTECCION CONTRA ATAQUES CSRF
from flask import flash  #usar mensajes  flash
import forms

app=Flask(__name__)
app.secret_key="Esta es la clave secreta"
csrf=CSRFProtect()
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.nombre="Mario"
    print(' Before request 1')

@app.after_request
def after_request(response):
    print('After request 3')
    return response

@app.route('/')
def index():
    lista={"betillo","betillo","antoi"}
    grupo="IDGS-803"
    #PARA LLEBVAR VARIABLE A FRONT inicializas la variable y la pones a un lado del archivo
    return render_template("index.html",grupo=grupo,lista=lista)

@app.route("/Alumnos",methods=["GET","POST"])
def alumnos():
    matricula=""
    nombre=""
    edad=""
    correo=""
    ape=""
    #obtendra los valores de formulario por default
    alumno_clase=forms.UserForm(request.form)
    if request.method=="POST" and alumno_clase.validate():#aqui no permite pasar sin cumplir con todas las validaciones
        matricula=alumno_clase.matricula.data
        nombre=alumno_clase.nombre.data
        ape=alumno_clase.apellidos.data
        edad=alumno_clase.edad.data
        correo=alumno_clase.correo.data
        mensaje=f'Bienvenido{nombre}' #creo mi mensaje
        flash(mensaje)
    return render_template("Alumnos.html",form=alumno_clase,matricula=matricula,nombre=nombre,ape=ape,edad=edad,correo=correo)


@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")
@app.route('/ejemplo1macro')
def ejemplo1macro():
    return render_template("ejemplomacro1.html")
@app.route('/ejemplo2')
def ejemplo2():
    return render_template("ejemplo2.html")
@app.route("/OperaBas")
def Operas():
    return render_template("OperaBas.html")

@app.route("/Resultado", methods=["GET","POST"])
def Resultado():
    if request.method == "POST":
        num1 = request.form.get("N1")
        num2 = request.form.get("N2")
        operacion = request.form.get("operacion")
        
        try:
            # Convertir a float para permitir operaciones con decimales
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            resultado = "Error: Números inválidos"
            return render_template("OperaBas.html", resultado=resultado)
        
        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            if num2 == 0:
                resultado = "Error: División por cero"
            else:
                resultado = num1 / num2
        else:
            resultado = "Operación no reconocida"
        
        return render_template("OperaBas.html", resultado=resultado)

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
    csrf.init_app(app)
    app.run(debug=True)

