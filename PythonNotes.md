A class in an except clause is compatible with an exception if it is the same class or a base class thereof,  and the first matching except clause is triggered if there are many except clauses.

"""

try...except statement has optional else clause which must follow all except clauses - and is executed if try clause does not raise an exception.

"""
finally statement could be there with try...except and would be executed regardless of the try..except execution, and would be used for clean up in general.

"""
The else clause is only executed when your while condition becomes false. If you break out of the loop, or if an exception is raised, it won't be executed. 

