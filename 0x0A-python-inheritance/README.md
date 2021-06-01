<p align="center"><img src='https://lh3.googleusercontent.com/proxy/v4d1SqHxXvXEBUd65zUn4Fumr2Ju4i6x3ApefpBkk7cxzKT9NqSnf5Shnk1_-TXrdQi5k8_Urgul8ERhAyloPrqnAwCIuZArB9qJkJaJSw1D_GNEcx5_qt3EPcLwxuC4di1UtKKODvUEJ5qj-yE8q_ALaMvzT-Lo8zU1L3o' alt='Banner' width=10%></p>

# 0x0A. Python - Inheritance

<p>
Of course, a language feature would not be worthy of the name “class” without supporting inheritance. The syntax for a derived class definition looks like this:

class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
The name BaseClassName must be defined in a scope containing the derived class definition. In place of a base class name, other arbitrary expressions are also allowed. This can be useful, for example, when the base class is defined in another module:

class DerivedClassName(modname.BaseClassName):
Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.

There’s nothing special about instantiation of derived classes: DerivedClassName() creates a new instance of the class. Method references are resolved as follows: the corresponding class attribute is searched, descending down the chain of base classes if necessary, and the method reference is valid if this yields a function object.

Derived classes may override methods of their base classes. Because methods have no special privileges when calling other methods of the same object, a method of a base class that calls another method defined in the same base class may end up calling a method of a derived class that overrides it. (For C++ programmers: all methods in Python are effectively virtual.)

An overriding method in a derived class may in fact want to extend rather than simply replace the base class method of the same name. There is a simple way to call the base class method directly: just call BaseClassName.methodname(self, arguments). This is occasionally useful to clients as well. (Note that this only works if the base class is accessible as BaseClassName in the global scope.)

Python has two built-in functions that work with inheritance:

Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.
Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int

</p>

###### General
- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

<p>

In this repo, you will find the following topics:

* __0. Lookup__
* __1. My list__
* __2. Exact same object__
* __3. Same class or inherit from__
* __4. Only sub class of__
* __5. Geometry module__
* __6. Improve Geometry__
* __7. Integer validator__
* __8. Rectangle__
* __9. Full rectangle__
* __10. Square #1__
* __11. Square #2__



### Authors :black_nib:
* __Maria Fernanda Lopez__

#### Software Academy 👨‍💻

<p aling="center">
<a href="https://www.holbertonschool.com" target="_blank">
*:sparkles: Follow me *[Twitter](https://twitter.com/ferchislopez910)</a>
</p>

<p>resource:
https://docs.python.org/3.4/tutorial/classes.html#inheritance
<p>