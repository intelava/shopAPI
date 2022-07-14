from flask import Flask, jsonify, request, make_response, render_template
from flask_restful import Resource, Api

from database import *
from filter import *

import objectModels


"""
Some libraries might seem unused but connected py files using each others lib
"""

connectionGate = sqlite3.connect("database.db")#Creates sqlite database if it doesn't exist.

engineMain = create_engine('sqlite:///database.db')#Session engine of sqlalchemy

objectModels.baseObject.metadata.create_all(bind=engineMain)

app = Flask(__name__)
api = Api(app)


@app.route('/search/', methods=['POST'])
def search():
    searchFilter = request.get_json()

    cleanedSearchFilter = cleanFilter(searchFilter, objectModels.template)

    statement = objectModels.filterCriteria(cleanedSearchFilter)

    objects = executeStatement(statement)

    list_of_objects = encode_to_json(objects)

    list_of_objects = objectModels.sort_func(list_of_objects, cleanedSearchFilter)

    return jsonify(list_of_objects)

@app.route('/insert/', methods=['POST'])
def insert():
    obj = request.get_json()
    return insertRow(obj)


# driver function
if __name__ == '__main__':
    app.run(debug=True)
