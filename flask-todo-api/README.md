# Flask Todo API

A simple RESTful API built with Flask to manage todo tasks.

## Features

- Get all todos
- Add a new todo
- Mark a todo as done
- Delete a todo
- JSON responses

## Setup & Installation

1. Clone the repo:
   git clone https://github.com/yourusername/flask-todo-api.git

2. Navigate to the project folder:
   cd flask-todo-api

3. Create and activate a virtual environment:
   python -m venv venv
   On Windows:
   venv\Scripts\activate

   On macOS/Linux:
   source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run the app:
   python app.py

## API Endpoints

| Method | Endpoint          | Description       |
| ------ | ----------------- | ----------------- |
| GET    | `/`               | Welcome message   |
| GET    | `/todo`           | Get all todos     |
| POST   | `/todo`           | Add a new todo    |
| PUT    | `/todo/<todo_id>` | Mark todo as done |
| DELETE | `/todo/<todo_id>` | Delete a todo     |

## Usage

Use tools like [Postman](https://www.postman.com/) or curl to test API endpoints.

Use the following steps to test each API endpoint using Postman:

1. Home (GET /)
   Method: GET

URL: http://127.0.0.1:5000/

No body needed.

Click Send to see the welcome message.

2. Get All Todos (GET /todo)
   Method: GET

URL: http://127.0.0.1:5000/todo

No body needed.

Click Send to retrieve the list of todos.

3. Add a New Todo (POST /todo)
   Method: POST

URL: http://127.0.0.1:5000/todo

Go to Body tab → Select raw → Choose JSON.

Enter JSON data, for example:

{
"tasks": "Build a REST API"
}

Click Send to add the todo.

4. Mark Todo as Done (PUT /todo/<todo_id>)
   Method: PUT

URL: http://127.0.0.1:5000/todo/1 (replace 1 with the todo ID)

No body needed (your current API marks as done automatically).

Click Send to mark the todo done.

5. Delete a Todo (DELETE /todo/<todo_id>)
   Method: DELETE

URL: http://127.0.0.1:5000/todo/1 (replace 1 with the todo ID)

No body needed.

Click Send to delete the todo.
