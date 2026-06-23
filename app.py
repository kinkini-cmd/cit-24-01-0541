from flask import Flask, request, redirect

app = Flask(__name__)

todos = [
    {"task": "Learn Docker", "done": False},
    {"task": "Build To-Do App", "done": False},
    {"task": "Deploy Application", "done": False}
]

@app.route('/')
def home():
    html = """
    <html>
    <head>
        <title>To-Do App</title>
        <style>
            body {
                font-family: Arial;
                background: #f4f6f9;
                display: flex;
                justify-content: center;
                margin-top: 50px;
            }
            .container {
                background: white;
                padding: 20px;
                width: 400px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px #ccc;
            }
            h1 {
                text-align: center;
            }
            li {
                list-style: none;
                margin: 10px 0;
                padding: 8px;
                background: #f0f0f0;
                border-radius: 5px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .done {
                text-decoration: line-through;
                color: gray;
            }
            a {
                text-decoration: none;
                color: green;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
    <div class="container">
        <h1>My To-Do List</h1>

        <form action="/add" method="post">
            <input type="text" name="task" placeholder="New task" required>
            <button type="submit">Add</button>
        </form>

        <ul>
    """

    for i, todo in enumerate(todos):
        checked = "checked" if todo["done"] else ""
        task_class = "done" if todo["done"] else ""

        html += f"""
        <li>
            <span class="{task_class}">{todo['task']}</span>
            <div>
                <a href="/toggle/{i}">✔</a>
            </div>
        </li>
        """

    html += """
        </ul>
    </div>
    </body>
    </html>
    """

    return html


@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    todos.append({"task": task, "done": False})
    return redirect('/')


@app.route('/toggle/<int:index>')
def toggle(index):
    todos[index]["done"] = not todos[index]["done"]
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
