# Lab 06

##  Como executar

Espera-se que a execução do arquivo `.java` seja feita da seguinte forma: 


```
javac LeitorEscritor
java LeitorEscritor.java >> log.py
python3 log.py
```

Entende-se que tudo aquilo que seria posto, usualmente no system.out, agora passará a ser um alimentador do arquivo log.py, que poesteriormente será interpretado para verificar a boa conformidade do LeitorEscritor.java.

Vale ressaltar que a condição necessária para o bom funcionamento da aplicação é que `verificaLE.py` esteja no mesmo diretório que o `log.py`, do contrário, não será possível importar a classe com as rotinas de verificação.

## Mudanças para implementar as especificações solicitadas

- Foi criado uma variável booleana `escritaPendente`
- Em consonância, foi criada outra variável auxiliar ao fluxo para controlar a quantidade de leitores esperando `escrEsperando`.

## Validação

Foi introduzido duas novas rotinas de controle, uma em relação ao número de leitores da classe LE, outra, do número de escritores.

```python
def leitorSaindo(self, id):
    '''Recebe o id do leitor e registra que terminou a leitura.'''
    self.leitores -= 1
    if self.leitores == 0 and self.escritores_esperando > 0:
        self.escrita_pendente = True

def escritorSaindo(self, id):
    '''Recebe o id do escritor e registra que terminou a escrita.'''
    self.escritores -= 1
    self.escrita_pendente = False
    if self.escritores_esperando > 0:
        self.escrita_pendente = True
```