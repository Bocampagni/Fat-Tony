import java.util.*;

/**
 * Classe para grafos simples, direcionados.
 * Utiliza HashSets de vizinhos de saída e de entrada,
 * para cada vértice.
 * Vértices são inteiros de 1 a n.
 */
public class Grafo {

    private Map<Integer, Set<Integer>> vizinhosDeSaidaPorVertice;
    private Map<Integer, Set<Integer>> vizinhosDeEntradaPorVertice;
    private List<Integer> cor;
    private int quantVertices;
    private int quantArestas;

    public Grafo(){};



    public Grafo(int n) {
        this.quantVertices = n;
        this.vizinhosDeSaidaPorVertice = new HashMap<>();
        this.vizinhosDeEntradaPorVertice = new HashMap<>();
        this.cor = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            this.vizinhosDeSaidaPorVertice.put(i, new HashSet<>());
            this.vizinhosDeEntradaPorVertice.put(i, new HashSet<>());
        }
    }

    public void adicionarVertice() {

    }

    public void removerVertice(int v) {
        for (int w : this.vizinhosDeSaidaPorVertice.get(v)) {
            this.vizinhosDeEntradaPorVertice.get(w).remove(v);
        }
        for (int w : this.vizinhosDeEntradaPorVertice.get(v)) {
            this.vizinhosDeSaidaPorVertice.get(w).remove(v);
        }
        this.quantArestas -=
                this.vizinhosDeEntradaPorVertice.get(v).size();
        this.quantArestas -=
                this.vizinhosDeSaidaPorVertice.get(v).size();
        this.vizinhosDeEntradaPorVertice.remove(v);
        this.vizinhosDeSaidaPorVertice.remove(v);
        this.quantVertices--;
    }

    public boolean existeAresta(int v, int w) {
        return this.vizinhosDeSaidaPorVertice.get(v).contains(w);
    }

    public void adicionarAresta(int v, int w) {
        if (this.vizinhosDeSaidaPorVertice.get(v).add(w)) {
            this.vizinhosDeEntradaPorVertice.get(w).add(v);
            this.quantArestas++;
        }
    }

    public void removerAresta(int v, int w) {
        if (this.vizinhosDeSaidaPorVertice.get(v).remove(w)) {
            this.vizinhosDeEntradaPorVertice.get(w).remove(v);
            this.quantArestas--;
        }
    }

    public int obterGrau(int v) {
        return this.vizinhosDeSaidaPorVertice.get(v).size();
    }

    public int getQuantVertices() {
        return this.quantVertices;
    }

    public int getQuantArestas() {
        return this.quantArestas;
    }

    public List<Integer> getVertices() {
        return new ArrayList<>(this.vizinhosDeEntradaPorVertice.keySet());
    }

    public Set<Integer> getVizinhosDeEntrada(int v) {
        return this.vizinhosDeEntradaPorVertice.get(v);
    }

    public Set<Integer> getVizinhosDeSaida(int v) {
        return this.vizinhosDeSaidaPorVertice.get(v);
    }

    public Set<Integer> getVizinhos(int v) {
        Set<Integer> vizinhos = new HashSet<>();
        vizinhos.addAll(getVizinhosDeEntrada(v));
        vizinhos.addAll(getVizinhosDeSaida(v));
        return vizinhos;
    }

    public List<Integer> getTopologicalSort() {
        int n = quantVertices;

        List<Integer> topSort = new ArrayList<>();

        Stack<Integer> fontes = new Stack<>();
        for (Integer v : this.vizinhosDeEntradaPorVertice.keySet()) {
            if (this.vizinhosDeEntradaPorVertice.get(v).size() == 0) {
                fontes.push(v);
            }
        }

        while (fontes.size() > 0) {
            int f = fontes.pop();
            topSort.add(f);
            for (int w : this.vizinhosDeSaidaPorVertice.get(f)) {
                if (this.vizinhosDeEntradaPorVertice.get(w).size() == 1) {
                    // w vai se tornar uma fonte quando remover f
                    fontes.add(w);
                }
            }
            removerVertice(f);
        }

        if (topSort.size() == n) {
            return topSort;
        }

        return null;  // não é um DAG!!!
    }

    public void colorir(int cor, int pos){
        this.cor.set(pos, cor);
    }

    public List<Integer> getList(){
        return this.cor;
    }
}