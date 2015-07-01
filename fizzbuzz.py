count = 0

user_input = raw_input("How high do we count?")
print user_input


for count in range(0,int(user_input) + 1):
    if count % 5 == 0 and count % 3 == 0:
        print ("FizzBuzz")
    elif count % 3 == 0:
        print ("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)
        
   