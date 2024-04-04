def es_palindromo(palabra):
    #Convierte la palabra a minúsculas para no cometer errores.
    palabra = palabra.lower()
    #Compara la palabra con su inverso para verificar si es un palíndromo.
    if palabra == palabra[::-1]:
        return True
    else:
        return False

#Ejemplos de palabras palíndromas y no palíndromas.
palabras = ["Adán", "amar", "amor", "animal", "Omar", "rata", "zorra", "sol"]

for palabra in palabras:
    if es_palindromo(palabra):
        print(f"{palabra} - {palabra[::-1]} es un palíndromo.")
    else:
        print(f"{palabra} no es un palíndromo.")

#Define funciones de prueba para verificar el funcionamiento del código.

def test_es_palindromo():
    assert es_palindromo("radar") == True
    assert es_palindromo("python") == False
    assert es_palindromo("reconocer") == True
    assert es_palindromo("casa") == False

def test_ejemplos():
    assert es_palindromo("Adán") == False
    assert es_palindromo("amar") == False
    assert es_palindromo("amor") == False
    assert es_palindromo("animal") == False
    assert es_palindromo("Omar") == False
    assert es_palindromo("rata") == False
    assert es_palindromo("zorra") == False
    assert es_palindromo("sol") == False

#Ejecuta las pruebas.
test_es_palindromo()
test_ejemplos()
print("Todas las pruebas han pasado correctamente.")