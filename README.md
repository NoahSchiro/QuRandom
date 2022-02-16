# QuRandom

### Table of contents
1. [About](#about)
2. [Documentation](#documentation)
3. [Open-source information](#contribute)

## About
Up until recently, all numbers generated for computer programs are [pseudo-random](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) by nature. This means that the data produced by these generators are deterministic, and therefore predictable. If someone wanted to predict the data produced, they would need to know the algorithm that's used for the generator and they would need to know the seed that is fed into the generator. This is traditionally very difficult to figure out, but it is still possible.

One area of computer science where it is very important that these numbers are *unpredictable* is cryptography. There exist very complex pseudo-random number generators that are deemed "cryptographically secure". With all of these algorithms, it is assumed that an assailant does not have access to the seed. There is also strong evidence that certain agencies have planted [back doors](https://blog.cryptographyengineering.com/2013/09/18/the-many-flaws-of-dualecdrbg/) in existing pseudo-random generators.

All of these problems can be avoided simply by getting rid of a deterministic algorithm. Quantum superposition is completely unpredictable ([as far as we know](https://www.nature.com/articles/439392d)). If we can induce particles into a 50/50 quantum superposition and then observe their state, we can get bits that are truly random. The purpose of this API is to give the entire world *quick* and *easy* access to quantum particles via IBM's quantum computing resources.

Normally, if users wanted to interface with these quantum computers, they have to wait in a queue for their program to run on the computer. Additionally, they occasionally have to pay for these services. This API is free and as quick as your internet connection!

## Documentation

The url that you are currently sitting on is the base for all calls, and for the purposes of this documentation we will denote it as `<url>` we will then use extensions to make the specific types of calls that we want to make.

All API calls will return a JSON data structure with some relevant meta-data and the random data

```
<url>/rand_bool/
```
Returns true or false

```
<url>/rand_int/<start>/<stop>
```
Returns a random integer between the range `<start>` and `<stop>` which is provided by the user. These values must be integers and if they are left blank, the function will default to start=0 and stop=100

```
<url>/rand_string/?<length>
```
Returns a random string of the user provided length. Again, this must be an integer and if it is left blank, the program defaults to a length of 10.

## Contribute
This whole project is on [GitHub](https://github.com/NoahSchiro/QuRandom) and I actively maintain it! The functionality is limited at the moment but the framework is in place for more random function to be added! Happy coding.
