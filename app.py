from flask import Flask,request,jsonify
import json
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)

app = Flask(__name__)

# GET endpoint
@app.get("/hello")

def hello():
    return jsonify({"message":"Hello, world!",
     "status": "success"
     })

# POST endpoint
@app.post("/echo")
def echo():

    data = request.get_json()

    if not data:
        return json({
            "error": "No JSON data provided"
        }), 400

    return jsonify({
        "you sent":data,
        "status": "received"
    })

if __name__ =="__main__":
    app.run(debug=True)