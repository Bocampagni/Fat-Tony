# Atividade 01


### **O TAD lista implementado nesses arquivos poderia ser compartilhado por threads de um programa concorrente ? Com qual finalidade e de que forma ?**

Apesar de não existir, na implementação da lista, uma forma de exclusão mútua, podemos adotar algumas trativas fora da própria implementação para que fosse possível utilizar dessa implementação de forma concorrente.

Toda a implementação é sequencial, dessa forma, para que fosse possível utilizá-la em aplicações concorrente, é necessário recorrer a mecanismo de exclusão mútua e tratativas concorrente um nível antes da chamada dessa implementação concorrente.


### **O que poderia acontecer se o programa não implementasse exclusão mútua no acesso às operações da lista encadeada ?**

Não previsibilidade dos resultados. Seria possível que duas threads escrevessem no mesmo endereço, que informações fossem alteradas enquanto uma thread tenta ler ou escrever nessa lista.


### **O que acontece com o tempo de execução do programa quando aumentamos o número de threads ? Por que isso ocorre ?**

Toda operação entre as listas é sequencializada, não dividimos carga de trabalho entre as threads aumentando o número de threads. Com isso, com o aumento do número de threads, notamos um aumento do tempo de execução da aplicação. 


# Atividade 02

### **Em quais cenários o uso do rwlock pode ser mais vantajoso que o uso do lock de exclusão mútua ?**

Em cenários onde eu tenho uma relação não simétrica entre leitores e escritores. Suponhamos a existência de um sistema de e-commerce. No sistema de exclusão mútua, a cada inserção em sessão crítica, teríamos que bloquear a leitura de todos os clientes. O que não, usualmente, seria a melhor situação. O cenário do rwlock facilita pois, a depender da implementação, nos da a liberdade bloquear os recursos a depender das threads e da implementação do bloqueio.


# Atividade 03

Nota-se que não existe ganho real em nenhuma combinação de escolha entre as estratégias implementadas, tanto da `main_list.c`, quanto da `main_list_rwlock.c`, quanto da `pub_sub.c`. Isso se da provavelmente pelo fato de que a lista inteira é implementada de forma sequencial, o ganho da abstração da camada que chama a implementação da lista tem uma variância pequena no tempo total gasto entre as tarefas porque a maior fração de tempo se da na implementação sequencial.