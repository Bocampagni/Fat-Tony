import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

D=[['Parasita é o grande vencedor do Oscar 2020, com quatro prêmios'],
['Green Book, Roma e Bohemian Rhapsody são os principais vencedores do Oscar 2019'],
['Oscar 2020: Confira lista completa de vencedores. Parasita e 1917 foram os grandes vencedores da noite'],
['Em boa fase, Oscar sonha em jogar a Copa do Mundo da Rússia'],
['Conheça os indicados ao Oscar 2020; Cerimônia de premiação acontece em fevereiro'],
['Oscar Schmidt receberá Troféu no Prêmio Brasil Olímpico 2019. Jogador de basquete com mais pontos em Jogos Olímpicos.'],
['Seleção brasileira vai observar de 35 a 40 jogadores para definir lista da Copa América'],
['Oscar 2020: saiba como é a escolha dos jurados e como eles votam'],
['Bem, Amigos! discute lista da Seleção, e Galvão dá recado a Tite: Cadê o Luan?'],
['IFAL-Maceió convoca aprovados em lista de espera do SISU para chamada oral'],
['Arrascaeta e Matías Viña são convocados pelo Uruguai para eliminatórias da Copa. Além deles, há outros destaques na lista.'],
['Oscar do Vinho: confira os rótulos de destaque da safra 2018'],
['Parasita é o vencedor da Palma de Ouro no Festival de Cannes'],
['Estatísticas. Brasileirão Série A: Os artilheiros e garçons da temporada 2020'],
['Setembro chegou! Confira o calendário da temporada 2020/2021 do futebol europeu']] #conjuntode documentos
stopwords=['a', 'o', 'e', 'é', 'de', 'do', 'da', 'no', 'na', 'são', 'dos', 'com','como',
'eles', 'em', 'os', 'ao', 'para', 'pelo'] #lista de stopwords
q='oscar 2020' #consulta
separadores=[' ',',','.','!','?',':',';','/'] #separadores para tokenizacao
R=[1, 3, 5, 8] #identificador dos documentos relevantes para a consulta q

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

def simVet(dataframe: pd.DataFrame, tf_idf: pd.DataFrame):
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


def plot_recall_x_precision(frame: pd.DataFrame, R, title, x_label, y_label):
    recall = [0.0,0.1,0.2,0.3,0.4,0.5,0.6, 0.7, 0.8, 0.9, 1.0]
    precision = [] 
    relevant_found = 0
    for doc_index in range(len(frame.index) + 1):
        if doc_index in R:

            relevant_found += 1
            potencial_precision = relevant_found/(doc_index + 1)

            if len(precision) == 0:
                precision.append(potencial_precision)
            else:
                if potencial_precision > max(precision):
                    precision.append(max(precision))
                else:
                    precision.append(potencial_precision)
    
    #Completar precision com 0 se não for do mesmo tamanho de recall
    if len(precision) < len(recall):
        for i in range(len(recall) - len(precision)):
            precision.append(0)
    

    # Marcar pontos no gráfico que se conectam
    plt.plot(recall, precision, 'o-')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


if __name__ == "__main__":
    D_tokens, q_tokens = build_context(D, stopwords, q, separadores)
    df = build_D_tokens(D_tokens)
    filtered_df = df.loc[q_tokens].T
    # Quantidade de elementos
    N = len(D)
    # Quantidade de elementos que contém a palavra
    ni = filtered_df.sum(axis=1)
    # número de documentos relevantes para a consulta q
    R_ = ni[ni > 0].count()
    # O número de documentos relevantes que contêm a palavra
    ri = ni[ni > 0]
    contingencia = pd.DataFrame(columns=['ri', 'ni-ri', 'ni'])
    contingencia['ri'] = ri
    contingencia['ni'] = ni
    contingencia['ni-ri'] = ni - ri
    nao_pertence = pd.DataFrame(columns=['ri', 'ni-ri', 'ni'])
    nao_pertence['ri'] = R_ - ri
    nao_pertence['ni'] = N - ni - (R_ - ri)
    nao_pertence['ni-ri'] = N - ni
    todos = {"relevantes": N, "naoRelevantes": (N-R_), "total": N}
    ranking = sim(contingencia, todos, k1=1.5, b=0.75)

    tf_idf = tf_idf(df)
    filtered_df = tf_idf.loc[q_tokens]
    similaridades = simVet(filtered_df, tf_idf)


    print("Probabilístico")
    print(ranking)
    print("Vetorial")
    print(similaridades.T)

    # Relevantes
    if not 0 in R:
        R = [x-1 for x in R] # Agora, o 0 é o primeiro termo.


    intercessao_ranking = ranking.index.intersection(R)
    recall_ranking = len(intercessao_ranking)/len(R)
    precision_ranking = len(intercessao_ranking)/len(ranking.index)
    print("-="*30)
    print("Precisão do probabilístico: ", precision_ranking)
    print("Recall do probabilístico: ", recall_ranking)


    intercessao_vetorial = similaridades.T.index.intersection(R)
    recall_vetorial = len(intercessao_vetorial)/len(R)
    precision_vetorial = len(intercessao_vetorial)/len(similaridades.T.index)
    print("-="*30)
    print("Precisão do vetorial: ", precision_vetorial)
    print("Recall do vetorial: ", recall_vetorial)
    print("-="*30)

    print("Média da precisão probabilística: ", precision_ranking/len(q_tokens))
    print("Média da precisão vetorial: ", precision_vetorial/len(q_tokens))

    # Plotando o gráfico um do lado do outro no mesmo gráfico
    # *!7''''1
    # 
    # gwer 
    # gfew
    # gef
    # we    
    plot_recall_x_precision(ranking, R, "Curva de Recall x Precision (Probabilístico)", "Recall", "Precision")
    plot_recall_x_precision(similaridades.T, R, "Curva de Recall x Precision (Vetorial)", "Recall", "Precision")

