from flask import Flask, jsonify, request

app = Flask(__name__)

tasks =[
    {
        'id':1,
        'title': u"To play",
        'description': 'Start playing at 4pm',
        'done': False

    },

    {
        'id':2,
        'title': u"Study English",
        'description': 'The Fallen Man',
        'done': False

    },


]

    


@app.route("/")
def hello():
    return "Hi Purnajith";

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })

@app.route("/add-task", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message":"Please try again, something went wrong!"
        },400)

    task ={
        "id": tasks[-1]['id'] + 1,
        "title": request.json['title'],
        "decription": request.json.get('description',""),
        'done': False
    }
    tasks.append(task)

    return jsonify({
            "status": "success",
            "message":"Task Successfully added"
        })




if __name__ == '__main__':
    app.run()

