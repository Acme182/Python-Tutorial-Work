lucky_numbers = [42, 8, 145, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", 'Toby']
friend = lucky_numbers.copy()

#tupls#
coordinates = [(4, 5), (6, 7), (23, 99)]
#print(coordinates[0])#

#Functions
#def say_hi(name, age):
#    print("Hello " + name + ", you are " + str(age))

#say_hi("Mike", 35)
#say_hi("Steve", 34)
#say_hi("Frank", 21)

#Return Statements

#def cube(num):
 #   return num*num*num

#result = cube(4)
#print(result)

#If Statments
is_male = False
is_tall = False

#if is_male and is_tall:
 #   print("You are a tall male")
#elif is_male and not(is_tall):
 #   print("You are a short male")
#elif not(is_male) and is_tall:
 #   print("You are not a male but are tall")
#else:
 #   print("You are neither a male or tall")

 #If Statements & Compairisons

#def max_num(num1, num2, num3):
    #if num1 >= num2 and num1 >= num3:
       # return num1
  #  elif num2 >= num1 and num2 >= num3:
   #     return num2
  #  else:
    #    return num3

#print(max_num(22, 1, 5))

#Building a Better Calculator

#num1 = float(input("Enter first number: "))
#op = input("Enter operator: ")
#num2 = float(input("Enter second number: "))

#if op == "+":
 #   print(num1 + num2)
#elif op == "-":
 #   print(num1 - num2)
#elif op == "/":
 #   print(num1 / num2)
#elif op == "*":
 #   print(num1 * num2)
#else:
 #   print("Invalid operator Stupid")

#DICTIONARIES

#monthCoversions = {
 #   1 : "January",
  #  "Feb" : "Febuary",
  #  "Mar" : "March",
  #  "Apr" : "April",
 #   "May" : "May",
  #  "Jun" : "June",
  #  "Jul" : "July",
  #  "Aug" : "August",
  #  "Sep" : "September",
  #  "Oct" : "October",
  #  "Nov" : "November",
  #  "Dec" : "December",
#}

#print(monthCoversions.get("love", "Not a Valid Key"))
#print(monthCoversions["Nov"])
#print(monthCoversions.get(1))

#WHILE LOOP

#i = 1
#while i <= 10:
 #   print(i)
  #  i += 1

#print("Done with loop")

#Building a Guessing Game

#secret_word = "giraffe"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False

#while guess != secret_word and not(out_of_guesses):
    #if guess_count < guess_limit:
     #   guess = input("Enter guess: ")
    #    guess_count += 1
    #else:
       # out_of_guesses = True

#if out_of_guesses:
    #print("Out of Guesses, YOU LOSE!")
#else:
    #print("You Win!")

#FOR LOOP
#friends = ["Jim", "Karen", "Kevin"]
#len(friends)
#for friends in friends:
  #  print(friends)

#for index in range(3, 10):
    #print(index)

#for index in range(len(friends)):
   # print(friends[index])

#for index in range(5):
    #if index == 0:
       # print("first Iteration")
   # else:
        #print("Not First")

#EXPONENT FUNCTION

#print(2**3)

#def raise_to_power(normal, timeser):
  #result = 1
  #for index in range(normal):
      #result = result + timeser
  #r#eturn result

#print(raise_to_power(3, 2))

#total2 = 0
#for i in range(1, 5):
   # total2 += i
#print(total2)

#print(list(range(1, 8)))
#total3 = 0
#for i in range(1, 8):
   # if i % 3 == 0:
     #   total3 += i
#print(total3)
#print(4 % 3)
#total = 0
#for index in range(1, 100):
   # if index % 3 == 0 or index % 5 == 0:
    #    total += index
#print(total)

#exampleList = [1, 3, 3, 4, 5, 6, 7, 8]
#for eachNumber in exampleList:
  #  print(eachNumber)
   # print('continue program')
#nums = [1, 2, 3, 4, 5]

#for num in nums:
    #if num == 3:
       # print("Found!")
        #continue
    #print(num)
#for num in nums:
    #for letter in "abc":
        #print(num)

#for i in range(10):
   # print(i)
#x = 0

#while x < 10:
    #print(x)

#2D lists & Nested loops

#number_grid = [
   # [1, 2, 3, 0, 0],
   # [4, 5, 6],
   # [7, 8, 9],[0]
#]

#print(number_grid[2][1])
#for row in number_grid:
  #  for col in row:

     #   print(col)

#BUILD A TRANSLATOR

#def translate(phrase):
    #translation = ""
    #for letter in phrase:
        #if letter.lower() in "aeiou":
            #if letter.isupper():
                #translation = translation + "G"
            #else:
                translation = translation + "g"
        #else:
            translation = translation + letter
    #return translation

#print(translate(input("Enter a Phrase:")))

#Comments
'''
sdsdsd
sdsdsd
sdsdsd
sdsd
'''

#Try Expect

