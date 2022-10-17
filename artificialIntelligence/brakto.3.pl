max(X,Y,Max):-
    X >= Y,
    Max is X.
max(X,Y,Max):-
    X =< Y,
    Max is Y.

maxList([],0).
maxList([H|T],Max):-
    maxList(T,N),
    max(H,N,Max).

ordered(_,[]).
ordered([H|T]):-
    ordered(H,T).

ordered(X,[H|T]):-
    max(X,H,H),
	ordered(H,T).