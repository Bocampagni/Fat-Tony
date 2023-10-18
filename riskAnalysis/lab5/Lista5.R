# 1)
# .
# Uma aproximacao empirica para a duração total do projeto mostrado.
# Função que retorna: Tempo mais cedo de inicio
#                     Tempo mais tarde de inicio
#                     Folgas
#                     Caminho Critico
#                     e o tempo mínimo de conclusão
calcular_caminho_critico <- function() {
  # Gráfico
  # ----------------//---------------------
  n <- 14
  
  tabela_distribuicao <- data.frame(
    Ativ = 1:14,
    Min = c(0, 4, 2, 2, 0.5, 3, 1, 0.5, 2, 2, 1, 1, 3, 0),
    Mprov = c(0.1, 6, 5, 3, 1, 6, 2, 1, 4, 3, 2, 3, 5, 0.1),
    Max = c(0.2, 10, 8, 6, 2, 10, 4, 3, 6, 5, 3, 4, 8, 0.2)
  )
  
  Suc <- list(c(2, 3, 4), c(9), c(5, 6, 7), c(8), c(10), c(12), c(8, 11), c(13), c(14), c(12), c(12), c(13), c(14), 0)
  
  Pre <- list(0, 1, 1, 1, 3, 3, 3, c(4,7), 2, 5, 7, c(6,10,11), c(8,12), c(9,13))
  
  gerar_amostras_duracao <- function() {
    amostras <- numeric(n)
    for (i in 1:n) {
      amostras[i] <- rtriangle(1, tabela_distribuicao$Min[i],tabela_distribuicao$Max[i],tabela_distribuicao$Mprov[i])
    }
    return(amostras)
  }
  # Converter as durações para inteiro
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

# .
# Uma aproximação empirica para a probabilidade das atividades pertencerem ao caminho critico
frq_ativ <- function(){
  frequencia <- rep(0, 14) # Variavel para guardar a quantidade de vezes que uma atividade aparece num caminho critico
  num_iteracoes <- 50000  
  for (i in 1:num_iteracoes) {
    resultado <- calcular_caminho_critico()  # Chama a função para calcular caminho crítico
    atividades <- resultado$caminho_critico
    for (j in atividades){
      frequencia[j]<-frequencia[j]+1
    }
  }
  #Imprimir
  for (a in 1:14 ){
    cat("atividade",a)
    cat(": probablidade de pertencer ao caminho critico", frequencia[a]/num_iteracoes)
    cat("\n")}
}

# .
# Supondo a politica de agendamento ”alocar todas atividades no tempo mais
# cedo de inicio”. Obtenha uma aproximaçãoo empirica para a distribuição de
# probabilidade do agendamento de cada uma das atividades.
simulacao_monte_carlo_agendamento <- function() {
  num_iteracoes <- 13000
  agendamentos <- list()  # Lista para armazenar os agendamentos de atividades em cada iteração
  
  for (i in 1:num_iteracoes) {
    resultado <- calcular_caminho_critico()
    agendamentos[[i]] <- resultado$est  # Armazena os agendamentos de atividades
  }
  #print
  for (atividade in 1:14) {
    tempos_inicio_atividade <- sapply(agendamentos, function(x) x[atividade]) # Pega os elementos da lista
    media <- mean(tempos_inicio_atividade)
    desvio_padrao <- sd(tempos_inicio_atividade)
    cat("Atividade", atividade, ": Média =", media, "Desvio Padrão =", desvio_padrao, "\n")
  }
}

# .
# Sabendo que a definição formal de um cronograma  ́e um conjunto de triplas
#{(ai, si, di)}, (atividade, data de inicio, duração), obtenha um cronograma de
# menor duração para este projeto que tenha uma chance de 85% de ser cumprido.
calcular_cronogramas <- function() {
  # Inicialize uma lista vazia para armazenar os cronogramas
  lista_cronogramas <- list()
  
  # Gere 1000 cronogramas
  for (i in 1:1000) {
    evento <- calcular_caminho_critico()
    
    # Crie uma sequência de números de 1 a 14 para representar as atividades
    atividades <- 1:14
    
    # Combine as atividades, est, d e minmakespan em uma lista e adicione à lista de cronogramas
    cronograma <- c(atividades, evento$est, evento$d)
    lista_cronogramas[[i]] <- c(cronograma,evento$minmakespan)
  }
  lista_cronogramas_ordenada <- lista_cronogramas[order(sapply(lista_cronogramas, function(x) x[length(x)]))]
  
  # Ordenar as durações mínimas em ordem crescente e encontrar o valor que corresponde ao percentil 85 
  # é uma abordagem para determinar uma duração mínima que tem uma alta probabilidade de ser cumprida.
  # Encontrar a duração mínima correspondente ao percentil 85 permite identificar um valor que 
  # é uma estimativa conservadora da duração mínima do projeto, considerando a incerteza nas durações das atividades. 
  # Em outras palavras, há uma alta probabilidade (85%) de que o projeto seja concluído dentro desse período, com base nas simulações realizadas.
  
  cronograma_na_posicao_850 <- lista_cronogramas_ordenada[[850]]
  atividades <- cronograma_na_posicao_850[1:14]
  tempos <- cronograma_na_posicao_850[15:28]
  duracoes <- cronograma_na_posicao_850[29:42]
  
  # Criar um data frame para formatar a tabela
  tabela <- data.frame(Atividade = atividades, Tempo = tempos, Duracao = duracoes)
  
  # Imprimir a tabela em formato Markdown
  cat("Cronograma com 85% de chances\n")
  cat("| A | T | D |\n")
  cat("| - | - | - |\n")
  for (i in 1:14) {
    cat("|", tabela$Atividade[i], "|", tabela$Tempo[i], "|", tabela$Duracao[i], "|\n")
  }
  return(cronograma_na_posicao_850)
}

criar_diagrama_gantt <- function() {
  cronograma_na_posicao_850 <- calcular_cronogramas()
  
  atividades <- cronograma_na_posicao_850[1:14]
  tempos_inicio <- cronograma_na_posicao_850[15:28]
  duracoes <- cronograma_na_posicao_850[29:42]
  
  # Gerar cores aleatórias para cada atividade
  cores_aleatorias <- rainbow(length(atividades))
  
  # Criar um data frame para o diagrama de Gantt
  df <- data.frame(
    Atividade = factor(atividades, levels = atividades),
    Inicio = tempos_inicio,
    Fim = tempos_inicio + duracoes,
    Cor = cores_aleatorias
  )
  
  # Criar o gráfico de Gantt com cores
  ggplot(df, aes(y = Atividade, x = Inicio, xend = Fim, yend = Atividade, color = Cor)) +
    geom_segment(linewidth = 10) +
    labs(x = "Tempo", y = "Atividade") +
    ggtitle("Diagrama de Gantt - Cronograma com 85% de Chances") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
    scale_color_identity()
}