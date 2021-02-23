import os
import math as m
import time
import csv
import random
start = time.time()
os.chdir('F:\\PYTON')
print(os.getcwd())
n = 1
x = 0
d = 0
z = 0
calk = int(input('Ile pytan: '))
baza = open('baza.csv')
reader = csv.reader(baza)
baza = list(reader)
klucz = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

countries = []
for row in baza:
    countries.append(row[0])
#print(countries)

capitols = []
for row in baza:
    capitols.append(row[1])
#print(capitols)

i = 1
while n <= calk:
    file = open('test' + str(n) + '.txt', 'w')
    file2 = open('test' + str(n) + 'odp.txt', 'w')
    c = list(zip(countries, capitols))
    random.shuffle(c)
    countries, capitols = zip(*c)
    capitolslist = list(capitols)
    capitols1 = random.shuffle(capitolslist)
    capitols2 = random.shuffle(capitolslist)
    capitols3 = random.shuffle(capitolslist)

    answers = []
    answers.append(capitols[i])
    answers.append(capitols[random.randint(0,239)])
    answers.append(capitols[random.randint(0,239)])
    answers.append(capitols[random.randint(0,239)])
    random.shuffle(answers)
    print('''
    Z%s %s:
    0 -%s
    1 -%s
    2 -%s
    3 -%s
             ''' % (i, countries[i], answers[0], answers[1], answers[2], answers[3]))
    ans = int(answers.index(capitols[i]))
    odp = str(input('Odp: '))
    print(odp)
    while odp != '0' and odp != '1' and odp != '2' and odp != '3':
        odp = input('Podaj odp. 0, 1, 2, 3: ')
    odp = int(odp)
    if odp == ans:
        print('Dobrze')
        d = d + 1
    else:
        print('Zle')
        z = z + 1
    i = i + 1
    n = n + 1
elapsed_time = time.time() - start
calk = float( d / (d+z))
print('Dobre: %s, Zle: %s, Procent: %.2f%%' % (d, z, calk))
print('Czas: %.2fs' % (elapsed_time))