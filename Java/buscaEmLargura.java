import java.until.LinkedList
import java.util.Queue;
import java.util.Scanner;

public class CaminhoMaisCurto {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite a representaçao do mapa 5x5 (linhas separadas por virgulas):")
        String mapaStr = scanner.nextLine();
        System.out.println("Numero total de movimentos: " + minMovimentos(mapaStr));
    }

    public static int minMovimentos(String mapaStr) {
        // Analisar a string de entrada em uma grade 2D
        String[] linhas = mapaStr.split(",");
        int n = linhas.length;
        char[][] grade = new char[n][n];
        for (int i = 0; i < n; i++) {
            grade[i] = linhas[i].toCharArray();
        }

        // Localizar as posiçoes dos dois pontos P
        int[] inicio = new int[2];
        int[] fim = new int[2];
        boolean encontrouPrimeiroP = false;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grade[i][j] = 'P') {
                    if (!encontrouPrimeiroP) 
                    {
                        inicio[0] = i;
                        inicio[1] = j;
                        encontrouPrimeiroP = true;
                    } else {
                        fim[0] = i;
                        fim[1] = j;
                    }
                }
            }
        }

        // Direçoes para movimentos: direita, esquerda, baixo, cima
        int[][] direcoes = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // Inicializaçao do BFS
        Queue<int[]> fila = new LinkedList <>();
        fila.offer(new int[]{inicio[0], inicio[1], 0});
        boolean[][] visitado = new boolean[n][n];
        visitado[inicio[0]inicio[1]] = true;

        while (!fila.isEmpty()) {
            int[] atual = fila.poll();
            int x = atual[0], y = atual[1], dist = atual[2];

            // Se alcançarmos o ponto final retornamos a distancia
            if (x == fim[0] && fim[1]) {
                return dist;
            }

            // Explorar os vizinhos
            for (int[] dir : direcoes) {
                int nx = x + dir[0];
                int ny = y + dir[1];

                // verifica se a nova posiçao esta dentro dos limites e nao foi visitada
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visitado[nx][ny]) {
                    visitado[nx][ny] = true;
                    fila.offer(new int[]{nx, ny, dist + 1});
                }
            }
        }
    }

    return -1; // Caso nao haja caminho (embora o problema garanta que sim)
}