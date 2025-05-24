from flask import Flask,jsonify,request

app=Flask(__name__)
@app.route("/")
def home():
    return jsonify({"message":"Welcome to the todo API"})

todos=[{"id":1,"tasks":"Learn Flask","done":False},
       {"id":2,"tasks":"Build Apis","done":False}]

@app.route("/todo",methods=["GET"])
def get_all_todos():
    return jsonify(todos)

@app.route("/todo",methods=["POST"])
def update_todo():
    data=request.get_json()
    new_todo={
        "id":len(todos)+1,
        "tasks":data["tasks"],
        "done":False
    }
    todos.append(new_todo)
    return jsonify(new_todo),201


@app.route("/todo/<int:todo_id>",methods=["PUT"])
def mark_done(todo_id):
    for todo in todos:
        if todo["id"]==todo_id:
            todo["done"]=True
            return jsonify(todos)
        
    return jsonify({"error":"Todo not found"})

@app.route("/todo/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    original_length = len(todos)
    todos = [todo for todo in todos if todo["id"] != todo_id]

    if len(todos) == original_length:
        return jsonify({"error": "Todo not found"}), 404

    return jsonify({"message": f"Todo {todo_id} deleted"}), 200


if __name__=="__main__":
    app.run(debug=True)
