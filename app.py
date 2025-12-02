# python
from flask import Flask, request, jsonify
from rules.bre01.flow import get_flow  # explicit, no discovery

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# instantiate flows manually
bre01_flow = get_flow()

@app.route('/bre01', methods=['POST'])
def call_bre01():
    try:
        payload = request.get_json(force=True, silent=True) or {}
        result = bre01_flow.execute(payload)
        return jsonify(result), 200
    except Exception as exc:
        app.logger.exception("bre01 flow failed")
        return jsonify({"error": "internal flow error", "details": str(exc)}), 500

@app.route('/bre02', methods=['POST'])
def call_bre02():
    return jsonify({"error": "not implemented"}), 501

if __name__ == '__main__':
    app.run()
