from flask import Flask
from flask import jsonify

applic=Flask("Flask_object")

@applic.route("/")
def index():
    return "Helloworld i"

@applic.route("/Denmark")
def index_dk():
    return "Copenhagen"

@applic.route("/api1")
def api1():
    data = {"name":"Trump", "Cities":["New York", "Washington"]}
    return jsonify(data)

@applic.route("/api2", methods=["POST"])
def api2():
    data = {"name":"Trump", "Cities":["New York", "Washington"]}
    return jsonify(data)

#print(__name__)
if __name__ == "__main__":
#    print("in app.py")
#    print(__name__)
    applic.run()
