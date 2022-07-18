""" Basic Example Python Program """

print("Hello World")

NAME = "david"
AGE = 49
MARRIED = True

if MARRIED:
    MARRIED_STRING = "married"
else:
    MARRIED_STRING = "single"

print(
    "Hello "
    + NAME
    + ", you are "
    + str(AGE)
    + " years old, and you are "
    + MARRIED_STRING
)

NAME = 14  # type: ignore

print(NAME)
