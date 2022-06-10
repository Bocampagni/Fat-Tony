import java.util.List;
import java.util.Set;

/**
 *
 * Classe responsável por executar o algoritmo de busca em profundidade
 *
 * */
public class DFS {

    /**
     *
     * Primeiramente, vamos colorir todos os vértices para branco, sinalizando que não existem vértices visitados ainda.
     * Se o vértice atual for branco, pintar de cinza, buscar seus vizinhos de saída e chamar o utilitário de visitar.
     * Depois que sair do loop, pintar de preto indicando que secou os vizinhos.
     * Tabela de cores {0 -> branco, 1-> cinza, 2-> preto}
     * */

    public static Grafo simpleDeepFirstSearchUsingColor(Grafo grafo){
        DFS.pintar(grafo);

        for(Integer i: grafo.getVertices()){
            if(grafo.getList().get(i) == 0){
                grafo.colorir(1,i);
                DFS.utilVisit(i,grafo.getVizinhosDeSaida(i), grafo);
            }
        }
        return new Grafo();
    }

    private static void pintar(Grafo grafo){
        for(int i: grafo.getVertices()){
            grafo.colorir(i,0);
        }
    }

    private static void  utilVisit(Integer pai, Set<Integer> listaAdj, Grafo grafo){
        for(Integer j: listaAdj){
            if(grafo.getList().get(j) == 0){
                grafo.colorir(1,j);
                DFS.utilVisit(j,grafo.getVizinhosDeSaida(j), grafo);
            }
        }
        grafo.colorir(2,pai);
    }
}
