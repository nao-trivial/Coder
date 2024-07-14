// Obtém um número do usuário
var numero = prompt();

// Converte a entrada para um número
numero = parseInt(numero);

// Verifica se o número é positivo, negativo ou zero
if (numero > 0) {
    console.log("O número é positivo.");
} else if (numero < 0) {
    console.log("O número é negativo.");
} else {
    console.log("O número é zero.");
}

