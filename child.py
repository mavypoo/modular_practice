import parent

"""
One way these .pyc files will be created is when a module is imported. 
his is why you may not have seen .pyc files before now. Once a .pyc file is generated, as long as we don't change that file, 
Python will not have to re-compile your code to bytecode, which may save processing time when working with large code bases.
"""

#! Namespace:
"""
Namespace refers to which variables, functions, and classes are accessible to us at any given time during a program’s execution. 
Namespace is important because we have to know what variables we have access to. 
To see what variables are available in any given place, add the line print(locals()) and see what variables are in your current namespace. 
"""