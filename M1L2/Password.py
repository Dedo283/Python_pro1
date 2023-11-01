import random
passwords = ['+', '-', '/', '*', '!', '&', '$', '#', '?', '=', '@', 'a', 'b', "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
p = int(input("Que tan grande quieres que sea tu contraseña??"))
a = ""
for i in range(p):
    b =random.choice(passwords) 
    a += b
print("La contraseña generada es :",a)








