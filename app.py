from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Variável para armazenar o JSON recebido
data_store = {}

html_template = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualização de JSON</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <h2>JSON Armazenado</h2>
    <pre>{{ data }}</pre>
</body>
</html>
"""

@app.route('/receber', methods=['POST'])
def receber_json():
    global data_store
    try:
        data_store = request.get_json()
        return jsonify({"mensagem": "JSON recebido com sucesso", "data": data_store}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@app.route('/visualizar', methods=['GET'])
def visualizar_json():
    return render_template_string(html_template, data=jsonify(data_store).get_data(as_text=True))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
