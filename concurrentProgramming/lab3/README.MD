# Atividade 3

A estrutura do while força que a validação daquilo que está sendo passado como argumento para o while seja testado toda vez que `pthread_cond_wait` tome o controle de volta. No caso da condicional padrão, com if, é testado apenas uma vez, o que pode gerar resultados incorretos como o valor ainda não ser múltiplo de 100.

O while nos garante que a condição é testada em um cenário de mutex_lock, ou seja, para-se a escrita e a leitura na variável global e testa-se a condição toda vez, isso no garante a corritude do resultado.
