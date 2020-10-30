import csv


x = input("Olá! 😀 Guarda o ficheiro que queres abrir na mesma pasta em que tens o programa!\n  Depois escreve aqui o nome desse ficheiro\n P.S. Não coloques o .csv\n")
y=input("Escreve aqui o nome que o ficheiro limpo deve ter\n")

def leitor ():
    with open(x + ".csv",'r') as lido:
        l = ['', '', '', 'Afghasssnistan', '2020-10-27 04:24:45', '33.93911', '67.709953', '40937', '1518', '34150', '5269', 'Afghanistan', '105.15988852440435', '3.7081368932750323']


        reader = csv.reader(lido, quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if(row[3]=='Country_Region' or row[3]=='Holy See' or row[3]=='Cote d\'Ivoire' or row[3]=='Diamond Princess' or row[3]=='MS Zaandam' or row[3]=='Tajikistan' or row[3]=='Congo (Brazzaville)' or  row[3]=='Solomon Islands' or row[3]=='Marshall Islands'):continue 
            if(l[3]=='Afghasssnistan'): l = row
            elif(l[3]==row[3]):
                row=fazcontas(row,l)
                l = row
            else:
                interpretador(l)
                l = row

    interpretador(l)




def fazcontas(l1,l2):
    l1[7] = int(l1[7])+int(l2[7])
    l1[8] = int(l1[8])+int(l2[8])
    l1[9] = int(l1[9]) + int(l2[9])
    return  l1



def interpretador(l) :
        with open(y +".csv",'a+') as escrever:
            writer = csv.writer(escrever,delimiter=';')
            writer.writerow([l[3],l[7], l[8],l[9]])


leitor()


z=input("O documento foi criado")