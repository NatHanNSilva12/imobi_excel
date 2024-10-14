from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask API!")

@app.route('/api/save', methods=['POST'])
def save_data():
    # Lógica para salvar os dados aqui
    return jsonify(message="Data saved successfully!")

if __name__ == '__main__':
    app.run(debug=True)
    