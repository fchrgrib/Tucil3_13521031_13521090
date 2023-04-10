from flask import Flask, render_template, request, jsonify
from algorithm.CSU import csu
from algorithm.Astar import a_star
import time


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    matrix = request.json['adjacencyMatrix']
    origin = int(request.json['origin'])
    destination = int(request.json['destination'])
    ucs = bool(request.json['ucs'])
    
    index_array = []
    # process the matrix data here
    start_time = time.time()
    if(ucs) :
        index_array = csu(matrix, origin, destination)
    else :
        index_array = a_star(matrix, origin, destination)
    end_time = time.time()

    time_in_ms = (end_time - start_time) * 1000
    
    
    # return the index array as a JSON response
    return jsonify({'index_array': index_array, 'runtime': time_in_ms})