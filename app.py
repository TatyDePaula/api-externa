from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

def get_cep_info(cep):
    cep = ''.join(filter(str.isdigit, cep))
    
    if len(cep) != 8 or not cep.isdigit():
        raise ValueError("CEP inválido. Deve conter 8 dígitos numéricos.")
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 400:
        raise ValueError("CEP inválido. Formato incorreto.")
    
    data = response.json()
    
    if 'erro' in data:
        raise ValueError("CEP não encontrado.")
    
    return data

def get_cnpj_info(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))
    
    if len(cnpj) != 14 or not cnpj.isdigit():
        raise ValueError("CNPJ inválido. Deve conter 14 dígitos numéricos.")
    
    url = f"https://publica.cnpj.ws/cnpj/{cnpj}"
    response = requests.get(url)
    
    if response.status_code == 429:
        raise Exception("Limite de consultas excedido. Tente novamente mais tarde.")
    elif response.status_code == 404:
        raise ValueError("CNPJ não encontrado.")
    elif response.status_code != 200:
        raise Exception("Erro ao consultar o CNPJ.")
    
    data = response.json()
    
    return data

@app.route('/cep/<cep>', methods=['GET'])
def cep_route(cep):
    try:
        print(cep)
        data = get_cep_info(cep)
        return jsonify(data), 200
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400
    except Exception as e:
        return jsonify({'erro': 'Erro interno do servidor'}), 500

@app.route('/cnpj/<cnpj>', methods=['GET'])
def cnpj_route(cnpj):
    try:
        data = get_cnpj_info(cnpj)
        return jsonify(data), 200
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400
    except Exception as e:
        return jsonify({'erro': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)

