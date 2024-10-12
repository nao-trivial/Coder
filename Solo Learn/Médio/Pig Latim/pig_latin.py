x = input()

palavras = x.split()
lista = []
for palavra in palavras:
	x = palavra[1:] #1° letra
	y = palavra[:1] #resto da palavra
	
	x += y + "ay"
	lista.append(x)

#acrescentar espacos
frase = ""
for palavra in lista:
	frase += palavra
	frase += " "
	
print(frase)