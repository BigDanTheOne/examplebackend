from flask import Flask, jsonify, request, abort
import enum
from flask_cors import CORS
import json
import random

app = Flask(__name__)
CORS(app)

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


class ContentType(int, enum.Enum):
    text = 0
    video = 1


class NodeStatus(int, enum.Enum):
    to_learn = 0  # Пользователь ещё не ознакомился с вершиной (серый цвет)
    learned = 1  # Пользователь знает вершину (зелёный цвет)
    to_repeat = 2  # Пользователю нужно повторить эту вершину (жёлтый цвет)



class TestStatus(int, enum.Enum):
    passed = 0
    not_passed = 1


class UpdateStatus(int, enum.Enum):
    no_updates = 0
    update_received = 1


class ContentUnit:
    def __init__(self, id: str, title: str, contentType: ContentType, summary: str, duration: str, url: str,
                 done: bool = False, liked: bool = False):
        self.id = id
        self.title = title
        self.contentType = contentType
        self.summary = summary
        self.duration = duration
        self.url = url
        self.done = done
        self.liked = liked

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "contentType": self.contentType,
            "summary": self.summary,
            "duration": self.duration,
            "url": self.url,
            "done": self.done,
            "liked": self.liked
        }


class Update:
    def __init__(self, status: UpdateStatus, title: str, text: str, url: str, timestamp: str):
        self.status = status
        self.title = title
        self.text = text
        self.url = url
        self.timestamp = timestamp

    def serialize(self):
        if self.status == UpdateStatus.update_received:
            return {
                "status": self.status,
                "title": self.title,
                "text": self.text,
                "url": self.url,
                "timestamp": self.timestamp
            }
        else:
            return {
                "status": self.status
            }


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    result = {
        "nodes": [
            ["nodeid1", "nodetitle1", NodeStatus.to_learn],
            ["nodeid2", "nodetitle2", NodeStatus.learned],
            ["nodeid3", "nodetitle3", NodeStatus.to_repeat],
        ],
        "edges": [
            ["nodeid1", "nodeid2"],
            ["nodeid2", "nodeid3"]
             ]
    }
    return jsonify(result), 200


@app.route('/node_content/<nodeId>', methods=['GET'])
def get_content(nodeId):
    first_sum = """"
    Differential equations are a mathematical tool for describing change, and can be used to model physical systems. In this video, a pendulum is used as an example to show how differential equations can be used to understand the behavior of a system. The equations are complex, but provide insight into how the system behaves. Differential equations can also be used to explore how systems interact, and to simulate the behavior of systems.
    """
    second_sum = """
        •   Дифференциальные уравнения - это уравнения, которые связывают производные функции с самой функцией и независимыми переменными.
        •   Они используются для описания различных физических, технических и биологических процессов.
        •   Существуют различные типы дифференциальных уравнений, включая обыкновенные дифференциальные уравнения, уравнения в частных производных и стохастические дифференциальные уравнения.
        •   Решение дифференциальных уравнений часто является сложной задачей, но существуют методы, такие как метод Эйлера и метод Рунге-Кутты, для их численного решения.
        •   Дифференциальные уравнения тесно связаны с теорией разностных уравнений и имеют приложения в различных областях, включая математику, физику, инженерию и экономику.
        •   Существует множество программ CAS, которые могут решать дифференциальные уравнения, включая Maple, Mathematica, Maxima, SageMath, SymPy и Xcas.
    """
    third_sum = """
    •   Функционально-дифференциальные уравнения (FDE) - это уравнения, которые включают в себя функции, зависящие от времени и от предыдущих значений функции.
    •   FDE используются в различных областях, включая медицину, механику, биологию и экономику.
    •   FDE могут быть решены с использованием численных методов, таких как метод Эйлера и метод Рунге-Кутты.
    •   FDE могут быть классифицированы по различным типам, включая уравнения с запаздыванием, нейтральные уравнения и интегро-дифференциальные уравнения.
    •   Уравнения с запаздыванием зависят от прошлых и текущих значений функции, нейтральные уравнения зависят от прошлых и текущих значений функции и производных с запаздываниями, а интегро-дифференциальные уравнения включают интегралы и производные некоторой функции по ее аргументу.
    •   FDE использовались в моделях, определяющих будущее поведение явлений, зависящих от прошлого.
    •   Примеры моделей, использующих FDE, включают модель смешивания, модель хищника-жертвы Вольтерры и модель эпидемии ВИЧ."""
    response = {
        "id": 1,
        "content": [
            ContentUnit('unitid_1', "Differential equations, a tourist's guide", ContentType.video, first_sum, "30 minutes", "https://www.youtube.com/watch?v=p_di4Zn4wz4").serialize(),
            ContentUnit('unitid_2', "Differential equatione", ContentType.text, second_sum, "45 minutes", "https://en.wikipedia.org/wiki/Differential_equation").serialize(),
            ContentUnit('unitid_3', "Functional differential equation", ContentType.text, third_sum, "1 hour 30 minutes", "https://en.wikipedia.org/wiki/Functional_differential_equation").serialize()
        ],
        "test": TestStatus.not_passed,
        "total": 3,
        "status": NodeStatus.to_learn,
    }
    return jsonify(response), 200


@app.route('/test/<nodeId>', methods=['GET'])
def test(nodeId):
    response = {
        "questions": ["question 1", "question 2", "question 3"],
        "len": 3
    }
    return jsonify(response), 200


@app.route('/get_feedback/<nodeId>', methods=['POST'])
def get_feedback(nodeId):
    json_data = request.json

    if not json_data:
        return jsonify({"error": "No JSON data provided"}), 400

    # здесь происходит обработка ответа пользователя

    response = {
        "questions": [["user's answer 1", "feedback 1"],
                      ["user's answer 2", "feedback 2"],
                      ["user's answer 3", "feedback 3"]],
        "len": 3
    }
    return jsonify(response), 200


@app.route('/mark_learned/<nodeId>', methods=['POST'])
def feedback(nodeId):
    return jsonify({"status": "success"}), 200


@app.route('/mark_learned/<nodeId>/<contentUnitId>', methods=['POST'])
def mark_learned_unit(nodeId, contentUnitId):
    return jsonify({"status": "success"}), 200


@app.route('/mark_liked/<nodeId>/<contentUnitId>', methods=['POST'])
def mark_liked_unit(nodeId, contentUnitId):
    return jsonify({"status": "success"}), 200


@app.route('/get_updates', methods=['GET'])
def get_updates():
    if random.randint(1, 10000) % 2 == 0:
        new_update = Update(UpdateStatus.update_received, "Update Title", "Update Text", "https://abc.ru", "11/27/23 14:28")
    else:
        new_update = Update(UpdateStatus.no_updates, '', '', '', '')
    return jsonify(new_update.serialize()), 200


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
