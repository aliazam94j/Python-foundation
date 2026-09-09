from flask import Flask, request, jsonify
app = Flask(__name__)
latest_data = {}

@app.route("/sensor-data", methods=["POST"])
def sensor_data():
    global latest_data
    latest_data = request.json
    return{"status": "saved"},200

@app.route("/temperature", methods=["GET"])
def temperature():
    return jsonify(latest_data)
app.run(debug=True)


@app.route("/device",methods=["GET"])
def device():
    return jsonify({"device":"ULTRA" })