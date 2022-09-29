objetivo((2,0)).
objetivo((2,1)).
objetivo((2,2)).
objetivo((2,3)).

acao((J1,J2),encher1,(4,J2)):- J1<4.
acao((J1,J2),encher2,(J1,3)):- J2<3.
acao((J1,J2),esvaziar1,(0,J2)):- J1>0.
acao((J1,J2),esvaziar2,(J1,0)):- J2>0.
acao((J1,J2),passar12,(0,J2FINAL)):- J1=<3-J2,
    J2FINAL is (J1+J2).
acao((J1,J2),passar12,(J1FINAL,3)):- J1>3-J2,
    J1FINAL is (J1-3+J2).
acao((J1,J2),passar21,(4,J2FINAL)):- J2>4-J1,
    J2FINAL is (J2+J1-4).
acao((J1,J2),passar21,(J1FINAL,0)):- J2=<4-J1,
    J1FINAL is (J1+J2).

vizinhos(N,FilhosN):-
    findall(Y,acao(N,_,Y),FilhosN).

enqueue(NN,F1,F2):- append(F1,NN,F2).
stackin(NN,F1,F2):- append(NN,F1,F2).
is_goal(Node):- objetivo(Node).

% % Base
% search([Node|_]):- is_goal(Node).
% search([Node|F1]):- vizinhos(Node, NN),
%     				enqueue(NN,F1,F2),
%     				search(F2).

% % Com lista de visitados
% search([Node|_],_):- is_goal(Node).
% search([Node|F1],Visited):- vizinhos(Node, NN),
%         			enqueue([Node],Visited,F3),
%     				enqueue(NN,F1,F2),
%     				search(F2,F3).

sanitize(L,[],L).
sanitize(NN,[H|T],L):-
    delete(NN,H,NewNN),
    sanitize(NewNN,T,L).

%Sem repetição de estados visitados.
search([Node|_],_):- is_goal(Node).
search([Node|F1],Visited):- vizinhos(Node, NN),
    				enqueue([Node],Visited,F3),
    				sanitize(NN,F3,SanitizedNN),
				    enqueue(SanitizedNN,F1,F2),
    				search(F2,F3).

% % Busca em profundidade
% search([Node|_],_):- is_goal(Node).
% search([Node|F1],Visited):- vizinhos(Node, NN),
%                 enqueue([Node],Visited,F3),
%                 sanitize(NN,F3,SanitizedNN),
%                 stackin(SanitizedNN,F1,F2),
%                 search(F2,F3).