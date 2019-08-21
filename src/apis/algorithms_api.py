import time
from flask import jsonify, Blueprint, request
from utils.algorithms import reverse_words
algorithms_api = Blueprint('algorithms_api', __name__)


@algorithms_api.route("/api/algorithms/<alg_name>", methods=['POST'])
def apply_alg(alg_name):
    start = int(time.time()*1000.0)
    result = apply_alg_f(alg_name, request.json)
    end = int(time.time()*1000.0)
    return jsonify({"time_elapsed": (end-start), "result": result})


def apply_alg_f(alg_name, input):
    if alg_name == "reverse_words":
        return reverse_words(input)
    return ""
