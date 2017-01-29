def info(object, spacing=50, collaspe=1):               #(1)(2)(3)
    """Print methods and doc strings.

    Takes module, class, list, dictionary or string."""
    methodlist = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collaspe and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                     (method.ljust(spacing),
                      processFunc(str(getattr(object, method).__doc__)))
                     for method in methodlist])

if __name__ == "__main__":                              #(4)(5)
    print info.__doc__

"""
(1)     This module has one function, info.
        According to its function decaration it takes three parameters:
        object, spacing and collaspe.
        The last two are actually optional parameters.
(2)     The info function has a multiline doc string that suffinctly describes the functions purpose.
        Note that no return walue is mentioned;
        This function will be used solely for its effects, rather than its value.
(3)     Code within the code is indented.
(4)     The if __name__ trick allows this program do something useful when run by itself,
        without interfering with its use as a module for other programs.
        In this case, the program simply prints the doc string or the info function.
(5)     if statements use == for comparison, and parentheses are not required.
        The info function is designed to be used by the programmer, while working in IDE.
        It takes any object that has functions or methods (like a module, which has functions,
        or a list, which has methods) and prints the functions and their doc strings.

console output
>>> from apihelper import info
>>> li = []
>>> info(li)

>>> import odbchelper
>>> info(odbchelper)
buildConnectionString Build a connection string from a dictionary of parameters. Returns String.
>>> info(odbchelper, 30)
buildConnectionString          Build a connection string from a dictionary of parameters. Returns String.
>>> info(li, 50)

>>> info(odbchelper,50)
buildConnectionString                              Build a connection string from a dictionary of parameters. Returns String.
>>> info(odbchelper,50,0)
buildConnectionString                              Build a connection string from a dictionary of parameters.

    Returns String.


>>> info(odbchelper)
buildConnectionString Build a connection string from a dictionary of parameters. Returns String.
>>> info(odbchelper,12)
buildConnectionString Build a connection string from a dictionary of parameters. Returns String.
>>> info(odbchelper, collaspe = 0)
buildConnectionString Build a connection string from a dictionary of parameters.

    Returns String.
>>> info(spacing = 25, object=odbchelper)
buildConnectionString     Build a connection string from a dictionary of parameters. Returns String.
>>>


"""