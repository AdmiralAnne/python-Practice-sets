from flask import Flask
from sympy import true
#to create a flask application
app=Flask(__name__) # initializes the application

#create some end points


if __name__ == '__main__':
    # keep refreshing ncase change is detected~
    app.run(debug=True, port=8000)