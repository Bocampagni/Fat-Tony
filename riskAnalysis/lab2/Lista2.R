# UFRJ
# Augusto Guimaraes
# Fabio Bocampagni
# Isaque Araujo
# Lucas Helio

#Exercicio 1. Cara ou Coroa
#Função recebe um vetor com o numero de lançamentos
#Retorna uma tabela com a frequencia de caras e coroas
q1<-function(vetor){
  i<-0
  for (i in vetor){
    
    resultados <-vector(mode='integer',length = i)
    resultados <- sample(c(0,1),i,replace = TRUE)
    
    #Vamos considerar cara como '1' e coroa como '0'
    cara<-sum(resultados)
    
    #Criando tabela com frequencia e printando
    table<-table(resultados)
    prob_table <- table / sum(table)     
    print(prob_table)
    
    #Espaço entre tabelas
    cat("\n")}
}

#Exercicio 2 a)
# Nesse caso, as variáveis aleatórias uniformes no intervalo [0, 1] têm uma média de 1/2 e uma variância de 1/12. 
# Como estamos somando 12 delas, a média da soma será 12 vezes a média individual, ou seja, 12 * 0,5 = 6, e a variância 
# da soma será 12 vezes a variância individual, ou seja, 12 * (1/12) = 1.
# Portanto, a distribuição da soma das 12 variáveis aleatórias uniformes no intervalo [0, 1] se aproxima 
# de uma distribuição normal com média 6 e variância 1. Matematicamente, isso pode ser representado como:
# X ~ N(6, 1)

q2a <- function(){
  #Gera uma distribuição normal com media 6 e desvio padrao 1
  eixo<-seq(0,10)
  distribuicao <- dnorm(eixo, mean = 6, sd = 1)
  plot(x=eixo,y=distribuicao)
}

#b)
# Função que recebe o numero y de amostragens de x
# Retorna o valor esperado de x (media das amostras), variancia e plota o grafico com sua distribuição
q2b<-function(y){
  i<-0
  amostras<-c()
  while(i<y){
    variaveis <-vector(mode='integer',length = 12)
    variaveis <- runif(12, min = 0, max = 1)  # Gere 12 variáveis aleatórias no intervalo [0, 1]
    x <- sum(variaveis)
    amostras<-c(amostras, x)
    i<-i+1
  }
  cat("media: ",mean(amostras))
  cat("\n")
  cat("variancia:",var(amostras))
  hist(amostras)
}

#Exercicio 3
# Instalar o pacote "triangle" (apenas uma vez)
# install.packages("triangle")
# Carregar o pacote "triangle"
# library(triangle)
q3<-function(y){
  j<-0
  i <- sample(c(1,10),1) #Gera numeros de [1,10]
  #print(i)
  amostras<-c()
  while(j<y){
    variaveis <-vector(mode='integer',length = 10)
    variaveis <- rtriangle(10,a=i, b = 20+i, c=10+i)  
    x <- sum(variaveis)
    amostras<-c(amostras, x)
    j<-j+1
  }
  cat("media: ",mean(amostras))
  cat("\n")
  cat("variancia:",var(amostras))
  hist(amostras)
}
# q3(10000)
# i =  10
# media:  199.8882
# variancia: 165.3156

#Exercicio 4
q4a <- function(a){
  x <- rnorm(a,mean=0,sd=1)
  y <- rnorm(a,mean=0,sd=1)
  z <- x*y
  cat("valor esperado: ",mean(z))
  hist(z)
}
# q4(10000)
# valor esperado:  0.006094949

q4b <- function(a){
  x <- rnorm(a,mean=0,sd=1)
  #print(x)
  y <- rnorm(a,mean=0,sd=1)
  #print(y)
  z <- x/y
  cat("valor esperado: ",mean(z))
  hist(z)
}
# Os resultados variam muito. Como estamos dividindo x, em certos casos, por um y muito pequeno obtemos z muito grande(168)
# Em outros casos, quando y fica perto de 1, obtemos valores bem pequenos(0.1)

#Exercicio 5
#Para obter uma aproximação empírica para a função de probabilidade do máximo dentre X variáveis, 
# cada uma seguindo uma distribuição normal padrão (Normal(0,1)),usaremos simulação Monte Carlo. 
# A ideia é gerar um grande número de amostras aleatórias dessas variáveis e, em seguida, calcular 
# a função de probabilidade do máximo.

q5 <- function(a){
  i <- sample(c(2,5,10),1)
  j <-1
  maximos<-vector(mode='integer',length=a)
  while(j<a+1){
    #print(j)
    x <- rnorm(i,mean=0,sd=1)
    maximo <- max(x)
    maximos[j]<-maximo
    j <- j+1
  }
  cat("Valor esperado: ",mean(maximos))
  hist(maximos)
}

# Exercicio 6
# Função recebe como parametro n como o intervalo 
# de num e a como o numero de amostras
q6 <- function(n,a){
  j <-1
  valores<-vector(mode='integer',length=a)
  while(j<a+1){
    x <- rnorm(n,mean=0,sd=1)
    #print(x)
    x_quadrado <- x*x
    #print(x_quadrado)
    amostra <- sum(x_quadrado)
    valores[j]<-amostra
    j <- j+1
  }
  cat("Valor esperado: ",mean(valores))
  hist(valores)
}

# Exercicio 7
q7 <- function(a){
  expoentes<- rnorm(a,mean=0,sd=1)
  amostras <- exp(expoentes)
  #print(amostras)
  valor_esperado <- mean(amostras)
  hist(amostras)
  cat("Valor esperado: ",valor_esperado)
}