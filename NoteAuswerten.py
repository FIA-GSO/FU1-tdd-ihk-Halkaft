from ast import With
import pytest # type: ignore

#Positive
def test_ProzentwerteAusweten_Untere_Sehr_Gut():
    #Arrange
    testwert_prozentwert= 92
    soll_Ergebnis = "Serh gut"
    
    #Act
    ist_ergbenis= ProzentwerteAusweten(testwert_prozentwert)

    #Assert
    assert ist_ergbenis == soll_Ergebnis
def test_ProzentwerteAusweten_Obere_Sehr_Gut():
    #Arrange
    testwert_prozentwert= 100
    soll_Ergebnis = "Serh gut"
    
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
    soll_Ergbnis = "Gut"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis

def test_ProzentwertAuswerten_Obere_Befriedigend():
    #Arrange
    testwert_Prozentwert = 80
    soll_Ergbnis = "Befriedigend"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis
def test_ProzentwertAuswerten_Untere_Befriedigend():
    #Arrange
    testwert_Prozentwert = 68
    soll_Ergbnis = "Befriedigend"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis

def test_ProzentwertAuswerten_Obere_Ausreichend():
    #Arrange
    testwert_Prozentwert = 66
    soll_Ergbnis = "Befriedigend"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis
def test_ProzentwertAuswerten_Untere_Ausreichend():
    #Arrange
    testwert_Prozentwert = 50
    soll_Ergbnis = "Befriedigend"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis

def test_ProzentwertAuswerten_Obere_Mangelhaft():
    #Arrange
    testwert_Prozentwert = 49
    soll_Ergbnis = "Mangelhaft"
    
    #Act
    ist_Ergebnis = ProzentwerteAusweten(testwert_Prozentwert)

    #Assert
    assert ist_Ergebnis == soll_Ergbnis
def test_ProzentwertAuswerten_Untere_Befriedigend():
    #Arrange
    testwert_Prozentwert = 0
    soll_Ergbnis = "Mangelhaft"
    
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
    testwert_prozentwert= "5";
    
    #Act
    with pytest.raises(ValueError):
        ProzentwerteAusweten(testwert_prozentwert)






def ProzentwerteAusweten(prozentwert):
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
