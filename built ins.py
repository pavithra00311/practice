
# 1. abs() - Returns the absolute value of a number
print("abs:", abs(-10))  # Output: 10

# 2. aiter() - Returns an asynchronous iterator for an asynchronous iterable
# (Must be used inside an async function, returns an async_generator object)
import asyncio
async def async_gen(): yield 1
print("aiter:", aiter(async_gen())) 

# 3. all() - Returns True if all items in an iterable are true
print("all:", all([True, 1, "yes"]))  # Output: True

# 4. any() - Returns True if any item in an iterable is true
print("any:", any([False, 0, "yes"]))  # Output: True

# 5. anext() - Returns the next item from an asynchronous iterator
# (Demonstrated here by awaiting its default value parameter for simplicity)
async def test_anext(): print("anext:", await anext(aiter(async_gen())))
asyncio.run(test_anext())  # Output: 1

# 6. ascii() - Returns a readable string version of an object, escaping non-ASCII characters
print("ascii:", ascii("Café"))  # Output: 'Caf\xe9'
# 7. bin() - Converts an integer into a binary string
print("bin:", bin(10))  # Output: 0b1010

# 8. bool() - Converts a value to a Boolean (True or False)
print("bool:", bool(1))  # Output: True

# 9. breakpoint() - Drops you into the debugger (commented out to prevent halting execution)
# breakpoint() 
print("breakpoint: Implemented by calling sys.breakpointhook()")

# 10. bytearray() - Returns a mutable array of bytes
print("bytearray:", bytearray([65, 66, 67]))  # Output: bytearray(b'ABC')

# 11. bytes() - Returns an immutable bytes object
print("bytes:", bytes([65, 66, 67]))  # Output: b'ABC'
# 12. callable() - Returns True if the object appears callable (like a function)
print("callable:", callable(print))  # Output: True

# 13. chr() - Converts an integer Unicode code point to its string character
print("chr:", chr(97))  # Output: a

# 14. classmethod() - Converts a method into a class method
class MyClass:
    @classmethod
    def hello(cls): return "Hello from Class"
print("classmethod:", MyClass.hello())  # Output: Hello from Class

# 15. compile() - Compiles source string into a code object that can be executed
code = compile("print('Hello')", "<string>", "exec")
print("compile:", code)  # Output: <code object <module> ...>

# 16. complex() - Creates a complex number
print("complex:", complex(3, 4))  # Output: (3+4j)
# 17. delattr() - Deletes an attribute from an object
class Item: x = 10
delattr(Item, 'x')
print("delattr: Attribute 'x' exists?", hasattr(Item, 'x'))  # Output: False

# 18. dict() - Creates a new dictionary
print("dict:", dict(a=1, b=2))  # Output: {'a': 1, 'b': 2}

# 19. dir() - Returns a list of valid attributes for an object
print("dir:", dir([]))  # Output: List of all list methods (e.g., 'append', 'clear')

# 20. divmod() - Returns the quotient and remainder of a division as a tuple
print("divmod:", divmod(20, 3))  # Output: (6, 2)
# 21. enumerate() - Adds a counter to an iterable and returns it as an enumerate object
print("enumerate:", list(enumerate(['apple', 'banana'])))  # Output: [(0, 'apple'), (1, 'banana')]

# 22. eval() - Parses and evaluates a dynamic string as a Python expression
print("eval:", eval("5 + 5"))  # Output: 10

# 23. exec() - Dynamically executes Python code (statements or blocks)
print("exec:"); exec("print('  -> Executed code inside a string!')")
# 24. filter() - Filters elements from an iterable based on a function condition
print("filter:", list(filter(lambda x: x > 5, [2, 7, 1, 9])))  # Output: [7, 9]

# 25. float() - Converts a number or string to a floating-point number
print("float:", float("10.5"))  # Output: 10.5

# 26. format() - Formats a value into a specified representation
print("format:", format(0.5, '%'))  # Output: 50.000000%

# 27. frozenset() - Returns an immutable set object
print("frozenset:", frozenset([1, 2, 2, 3]))  # Output: frozenset({1, 2, 3})
# 28. getattr() - Returns the value of a named attribute of an object
class User: name = "Bob"
print("getattr:", getattr(User, "name"))  # Output: Bob

# 29. globals() - Returns a dictionary representing the current global symbol table
print("globals: Contains current module keys like '__name__':", "__name__" in globals())  # Output: True
# 30. hasattr() - Returns True if an object has the given attribute
class Bike: wheels = 2
print("hasattr:", hasattr(Bike, "wheels"))  # Output: True

# 31. hash() - Returns the hash value of an object (if it is hashable)
print("hash:", hash("hello"))  # Output: (An integer hash value)

# 32. help() - Invokes the built-in help system (passing string to avoid interactive console hang)
print("help:", help(str.upper))  # Output: Prints help text for str.upper method

# 33. hex() - Converts an integer number to a lowercase hexadecimal string
print("hex:", hex(255))  # Output: 0xff
# 34. id() - Returns the unique identity/memory address of an object
print("id:", id(5))  # Output: (Unique integer location in memory)

