from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


#http://127.0.0.1:5000

@app.route('/')
def index():
    return render_template("index.html",
                           length = 8, 
                           width = 8)

@app.route('/<int:leng>/<int:width>/<colorOne>/<colorTwo>')          # The "@" decorator associates this route with the function immediately following
def index1(leng, width,colorOne,colorTwo):
    return render_template("index.html",
                           length = leng, 
                           width = width,
                           colorOne = colorOne,
                           colorTwo = colorTwo
                           )


@app.route('/<path:path>') #went to the wrong site.
def wrong_path(path):
    return "this is the wrong site"


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.