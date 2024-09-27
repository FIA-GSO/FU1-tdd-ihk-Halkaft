import pytest
from ihk import *

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
    with pytest.raises(TypeError):
        GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte)

def test_GetProzentwertBerechnen__Failed_ErreichtePunkte_Nur_Int_Positive_Erlaubt():
     #Arrange
     tesWert_ErreichtePunkte = -1
     tesWert_GesamtePunkte = 100

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
    tesWert_ErreichtePunkte = 65
    tesWert_GesamtePunkte = 101

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
    tesWert_ErreichtePunkte = 65
    tesWert_GesamtePunkte = 0

    #Act
    with pytest.raises(ValueError):
        GetProzentwertBerechnen(tesWert_ErreichtePunkte,tesWert_GesamtePunkte)

#Positive
def test_ProzentwerteAusweten__Untere_Sehr_Gut():
    #Arrange
    testwert_prozentwert= 92
    soll_Ergebnis = "sehr gut"
    
    #Act
    ist_ergbenis= ProzentwerteAusweten(testwert_prozentwert)

    #Assert
    assert ist_ergbenis == soll_Ergebnis


def test_ProzentwerteAusweten_Obere_Sehr_Gut():
    #Arrange
    testwert_prozentwert= 100
    soll_Ergebnis = "sehr gut"
    
    #Act
    ist_ergbenis= ProzentwerteAusweten(testwert_prozentwert)

    #Assert
    assert ist_ergbenis == soll_Ergebnis

def test_ProzentwerteAusweten_Untere_Gut():
    #Arrange
    testwert_Prozentwert=68
    soll_Ergebnis = "Gut"

    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergebnis
def test_ProzentwertAuswerten_Obere_Gut():
    #Arrange
    testwert_Prozentwert = 81
    soll_Ergbnis = "gut"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis

def test_ProzentwertAuswerten_Obere_Befriedigend():
    #Arrange
    testwert_Prozentwert = 80
    soll_Ergbnis = "befriedigend"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis


def test_ProzentwertAuswerten_Untere_Befriedigend():
    #Arrange
    testwert_Prozentwert = 68
    soll_Ergbnis = "befriedigend"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis



def test_ProzentwertAuswerten_Obere_Ausreichend():
    #Arrange
    testwert_Prozentwert = 66
    soll_Ergbnis = "ausreichend"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis



def test_ProzentwertAuswerten_Untere_Ausreichend():
    #Arrange
    testwert_Prozentwert = 50
    soll_Ergbnis = "ausreichend"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis

def test_ProzentwertAuswerten_Obere_Mangelhaft():
    #Arrange
    testwert_Prozentwert = 49
    soll_Ergbnis = "mangelhaft"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis



def test_ProzentwertAuswerten_Untere_Befriedigend():
    #Arrange
    testwert_Prozentwert = 0
    soll_Ergbnis = "mangelhaft"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis

#Negative Tests
def test_ProzentwerteAusweten_Failed_Untere_Grenze():
    
    #Arrange
    testwert_prozentwert= -1;
    
    #Act
    with pytest.raises(ValueError):
        ProzentwerteAusweten(testwert_prozentwert)

        
def test_ProzentwerteAusweten_Failed_Obere_Grenze():
    
     #Arrange
     testwert_prozentwert= 101;
    
     #Act
     with pytest.raises(ValueError):
         ProzentwerteAusweten(testwert_prozentwert)


def test_ProzentwerteAusweten_Failed_Nur_Int():
    
     #Arrange
     testwert_prozentwert= "5"
    
     #Act
     with pytest.raises(TypeError):
         ProzentwerteAusweten(testwert_prozentwert)