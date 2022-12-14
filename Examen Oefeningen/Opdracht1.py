#De gebruiker naar informatie vragen zoals kilometer per dag en totale afgelegde kilometer en die dan in variables km_per_dag en totaal_km opslaan
km_per_dag = int(input("Hoeveel kilometer leg je per dag af?: "))
totaal_km = int(input("Hoeveel kilometer moet je in totaal afleggen?:"))

#Berekenen hoeveel dagen het duurt om de totale afstand af te leggen
oplossing = -(-totaal_km // km_per_dag)

#De gebruiker het aantal tijd in dagen dat het duurt om de afstand af te leggen terug geven
print(oplossing)
