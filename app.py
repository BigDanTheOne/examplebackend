from flask import Flask, jsonify, request, abort, Response
import enum
from flask_cors import CORS
import json
import random
import time
from data import *
# from llm import build_graph


app = Flask(__name__)
CORS(app)

liked = False
knows = False
knows_node = False
# Dummy data for demonstration purposes
users = {
    "user_123": {"username": "JohnDoe", "progress": {}}
}

contents = {
    "content_123": {"title": "UX Design Introduction", "type": "video", "liked": False}
}

quizzes = {
    "content_123": [
        {"questionId": "q1", "questionText": "What does UX stand for?", "answer": "User Experience"}
    ]
}

# Mock data for the purpose of this example
users_progress = {}
contents = {}
exercises = {}
sections = {}



@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    return jsonify(math_graph), 200


@app.route('/node_content/<nodeId>', methods=['GET'])
def get_content(nodeId):
    units_len = len(math_graph['nodes'][id_to_index_math[nodeId]]) - 3
    units = []
    for i in range(units_len):
        units.append(math_graph['nodes'][id_to_index_math[nodeId]][3 + i])
    response = {
        "id": 1,
        "content": units,
            # # ContentUnit('unitid_1', "Differential equations, a tourist's guide", ContentType.video, first_sum, "30 minutes", "https://www.youtube.com/watch?v=p_di4Zn4wz4", done, liked_).serialize(),
            # # ContentUnit('unitid_2', "Differential equationes", ContentType.text, second_sum, "45 minutes", "https://en.wikipedia.org/wiki/Differential_equation", done, liked_).serialize(),
            # # ContentUnit('unitid_3', "Functional differential equations", ContentType.text, third_sum, "1 hour 30 minutes", "https://en.wikipedia.org/wiki/Functional_differential_equation", done, liked_).serialize()
            # cu
        # ],
        "test": TestStatus.not_passed,
        "total": units_len,
        "status": math_graph['nodes'][id_to_index_math[nodeId]][2],
    }
    return jsonify(response), 200


@app.route('/test/<nodeId>', methods=['GET'])
def test(nodeId):
    response = {
        "questions": ["question 1", "question 2", "question 3", "question 4"],
        "len": 4
    }
    return jsonify(response), 200

# @app.route('/llm/<subject>', methods=['GET'])
# def tessdsdst(subject):
#     response = build_graph(subject)
#     return jsonify(response), 200

@app.route('/get_feedback/<nodeId>', methods=['POST'])
def get_feedback(nodeId):
    json_data = request.json

    if not json_data:
        return jsonify({"error": "No JSON data provided"}), 400

    # здесь происходит обработка ответа пользователя

    response = {
        "questions": [["user's answer 1", "feedback 1"],
                      ["user's answer 2", "feedback 2"],
                      ["user's answer 3", "feedback 3"],
                      ["user's answer 4", "feedback 4"]],
        "len": 4
    }
    return jsonify(response), 200


def paint(nodeId, visited):
    visited.add(nodeId)
    math_graph['nodes'][id_to_index_math[nodeId]][2] = NodeStatus.learned
    for edge in math_graph['edges']:
        if edge[1] == nodeId and edge[0] not in visited:
            print("Paint", edge[0])
            paint(edge[0], visited)

def unpaint(nodeId, visited):
    visited.add(nodeId)
    math_graph['nodes'][id_to_index_math[nodeId]][2] = NodeStatus.to_repeat
    for edge in math_graph['edges']:
        if edge[0] == nodeId and edge[1] not in visited:
            print("Unpaint", edge[1])
            unpaint(edge[1], visited)


@app.route('/mark_learned/<nodeId>', methods=['POST'])
def feedback(nodeId):
    visited = set()
    if math_graph['nodes'][id_to_index_math[nodeId]][2] == NodeStatus.learned:
        print("Unpaint", nodeId)
        unpaint(math_graph['nodes'][id_to_index_math[nodeId]][0], visited)
    else:
        print("Paint", nodeId)
        paint(math_graph['nodes'][id_to_index_math[nodeId]][0], visited)


    # global knows_node
    # knows_node = not knows_node
    # print(math_graph['nodes'])
    return jsonify({"status": "success"}), 200


@app.route('/mark_learned/<nodeId>/<contentUnitId>', methods=['POST'])
def mark_learned_unit(nodeId, contentUnitId):
    global knows
    knows = not knows
    return jsonify({"status": "success"}), 200


@app.route('/mark_liked/<nodeId>/<contentUnitId>', methods=['POST'])
def mark_liked_unit(nodeId, contentUnitId):
    global liked
    liked = not liked
    return jsonify({"status": "success"}), 200


@app.route('/get_updates', methods=['GET'])
def get_updates():
    if random.randint(1, 10000) % 2 == 0:
        new_update = Update(UpdateStatus.update_received, "Update Title", "Update Text", "https://abc.ru", "11/27/23 14:28")
    else:
        new_update = Update(UpdateStatus.no_updates, '', '', '', '')
    return jsonify(new_update.serialize()), 200

def generate_bot_response(message):
    # Эмуляция генерации ответа по частям
    for symbol in message:
        time.sleep(0.5)
        yield symbol
    yield 'END'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    def generate():
        answer = ''
        for piece in generate_bot_response(message):
            if piece == 'END':
                json_data = json.dumps({"end": True})
            else:
                answer += piece
                json_data = json.dumps({"response": answer})
            yield f"data:{json_data}\n\n"

    return Response(generate(), content_type='text/plain')

if __name__ == '__main__':
    # app.run(ssl_context='adhoc')
    app.run()
