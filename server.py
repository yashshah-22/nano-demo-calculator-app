from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return 'Hello world!', 200

@app.route('/calculator/add', methods=['POST'])
def add():
    try:
        data = request.get_json()
        first = data['first']
        second = data['second']
        result = first + second
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    try:
        data = request.get_json()
        first = data['first']
        second = data['second']
        result = first - second
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
