# Banner proveniente de https://www.programcreek.com/python/?CodeExample=print+banner
# modificado para este proyecto

from flask import Flask, render_template,request

app = Flask(__name__)
print("Running ...")

banner = """\
    ,-~~-.___.    
    / |  x     \    
    (  )        0   
    \_/-, ,----'  ____ 
        ====      ||  
    /  \-'~;   ||     |   
    /  __/~| ...||__/|-" 
    =(  _____||________| 
"""

app = Flask(__name__)

@app.route('/S', )
def crazy():
    return render_template("hello.html", banner=banner)

if __name__ == "__main__":
    app.run(debug=True)
