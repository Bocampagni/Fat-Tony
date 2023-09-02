# Atividade 01 - Corrida de Dados

Quando estamos fazendo uma operação de soma, ela não é atomica. Temos 3 instruções de máquina que precisam ser executadas. Quando uma thread executa a instrução de trazer o valor da variável para um registrador, assumindo que estão em processadores separados, uma outra thread pode também pegar esse mesmo valor. Ambas escrevem o mesmo valor na mesma variável, fazendo com que perdamos uma iteração de soma.

Em outras situações, podemos ter uma thread que demora mais que a outra para executar, devido a diversos motivos. A condição de corrida faz com que tenhamos um resultado diferente a cada execução, o que é um erro. 

A não previsibilidade do valor final da variável "soma" é um erro lógico.

# Atividade 02 - Locks

Sim, os valores impressos sempre foram os valores esperados devido ao fato de todas as threads precisarem seguir um comportamento de trancamento dado pela estrutura de trancamento mutex. Para cada thread, antes de alterar o valor da variável global, pergunta se existe outra thread utilizando utilizando aquele mesmo endereço de variável global. 

Quando é permitido a passagem da thread para a área critica (área entre as subrotinas de chamada de sistema pthread_mutex_lock e pthread_mutex_unlock), é assertivo que apenas aquela thread escreve na variável "soma". Assim, garante-se a corritude e sempre o mesmo valor impresso.

# Atividade 03 - Mostrar como fazer a tomada de tempo de execução de um programa

Concluí-se, empiricamente, que a fronteira eficiente do número de threads para a execução do programa é 4, em uma máquina quadcore convencional. Assumindo, claro, condições normais de execução onde outras tarefas estão sendo executadas em consonância com o programa `matvet.c`.

```
Tempo multiplicacao (dimensao 10000) (nthreads 1): 0.191862
Tempo multiplicacao (dimensao 10000) (nthreads 2): 0.099639
Tempo multiplicacao (dimensao 10000) (nthreads 3): 0.074475
Tempo multiplicacao (dimensao 10000) (nthreads 4): 0.055424
Tempo multiplicacao (dimensao 10000) (nthreads 5): 0.082710
```

Processador do Lab: 12th Gen Intel© Core™ i3-12100 × 4

obs: Posterior ao conhecimento do número de cores da máquina e da análise empirca, fica claro que não haverá ganho depois da instanciação da quarta thread pois não há mais núcleos de processamento.