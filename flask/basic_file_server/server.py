'''
    Servidor web básico para servir ficheros. Pensado para ejecutarlo durante
    las pruebas locales con ficheros js que necesitan ser servidos por hppt por
    motivos de seguridad en el navegador.

    Uso: copiar en el directorio raíz del proyecto. Una vez arrancado nos servirá
    los ficheros que le pidamos de cualquier directorio del proyecto. Para ejecutar
    el servidor:
        export FLASK_APP=server.py
        flask run
'''
from flask import Flask, send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content_Type'

@app.route("/")
@cross_origin()
def root_url():
    return "Basic js file server using flask"

@app.route('/<path:path>')
def send_js_file(path):
    return send_from_directory('.', path)

# Para arrancarlo con python en lugar de flask (con sudo por seguridad al ser un puerto <1024)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

