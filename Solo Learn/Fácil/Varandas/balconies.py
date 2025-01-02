# Função principal
def main():
    # Entrada de dimensões para o apartamento A
    dimensionsA = input().split(',')
    heightA, widthA = map(int, dimensionsA)

    # Entrada de dimensões para o apartamento B
    dimensionsB = input().split(',')
    heightB, widthB = map(int, dimensionsB)

    # Calculando as áreas
    areaA = heightA * widthA
    areaB = heightB * widthB

    # Comparando as áreas e exibindo o resultado
    if areaA > areaB:
        print("Apartment A")
    elif areaB > areaA:
        print("Apartment B")
    else:
        print("Both apartments have balconies of the same size.")

# Executa o programa
if __name__ == "__main__":
    main()