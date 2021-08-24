from flask import Flask

applic=Flask("Flask_object")

@applic.route("/")
def index():
    return "Helloworld i"


@applic.route("/Denmark")
def index_dk():
    return "Copenhagen"

print(__name__)
if __name__ == "__main__":
    print("in app.py")
    print(__name__)
    applic.run()
