from flask import Flask, render_template, request
#digo que quiero una aplicacion flask
app = Flask(__name__)
#defino la ruta por defecto de mi aplicacion flask
@app.route('/')
def cinepolis():
    #renderizo mi platilla principal
    return render_template("cine.html")

#defino la ruta donde recibire parametros y retornare mi resultado, tipo de peticion
@app.route("/Resultado", methods=["GET", "POST"])
def Resultado():
    #espero que mi peticion sea post asi que  creo la condicion
    if request.method == "POST":
        #Primero obtengo los valores de mi front
        nombre = request.form.get("Nombre")
        compradores = request.form.get("Compradores")
        tarjeta_cineco = request.form.get("TarjetaCineco")  
        boletos = request.form.get("Boletos")

        #verifico que mis valores sean enteros
        try:
            compradores = int(compradores)
            boletos = int(boletos)
        except ValueError:
            # si los valores no son enteros mando mensaje de error
            resultado = "Error: Datos incorrectos para compradores o boletos."
            return render_template("cine.html", resultado=resultado)

        # Me aseguro que el limite de boletos por pesona sea de 7
        if boletos > (compradores * 7):
            resultado = f"Error: Máximo {7 * compradores} boletos para {compradores} compradores."
            return render_template("cine.html", resultado=resultado)

        # calculo el precio base
        valor_base = 12.0
        valor_a_pagar = valor_base * boletos

        #Aplico descuento si es necesario segun en numero de boletos comprados
        #15% para mas de 5 boletos
        if boletos > 5:
            valor_a_pagar *= 0.85  
        elif 3 <= boletos <= 5:
            valor_a_pagar *= 0.90  

        # 10% descuento adicional si tienes tarjeta cineco
        if tarjeta_cineco == "Si":
            valor_a_pagar *= 0.90

        #Una ves aplicados todos los descuentos genero mi resultado
        resultado = f"""
        Nombre del comprador: {nombre}<br>
        Boletos comprados: {boletos}<br>
        Valor a pagar (MXN): {round(valor_a_pagar, 2)}
        """

        # Retorno mi plantilla
        return render_template(
            "cine.html", 
            resultado=resultado, 
            valor_pagar=round(valor_a_pagar, 2)
        )
    else:
        return "Metodo invalido, utilice el formulario"

if __name__ == '__main__':
    app.run(debug=True)
