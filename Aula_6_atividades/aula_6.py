#Link1
#1. Write a Python program to calculate the length of a string.
text1 = input()
print(f"""Meu texto é {text1} e possui {len(text1)} elementos""")

lista = []
import random
while (len(lista)<5):
  lista.append(random.randint(1,10))
print(f"lista 2 :{lista}")

#2. Write a Python program to sum all the items in a list.
print(f"A soma dos numeros da lista é {sum(lista)}")

#3. Write a Python program to multiplies all the items in a list.
m = 1
for i in range(len(lista)):
  m *= lista[i]
print(f"A multiplicação dos numeros da lista é {m}")

#4. Write a Python program to get the largest number from a list.
print(f"O maior numero da lista é {max(lista)}")

#5. Write a Python program to get the smallest number from a list. 
print(f"O menor numero da lista é {min(lista)}")

#6. Write a Python program to count the number of characters in a string.
text_count ={}
for letra in text1.lower(): 
  text_count[letra] = text1.lower().count(letra)
  print(text1,text_count) 

#from collections import Counter

#print (Counter(text1))

#link 2

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
lista=[]
for i in range(1500, 2700):
  if i%7==0 and i%5==0:
    lista.append(i)

print(lista)

# 4. Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for i in range (1,6):
  print("*"*i)
for i in range (1,6):
  print("*"*(5-i))

# 5. Write a Python program that accepts a word from the user and reverse it.

palavra = input ("Escreva uma palavra:")
palavraInvertida = ""

for l in range (len(palavra)):
  palavraInvertida += palavra[(len(palavra)-1)-l]

print (palavraInvertida)

#9. Write a Python program to get the Fibonacci series between 0 to 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
 
sequencia=[]

ultimo_digito=0

while (ultimo_digito<50):
  sequencia.append(ultimo_digito)
  if (len(sequencia)-2) >=0:
    ultimo_digito = sequencia[len(sequencia)-1]+sequencia[len(sequencia)-2]
  else:
    ultimo_digito=1
  print(sequencia)

# 10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz
listaFizzBuzz = []
for i in range (1,50):
  if i%3 == 0 and i%5 == 0:
    listaFizzBuzz.append("fizzbuzz")
  elif i%3 == 0:
    listaFizzBuzz.append("fizz")
  elif i%5 == 0:
    listaFizzBuzz.append("buzz")
  else:
    listaFizzBuzz.append(i)
print (listaFizzBuzz)
  
