# Check that a tuple type cannot be changed in python
a = (34,234,"Nisu")
a[2] = "Nisa"
#    TypeError: 'tuple' object does not support item assignment
