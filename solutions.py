# 1) Gib folgendes Statement aus: “\” wird «Backslash» genannt
# 2) Erstelle folgende Variable: hotel_name = "Adler"
# Gib den Datentyp aus (Tipp: type())
# 3) Schreibe ein Script, welches eine Zahl als Input vom User verlangt. Das Programm soll
# danach die Zahl ausgeben. (Tipp: input())
# 4) Schreibe ein Script, dass den User auffordert einen Wochentag einzugeben. Danach
# soll folgendes ausgegeben werden:
# a. für die Wochentage Montag bis Freitag: Arbeitstag
# b. für die Wochentage Samstag und Sonntag: Wochenende
# Tipp: if/else/elif
# 5) Schreibe eine Funktion, die den BMI berechnet und retourniert, basierend auf dem
# Gewicht und der Körpergrösse. Folgendes ist die Funktion: BMI = Gewicht in kg /
# (Körpergrösse in m)2
# Tipp 1: die Funktion muss zwei Parameter haben, Gewicht und Körpergrösse
# Tipp 2: eine Zahl zu quadrieren geht mit «**»
# 6) Schreibe eine Funktion, in welcher ein User zuerst das Gewicht und danach die
# Körpergrösse eingeben muss. Speichere die Eingabe in jeweiligen Variablen.
# 7) Füge die beiden Funktionen von Nr. 6) und Nr. 7) zu einer neuen Funktion
# zusammen. Tipp: Falls es eine Fehlermeldung gibt, musst du allenfalls die Datentypen
# explizit zuweisen. Du kannst das machen mit z.B. folgenden Funktionen: int(), float(),
# str().

# 1) Backslash ausgeben
print("\"\\\" wird 'Backslash' genannt")

# 2) Typ einer Variable ausgeben
hotelname = "Adler"
print(type(hotelname))

# 3) Benutzerinput als Zahl
number = input("Gib eine beliebige Zahl ein: ")
print(number)

# 4) Wochentag abfragen und klassifizieren
weekday = input("Gib einen Wochentag an: ")
if weekday == "Montag":
    print("Arbeitstag")
elif weekday == "Dienstag":
    print("Arbeitstag")
elif weekday == "Mittwoch":
    print("Arbeitstag")
elif weekday == "Donnerstag":
    print("Arbeitstag")
elif weekday == "Freitag":
    print("Arbeitstag")
elif weekday == "Samstag":
    print("Wochenende")
elif weekday == "Sonntag":
    print("Wochenende")
else:
    print("Dies ist kein Wochentag")

# 5) BMI Berechnung mit Rückgabe
def bmi_berechner(gewicht, körpergrösse):
    BMI = gewicht / (körpergrösse ** 2)
    return BMI

print(bmi_berechner(74, 1.87))

# 6) Eingabe von Gewicht und Größe als Funktion
def bmi_input():
    gewicht = input("Gib dein Gewicht ein in kg: ")
    körpergrösse = input("Gib deine Körpergrösse ein in m: ")
    return (gewicht, körpergrösse)

bmi_input()

# 7) BMI Rechner mit Benutzereingabe und Berechnung
def bmi_rechner():
    gewicht = input("Gib dein Gewicht ein in kg: ")
    gewicht = int(gewicht)
    körpergrösse = input("Gib deine Körpergrösse ein in m: ")
    körpergrösse = float(körpergrösse)
    BMI = gewicht / (körpergrösse ** 2)
    print(BMI)

bmi_rechner()

