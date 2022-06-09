import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * Implementa um algoritmo de força bruta (backtracking) para encontrar
 * uma coloração para os vértices de um grafo, isto é, uma atribuição de
 * "cores" para seus vértices de forma que dois vértices adjacentes jamais
 * tenham a mesma cor.
 */
public class Coloracao {

    /**
     * Tenta colorir o grafo com apenas 'kCores' cores.
     *
     * @param g o grafo desejado
     * @param kCores a quantidade máxima de cores
     * @return um Map {chave: o id do vértice; valor: a cor daquele vértice},
     *         onde cada cor é um número inteiro entre 1 e kCores;
     *         ou null, caso não seja possível colorir com kCores.
     */
    public static Map<Integer, Integer> colorir(Grafo g, int kCores) {

        Map<Integer, Integer> corPorVertice = new HashMap<>();

        if (backtrack(g, kCores, corPorVertice)) {
            return corPorVertice;
        }

        return null;
    }

    /**
     * A estratégia aqui seria colorir os vértices, de um em um,
     * em ordem crescente de rótulo, sempre cuidando para não
     * atribuir ao vértice da vez uma cor já utilizada por algum
     * vizinho seu.
     *
     * @param g o grafo
     * @param kCores onúmero máximo de cores
     * @param coloracaoParcial o estado corrente
     *
     * @return true, se encontrou solução; false, caso contrário
     */
    private static boolean backtrack(
            Grafo g, int kCores,
            Map<Integer, Integer> coloracaoParcial) {

        // PRIMEIRA COISA: VERIFIQUE SE É ESTADO FINAL (ALVO)
        if (coloracaoParcial.size() == g.getQuantVertices()) {
            return true;
        }

        // AGORA LOOP POR TODOS OS PRÓXIMOS ESTADOS POSSÍVEIS
        int quantVerticesJaColoridos = coloracaoParcial.size();
        int verticeDaVez = g.getVertices().get(quantVerticesJaColoridos);
        Set<Integer> vizinhos = g.getVizinhos(verticeDaVez);

        for (int cor = 1; cor <= kCores; cor++) {
            // POSSO DAR ESSE PASSO? ELE É VÁLIDO?
            // no caso: a cor já foi usada por algum vizinho do vértice da vez?
            boolean corOk = true;
            for (Integer vizinho : vizinhos) {
                final Integer corDoVizinho = coloracaoParcial.get(vizinho);
                if (corDoVizinho != null && corDoVizinho == cor) {
                    corOk = false;
                    break;
                }
            }
            if (!corOk) {
                continue;  // NÃO É SEQUER UM PASSO VÁLIDO, NEM VOU TENTAR
                // no caso: passo direto pra outra cor
            }

            // É OK DAR O PASSO, ENTÃO
            // MODIFIQUE O ESTADO CORRENTE (ou seja, dê o passo!!!)
            // no caso: atribui a cor ao vértice da vez
            coloracaoParcial.put(verticeDaVez, cor);

            // BACKTRACK (RECURSÃO)
            if (backtrack(g, kCores, coloracaoParcial)) {
                return true;
            }

            // CASO SEU FILHO NÃO TENHA TIDO SUCESSO...
            // DESFAÇA A MUDANÇA NO ESTADO CORRENTE!!!!!!!
            // no caso: desaplique a cor dado ao vértice corrente
            coloracaoParcial.remove(verticeDaVez);
        }

        return false;  // não obtive sucesso, sou um beco sem saída
    }
}
