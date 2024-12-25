from flask import Flask, request, jsonify
#from flask_restful import Resource, Api

app = Flask(__name__)

@app.route('/health', methods=['GET'])
@app.route('/payload', methods=['POST'])
def get_payload():
    data = request.get_json()
    if data:
        # add tests and send to sqs
        return jsonify({"status": "success", "data": data}), 200
    else:
        return jsonify({"status": "error", "message": "No payload received"}), 400

if __name__ == '__main__':
    payload=app.run(host='0.0.0.0', port=8080)
