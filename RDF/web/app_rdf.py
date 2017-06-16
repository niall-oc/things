from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from rdflib.namespace import DC, FOAF
from rdflib import Graph, RDF, BNode, URIRef
import urllib

#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in the app root folder

e = create_engine('sqlite:///salaries.db')

app = Flask(__name__)
api = Api(app)

class Departments(Resource):
    def get(self):
        # Connect to our Database
        conn = e.connect()
        # Perform query
        sql = "select distinct DEPARTMENT from salaries"
        query = conn.execute(sql)
        # Wrap the data and return
        departments = [i[0] for i in query.cursor.fetchall()]
        accept = request.headers['Accept']
        if 'rdf' in accept:
            resp = make_response(self.rdf_get(departments), 200)
            resp.headers['Content-Type'] = 'application/rdf+xml'
        elif 'json' in accept:
            resp = jsonify({'departments': departments})
        else:
            resp = make_response('\n'.join(departments), 200)
        return resp
    
    def rdf_get(self, departments):
        us_dept = URIRef('https://en.wikipedia.org/wiki/List_of_federal_agencies_in_the_United_States')
        g = Graph()
        for dept in departments:
            this_dept = URIRef('http://127.0.0.1:5000/departments/{0}'.format(urllib.quote(dept)))
            g.add((this_dept, RDF.type, us_dept,))
        return g.serialize(format='n3')
        

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
api.add_resource(Departments,    '/departments')

if __name__ == '__main__':
    app.run(debug=True)
