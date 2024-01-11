import csv
l = []
j = []
a = []
k = ['blue.txt','orange.txt','yellow.txt','magenta.txt','violet.txt','red.txt','green.txt']
with open("blue.txt",'r') as file:
    File = csv.reader(file,delimiter=' ')
    for row in File:
        stop_name=''
        for i in range(len(row)-1):
            stop_name+=row[i]
            if(i!=len(row)-2):
                stop_name+=' '
        l.append(stop_name)
with open("violet.txt",'r') as file:
    File = csv.reader(file,delimiter=' ')
    for row in File:
        stop_name=''
        for i in range(len(row)-1):
            stop_name+=row[i]
            if(i!=len(row)-2):
                stop_name+=' '
        if(stop_name in l):
            j.append(stop_name)
for line in k:
    with open(line,'r') as file:
        File = csv.reader(file,delimiter = ' ')
        for row in File:
            a.append(row[0])
print(len(a))
        
        
