#include <iostream>
#include <sstream>
#include <vector>

int main() {
    std::string frase;
    std::getline(std::cin, frase);

    std::istringstream iss(frase);
    std::string palavra;
    std::vector<std::string> lista;

    while (iss >> palavra) {
        std::string x = palavra.substr(1); // 1ª letra
        std::string y = palavra.substr(0, 1); // resto da palavra

        x += y + "ay";
        lista.push_back(x);
    }

    for (const std::string &palavra_piglatin : lista) {
        std::cout << palavra_piglatin << " ";
    }

    return 0;
}
