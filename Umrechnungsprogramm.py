#Begrüßung des Nutzers
print("Willkommen im Umrechnungsprogramm!")
#Benutzermenü
print("Menüauswahl:")
print("1: Bar in Pascal.")
print("2: m/s in Km/h.")
print("3: Kilometer in Meilen.")
print("4: Celsius in Fahrenheit")
print("5: Zentimeter in Zoll")
eingabe = input("Welche Einheit darf ich für dich umrechnen?\n")
#Umrechnung Bar in Pascal
if eingabe == '1' :
    print("Du möchtest Bar in Pascal umrechnen.")
    bar = float(input("Gebe deinen Wert in Bar ein:"))
    urf_bar_pa = 100000
    pascal = bar * urf_bar_pa
    print(bar, "Bar sind", pascal, "Pascal.")
#Umrechnung m/s in Km/h
if eingabe == '2' :
    print("Du möchtest m/s in Km/h umrechnen.")
    m_s = float(input("Gebe deinen Wert in m/s ein:"))
    urf_ms_kmh = float(3.6)
    km_h = m_s / urf_ms_kmh
    print(m_s,"m/s sind", km_h,"Km/h.")
#Umrechnung Kilometer in Meilen
if eingabe == '3' :
    print("Du möchtest Kilometer in Meilen umrechnen.")
    km = float(input("Gebe deinen Wert in Km ein: "))
    urf_km_mi = float(1.609)
    mi = km / urf_km_mi
    print(km,"Km sind", mi,"Meilen.")
#Umrechnung Celsius in Fahrenheit
if eingabe == '4' :
    print("Du möchtest Celsius in Fahrenheit umrechnen.")
    tc = float(input("Gebe deinen Wert in Grad Celsius ein: "))
    tf = (tc + 1.8) + 32
    print(tc, "Grad Celsius sind", tf,"Grad Fahrenheit.")
#Umrechnung Zentimeter in Zoll
if eingabe == '5' :
    print("Du möchtest Zentimeter in Zoll umrechnen.")
    cm = float(input("Gebe deinen Wert in cm ein: "))
    urf_cm_zoll = float(2.54) 
    zoll = cm / urf_cm_zoll
    print(cm,"cm sind", zoll,"Zoll.")
    
