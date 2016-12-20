# coding: utf-8
"""
In this module, we encapsulated some useful function to get the info in module, class, function, object, etc.
"""
import objects

def getDoc(obj):
    """
    Get the document of a method, object, class, etc.
    """
    if obj.__doc__:
        # print(obj.__doc__)
        return obj.__doc__.strip()
    else:
        return u''

if __name__ == u'__main__':
    def sayHi():
        """
        This is a sample function.
        """
        pass

    class Dog:
        """
        This dog can not wauf.
        """
        pass

    print(getDoc(sayHi))
    print(getDoc(Dog))
    print(getDoc(Dog()))
    # print(getDoc(objects))
