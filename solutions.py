"""
# Lösungen Woche 1 & 2

## Legende: Wichtige Python-Funktionen

### Listen-Methoden
- `.append(x)`: Fügt `x` am Ende der Liste hinzu.
- `.extend(iterable)`: Fügt Elemente aus `iterable` zur Liste hinzu (ohne Verschachtelung).
- `.insert(i, x)`: Fügt `x` an Index `i` in die Liste ein.
- `.remove(x)`: Entfernt das erste Vorkommen von `x` in der Liste.
- `.pop(i)`: Entfernt und gibt das Element an Index `i` zurück (Standard: letztes Element).
- `.index(x)`: Gibt den Index des ersten Vorkommens von `x` zurück.
- `.count(x)`: Zählt, wie oft `x` in der Liste vorkommt.
- `.sort()`: Sortiert die Liste in aufsteigender Reihenfolge.
- `.reverse()`: Kehrt die Reihenfolge der Liste um.

### String-Methoden
- `.strip()`: Entfernt Leerzeichen oder bestimmte Zeichen am Anfang und Ende des Strings.
- `.lower()`, `.upper()`: Wandelt den String in Klein- bzw. Großbuchstaben um.
- `.replace(a, b)`: Ersetzt `a` durch `b` im String.
- `.split(sep)`: Teilt den String an `sep` und gibt eine Liste zurück.
- `.join(iterable)`: Verbindet Elemente aus `iterable` mit dem String als Trennzeichen.

### Dictionary-Methoden
- `.keys()`: Gibt eine Liste der Schlüssel zurück.
- `.values()`: Gibt eine Liste der Werte zurück.
- `.items()`: Gibt eine Liste von Schlüssel-Wert-Tupeln zurück.
- `.get(key, default)`: Gibt den Wert zu `key` zurück oder `default`, falls `key` nicht existiert.
- `.pop(key)`: Entfernt den Schlüssel `key` und gibt den Wert zurück.

### Wichtige Funktionen
- `type(x)`: Gibt den Datentyp von `x` zurück.
- `int(x)`, `float(x)`, `str(x)`: Wandelt `x` in einen anderen Datentyp um.
- `range(start, stop, step)`: Erstellt eine Zahlenreihe von `start` bis `stop-1` mit `step`-Schritten.
- `input(prompt)`: Fragt den Benutzer nach einer Eingabe.
- `len(x)`: Gibt die Länge von `x` zurück (z. B. Anzahl der Elemente in einer Liste).

Weitere Infos:
- [Python Listen-Methoden](https://www.python-kurs.eu/python3_listen.php)
- [Python Datentypen](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Collections Vergleich](https://www.educative.io/answers/list-vs-tuple-vs-set-vs-dictionary-in-python)

"""

# -------------------------------
# Lösungen Woche 1
# -------------------------------

# 1) Backslash ausgeben
print('"\\" wird "Backslash" genannt')

# 2) Typ einer Variable ausgeben
hotel_name = "Adler"
print(type(hotel_name))

# 3) Benutzerinput als Zahl
type_number = input("Gib eine beliebige Zahl ein: ")
print(type_number)

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

# 6) Eingabe von Gewicht und Körpergrösse
def bmi_input():
    gewicht = input("Gib dein Gewicht ein in kg: ")
    körpergrösse = input("Gib deine Körpergrösse ein in m: ")
    return gewicht, körpergrösse

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

# -------------------------------
# Lösungen Woche 2
# -------------------------------

# 1) Variablen definieren
number_1 = 224
number_2 = '435.5'
number_3 = 435.5

# 2) Datentypen ausgeben
print(type(number_1))
print(type(number_2))
print(type(number_3))

# 3) Datentypen konvertieren
number_1 = str(number_1)
number_2 = float(number_2)
number_3 = int(number_3)
print(type(number_1))
print(type(number_2))
print(type(number_3))
print(number_3)

# 4) Warum ist das wichtig?
# Datentypen müssen korrekt sein, um Fehler in Berechnungen zu vermeiden.

# 5) Verschiedene Datentypen und ihre Typen
var_1 = ["this is my ", "list number", 1]
var_2 = ("this is my ", "tuple number", 1)
var_3 = {"dict_numb": 1, "content": "this is my first dictionary"}
var_4 = {"this is my ", "set number", 1}
print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

# 6) N.A.

# 7) Listenoperationen
list_1 = ["liste", 455, "another string"]
print(list_1[1])

# 8a) Integer zur Liste hinzufügen
list_1.append(66)

# 8b) Liste zu einer Liste hinzufügen
print(list_1)
list_2 = ["hello", 312]
list_1.append(list_2)
print(list_1)

# 8c) Nested List erhalten

# 8d) Zugriff auf verschachtelte Liste
print(list_1[4][1])

# 8e) Elemente der Liste hinzufügen
list_3 = ["another", "list"]
list_1.extend(list_3)
print(list_1)

# 8f) Negativer Index für 'another'
print(list_1[-2])

# 9a) Zahlen mit for-Loop ausgeben
for i in range(1, 11):
    print(i)

# 9b) Zahlen mit while-Loop ausgeben
z = 1
while z <= 10:
    print(z)
    z += 1
