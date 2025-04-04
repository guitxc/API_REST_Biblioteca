from flask import Flask, jsonify, request

app = Flask(__name__)

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Sva740742",
    database="biblioteca"
)

cursor = db.cursor(dictionary=True)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien',
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling',
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Hábitos Atômicos',
    },
]

# Consultar
@app.route('/livros', methods=['GET'])
def obter_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    return jsonify(livros)
# Consultar por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    cursor.execute("SELECT * FROM livros WHERE id = %s", (id,))
    livro = cursor.fetchone()
    if livro:
        return jsonify(livro)
    return jsonify({"erro": "Livro não encontrado"}), 404

# Alterar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    cursor.execute("UPDATE livros SET titulo = %s, autor = %s WHERE id = %s",
                   (livro_alterado['titulo'], livro_alterado['autor'], id))
    db.commit()
    
    return jsonify({"mensagem": "Livro atualizado com sucesso"})

# Adicionar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    cursor.execute("INSERT INTO livros (titulo, autor) VALUES (%s, %s)",
                   (novo_livro['titulo'], novo_livro['autor']))
    db.commit()
    
    return jsonify({"mensagem": "Livro adicionado com sucesso"}), 201

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    cursor.execute("DELETE FROM livros WHERE id = %s", (id,))
    db.commit()
    
    return jsonify({"mensagem": "Livro excluído com sucesso"})



app.run(port=5000, host='localhost', debug=True)