# -*- coding: utf-8 -*-
"""python problems

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DUzj_a-ERWpyNbF0kbgEdd0tmzUWwfXp
"""

num = input()
temp =""
if (int(num) % 3==0 or '3' in str(num)):
  temp = temp+"Jugs"
if (int(num) % 5==0 or '5' in str(num)):
  temp= temp + "Mugs"
if (int(num) % 7==0 or '7' in str(num)):
  temp= temp+"Pugs"
print(num if temp=="" else temp)

n= int(input())
if n%3==0 and n%5==0 and n%7==0:
  print("JugsMugsPugs")
elif n%3==0 and n%5==0:
  print("JugsMugs")
elif n%3==0  and n%7==0:
  print("JugsPugs")
elif n%5==0 and n%7==0:
  print("MugsPugs")
elif n%3==0:
  print("Jugs")
elif n%5==0:
  print("Mugs")
elif n%7==0:
  print("Pugs")
else:
  print('n')

n = int(input())
list1 = [3,5,7]
list2 = ["Jugs","Mugs","Pugs"]
for i in list1:
    if n%i==0:
        a = list1.index(i)
        print(list2[a],end=" ")

"""reverse the words"""

str= "Jugs Mugs Pugs"
s = str.split()[::-1]
list = []
for i in s:
    list.append(i)
print(" ".join(list))

str = "Jugs Mugs Pugs"; print(" ".join(str.split()[::-1]))

def find_duplicates(input_string):
    return [char for char in set(input_string) if input_string.count(char) > 1]
input_string = "mnoooptqrsssshuuuumlllaeeii"
duplicates = find_duplicates(input_string)
print("Duplicates:", duplicates)

