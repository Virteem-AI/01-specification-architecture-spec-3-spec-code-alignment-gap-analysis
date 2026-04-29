import uuid
from datetime import datetime, date
from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = {}


def validate_task_input(data, require_title=True):
    errors = []
    if require_title and not data.get("title"):
        errors.append("title is required")
    if "priority" in data and data["priority"] not in ("low", "medium", "high"):
        errors.append("priority must be one of: low, medium, high")
    if "status" in data and data["status"] not in ("todo", "in_progress", "done"):
        errors.append("status must be one of: todo, in_progress, done")
    if "due_date" in data and data["due_date"] is not None:
        try:
            date.fromisoformat(data["due_date"])
        except (TypeError, ValueError):
            errors.append("due_date must be ISO 8601 (YYYY-MM-DD)")
    return errors


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    errors = validate_task_input(data, require_title=True)
    if errors:
        return jsonify({"error": "; ".join(errors)}), 400

    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": data["title"],
        "description": data.get("description", ""),
        "priority": data.get("priority", "medium"),
        "status": data.get("status", "todo"),
        "due_date": data.get("due_date"),
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    tasks[task_id] = task
    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def list_tasks():
    result = list(tasks.values())
    status_filter = request.args.get("status")
    priority_filter = request.args.get("priority")
    if status_filter:
        result = [t for t in result if t["status"] == status_filter]
    if priority_filter:
        result = [t for t in result if t["priority"] == priority_filter]
    return jsonify(result), 200


@app.route("/tasks/<task_id>", methods=["GET"])
def get_task(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json(silent=True) or {}
    errors = validate_task_input(data, require_title=False)
    if errors:
        return jsonify({"error": "; ".join(errors)}), 400
    for field in ("title", "description", "priority", "status", "due_date"):
        if field in data:
            task[field] = data[field]
    return jsonify(task), 200


@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    del tasks[task_id]
    return "", 204
