import pytest

#Positive Tests für Berchnung der Prozentwere 
def test_GetProzentwertBerechnen__untere_Grenze_ErreichtePunkte():
    #Arrange
    tesWert_ErreichtePunkte = 0;
    tesWert_GesamtePunkte = 100;
    soll_ergebnis= 0

    #Act
    ist_ergbenis= GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte)

    #Assert
    assert ist_ergbenis == soll_ergebnis

def test_GetProzentwertBerechnen__Obere_Grenze_ErreichtePunkte():
    #Arrange
    tesWert_ErreichtePunkte = 100;
    tesWert_GesamtePunkte = 100;
    soll_ergebnis= 100

    #Act
    ist_ergbenis= GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte)

    #Assert
    assert ist_ergbenis == soll_ergebnis

def test_GetProzentwertBerechnen__mittlere_Grenze_ErreichtePunkte():
    #Arrange
    tesWert_ErreichtePunkte = 50;
    tesWert_GesamtePunkte = 100;
    soll_ergebnis= 50

    #Act
    ist_ergbenis= GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte)

    #Assert
    assert ist_ergbenis == soll_ergebnis

def test_GetProzentwertBerechnen__ubere_mittlere_Grenze_ErreichtePunkte():
    #Arrange
    tesWert_ErreichtePunkte = 75;
    tesWert_GesamtePunkte = 100;
    soll_ergebnis= 75

    #Act
    ist_ergbenis= GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte)

    #Assert
    assert ist_ergbenis == soll_ergebnis


#Negative Tests für Berchnung der Prozentwere
def test_GetProzentwertBerechnen__Failed_Nur_Int():
    #Arrange
    tesWert_ErreichtePunkte = "";
    tesWert_GesamtePunkte = "Ge";

    #Act
    with pytest.raises(ValueError):
        GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte)

def test_GetProzentwertBerechnen__Failed_ErreichtePunkte_Nur_Int_Positive_Erlaubt():
    #Arrange
    tesWert_ErreichtePunkte = -1;
    tesWert_GesamtePunkte = 100;

    #Act
    with pytest.raises(ValueError):
        GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte)

def test_GetProzentwertBerechnen__Failed_ErreichtePunkte_Nur_Kleine_100():
    #Arrange
    tesWert_ErreichtePunkte = 101;
    tesWert_GesamtePunkte = 100;

    #Act
    with pytest.raises(ValueError):
        GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte)

def test_GetProzentwertBerechnen__Failed_GesamtePunkte_Nur_Kliene_100():
    #Arrange
    tesWert_ErreichtePunkte = 65;
    tesWert_GesamtePunkte = 101;

    #Act
    with pytest.raises(ValueError):
        GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte)

def test_GetProzentwertBerechnen__Failed_GesamtePunkte_Nur_Positiv_Integer():
    #Arrange
    tesWert_ErreichtePunkte = 65;
    tesWert_GesamtePunkte = -1;

    #Act
    with pytest.raises(ValueError):
        GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte)

def test_GetProzentwertBerechnen__Failed_GesamtePunkte_Not_Null():
    #Arrange
    tesWert_ErreichtePunkte = 65;
    tesWert_GesamtePunkte = 0;

    #Act
    with pytest.raises(ValueError):
        GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte)


def GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte):
        if gesamt_punkte == 0:
            return 0
        return (tesWert_ErreichtePunkte / tesWert_GesamtePunkte) * 100


