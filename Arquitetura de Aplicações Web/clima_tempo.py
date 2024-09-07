from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Defina o token da API e a URL base
API_TOKEN = '022438723783ca4be9dd4c3d91b5474b'
BASE_URL = 'https://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR'

@app.route('/weather', methods=['GET'])
def weather():
    # Faça a requisição para a API Climatempo
    response = requests.get(BASE_URL, params={
        'token': API_TOKEN
    })

    # Verifique se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        
        # Verifique se a resposta contém dados
        if data:
            # Normaliza a resposta para um formato amigável
            # Dependendo da estrutura da resposta, ajuste os campos aqui
            result = {
                'data': data  # Aqui você pode precisar ajustar com base na estrutura real da resposta
            }
            return jsonify(result)
        else:
            return jsonify({'error': 'No data found'}), 404
    else:
        return jsonify({'error': 'Failed to fetch data from Climatempo API'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
