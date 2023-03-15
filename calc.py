#Calcultor 

number1 = int(input('Enter first number \n'))
option_question = input('Enter option you would like \n')
number2= int(input('Enter second number \n'))
should_continue = input('would like to continue with this "yes" or "no"\n ')
def add (number1, number2 ):
   return number1 + number2

def minus (number1, number2):
   return number1-number2

def multiply (number1, number2):
   return number1*number2

def divide (number1, number2):
   return number1/number2


options ={
   "+":add, 
   "-":minus , 
   "*":multiply, 
   "/":divide
}

def identify():
     function = options[option_question]
     print(function(number1, number2))


again = True
if should_continue=="yes":
 while again == True  :
     operation_symbol = input('Enter a operation \n')
     number3 = int(input('Enter a number '))
     function = options[option_question]
     answer = function(function(number1, number2),number3)
     should_continue = input('would like to continue with this "yes" or "no"\n ')
     print(answer)
     again =  False
       
if should_continue == "no":
    again =  False
    function = options[option_question]
    answer = function(number1, number2)
  
   



   