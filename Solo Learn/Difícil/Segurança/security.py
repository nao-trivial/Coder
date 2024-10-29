def check_security(floor):
    # Encontre posições de dinheiro, ladrão e guardas
    money_position = floor.find('$')
    thief_position = floor.find('T')
    
    # Se não há dinheiro ou ladrao, não há necessidade de checar
    if money_position == -1 or thief_position == -1:
        return 'quiet'
    
    # Check if there is a guard between the money and the thief
    if money_position < thief_position:
        # Check between money and thief positions
        if 'G' in floor[money_position:thief_position]:
            return 'quiet'
    else:
        # Check between thief and money positions
        if 'G' in floor[thief_position:money_position]:
            return 'quiet'
    
    # If no guard is found between money and thief
    return 'ALARM'

# Test the function with the sample input
casino_floor = input()
print(check_security(casino_floor))  # Output should be 'ALARM'
