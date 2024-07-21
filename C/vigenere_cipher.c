#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Função para criptografar a mensagem
void encrypt(char *message, char *key, char *encrypted) {
    int msgLen = strlen(message);
    int keyLen = strlen(key);
    int i, j;

    for (i = 0, j = 0; i < msgLen; i++) {
        if (isalpha(message[i])) {
            char offset = isupper(message[i]) ? 'A' : 'a';
            encrypted[i] = ((message[i] - offset + (toupper(key[j]) - 'A')) % 26) + offset;
            j = (j + 1) % keyLen;
        } else {
            encrypted[i] = message[i];
        }
    }
    encrypted[msgLen] = '\0';
}

// Função para descriptografar a mensagem
void decrypt(char *encrypted, char *key, char *decrypted) {
    int msgLen = strlen(encrypted);
    int keyLen = strlen(key);
    int i, j;

    for (i = 0, j = 0; i < msgLen; i++) {
        if (isalpha(encrypted[i])) {
            char offset = isupper(encrypted[i]) ? 'A' : 'a';
            decrypted[i] = ((encrypted[i] - offset - (toupper(key[j]) - 'A') + 26) % 26) + offset;
            j = (j + 1) % keyLen;
        } else {
            decrypted[i] = encrypted[i];
        }
    }
    decrypted[msgLen] = '\0';
}

int main() {
    char message[1024];
    char key[1024];
    char encrypted[1024];
    char decrypted[1024];

    // Entrada da mensagem e da chave
    printf("Digite a mensagem: ");
    fgets(message, sizeof(message), stdin);
    message[strcspn(message, "\n")] = '\0';  // Remover a nova linha do final

    printf("Digite a chave: ");
    fgets(key, sizeof(key), stdin);
    key[strcspn(key, "\n")] = '\0';  // Remover a nova linha do final

    // Criptografar a mensagem
    encrypt(message, key, encrypted);
    printf("Mensagem criptografada: %s\n", encrypted);

    // Descriptografar a mensagem
    decrypt(encrypted, key, decrypted);
    printf("Mensagem descriptografada: %s\n", decrypted);

    return 0;
}
