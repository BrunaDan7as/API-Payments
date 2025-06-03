from flask import Flask, jsonify

app = Flask(__name__)  # se executada manualmente armazena o name

# rotas

@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    return jsonify({"message": "The payment has been created"})

@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({"message": "The payment has been confirmed"})

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return 'pagamento pix'

# o sistema só roda se o name for igual a main, isso previne que execute esse sistema numa eventual importação
if __name__ == '__main__':
    app.run(debug=True)