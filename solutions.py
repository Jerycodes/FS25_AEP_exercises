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