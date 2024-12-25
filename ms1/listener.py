from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/payload', methods=['POST'])
def get_payload():
    data = request.get_json()
    if data:
        return jsonify({"status": "success", "data": data}), 200
    else:
        return jsonify({"status": "error", "message": "No payload received"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)