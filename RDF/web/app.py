from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in the app root folder

e = create_engine('sqlite:///salaries.db')

app = Flask(__name__)
api = Api(app)

class Departments_Meta(Resource):
    def get(self):
        # Connect to our Database
        conn = e.connect()
        # Perform query
        sql = "select distinct DEPARTMENT from salaries"
        query = conn.execute(sql)
        # Wrap the data and return
        results = {'departments': [i[0] for i in query.cursor.fetchall()]}
        return jsonify(results)

class Departmental_Salary(Resource):
    def get(self, department_name):
        # Connect to our Database
        conn = e.connect()
        # Perform query
        sql = "select * from salaries where Department='{0}'".format(department_name.upper())
        query = conn.execute(sql)
        # Wrap the data and return
        result = {'data': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)
       
api.add_resource(Departmental_Salary, '/departments/<string:department_name>')
api.add_resource(Departments_Meta,    '/departments')

if __name__ == '__main__':
    app.run(debug=True)