# 35. input() - Prompts for user input (mocked out here with a variable to ensure non-blocking)
# user_input = input("Enter something: ")
print("input: Reads a line from input as a string.")

# 36. int() - Converts a number or string to an integer
print("int:", int("42"))  # Output: 42

# 37. isinstance() - Checks if an object is an instance or subclass of a given class
print("isinstance:", isinstance("hello", str))  # Output: True

# 38. issubclass() - Checks if a class is a subclass of another class
print("issubclass:", issubclass(bool, int))  # Output: True

# 39. iter() - Returns an iterator object
my_iterator = iter([1, 2, 3])
print("iter:", my_iterator)  # Output: <list_iterator object ...>
# 40. len() - Returns the length (number of items) of an object
print("len:", len("Python"))  # Output: 6

# 41. list() - Creates a mutable list object
print("list:", list("abc"))  # Output: ['a', 'b', 'c']

# 42. locals() - Returns a dictionary representing the current local symbol table
print("locals: Check if a local variable is tracked:", "my_iterator" in locals())  # Output: True
# 43. map() - Applies a function to all items in an iterable
print("map:", list(map(lambda x: x * 2, [1, 2, 3])))  # Output: [2, 4, 6]

# 44. max() - Returns the largest item in an iterable or among arguments
print("max:", max(10, 50, 20))  # Output: 50

# 45. memoryview() - Returns a memory view object from a bytes/bytearray argument
print("memoryview:", memoryview(b'abc'))  # Output: <memory at ...>

# 46. min() - Returns the smallest item in an iterable or among arguments
print("min:", min(10, 50, 20))  # Output: 5
# 47. next() - Retrieves the next item from an iterator
nums = iter([10, 20])
print("next:", next(nums))  # Output: 10
# 48. object() - Returns a base featureless object that acts as the base for all classes
print("object:", object())  # Output: <object object at ...>

# 49. oct() - Converts an integer into an octal string
print("oct:", oct(8))  # Output: 0o10

# 50. open() - Opens a file and returns a corresponding file object (mocked to prevent disk writes)
# file = open("test.txt", "w")
print("open: Opens file paths for reading, writing, or appending.")

# 51. ord() - Converts a single character into its integer Unicode code point
print("ord:", ord('a'))  # Output: 97
# 52. pow() - Returns the base to the power of exponent ($x^y$)
print("pow:", pow(2, 3))  # Output: 8

# 53. print() - Prints objects to the text stream file
print("print: Outputs messages directly to the terminal console!")

# 54. property() - Returns a property attribute for managing class attributes safely
class Person:
    def __init__(self): self._age = 0
    def get_age(self): return self._age
    age = property(get_age)
p = Person()
print("property:", p.age)  # Output: 0
# 55. range() - Generates an immutable sequence of numbers
print("range:", list(range(0, 5)))  # Output: [0, 1, 2, 3, 4]

# 56. repr() - Returns a printable string representation of an object
print("repr:", repr("hello"))  # Output: 'hello' (includes quotes)

# 57. reversed() - Returns a reversed iterator sequence
print("reversed:", list(reversed([1, 2, 3])))  # Output: [3, 2, 1]

# 58. round() - Rounds a floating-point number to a specific decimal precision
print("round:", round(3.14159, 2))  # Output: 3.14
# 59. set() - Creates a new set collection of unique elements
print("set:", set([1, 2, 2, 3]))  # Output: {1, 2, 3}

# 60. setattr() - Sets the value of a specified attribute of an object
class Car: pass
setattr(Car, "color", "red")
print("setattr:", Car.color)  # Output: red

# 61. slice() - Returns a slice object representing the set of indices specified by range()
s = slice(1, 4)
print("slice:", "abcdef"[s])  # Output: bcd

# 62. sorted() - Returns a new sorted list from the items in an iterable
print("sorted:", sorted([3, 1, 2]))  # Output: [1, 2, 3]

# 63. staticmethod() - Transforms a method into a static method
class Math:
    @staticmethod
    def add(a, b): return a + b
print("staticmethod:", Math.add(5, 5))  # Output: 10

# 64. str() - Converts an object into a clean string version
print("str:", str(123) + " dollars")  # Output: 123 dollars

# 65. sum() - Sums the start value and the items of an iterable
print("sum:", sum([1, 2, 3, 4]))  # Output: 10

# 66. super() - Returns a proxy object that delegates method calls to a parent class
class Parent:
    def greet(self): return "Hi"
class Child(Parent):
    def greet(self): return super().greet() + " from Child"
print("super:", Child().greet())  # Output: Hi from Child
# 67. tuple() - Creates an immutable tuple collection
print("tuple:", tuple([1, 2, 3]))  # Output: (1, 2, 3)

# 68. type() - Returns the data type class of an object
print("type:", type(123))  # Output: <class 'int'>
# 69. vars() - Returns the __dict__ attribute of a module, class, or object instance
class Dog:
    def __init__(self): self.name = "Rex"
print("vars:", vars(Dog()))  # Output: {'name': 'Rex'}
