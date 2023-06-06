
from scipy.spatial import distance
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')

def my_form():
    return render_template('index6.html')


@app.route("/get", methods=["POST"])


def my_form_post():
    
    

    
    x1 = int( request.form['wordCount1'])
    y1 = int( request.form['wordCount2'])
    
    x2 = int(request.form['sentNumber1'])
    y2 = int(request.form['sentNumber2'])
    
    start=[x1,y1]
    goal=[x2,y2]
    
    
    dist= distance.euclidean(start, goal)
    
      
    
    return str(dist)



if __name__ == "__main__":
    app.run(debug=False)
