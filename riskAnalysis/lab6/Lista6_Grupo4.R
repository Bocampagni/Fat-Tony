# Grupo 4
# Augusto Guimarães
# Fábio Bocampagni
# Isaque Araujo
# Lucas Hélio
# .
gerar_aproximacoes<-function(){
  # Valores dos parâmetros para as atividades
  atividades <- data.frame(
    Atividade = c("A", "B", "C", "D", "E", "F", "G", "H", "I", "J"),
    Pred = c(NA, NA, "A", "C", "B,D", "E", "E", "F,G", "F", "H,I"),
    DMin = c(2, 5, 4, 8, 44, 30, 9, 24, 28, 10),
    DMp = c(4, 9, 10, 13, 60, 40, 20, 30, 29, 10),
    DMax = c(18, 19, 28, 36, 100, 74, 43, 48, 96, 12),
    CMin = c(300, 480, 3750, 8400, 300000, 37650, 10500, 36000, 48750, 360),
    CMp = c(450, 600, 4500, 9600, 312000, 39600, 11550, 38400, 52500, 450),
    CMax = c(600, 720, 5250, 10800, 322500, 41400, 12600, 40800, 56250, 540)
  )
  cm<-diag(1,10,10)
  dimnames(cm) <- list(LETTERS[1:10], LETTERS[1:10])
  cm[1,2]<-0.90
  cm[2,1]<-0.90
  cm[5,4]<-0.85
  cm[4,5]<-0.85
  cm[6,7]<-0.90
  cm[7,6]<-0.90
  cm[8,9]<-0.85
  cm[8,10]<-0.85
  cm[9,8]<-0.85
  cm[9,10]<-0.85
  cm[10,8]<-0.85
  cm[10,9]<-0.85
  library(MASS)
  Z <- mvrnorm(3000, mu = rep(0,times = 10), Sigma = cm)
  U <- pnorm(Z)
  # Gerar matriz de triangulares correlacionadas
  D <- matrix(0, nrow = 3000, ncol = 10)
  for (i in 1:10) {
    D[, i] <- qtriangle(U[, i], atividades$DMin[i], atividades$DMax[i], atividades$DMp[i])
  }
  duracao_total <- rowSums(D)
  aprox_duracao <- mean(duracao_total)
  hist(duracao_total)
  C <- matrix(0, nrow = 3000, ncol = 10)
  for (i in 1:10) {
    C[, i] <- qtriangle(U[, i], atividades$CMin[i], atividades$CMax[i], atividades$CMp[i])
  }
  custo_total <- rowSums(C)
  aprox_custo <- mean(custo_total)
  hist(custo_total)
  print("Aproximações Empíricas para o Risco de Custo:")
  print(aprox_custo)
  print("Aproximações Empíricas para o Risco de Prazo:")
  print(aprox_duracao)
}

# .
calcular_caminho_critico <- function() {
  library(MASS)
  # Gráfico
  # ----------------//---------------------
  n <- 10
  
  atividades <- data.frame(
    Atividade = c("A", "B", "C", "D", "E", "F", "G", "H", "I", "J"),
    Pred = c(NA, NA, "A", "C", "B,D", "E", "E", "F,G", "F", "H,I"),
    DMin = c(2, 5, 4, 8, 44, 30, 9, 24, 28, 10),
    DMp = c(4, 9, 10, 13, 60, 40, 20, 30, 29, 10),
    DMax = c(18, 19, 28, 36, 100, 74, 43, 48, 96, 12),
    CMin = c(300, 480, 3750, 8400, 300000, 37650, 10500, 36000, 48750, 360),
    CMp = c(450, 600, 4500, 9600, 312000, 39600, 11550, 38400, 52500, 450),
    CMax = c(600, 720, 5250, 10800, 322500, 41400, 12600, 40800, 56250, 540)
  )
  cm<-diag(1,10,10)
  dimnames(cm) <- list(LETTERS[1:10], LETTERS[1:10])
  cm[1,2]<-0.90
  cm[2,1]<-0.90
  cm[5,4]<-0.85
  cm[4,5]<-0.85
  cm[6,7]<-0.90
  cm[7,6]<-0.90
  cm[8,9]<-0.85
  cm[8,10]<-0.85
  cm[9,8]<-0.85
  cm[9,10]<-0.85
  cm[10,8]<-0.85
  cm[10,9]<-0.85

  
  Suc <- list(3, 5, 4, 5, c(6,7), c(8,9), 8, 10, 10, 0)
  Pre <- list(0, 0, 1, 3, 2,5,5,c(6,7),6,c(8,9))
  
  gerar_amostras_duracao <- function() {
    Z <- mvrnorm(3000, mu = rep(0,times = 10), Sigma = cm)
    U <- pnorm(Z)
    # Gerar matriz de triangulares correlacionadas
    D <- matrix(0, nrow = 3000, ncol = 10)
    for (i in 1:10) {
      D[, i] <- qtriangle(U[, i], atividades$DMin[i], atividades$DMax[i], atividades$DMp[i])
    }
    return(D)
  }
  d<-gerar_amostras_duracao()
  d <- as.integer(d)
  # ----------------//---------------------
  
  est<-vector (mode="numeric",length=n)
  eft<-vector (mode="numeric",length=n)
  lst<-vector (mode="numeric",length=n)
  lft<-vector (mode="numeric",length=n)
  
  cpmf<-function(s,est){
    eft[s]<-est[s]+d[s]
    if ((Suc[[s]][1]!=0)){
      for (i in Suc[[s]]){
        if (est[i] < eft[s]){
          est[i]<-eft[s]
        }
        est<-cpmf(i,est)
      }
    }
    est
  }
  
  cpmb<-function(s,lft){
    lst[s]<-lft[s]-d[s]
    if (Pre[[s]][1]!=0){
      for (i in Pre[[s]]){
        if (lft[i]>lst[s]){
          lft[i]<-lst[s]                
        }                  
        lft<-cpmb(i,lft)
      }
    }
    lft
  }  
  
  rf <- cpmf(1, est)                      
  lft <- rep(rf[n], times = n)            
  rb <- cpmb(n, lft) - d                  
  slack<-rb-rf
  caminho_critico <- which(slack == 0)
  duracao_criticos <- d[caminho_critico]
  minmakespan <- sum(duracao_criticos)
  r <- list(est = rf, lst = rb, slack=slack,caminho_critico=caminho_critico,minmakespan=minmakespan,d=d)
  r
}

# Função para simular uma iteração de Monte Carlo e obter uma aproximacao empirica para a duração total do projeto mostrado
simulacao_monte_carlo <- function() {
  num_iteracoes <- 1000  
  
  # Armazena os resultados de cada iteração
  resultados_simulacao <- numeric(num_iteracoes)
  
  # Realiza as simulações de Monte Carlo
  for (i in 1:num_iteracoes) {
    resultado <- calcular_caminho_critico()  # Chama a função para calcular caminho crítico
    tempo <- resultado$minmakespan
    resultados_simulacao[i] <- tempo
  }
  
  duracao_media <- mean(resultados_simulacao)
  
  # Imprime a estimativa empírica da duração total do projeto
  cat("Estimativa empírica da duração total do projeto:", duracao_media, "\n")
}