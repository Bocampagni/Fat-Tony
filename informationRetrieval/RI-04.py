import pandas as pd
import math
import numpy as np
# D=[['Parasita é o grande vencedor do Oscar 2020, com quatro prêmios'],
# ['Green Book, Roma e Bohemian Rhapsody são os principais vencedores do Oscar 2019'],
# ['Oscar 2020: Confira lista completa de vencedores. Parasita e 1917 foram os grandes vencedoresda noite'],
# ['Em boa fase, Oscar sonha em jogar a Copa do Mundo da Rússia'],
# ['Conheça os indicados ao Oscar 2020; Cerimônia de premiação acontece em fevereiro'],
# ['Oscar Schmidt receberá Troféu no Prêmio Brasil Olímpico 2019. Jogador de basquete com maispontos em Jogos Olímpicos.'],
# ['Seleção brasileira vai observar de 35 a 40 jogadores para definir lista da Copa América'],
# ['Oscar 2020: saiba como é a escolha dos jurados e como eles votam'],
# ['Bem, Amigos! discute lista da Seleção, e Galvão dá recado a Tite: Cadê o Luan?'],
# ['IFAL-Maceió convoca aprovados em lista de espera do SISU para chamada oral'],
# ['Arrascaeta e Matías Viña são convocados pelo Uruguai para eliminatórias da Copa. Além deles,há outros destaques na lista.'],
# ['Oscar do Vinho: confira os rótulos de destaque da safra 2018'],
# ['Parasita é o vencedor da Palma de Ouro no Festival de Cannes'],
# ['Estatísticas. Brasileirão Série A: Os artilheiros e garçons da temporada 2020'],
# ['Setembro chegou! Confira o calendário da temporada 2020/2021 do futebol europeu']] #conjuntode documentos
# stopwords=['a', 'o', 'e', 'é', 'de', 'do', 'da', 'no', 'na', 'são', 'dos', 'com','como','eles', 'em', 'os', 'ao', 'para', 'pelo'] #lista de stopwords
# q='oscar 2020' #consulta
# separadores=[' ',',','.','!','?',':',';','/'] #separadores para tokenizacao

# D=[['O peã e o caval são pec de xadrez. O caval é o melhor do jog torr.'],
# [' A jog envolv a torr, o peã e o rei.'],
# [' O peã lac o boi'],
# ['xadrez Caval de rodei!'],
# [' Polic o jog no xadrez.']] #conjunto de documentos
# stopwords=['a', 'o', 'e', 'é', 'de', 'do', 'no', 'são'] #lista de stopwords
# q='xadrez peã caval torr' #consulta
# separadores=[' ',',','.','!','?']

# D=[["To do is to be. To be is to do."],["To be or not to be. I am what I am."],["I think therefore I am. Do be do be do."], ["Do do do, da da da. Let it be, let it be."]]
# stopwords = []
# #q = "to do is to be or not I am what think therefore da let it"
# q = "to do"
# separadores = [' ',',','.','!','?'] 

q =  "gold silver truck"
D = [["shipment of gold damaged in a fire"],
["delivery of silver arrived in a silver truck"],
["shipment of gold arrived in a truck"]]
stopwords = []
separadores = [' ',',','.','!','?']

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def remove_stopwords(D_tokens, stopwords):
    c_stopwords = [word.lower() for word in stopwords]
    return [word.lower() for word in D_tokens if word.lower() not in c_stopwords]

def sanitize_tokens(tokens):
    lista = []
    for token in tokens:
        if token == " " or token == "":
            continue
        lista.append(token.strip())
    return lista


def build_context(D, stopwords, q, separadores):
    for separador in separadores:
        q = q.replace(separador, '\n')

    q_tokens = q.split('\n')
    q_tokens = [word.lower() for word in q_tokens]
    D_tokens = []

    for phrase in D:
        P = phrase[0]
        for separador in separadores:
            P = P.replace(separador, '\n')
        
        tokenized_phrase = P.split('\n')
        token_limpo = sanitize_tokens(tokenized_phrase)
        token_limpo = remove_stopwords(token_limpo, stopwords)
                
        D_tokens.extend(token_limpo)
    
    return unique(D_tokens), q_tokens


def build_D_tokens(D_tokens):
    df = pd.DataFrame(columns=D_tokens)
    
    for i in range(len(D)):
        for j in range(len(D_tokens)):
            stopwords_removed = remove_stopwords(D[i], stopwords)[0]
            for separador in separadores:
                stopwords_removed = stopwords_removed.replace(separador, '\n')
            stopwords_removed = stopwords_removed.split('\n')

            count = 0
            for word in stopwords_removed:
                if word == D_tokens[j]:
                    count += 1
            df.loc[i, D_tokens[j]] = count            
    return df.T


def sim(contin, todos, k1=1.5, b=0.75):
    probability_ranking = pd.DataFrame(index=contin.index)

    # Comprimento médio dos documentos
    avg_doc_length = contin['ni'].mean()

    # Cálculo dos parâmetros do BM25
    idf = (todos['total'] - contin['ni'] + 0.5) / (contin['ni'] + 0.5)
    idf.apply(lambda x: np.log(x) if x > 0 else 0)


    bm25 = (contin['ri'] * (k1 + 1)) / (contin['ri'] + k1 * (1 - b + b * (contin['ni'] / avg_doc_length)))
    
    # Cálculo da probabilidade de relevância para cada documento
    probability_ranking['Rank'] = idf * bm25

    # Ordenando por probabilidade de relevância em ordem decrescente
    probability_ranking = probability_ranking.sort_values(by='Rank', ascending=False)

    return probability_ranking

if __name__ == "__main__":
    D_tokens, q_tokens = build_context(D, stopwords, q, separadores)

    df = build_D_tokens(D_tokens)
    filtered_df = df.loc[q_tokens].T
    
    # Quantidade de elementos
    N = len(D)

    # Quantidade de elementos que contém a palavra
    ni = filtered_df.sum(axis=1)

    # número de documentos relevantes para a consulta q
    R = ni[ni > 0].count()

    # O número de documentos relevantes que contêm a palavra
    ri = ni[ni > 0]

    contingencia = pd.DataFrame(columns=['ri', 'ni-ri', 'ni'])
    contingencia['ri'] = ri
    contingencia['ni'] = ni
    contingencia['ni-ri'] = ni - ri

    nao_pertence = pd.DataFrame(columns=['ri', 'ni-ri', 'ni'])
    nao_pertence['ri'] = R - ri
    nao_pertence['ni'] = N - ni - (R - ri)
    nao_pertence['ni-ri'] = N - ni

    todos = {"relevantes": N, "naoRelevantes": (N-R), "total": N}

    # Chamando a função para obter o ranking probabilístico com BM25
    ranking = sim(contingencia, todos, k1=1.5, b=0.75)

    ranking
