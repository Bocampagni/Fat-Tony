paridade([],0,0).

paridade([H|T],P,I):-
    0 is mod(H,2),!,
    paridade(T,PN,I),
    P is 1 + PN.

paridade([H|T],P,I):-
    1 is mod(H,2),!,
    paridade(T,P,IN),
    I is 1 + IN.

