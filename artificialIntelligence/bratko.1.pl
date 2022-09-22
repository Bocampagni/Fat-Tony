parent(tom,lisa).
parent(tom,bru).
parent(lisa,bob).
parent(tom,lucas).
parent(ed,anne).

sister(X,Y):-
    parent(Z,X),
    parent(Z,Y).

hastwochildren(Z):-
    parent(Z,X),
    sister(X,Y).

aunt(X,Y):-
    sister(X,Z),
    parent(Z,Y).
