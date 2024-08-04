function convertTo24Hour(time) {
    // Dividir a string em duas partes: a hora e o indicador AM/PM
    let [timePart, modifier] = time.split(' ');

    // Dividir a parte da hora em horas e minutos
    let [hours, minutes] = timePart.split(':');

    // Converter as horas e minutos para números inteiros
    hours = parseInt(hours, 10);
    minutes = parseInt(minutes, 10);

    // Verificar se o tempo é PM
    if (modifier === 'PM') {
        // Se for PM e a hora não for 12, adicionar 12 horas
        if (hours !== 12) {
            hours += 12;
        }
    } else {
        // Se for AM e a hora for 12, definir as horas para 0
        if (hours === 12) {
            hours = 0;
        }
    }

    // Formatar as horas e minutos para garantir dois dígitos
    let hoursString = hours.toString().padStart(2, '0');
    let minutesString = minutes.toString().padStart(2, '0');

    // Retornar a hora formatada em 24 horas
    return `${hoursString}:${minutesString}`;
}

// Exemplo de uso:
let sampleInput = "1:15 PM";
let result = convertTo24Hour(sampleInput);
console.log(result);  // Saída: "13:15"
