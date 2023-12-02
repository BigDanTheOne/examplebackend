from flask import Flask, jsonify, request, abort
import enum
from flask_cors import CORS

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


class ContentType(enum.Enum):
    text = 0
    video = 1


class NodeStatus(enum.Enum):
    to_learn = 0  # Пользователь ещё не ознакомился с вершиной (серый цвет)
    learned = 1  # Пользователь знает вершину (зелёный цвет)
    to_repeat = 2  # Пользователю нужно повторить эту вершину (жёлтый цвет)



class TestStatus(enum.Enum):
    passed = 0
    not_passed = 1


class UpdateStatus(enum.Enum):
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
        return {
            "status": self.status,
            "title": self.title,
            "text": self.text,
            "url": self.url,
            "timestamp": self.timestamp,
        }


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    result = {
        "nodes": [
            ["nodeid1", "nodetitle1", 0],
            ["nodeid2", "nodetitle2", 1],
            ["nodeid3", "nodetitle3", 2],
        ],
        "edges": [
            ["nodeid1", "nodeid2"],
            ["nodeid2", "nodeid3"]
             ]
    }
    return jsonify(result), 200


@app.route('/node_content/<nodeId>', methods=['GET'])
def get_content(nodeId):
    response = {
        "id": 1,
        "content": [
            ContentUnit(1, "asasas", ContentType.video, "sdsd", "1 hour", "https://sdsd/com").serialize(),
            ContentUnit(2, "asasas", ContentType.text, "sdsd", "1 hour", "https://sdsd/com").serialize(),
            ContentUnit(3, "asasas", ContentType.text, "sdsd", "1 hour", "https://sdsd/com").serialize()
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
    new_update = Update(UpdateStatus.update_received, "title", "text", "url", "11/27/23 14:28")
#     return jsonify(new_update.serialize()), 200


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
