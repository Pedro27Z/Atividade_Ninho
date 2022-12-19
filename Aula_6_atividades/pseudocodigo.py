# par ou impat

n=0
print("_________________________________")
n=int(input("Digite um numero inteiro:"))
print("_________________________________")
print(n)
if n%2 == 0:
  print(n,"é um número par")
else:
  print(n,"é um número ímpar")

# faixa permitida

print("Digite um valor: ")
n=float(input())
if (n>=1) and (n<=9):
  print("O valor está na faixa permitida!!")
else: 
  print("O valor não está na faixa permitida!!")

# armazenamento

print("Digite um valor: ")
n=float(input())
if n>=0:
  a=n
  print(f"O número {a} é variável de A")
else:
  b=n
  print(f"O número {b} é variável de B")

# peso ideal

print("Digite o seu sexo F ou M:")
s=input()
print("Digite sua altura:")
a=float(input())
def peso_ideal():
  if (s=="F" or s=="f"):
      p=(62.1*a)-44.7
      print(f"Seu peso ideal é {p:.3f}")
  elif (s=="M" or s=="m"):
      p=(72.7*a)-58
      print(f"Seu peso ideal é {p:.3f}")


if (s=="F" or s=="f") or (s=="M" or s=="m"):
  peso_ideal()
else:
  print("Digite um sexo válido.")
  s=input()
  peso_ideal()
  
# situação com media

print("Digite as 5 notas:")
n1=float(input())
n2=float(input())
n3=float(input())
n4=float(input())
n5=float(input())
soma=(n1+n2+n3+n4+n5)
media=soma/5
print(F"A soma das notas é {soma}")
print(f"A media das notas é {media:.2f}")
if media >=7:
  print ("resultado final: APROVADO")
elif media >= 5 and media < 7:
  print ("resultado final: RECUPERAÇÃO")
elif media < 5 :
  print ("resultado final: REPROVADO")
else:
  print ("Notas inválidas")

# media e comparação

notas = []
nota = 0
maiormedia = []
while len(notas) < 5:
  nota= float(input("Escreva uma nota: "))
  if nota <=10 and nota >=0:
    notas.append(nota)
  else:
    print("Valor invalido")

media = sum(notas)/len(notas)

for i in notas:
  if i >7:
    maiormedia.append(i)
    
print(f"A soma das notas é : {sum(notas)}")
print (f"A média das notas é: {media}")    
print (f"Os valores maiores que a média são: {maiormedia}")

# financiamento

s=0 # salário
f=0 # financiamento
print("Digite o valor do salário:")
s=float(input())
print("Digite o valor do financiamento:")
f=float(input())
if f<=(5*s):
  print("financiamento concedido, obrigado por nos consultar.")
else:
  print("financiamento negado, obrigado por nos consultar.")

# maior número 

maior=0
n = 1
while n!=0:
  n = int(input("Digite um número positivo maior que zero: "))
  if n > maior:
    maior = n
print (f"O maior número é: {maior}")

# multiplos de 10

i=0
print("Os multiplos de 10 são:")
for i in range(1,100,1):
  if (i%10==0):
    print(i)

# ímpares de 100 a 200

i=0
q=0
print("Os numeros ímpares de 100 a 200 são:")
for i in range(100,200,1):
  if (i%2!=0):
    q+=1
    print(i)
print (f"A quantidade de números impares entre 100 e 200 é {q}")


