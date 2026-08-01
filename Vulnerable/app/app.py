from flask import Flask, request
import sqlite3

app = Flask(__name__)

# VULNERABILIDAD: Credencial desactivada para pase de hook local
TEST_TOKEN = "CLAVE_REMOVIDA_PARA_EVIDENCIA"

@app.route("/buscar")
def buscar():
    termino = request.args.get("q", "")
    conexion = sqlite3.connect("database.db")
    # VULNERABILIDAD: SQL Injection
    consulta = f"SELECT * FROM productos WHERE nombre = '{termino}'"
    resultado = conexion.execute(consulta)
    return str(resultado.fetchall())

@app.route("/evaluar")
def evaluar():
    codigo = request.args.get("code", "")
    # VULNERABILIDAD: Ejecución de código arbitrario
    return str(eval(codigo))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
