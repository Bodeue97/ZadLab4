# # Zad1
#
# list = [0+x for x in range(1, 31, 1)]
# listx2 = [str(x*2) for x in list]
# plik = open("liczyx2.txt", "w")
# plik.writelines(listx2)
# # Zad2
#
# plik = open("liczyx2.txt", "r")
# odczyt = plik.readlines()
# print(odczyt)
# Zad3

with open("tekst.txt", "w") as plik4:
    for newLine in range(10) :
        plik4.write("hehe\n")
with open("tekst.txt", "r") as plik4:
    for line in plik4:
        print(line, end="")