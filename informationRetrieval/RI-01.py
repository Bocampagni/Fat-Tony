import pandas as pd


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

D=[['O peã e o caval são pec de xadrez. O caval é o melhor do jog.'],
['A jog envolv a torr, o peã e o rei.'],
['O peã lac o boi'],
['Caval de rodei!'],
['Polic o jog no xadrez.']] #conjunto de documentos
stopwords=['a', 'o', 'e', 'é', 'de', 'do', 'no', 'são'] #lista de stopwords
q='xadrez peã caval torr' #consulta
separadores=[' ',',','.','!','?']


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
    D_tokens = []

    for phrase in D:
        P = phrase[0]
        for separador in separadores:
            P = P.replace(separador, '\n')
        
        tokenized_phrase = P.split('\n')
        token_limpo = sanitize_tokens(tokenized_phrase)


        for stopword in stopwords:
            if stopword in token_limpo:
                token_limpo.remove(stopword)

        D_tokens.append(token_limpo)

    return D_tokens, q_tokens

def build_dataframe(D_tokens, q_tokens, strict_mode):
    df = pd.DataFrame(columns=q_tokens)

    if strict_mode:
        for q_token in q_tokens:
            for i in range(len(D_tokens)):
                cell_value = 0
                for target in D_tokens[i]   :
                    if target == q_token:
                        cell_value +=1 
                df.loc[i, q_token] = cell_value
        return df.T


    for q_token in q_tokens:
        for i in range(len(D_tokens)):
            lower_case_matching = [token.lower() for token in D_tokens[i]]
            
            cell_value = 0
            for target in lower_case_matching:
                if target == q_token.lower():
                    cell_value +=1 

            df.loc[i, q_token] = cell_value

    return df.T


if __name__ == "__main__":
    strict_mode = False # Strict_mode é usado para buscar EXATAMENTE a palavra que está na busca, não retornando o documento caso qualquer diferença seja encontrada.
    D_tokens, q_tokens = build_context(D, stopwords, q, separadores)
    df = build_dataframe(D_tokens, q_tokens, strict_mode)
    print(df)