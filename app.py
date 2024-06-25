from flask import Flask,render_template, request #libreria flask

app = Flask(__name__)#nombre del proyecto

@app.route("/")#decorador o ruta
def hello_world():
    return 
    
@app.route("/submit", methods = ["GET", "POST"])
def formulario():
    if request.method == "POST":
        valorA = int(request.form['A'])
        valorB = int(request.form['B'])
        valorC = int(request.form['C'])

        raiz = (valorB**2)-(4*valorA*valorC)

        resultado_mas = (int(-valorB)+(raiz**1/2))/2*valorA
        resultado_menos = (int(-valorB)-(raiz**1/2))/2*valorA

        return render_template("index.html", A=valorA, B=valorB, C=valorC, resultado_mas = resultado_mas, resultado_menos = resultado_menos)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)