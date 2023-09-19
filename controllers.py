f1 = open("files/diary.txt", "r")
print(f1.read())
f1.close()

f2 = open("files/diary2.txt", "w")
print(f2.write("Espero poder entenderlos"))
f2.close()


# Abrir el archivo en modo escritura
f3 = open("files/diary3.txt", "w")
# Lista de nombres
names = ["Rosana", "Juan", "Avelino"]
# Utilizamos el bucle “for” para recorrer cada nombre de la lista. En cada iteración, la variable “name” toma el valor de un nombre de la lista.
for name in names:
    f3.write(name + "\n")
# Cerrar el archivo
f3.close()    