# Identity operators
# The is operator is used to tell whether two variable refers to same object. Its different from the == oprator which equals.

# the is and == poperator

firstClass = []
secondClass = []

if firstClass == secondClass:
    print('Both are equal')
else:
    print('Both are not equal')
if firstClass is secondClass:
    print('Both variable are pointing to the same object')
else:
    print('Both variables are not pointing to the same object')

# Logicsl operators
# These operaors ae used to combine conditional statements to True or False
# They incude and, or and not
# Logial and returns true if both of the stetements are true otherwise it returns false

a = 45
b = 345
if a > 0 and b > 0:
     print(' Both a and b ae greater than 0')
else:
 print("At least one variable is less than 0")

 # Logical or returns true if ano of the statements are true

 c = 60
 if not c:
     print('Boolean value is true')
 else:
     print('Boolean value is nt true')
