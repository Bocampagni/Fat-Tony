import java.util.Map;

public class main {
    public static void main(String[] args){



        Grafo grafo = new Grafo(8);

        grafo.adicionarAresta(1, 6);
        grafo.adicionarAresta(2, 6);
        grafo.adicionarAresta(4, 3);
        grafo.adicionarAresta(5, 3);
        grafo.adicionarAresta(1, 3);
        grafo.adicionarAresta(1, 2);
        grafo.adicionarAresta(7, 6);
        grafo.adicionarAresta(7, 1);
        grafo.adicionarAresta(7, 4);
        grafo.adicionarAresta(7, 2);

//        List<Integer> topSort = grafo.getTopologicalSort();
//        System.out.println(topSort);

        Map<Integer, Integer> coloracao = Coloracao.colorir(grafo, 4);
        System.out.println(coloracao);
    }
}
