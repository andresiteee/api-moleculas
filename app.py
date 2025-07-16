# Importamos las herramientas que necesitamos
from flask import Flask, send_file, request
from rdkit import Chem
from rdkit.Chem import Draw
import io

# Creamos la aplicación web
app = Flask(__name__)

# Definimos la ruta principal de nuestra API
# Aceptará peticiones en /generar
@app.route('/generar')
def generar_imagen_molecula():
    """
    Esta función toma un código SMILES de la URL (ej: /generar?smiles=CCO),
    genera una imagen de la molécula y la devuelve como un PNG.
    """
    # 1. Obtenemos el código SMILES desde los parámetros de la URL
    smiles = request.args.get('smiles')

    # Si no nos dan un código SMILES, devolvemos un error
    if not smiles:
        return "Error: Por favor, proporciona un código SMILES en la URL. Ejemplo: /generar?smiles=CCO", 400

    try:
        # 2. RDKit convierte el texto SMILES en un objeto molécula
        molecula = Chem.MolFromSmiles(smiles)
        
        if molecula is None:
            raise ValueError("SMILES inválido")

        # 3. RDKit dibuja la estructura 2D de la molécula
        img = Draw.MolToImage(molecula, size=(300, 300))
        
        # 4. Guardamos la imagen en un "buffer" en memoria
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)

        # 5. Enviamos la imagen guardada en el buffer como respuesta
        return send_file(buffer, mimetype='image/png')

    except Exception as e:
        return f"Error: El código SMILES '{smiles}' no es válido o no se pudo interpretar. Detalle: {e}", 400

# Esta parte hace que el servidor se ejecute cuando corres el archivo
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
