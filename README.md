# **AirBnB clone** - The console

## Content:

  * [Introduction](#Introduction)
  * [Installation](#Installation)
  * [Usage](#Usage)
  * [Authors](#Authors)

### Introduction:

This console application is designed to mimic the functionality of [Airbnb](https://www.airbnb.com/), a popular online platform for booking accommodations. Users can interact with the application through a command-line interface to perform various tasks related to property listings, bookings, and user management.

The console or the command interpreter is an application to manage object abstraction.
the following functionalities are supported:
  * new objects creation.
  * Retrieving Objects from a file.
  * Operating on objects.
  * Destroying Objects.

### Installation:

to install the console, simply clone the repository on your local machine by running the following command
```bash
git clone https://github.com/aysuarex/AirBnB_clone.git
```
find and run the executable file `console.py` by
```bash
./console.py
```
#### Execution:

In interactive mode
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
In Non-interactive mode
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
### Usage:

starting the console on the interactive mode should look like this:
```bash
$ ./console.py
(hbnb)
```
using the help command will display the available commands in the console
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```
to quit the console use quit command (alternatively use Ctr+D)
```bash
(hbnb) quit
$
```

### Authors

all the contributers in this project are listed in the [AUTHORS](./AUTHORS) file.
