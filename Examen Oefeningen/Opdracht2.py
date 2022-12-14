#Gebruiker naar totale afgelegde afstand en hoelang het duurde vragen en opslaan in variables aantal_km en tijd
aantal_km = float(input("Hoeveel kilometer heb je gejogd/gewandelt?: "))
tijd = int(input("Hoeveel minuten heeft dit geduurd?: "))

#Tijd van minuten naar uren omzetten
tijd_uren = tijd / 60

#Snelheid berekenen
oplossing = aantal_km / tijd_uren

#Snelheid in km/h terug geven aan de gebruiker
print(f"Gemiddelde snelheid : {oplossing} km/h")