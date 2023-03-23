# FlaskApi_fkart

## Rotas

### Obter dados do torneio
@app.route('/api/torneio', methods=['GET'])


### Consultar piloto por nome'
@app.route('/api/piloto/nome/<nome>', methods=['GET'])


### Consultar piloto por id'
@app.route('/api/piloto/id/<int:id>', methods=['GET'])
