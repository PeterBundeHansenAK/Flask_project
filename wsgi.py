from app import applic
print("inside wsgi.py")
if __name__ == "__main__":
    print(__name__)
    applic.run()
