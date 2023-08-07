# AirBnB clone - The console

## Overview
- A command line interpreter to manage AirBnb objects
- This is the beginning of the a full web appliction of the ALX SE journey
- A clone of the [AirBnb](https://www.airbnb.com/)

### The command line interpreter
The command line interpreter is simillar to the shell but limited
- It manages the objects of our project
   - Create a new object(ex: a new User or a new place)
   - Retrieve an object from a file, a database etc…
   - Do operations on objects (count, compute stats, etc…)
   - Update attributes of an object
   - Destroy an object

### How the command line interpreter works
- The shell works in the interative mode:
```bash
$./console.py
(hbnb) help

Documented commands(type help <topic>):
=======================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
- And also works in non-interactive mode:(like shell project in C)
- All tests pass in the non - interactive mode
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
This a team project by Gideon and Edwin
