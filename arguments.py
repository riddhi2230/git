# def sum(a,b,c):
#     sum=int(a+b+c)
#     print(sum)
#     print(type(sum))

# a=int(input("enter the 1st number"))
# b=int(input("enter the 2nd number"))
# c=int(input("enter the 3rd number"))

# sum(a,b,c)

# Default arguments

# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy","Riddhi")

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))

def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)
