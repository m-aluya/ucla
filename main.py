from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api =  Api(app)

class HelloWorld(Resource):
    def get(self,name,id):
        return {"data": name,"ID" : id}

 


api.add_resource(HelloWorld, "/index/<string:name>/<int:id>")






if __name__ == "__main__":
    app.run(debug=True)