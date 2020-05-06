from flask import Flask, request, jsonify, Response, render_template
import pandas as pd
import numpy as np


print('running')

app = Flask(__name__) 
  
@app.route("/") 
def home_view(): 
        return "<h1>test</h1>"
        
if __name__ == "__main__":
    app.run(debug=True)