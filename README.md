# CRUD Testing Application
 This application is developed for Hyperreality Technologies as part of their assignment

## Index



## Problem Statement

Create a RESTful API for the CRUD(Create, Read, Update, Delete) operations for a single model. Also you need to write basic unit tests to test the API. Model fields are listed below.

### Model Fields

```
id: Integer
checked: Boolean
name: String
type : String
age: Number
description: String
date: Datetime
```

## Prerequisits

To initialize with this project the following software packages should be installed in the host machine

- Python v3.9.6

## Installation

To setup the Flask Application, under the home directory locate requiremment.txt and with the help the file install all the dependancies. It is recommended to setup a virtual environment for the flast application before installing requirement.txt

### Setting Up Virtual Environment 

Windows: ```python -m venv env```

Mac/Linux: ```python3 -m venv env```

### Activate the Virtual Environment

Windows: ```env\Scripts\activate```

Mac/Linux: ```source env/bin/activate```

### Installing Dependancies

```pip install -r requirement.txt```

## Running the Code

Once the prerequisits are met and the environment is setup you can run the following commands. By default Flask application runs at port 5000.

### Start the application

From the home directory run the following command, provided you have already activated your virtual environment

```flask run```

### Basic Info of the APIs

You can open the application link to explore more on the API

Default Link: [http://localhost:5000/](http://localhost:5000/)