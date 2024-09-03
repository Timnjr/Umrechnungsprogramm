#Variablen definieren urf steht hier immer für umrechnungsfaktor
urf_bar_pa = 100000
urf_ms_kmh = 3.6
urf_km_mi = 1.609
urf_cm_zoll = 2.54

#Begrüßung des Nutzers
print("Willkommen im Umrechnungsprogramm!")

#Benutzermenü
def menü():
    print("Menüauswahl:")
    print("[1] Bar zu Pascal.")
    print("[2] Meter pro Sekunde zu Kilometer pro Stunde.")
    print("[3] Kilometer zu Meilen.")
    print("[4] Grad Celsius zu Grad Fahrenheit.")
    print("[5] Zentimeter zu Zoll.")
    print("[0] Beenden.")

#Hauptschleife des Programms
while True:
    menü()
    eingabe = int(input("Welche Einheit darf ich für dich umrechnen?\n"))
    
    #Abbruchbedingung der Schleife
    if eingabe == 0:
        print("Ich hoffe, ich konnte dir helfen. Bis bald!")
        break
    
    #Umrechnung Bar in Pascal
    elif eingabe == 1:
        print("Du möchtest Bar zu Pascal umrechnen.")
        bar = float(input("Gib deinen Wert in Bar ein: "))
        pascal = bar * urf_bar_pa
        print(bar, "Bar sind", pascal, "Pascal.")
    
    #Umrechnung Meter pro Sekunde in Kilometer pro Stunde
    elif eingabe == 2:
        print("Du möchtest Meter pro Sekunde in Kilometer pro Stunde umrechnen.")
        m_s = float(input("Gib deinen Wert in m/s ein: "))
        km_h = m_s * urf_ms_kmh
        print(m_s, "m/s sind", km_h, "km/h.")
    
    #Umrechnung Kilometer in Meilen
    elif eingabe == 3:
        print("Du möchtest Kilometer zu Meilen umrechnen.")
        km = float(input("Gib deinen Wert in km ein: "))
        mi = km / urf_km_mi
        print(km, "km sind", mi, "Meilen.")
    
    #Umrechnung Grad Celsius in Grad Fahrenheit
    elif eingabe == 4:
        print("Du möchtest Grad Celsius zu Grad Fahrenheit umrechnen.")
        tc = float(input("Gib deinen Wert in Grad Celsius ein: "))
        tf = (tc * 1.8) + 32
        print(tc, "Grad Celsius sind", tf, "Grad Fahrenheit.")
    
    #Umrechnung Zentimeter in Zoll
    elif eingabe == 5:
        print("Du möchtest Zentimeter zu Zoll umrechnen.")
        cm = float(input("Gib deinen Wert in cm ein: "))
        zoll = cm / urf_cm_zoll
        print(cm, "cm sind", zoll, "Zoll.")
    
    #Antwort auf ungültige Option
    else:
        print("Ungültige Option! Bitte gebe eine der Optionen von '0' bis '5' ein!")
            

    #Abfrage, ob der Nutzer zurück ins Menü möchte.
    while True:
        back_to_menu = input("Möchtest du eine weitere Umrechnung durchführen? [J]/[N] \n").upper()
        if back_to_menu == 'J':
            break
        elif back_to_menu == 'N':
            print("Ich hoffe, ich konnte dir helfen. Bis bald!")
            exit()
        else:
            print("Ungültige Option! Bitte gib 'J' oder 'N' ein.")