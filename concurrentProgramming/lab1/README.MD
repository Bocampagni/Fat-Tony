## Os resultados estão de acordo com o esperado ?

Sim, não necessariamente os fluxos seguirão uma ordem esperada pelo usuário.
Não existe algo que garanta qual thread será executada antes da outra, em outras palavras, qual fluxo de execução terminará dado a existência de outros fluxos de execução.


## Por que foi necessário long int na variável iteradora?

Devido ao tamanho tamanho do (void*), em bytes, houve a necessidade de aumentar o tamanho do tipo que usaríamos para fazer a passagem do valor para a rotina que executa na thread.
Por exemplo, se fosse utilizado um int padrão, teriamos 4 bytes, 4 a menos do que o necessário pelo (void*), o que pode gerar problemas. Devido a isso, foi utilizado long int para type cast para tipos de mesmo tamanho.

## Por que foi necessário criar uma estrutura de dados nova ?

Em função de passar mais variáveis, mais valores para a rotina que será executada na main,
foi necessário criar uma estrutura para que possamos endereçar essa estrutura de forma única, assim, podemos acessar essas informações em um único lugar. 

Como temos apenas um ponteiro (void*), não podemos endereçar muitos lugares, sendo assim, torna-se útil agrupar as informações que serão usadas pela rotina da thread em uma struct.

## O que aconteceu de diferente em relação ás versões/execuções anteriores ?

É utilizado a rotina pthread_join que faz uma chamada de sistema que espera a execução das threads terminarem antes do fluxo principal finalizar. 
Isso muda o comportamento anterior onde o fluxo principal (rotina main), podia terminar antes do fluxo das threads criadas.
