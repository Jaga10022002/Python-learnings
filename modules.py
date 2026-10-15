# 8)What is Module
# A module is a Python file containing reusable code, such as functions, classes, and variables.
# Imagine a backend project that contains employee logic, database utilities, and validation functions. You can organize those functions into separate files rather than putting everything into one large script.
# Example project structure:
# employee_app/

# main.py

# employee.py

# validation.py

# Inside employee.py:
def get_employee_name():
    return "Ravi"


def calculate_salary(monthly_salary):
    return monthly_salary * 12

# inside main.py
# from employee import get_employee_name, calculate_salary

print(get_employee_name())
print(calculate_salary(30000))

# When main.py imports from employee.py, it can reuse the functions defined there.
# Why modules matter
# - Code becomes easier to maintain.
# - Functions can be reused across files.
# - Responsibilities are separated.
# - Testing becomes easier.
# - Larger projects become easier to navigate.

# 9. Importing modules
# Python supports several import styles.
# Import the whole module

import math

print(math.sqrt(25))
print(math.pi)

# we can do import math or from math import module name
from math import pi,sqrt
print(sqrt(36))
print(pi)

# use an alias
import math as m
print(m.sqrt(49))
print(m.pi)

# Aliases are useful when they improve clarity or follow an established convention, such as import numpy as np.

# Avoid wildcard imports
# from math import *
# This imports many names directly into the current namespace and can make it difficult to understand where a name came from. Prefer explicit imports.

# Built-in modules to know
# Module	Typical use
# math	Mathematical operations
# random	Random selections and values
# datetime	Dates and times
# os	Operating-system interfaces
# pathlib	Filesystem paths
# json	JSON encoding and decoding
# logging	Application logging
# configparser	INI configuration files
# collections	Specialized collection types
# unittest	Testing

import json
user = {"id":101,"name":"Jaga"}
json_text = json.dumps(user)
print(json_text)
# json.dumps() converts a Python object into a JSON-formatted string.

# 10)the if __name__ == "__main__" pattern
# When Python executes a file directly, its special variable __name__ is set to "__main__". When the file is imported as a module, its __name__ is normally the module's name.

# example employee.py
def greet():
  print("Hello From Employee Module")
if __name__ == "__main__":
  greet()

# if you run
# python employee.py
# The greeting executes.
# If another file imports employee, the greeting does not execute automatically.
# This pattern separates reusable definitions from code intended to run when a file is executed directly

# 11)Installing packages using pip
# pip -> is standard package installer
# commonly used for install third-party-packages
# For example, to install Django:
python -m pip install django

# To install Django REST Framework:
python -m pip installdjangorestframework

# Using python -m pip helps ensure that pip belongs to the Python interpreter you're invoking.

# Useful commands:
# Command	Purpose
# python --version	Check Python version
# python -m pip --version	Check pip and interpreter association
# python -m pip install requests	Install a package
# python -m pip show requests	Inspect an installed package
# python -m pip list	List installed packages
# python -m pip uninstall requests	Uninstall a package

# 12)Virtual environment(venv)
A virtual environment isolates the packages for one project from other projects.

Suppose one project requires Django 4.2 and another requires a newer Django release. Installing everything into the same global environment can create dependency conflicts.
A virtual environment gives each project its own package installation area.

Create and activate an environment
On Windows:

python -m venv .venv
.venv\Scripts\activate

On macOS or Linux:
python3 -m venv .venv
source .venv/bin/activate

Then install packages inside the activated environment:
python -m pip install django djangorestframework

Check which Python is active:
python -c "import sys; print(sys.executable)"

Deactivate the environment when you're finished:
deactivate

  Recommended project setup
  employee_backend/
├── .venv/
├── manage.py
├── requirements.txt
└── ...

  Normally, add .venv/ to .gitignore; don't commit the environment directory to your source repository.

  
  13. Dependency management
A backend project should document its dependencies so that another developer can reproduce the environment.
Export installed packages:

  python -m pip freeze > requirements.txt

    install dependencies from file
  python -m pip install -r requirements.txt

  example requirement.txt
  Django==5.2.0
djangorestframework==3.16.0


    What does pinning a version mean?
- Django==5.2.0 specifies an exact version.
- Django>=5.2,<6.0 specifies a range.
- An unpinned dependency can resolve to different compatible releases at different times.

  Your future Django workflow: Create a virtual environment first, activate it, install Django and DRF, then record and manage the dependencies. This prevents many common setup problems.

14)Python packages and  roject organization
A Python package organizes related modules into a directory structure.
For example, rather than keeping all employee-related code in individual files at the project root, group it into an employees package.

employee_backend/

main.py

employees/

__init__.py

models.py

services.py

exceptions.py

Each module has a specific responsibility:
 - models.py — data structures or model definitions.
 - services.py — business logic.
 - exceptions.py — custom exceptions.
 - __init__.py — optional package initialization and a place for carefully selected public exports.

   Import from a package

in employyes/service.py

def get_employee(employee_id):
    return {"id": employee_id, "name": "Ravi"}

  in main.py
  from employees.services import get_employee

employee = get_employee(101)
print(employee)

  # expected output
  {'id': 101, 'name': 'Ravi'}

  An __init__.py file is commonly used to identify a regular package, although Python also supports namespace packages without it. For your initial projects, including __init__.py in your own packages is a clear and familiar convention.

 Absolute vs relative imports
Absolute import:

from employees.services import get_employee

Relative import, used from a module inside the same package:

from .services import get_employee

  Relative imports help organize imports within a package. They generally require the module to be loaded as part of a package, rather than executed as a standalone file.

Avoid circular imports
A circular import occurs when module A imports module B while module B also imports module A, directly or indirectly.
Common solutions include:
- Moving shared logic into a third module.
- Restructuring module responsibilities.
- Importing dependencies at a narrower scope when appropriate.
- Using type-checking-only imports for annotations when suitable.
Don't fix circular imports by randomly moving imports around without understanding the dependency
In employees/services.py: