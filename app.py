from flask import Flask, request, jsonify

app = Flask(__name__)
stored_string = ""

@app.route('/api/string', methods=['GET', 'POST'])
def handle_string():
    global stored_string
    if request.method == 'POST':
        data = request.get_json()
        stored_string = data.get("value", "")
        return jsonify({"message": "String updated"})
    return jsonify({"value": stored_string})
