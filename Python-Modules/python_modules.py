# What is a python module?
# A module is a file containing Python code.
# Modules are used to organize Python code into 
# 		better-organized code.

# What is a python package?
# A package is a collection of modules.

# Accessing Modules
# We can access modules by importing them.

# Importing a Module
import sys
locations = sys.path
for i in locations:
	print(i)
 
import calendar

leapdays = calendar.leapdays(2000,2050) 
print(leapdays)
is_it_leap = calendar.isleap(2036)
print(is_it_leap)
