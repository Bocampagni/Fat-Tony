
classN(0, zero):-!.
classN(Number, positivo):- Number > 0,!.
classN(_,negativo).

membro(Item,Candidatos),not(membro(Item,Excluidos))

difference([],_,[]).
difference([X|Y],Set2,[X|YR]):-
    not(member(X,Set2)),!,
	difference(Y,Set2,YR).
difference([_|Y],Set2,R):-
    difference(Y,Set2,R).
    