from flask import Flask, render_template, request
# como decir que quiero una aplicacion flask
app=Flask(__name__)
# defino la ruta por defecto de mi aplicacion 
@app.route('/')
def cinepolis():
    #renderizo mi plantilla principal
    return render_template("cine.html")


# defino la ruta donde recibire mis parametros, retornare mi resultado, y definire que tipo de peticion es 
@app.route("/Resultado",methods=["POST","GET"])
def Resultado():
    # Espero que mi peticion sea post asi que creo la condicion con respecto a eso
    if request.method =="POST":
        #de ser post, procedo a recuperar los datos del front
        nombre= request.form.get("Nombre")
        compradores= request.form.get("Compradores")
        tarjeta_cineco= request.form.get("TarjetaCineco")
        boletos= request.form.get("Boletos")
        #Primero verifico que mis valores numericos efectivamente sean enteros
        try:
            compradores=int(compradores)
            boletos=int(boletos)
        except ValueError:
            # de no ser valores numericos devuelvo en resultado un mensaje de error
            resultado="valores incorrectos"
            return render_template("cine.html", resultado=resultado)
        # despues de verificar que mis valores en efecto son numericos 
        # limito el numero de boletos a 7 por persona 
        if boletos > (compradores*7):
            #devuelvo nuevamente un mensaje de error en caso de que quiera comprar mas boletos de lo permitido
            resultado=f"error como maximo puede comprar {compradores*7} para {compradores} compradores"
            return render_template("cine.html",resultado=resultado)
        
        # calculo el precio base
        valor_base= 12.0
        valor_a_pagar = valor_base*boletos

        #Aplico descuento si es necesario segun en numero de boletos comprados
        #15% para mas de 5 boletos
        if boletos > 5:
            valor_a_pagar*=0.85
        elif 3 <= boletos <= 5:
            valor_a_pagar*=0.90
        
        # 10% descuento adicional si tienes tarjeta cineco
        if tarjeta_cineco == "Si":
            valor_a_pagar *= 0.90
        
         #Una ves aplicados todos los descuentos genero mi resultado
        resultado= f"""
            Nombre del comprador: {nombre}<br>
            Boletos comprados: {boletos}<br>
            Cantidad a pagar: {round(valor_a_pagar,2)}
         """
        # retorno mis valores correctamente a la plantilla
        return render_template(
            "cine.html",
            resultado=resultado,
            valor_a_pagar=round(valor_a_pagar,2)
                               )
    else:
        return "Use el formulario wey"
    
if __name__ == '__main__':
    app.run(debug=True)
         





