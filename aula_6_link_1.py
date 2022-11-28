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
