import math

functions = [name for name in dir(math) if callable(getattr(math, name))]

print(functions)
