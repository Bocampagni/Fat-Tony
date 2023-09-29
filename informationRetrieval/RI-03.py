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

D=[["To do is to be. To be is to do."],["To be or not to be. I am what I am."],["I think therefore I am. Do be do be do."], ["Do do do, da da da. Let it be, let it be."]]
stopwords = []
#q = "to do is to be or not I am what think therefore da let it"
q = "to do"
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

def boolean_search(df, q_tokens: list, D_tokens: list):
    or_search = []
    for i in range(len(df.index)):
        for j in range(len(df.columns)):
            if df.iloc[i,j] == 1:
                if j in or_search:
                    continue
                or_search.append(j)
                

    and_search = []
    for i in range(len(df.columns)):
        #Numero de q encontrados
        found = 0
        for j in range(len(df.index)):
            if df.iloc[j,i] > 0:
                found += 1

        # Se encontrou todos os q, então esse documento precisa ser retornado.
        if found == len(q_tokens):
            and_search.append(i)

    return sorted(or_search), and_search

def tf_idf(df: pd.DataFrame):
    df = df
    n_buffer = []
    idf_buffer = []
    for i in range(len(df.index)):
        ni = df.iloc[i,:].apply(lambda x: 1 if x > 0 else 0).sum()
        idf = math.log2(len(df.columns)/ni)
        n_buffer.append(ni)
        idf_buffer.append(idf)
        for j in range(len(df.columns)):
            if df.iloc[i,j] > 0:
                df.iloc[i,j] = (1 + math.log2(df.iloc[i,j])) * idf 
            else:
                df.iloc[i,j] = 0

    df['ni'] = n_buffer
    df['idf'] = idf_buffer
    return df

def compute_norma(vector: list):
    return np.linalg.norm(vector)

def sim(dataframe: pd.DataFrame, tf_idf: pd.DataFrame):
    rank = []
    for feature in range(len(dataframe.columns)-2): # Precisa subtrair para tirar ni e idf
        vector = dataframe.iloc[:,feature].to_numpy()
        norma = compute_norma(tf_idf.iloc[:,feature].to_numpy())

        q_vector = dataframe['idf'].to_numpy()
        norma_q = compute_norma(q_vector)

        dot_product = np.dot(vector, q_vector)
        norma_product = norma * norma_q
        rank_i = dot_product / norma_product
        rank.append(rank_i)


    dataframe.drop(['ni', 'idf'], axis=1, inplace=True)

    return dataframe.T.assign(rank=rank).T



if __name__ == "__main__":
    D_tokens, q_tokens = build_context(D, stopwords, q, separadores)

    df = build_D_tokens(D_tokens)
    filtered_df = df.loc[q_tokens]
    
    tf_idf = tf_idf(df)
    filtered_df = tf_idf.loc[q_tokens]
    similaridades = sim(filtered_df, tf_idf)
    print(similaridades)