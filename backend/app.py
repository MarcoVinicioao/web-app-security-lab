from flask import Flask, jsonify, request
from flask_cors import CORS

from database import get_connection, init_db

app = Flask(__name__)

CORS(app, origins=["http://localhost:8080"])

init_db()


@app.route("/")
def home():
    return "Web Application Security Lab"


@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    task = data.get("task")

    connection = get_connection()

    cursor = connection.execute(
        "INSERT INTO tasks (task) VALUES (?)",
        (task,)
    )

    connection.commit()

    task_id = cursor.lastrowid

    connection.close()

    return jsonify({
        "message": "Task created",
        "id": task_id,
        "task": task
    }), 201


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    connection = get_connection()

    rows = connection.execute(
        "SELECT id, task FROM tasks ORDER BY id"
    ).fetchall()

    connection.close()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row["id"],
            "task": row["task"]
        })

    return jsonify(tasks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
