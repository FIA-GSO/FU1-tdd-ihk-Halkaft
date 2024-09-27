def ProzentwerteAusweten(prozentwert):
    if not isinstance(prozentwert, int):
            raise TypeError("Nur int erlaubt")
    if(prozentwert<1 or prozentwert>100):
            raise ValueError("Nur werte zweischen 0 und 100 erlaubt")

    if prozentwert >= 92:
        return "sehr gut"
    elif prozentwert >= 81:
        return "gut"
    elif prozentwert >= 67:
        return "befriedigend"
    elif prozentwert >= 50:
        return "ausreichend"
    else:
        return "mangelhaft"


#Funktion
def GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte):
        if not isinstance(tesWert_ErreichtePunkte, int):
             raise TypeError("Nur int erlaubt")
        if(tesWert_ErreichtePunkte > 100 or  tesWert_ErreichtePunkte < 0 ):
             raise ValueError("Nur positive int erlaubt")
        if(tesWert_GesamtePunkte > 100 or  tesWert_GesamtePunkte < 0 ):
             raise ValueError("Nur positive int erlaubt")
        if tesWert_GesamtePunkte == 0:
            raise ValueError("GesamtePunkte nur positive int erlaubt großer als 0 erlaubt")
        return (tesWert_ErreichtePunkte / tesWert_GesamtePunkte) * 100


