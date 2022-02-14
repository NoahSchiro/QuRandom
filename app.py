from logging import NullHandler
from flask import *         # Main imports for API creation
import json                 # We are going to return JSON files
import time

from QuRandom import QuRandom                 # We are going to return timestamps for people's API calls

# Create the API
app = Flask(__name__)

# Quantum computer interface
generator = QuRandom()

@app.route('/')
def home_page():

    # Flask method of rendering an html
    return """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <title>QuRandom</title>
        <meta charset="utf-8">
        <meta name="viewport" content=width=device,user-scalable=yes">
        <style></style>
        <script></script>
    </head>

    <body class="content">
        <h1>Landing Page</h1>
    </body>
    </html>
    """

@app.route('/rand_bool/')
def get_random_bool():

    # Since there is no input, we don't need to ensure that 
    # the input is properly shaped. We can just pop a random bit from the queue
    data = json.dumps({

        # Tells the user the call type
        "call_type" : "random_bool",
        
        # Tells the user down to the second when the call was made (this may be 
        # the local time of the server on which the API is running)
        "time_stamp" : time.asctime( time.localtime(time.time()) ),

        # Make the appropriate call to the generator
        "data" : generator.get_bool()

    })
    
    return data

@app.route('/rand_int/')
@app.route('/rand_int/<start>/<stop>')
def get_random_int(start='0', stop='100'):

    # Convert to ints
    start = int(start)
    stop = int(stop)

    if start > stop:

        # If for some reason start comes after stop, 
        # then pass these parameters into the function in the correct order
        integer = generator.get_int(stop, start)

    # Else, the input was a well formed expression
    else:

        # Normal call to the generator
        integer = generator.get_int(start, stop)
    
    # Form the response
    data = json.dumps({

        # Tells the user the call type
        "call_type" : "random_int",
        
        # Tells the user down to the second when the call was made (this may be 
        # the local time of the server on which the API is running)
        "time_stamp" : time.asctime( time.localtime(time.time()) ),

        # Get the approriate data call
        "data" : integer
    })

    return data

@app.route('/rand_string/')
@app.route('/rand_string/<length>')
def get_random_string(length='10'):

    # Convert to int
    length = int(length)

    # If length is unintialized just call the default function
    if not length:
        string = generator.get_string()
    
    # If the user specifies some sort of string length, pass that in
    else:
        string = generator.get_string(length)
    
    # Form the response
    data = json.dumps({

        # Tells the user the call type
        "call_type" : "random_string",
        
        # Tells the user down to the second when the call was made (this may be 
        # the local time of the server on which the API is running)
        "time_stamp" : time.asctime( time.localtime(time.time()) ),

        # Get the approriate data call
        "data" : string
    })
    
    return data

if __name__ == "__main__":
    app.run()