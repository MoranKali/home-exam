from flask import Flask, request, jsonify
from json import dumps, loads
from marshmallow import Schema, fields, ValidationError
#from flask_restful import Resource, Api

class PayloadSchema(Schema):
    email_subject = fields.String(required=True)
    email_sender = fields.String(required=True)
    email_timestream = fields.String(required=True)
    email_content = fields.String(required=True)
    
app = Flask(__name__)

@app.route('/health', methods=['GET'])
@app.route('/payload', methods=['POST'])
def get_payload():
    data = request.json()
    schema=PayloadSchema()
    if data:
        # add tests and send to sqs
        try:
            schema.load(data)
        except ValidationError as err:
            return jsonify({"status": "error", "message": err.messages}), 400
        return jsonify({"status": "success", "data": data}), 200
    else:
        return jsonify({"status": "error", "message": "No payload received"}), 400

if __name__ == '__main__':
    payload=app.run(host='0.0.0.0', port=8080)
