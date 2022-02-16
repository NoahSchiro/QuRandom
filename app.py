from flask import *                         # Main imports for API creation
import json                                 # We are going to return JSON files
import time
from QuRandom import QuRandom               # We are going to return timestamps for people's API calls

# Create the API
app = Flask(__name__)

# Quantum computer interface
generator = QuRandom()

@app.route('/')
def home_page():

    # Flask method of rendering an html page. This will serve 
    # as the documentation for the project
    return """
    <h1 id="qurandom">QuRandom</h1>
    <h3 id="table-of-contents">Table of contents</h3>
    <ol>
    <li><a href="#about">About</a></li>
    <li><a href="#documentation">Documentation</a></li>
    <li><a href="#contribute">Open-source information</a></li>
    </ol>
    <h2 id="about">About</h2>
    <p>Up until recently, all numbers generated for computer programs are <a href="https://en.wikipedia.org/wiki/Pseudorandom_number_generator">pseudo-random</a> by nature. This means that the data produced by these generators are deterministic, and therefore predictable. If someone wanted to predict the data produced, they would need to know the algorithm that&#39;s used for the generator and they would need to know the seed that is fed into the generator. This is traditionally very difficult to figure out, but it is still possible.</p>
    <p>One area of computer science where it is very important that these numbers are <em>unpredictable</em> is cryptography. There exist very complex pseudo-random number generators that are deemed &quot;cryptographically secure&quot;. With all of these algorithms, it is assumed that an assailant does not have access to the seed. There is also strong evidence that certain agencies have planted <a href="https://blog.cryptographyengineering.com/2013/09/18/the-many-flaws-of-dualecdrbg/">back doors</a> in existing pseudo-random generators.</p>
    <p>All of these problems can be avoided simply by getting rid of a deterministic algorithm. Quantum superposition is completely unpredictable (<a href="https://www.nature.com/articles/439392d">as far as we know</a>). If we can induce particles into a 50/50 quantum superposition and then observe their state, we can get bits that are truly random. The purpose of this API is to give the entire world <em>quick</em> and <em>easy</em> access to quantum particles via IBM&#39;s quantum computing resources.</p>
    <p>Normally, if users wanted to interface with these quantum computers, they have to wait in a queue for their program to run on the computer. Additionally, they occasionally have to pay for these services. This API is free and as quick as your internet connection!</p>
    <h2 id="documentation">Documentation</h2>
    <p>The url that you are currently sitting on is the base for all calls, and for the purposes of this documentation we will denote it as <code>&lt;url&gt;</code> we will then use extensions to make the specific types of calls that we want to make.</p>
    <p>All API calls will return a JSON data structure with some relevant meta-data and the random data</p>
    <pre><code>&lt;<span class="hljs-built_in">url</span>&gt;<span class="hljs-regexp">/rand_bool/</span>
    </code></pre><p>Returns true or false</p>
    <pre><code><span class="hljs-tag">&lt;<span class="hljs-name">url</span>&gt;</span>/rand_int/<span class="hljs-tag">&lt;<span class="hljs-name">start</span>&gt;</span>/<span class="hljs-tag">&lt;<span class="hljs-name">stop</span>&gt;</span>
    </code></pre><p>Returns a random integer between the range <code>&lt;start&gt;</code> and <code>&lt;stop&gt;</code> which is provided by the user. These values must be integers and if they are left blank, the function will default to start=0 and stop=100</p>
    <pre><code><span class="hljs-tag">&lt;<span class="hljs-name">url</span>&gt;</span>/rand_string/<span class="hljs-tag">&lt;<span class="hljs-name">length</span>&gt;</span>
    </code></pre><p>Returns a random string of the user provided length. Again, this must be an integer and if it is left blank, the program defaults to a length of 10.</p>
    <h2 id="contribute">Contribute</h2>
    <p>This whole project is on <a href="https://github.com/NoahSchiro/QuRandom">GitHub</a> and I actively maintain it! The functionality is limited at the moment but the framework is in place for more random function to be added! Happy coding.</p>
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