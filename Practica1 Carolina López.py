import re
file1 = open('mbox-short.txt')
texto1='^New Revision: ([0-9.]+)'
NewRevisionNumero1=[]

for line in file1:
    result1=re.findall(texto1, line)

    if result1:
        NewRevisionNumero1.append(int(result1[0]))


print(int (sum (NewRevisionNumero1)/len(NewRevisionNumero1)))



import re
file2 = open('mbox.txt')
texto2='^New Revision: ([0-9.]+)'
NewRevisionNumero2=[]

for line in file2:
    result2=re.findall(texto2, line)

    if result2:
        NewRevisionNumero2.append(int(result2[0]))


print(int (sum (NewRevisionNumero2)/len(NewRevisionNumero2)))