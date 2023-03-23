from flask import Flask, request, render_template, redirect, jsonify
from flask_cors import CORS
import json

# CRIANDO O APP
app = Flask(__name__)
CORS(app, resources={r"/*": {"crossOrigin": "*"}})
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    #abre o arquivo
    arq = open("rankingPilotos.txt", encoding="utf-8")
    linhas = arq.readlines()
    torneio = {}
    piloto = {}
    i = 1
    # faz a leitura linha a linha e configura o dicionario
    for linha in linhas:
        linha = linha.strip("\n")
        linha = linha.split("\t")
        piloto["posicao"] = linha[0]
        piloto["sd"] = linha[1]
        piloto["nome"] = linha[2]
        piloto["pontos"] = linha[3]
        piloto["desc"] = linha[4]
        piloto["pontos_geral"] = linha[5]
        piloto["posicao_qualify_day"] = linha[6]
        piloto["pontos_qualify_day"] = linha[7]
        piloto["categoria_etapa1"] = linha[8]
        piloto["posicao_etapa1"] = linha[9]
        piloto["bonus_etapa1"] = linha[10]
        piloto["advertencia_etapa1"] = linha[11]
        piloto["pontos_etapa1"] = linha[12]
        piloto["categoria_etapa2"] = linha[13]
        piloto["posicao_etapa2"] = linha[14]
        piloto["bonus_etapa2"] = linha[15]
        piloto["advertencia_etapa2"] = linha[16]
        piloto["pontos_etapa2"] = linha[17]
        torneio[i] = piloto
        piloto = {}
        i = i + 1
    # retornando apenas um dicionário
    return torneio


@app.route('/api/torneio', methods=['GET'])
def getAll():
    torneio = index()
    # retorna um json do dicionário acima
    return jsonify(torneio)


# Consultar piloto por nome'
@app.route('/api/piloto/nome/<nome>', methods=['GET'])
def obter_piloto_por_nome(nome):
    torneio = index()
    nome = nome.replace('%20', ' ').lower()
    for id, value in torneio.items():
        if value.get('nome').lower() == nome:
            return jsonify(value)
    if TypeError:
        return ('Nome não encontrado')


# Consultar piloto por id'
@app.route('/api/piloto/id/<int:id>', methods=['GET'])
def obter_piloto_por_id(id):
    torneio = index()
    for i in torneio:
        if i == id:
            return jsonify(torneio.get(id))
    if TypeError:
        return ('ID inválido')

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True,
            threaded=True, use_reloader=True)