
#lineare Anweisung
x = 10
y = x + 5
z =  y * 2
print(x,y,z)

#Gerade oder Ungerade
a = int(input("Gebe eine ganze Zahl an: "))
if a % 2 == 0:
    print(a, "ist gerade")
else:
    print(a, "ist ungerade")

#Größer als 100?
b = int(input("Gebe eine ganze Zahl an: "))
if b <= 100:
    print(b, "ist kleiner als 100")
else:
    print(b, "ist größer als 100")

#Passwort
korrektes_passwort = "geheim"
benutzer_passwort = input("Bitte Passwort angeben: ")

if benutzer_passwort == korrektes_passwort:
    print("Erolgreich eingeloggt")
else:
    print("Passwort inkorrekt")

#Zwischen 50 und 100?
c = int(input("Bitte Zahl angeben: "))
if c > 50 and c < 100:
    print("Die Zahl liegt zwischen 50 und 100")
else:
    print("Die Zahl liegt nicht zwischen 50 und 100")

#Führerschein
alter = int(input("Bitte Alter angeben: "))
if alter > 17:
    print("Du darfst Auto fahren, falls du den Führerschein schon gemacht hast")
elif alter > 15 and alter < 18:
    print("Du darfst einen Führerschein machen")
elif alter < 18:
    print("Du bist zu jung für den Führerschein")

#Zahlen vergleichen
num1 = int(input("Gebe Zahl ein: "))
num2 = int(input("Gebe Zahl ein: "))

if num1 == num2:
    print("Beide Zahlen sind gleich")
elif num1 > num2:
    print(num1, "ist größer")
else:
    print(num2, "ist größer")

if (num1 + num2) % 2 == 0:
    print("Die Summe ist gerade")
else:
    print("Die Summe ist ungerade")

#Teil 5
name = "Laurin Adolphs"
ausbildung = "FIAE"
zitat = "Träume nicht dein Leben, sondern lebe deine Träume."

# Ausgabe mit Formatierung
print("+" + "-" * 75 + "+") #hab mich hier online inspirieren lassen, da ich anfangs nicht wusste was gemeint war
print(f"| Name:          {name:<58} |")
print(f"| Ausbildung:    {ausbildung:<58} |")
print(f"| Zitat:         {zitat:<58} |")
print("+" + "-" * 75 + "+")

#Tabulator und Zeilenumbruch
print("Laurin\tAdolphs")
print("Laurin\nAdolphs")

#Begrüßungsnachricht
Name = input("Geben sie ihren Namen an: ")
Alter = int(input("Wie alt sind sie?: "))
Beruf = input("Welchen Beruf üben sie aus?: ")
print("Guten Tag",Name,"sie sind",Alter,"Jahre alt","und sind vom Beruf", Beruf)

#Eingabe validieren
d = input("Geben sie eine Zahl an: ")
if not d.isdigit():
    print("Die Eingabe war keine Zahl")

#Datentypen
int_ = 33
float_ = 33.0
str_ = "dreiunddreißig"
bool_ = True
print(int_,(type(int_)))
print(float_,(type(float_)))
print(str_,(type(str_)))
print(bool_,(type(bool_)))

#Typkonvertierung
ganzzahl = 20

gleitkommazahl = float(ganzzahl)
string = str(ganzzahl)
print(ganzzahl)
print(gleitkommazahl)
print(string)

#Exception Handling
try:
    e = float(input("Geben sie eine Zahl an: "))
    if e == 0:
        print("Zahl darf nicht 0 sein")
    else:
        f = e / 2
    print("Die Hälfte ist:",f)
except:
    print("Fehler: keine gültige Zahl")

#Benutzerdefinierter Fehler
try:
    g = float(input("Bitte Zahl angeben: "))
    if g < 0:
        print("Fehler: Zahl darf nicht negativ sein.")
    else:
        print("Die Zahl",g,"ist gülitg und positiv.")
except:
    print("Fehler: Zahl ist ungültig.")