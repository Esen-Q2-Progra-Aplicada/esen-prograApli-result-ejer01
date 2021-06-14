from flask import Flask
from flask_restful import Api
from resources.empresa_resource import Empresa

app = Flask(__name__)
api = Api(app)

api.add_resource(Empresa, "/empresa/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
