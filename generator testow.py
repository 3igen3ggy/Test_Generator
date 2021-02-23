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





while n <= 30:
    file = open('test' + str(n) + '.txt', 'w')
    file2 = open('test' + str(n) + 'odp.txt', 'w')
    c = list(zip(countries, capitols))
    random.shuffle(c)
    countries, capitols = zip(*c)
    capitolslist = list(capitols)
    capitols1 = random.shuffle(capitolslist)
    capitols2 = random.shuffle(capitolslist)
    capitols3 = random.shuffle(capitolslist)
    file.write('Test nr %s \n\n' % (n))
    i = 1
    while i <= 30:
        answers = []
        answers.append(capitols[i])
        answers.append(capitols[random.randint(0,239)])
        answers.append(capitols[random.randint(0,239)])
        answers.append(capitols[random.randint(0,239)])
        random.shuffle(answers)

        file.write('''
Z%s %s:
A - %s
B - %s
C - %s
D - %s
         ''' % (i, countries[i], answers[0], answers[1], answers[2], answers[3]))
        ans = int(answers.index(capitols[i]))
        file2.write('''Z%s %s
''' %(i, klucz[ans]))

        i = i + 1
    n = n + 1
elapsed_time = time.time() - start
print(elapsed_time)