from flask import Flask, request
from math_json_tree.json_mutator import math_mutator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tree = request.get_json(force=True)
    result = math_mutator(tree)
    return str(result) + '\n'

if __name__ == '__main__':
    app.run(debug=True)