from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from supabase_utils import save_to_supabase
from excel_utils import generate_excel
from email_utils import send_email

routes_blueprint = Blueprint('routes', __name__)

users = {}

@routes_blueprint.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if email in users:
        return jsonify({'message': 'Usuário já existe'}), 400

    users[email] = password
    return jsonify({'message': 'Usuário registrado com sucesso'}), 200

@routes_blueprint.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if email not in users or users[email] != password:
        return jsonify({'message': 'Credenciais inválidas'}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200

@routes_blueprint.route('/api/save', methods=['POST'])
@jwt_required()
def save_data():
    data = request.json
    save_to_supabase(data)
    filename = generate_excel(data)
    send_email(data['emailUsuario'], filename)
    return jsonify({'message': 'Dados salvos com sucesso'}), 200