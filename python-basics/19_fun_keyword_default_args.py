# Here argument by will have default value as 10. If the calling function does not provide a value for by, it will use 10.
# If a value is provided, it will override the default.
# Default parameters must be declared after non-default parameters.
def increment(number, by=10):
    return number + by
# Default argument 'by' is set to 10


value = increment(5)
print(value)


value = increment(5, 20)
print(value)
