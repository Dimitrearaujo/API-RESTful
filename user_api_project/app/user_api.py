
from flask import Flask, request, jsonify
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# Banco de dados em memória (para fins de exemplo)
# Normalmente você usaria um banco de dados relacional ou NoSQL como MySQL, PostgreSQL, MongoDB, etc.
users_db = {}

@app.route('/users', methods=['GET'])
def get_users():
    """
    Retorna todos os usuários cadastrados.
    """
    if not users_db:
        return jsonify({"message": "Nenhum usuário encontrado."}), 404
    return jsonify(users_db), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retorna um usuário específico com base no ID.
    """
    user = users_db.get(user_id)
    if not user:
        raise NotFound(f"Usuário com ID {user_id} não encontrado.")
    return jsonify(user), 200


@app.route('/users', methods=['POST'])
def create_user():
    """
    Cria um novo usuário.
    Requer um corpo JSON com os campos: nome e e-mail.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"message": "Nome e e-mail são obrigatórios."}), 400

    user_id = len(users_db) + 1
    users_db[user_id] = {
        "name": data['name'],
        "email": data['email']
    }
    return jsonify({"message": "Usuário criado com sucesso.", "user_id": user_id}), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Atualiza os dados de um usuário existente.
    Requer um corpo JSON com os campos a serem atualizados: nome e/ou e-mail.
    """
    user = users_db.get(user_id)
    if not user:
        raise NotFound(f"Usuário com ID {user_id} não encontrado.")

    data = request.get_json()
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        user['email'] = data['email']

    return jsonify({"message": "Usuário atualizado com sucesso."}), 200


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Exclui um usuário pelo ID.
    """
    user = users_db.pop(user_id, None)
    if not user:
        raise NotFound(f"Usuário com ID {user_id} não encontrado.")
    return jsonify({"message": "Usuário excluído com sucesso."}), 200


if __name__ == '__main__':
    app.run(debug=True)
