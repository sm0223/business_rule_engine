# python
from flask import Flask, request, jsonify

from repos.bre01.flow import Bre01Flow

from repos.bre02.flow import Bre02Flow

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bre01', methods=['POST'])
def call_bre01():
    try:
        payload = request.get_json() or {}
        bre_flow = Bre01Flow()
        result = bre_flow.execute(payload)
        return jsonify(result), 200
    except Exception as exc:
        app.logger.exception("bre01 flow failed")
        return jsonify({"error": "internal flow error", "details": str(exc)}), 500



@app.route('/bre02', methods=['POST'])
def call_bre02():
    try:
        payload = request.get_json() or {}
        bre_flow = Bre01Flow()
        result1 = bre_flow.execute(payload)
        bre_flow = Bre02Flow()
        result2 = bre_flow.execute(result1)
        return jsonify(result2), 200
    except Exception as exc:
        app.logger.exception("bre01 flow failed")
        return jsonify({"error": "internal flow error", "details": str(exc)}), 500


if __name__ == '__main__':
    app.run()