# Aufgaben:
# 1) Erstelle folgende Variablen:
# a. number_1 = 224
# b. number_2 = '435.5'
# c. number_3 = 435.5
# 2) Gib bei allen nummern den Typ aus
# 3) Wechsle:
# a. number_1 in einen string
# b. number_2 in einen float
# c. number_3 in einen integer
# und gib erneut den Datentyp aus. Was geschah mit number_3?
# 4) Weshalb ist das wichtig?
# 5) Erstelle folgende Variablen und gib für alle den Datentyp aus.
# a. var_1 = ["this is my ", "list number", 1]
# b. var_2 = ("this is my ", "tuple number", 1)
# c. var_3 = {"dict_numb " : 1, "content": "this is my first dictionary"}
# d. var_4 = {"this is my ", "set number", 1}
# 6) lies die kurze Zusammenfassung über die verschiedenen python collections nach:
# https://www.educative.io/answers/list-vs-tuple-vs-set-vs-dictionary-in-python.
# Detailliertere Informationen findet ihr beispielsweise hier:
# https://docs.python.org/3/tutorial/datastructures.html
# a.
# 7) 8) 9) a. b. c. d. e. Erstelle eine Liste (list_1) mit folgenden 3 Werten: «liste», 455, «another string».
# Gebe den zweiten Wert (455) aus via Index. Recap Woche 1: Welche Nummer wird
# gebraucht für den zweiten Wert?
# Schau dir die methoden von Listen an: https://www.python-
# kurs.eu/python3_listen.php
# Füge den integer «66» zur list_1 hinzu
# Füge eine liste (list_2 = ["hello", 312]) zur list_1 hinzu
# Was ist das Resultat von b?
# Gebe nun den integer «312» der list_2 aus. Benutze dazu die list_1 und
# Indexierung.
# Füge die Elemente der folgenden Liste (list_3 = ["another", "list"]) der list_1
# hinzu. Beachte: wir wollen hier keine weitere Verschachtelung, wir wollen nur
# die Elemente hinzufügen!
# f. Gebe den string «another» aus, indem du negative indexierung benutzt
# Wir haben die Zahlen von 1 bis (und mit) 10. Gebe die Zahlen untereinander aus,
# indem du:
# a. Dafür einen «for-loop» programmierst
# b. Dafür einen «while-loop» programmierst
# Tipp: Benutze für die Funktion von range(), oder mache eine Liste mit allen
# Nummern von 1 bis 10.

# 1)
number_1 = 224
number_2 = '435.5'
number_3 = 435.5

# 2)
print(type(number_1))
print(type(number_2))
print(type(number_3))

# 3)
number_1 = str(number_1)
number_2 = float(number_2)
number_3 = int(number_3)
print(type(number_1))
print(type(number_2))
print(type(number_3))
print(number_3)

# 4) Wenn man z.b. mathematische funktionen erstellt, kann es zu einem
# «Type error» kommen, da wir allenfalls im Hintergrund einen string
# mit einem integer versuchen zu multiplizieren. Deshalb ist es immer
# wichtig zu überprüfen, welche datentypen man vor sich hat und wo man
# allenfalls eine datenkonvertierung braucht. Man kann auch bei
# Funktionen dafür vorprogrammieren, welcher Datentyp der Argumente
# erwartet wird.

# 5)
var_1 = ["this is my ", "list number", 1]
var_2 = ("this is my ", "tuple number", 1)
var_3 = {"dict_numb " : 1, "content": "this is my first dictionary"}
var_4 = {"this is my ", "set number", 1}
print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

# 6) N.a.

# 7)
list_1 = ["liste", 455, "another string"]
print(list_1[1])

# Da der Computer bei «0» mit dem Zählen beginnt, müssen wir für den
# Index des zweiten Wertes die Nummer «1» benutzen. Eine Übersicht gibt
# es hier:

# 8) Aufgaben:
# a.
list_1.append(66)

# b.
print(list_1)
list_2 = ["hello", 312]
list_1.append(list_2)
print(list_1)

# c.
# Wir erhalten eine “verschachtelte” (engl: “nested») Liste, also
# eine Liste die eine andere Liste enthält.

# d.
print(list_1[4][1])

# was geschieht hier? Die Liste «list_1» sieht folgendermassen
# aus: ['liste', 455, 'another string', 66, ['hello', 312]]. wir
# gehen nun auf den Index «4», welcher wiederum eine Liste
# enthält (['hello', 312]). Wenn wir nur das print statement
# print(list_1[4]) ausgeben, geben wir die gesamte Liste aus. Wir
# wollen aber wiederum nur das zweite Element (Index: 1)
# ausgeben. Deshalb «verketten» wir beide Indexe miteinander:
# print(list_1[4][1]).

# e.
list_3 = ["another", "list"]
list_1.extend(list_3)
print(list_1)

# f.
print(list_1[-2])

# 9)
print("+++++++++++++++++++++ \n for-loop mit Liste:")
numbers_1_10 = [1,2,3,4,5,6,7,8,9,10]
for i in numbers_1_10:
print(i)
print("+++++++++++++++++++++ \n for-loop mit range()")
for q in range(1,11):
print(q)
print("+++++++++++++++++++++ \n while loop mit range()")
z = 1
while z < 11:
print(z)
z += 1