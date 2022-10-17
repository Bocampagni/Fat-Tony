oddLength([_|[]]).
oddLength([_|T]):-
    oddLength(T).



evenLength([_|[_|[]]]).
evenLength([_|T):-
	evenLength(T).


reverse(List, Rev) :-
        reverse(List, Rev, []).
reverse([], L, L).
reverse([H|T], L, SoFar) :-
        reverse(T, L, [H|SoFar]).


palindrome2(X,X).
palindrome2(List):-
    reverse(List,ReversedList),
    palindrome2(List,ReversedList).


shift([H|T],List2):-
    reverse(T,L3),
	shift(L3,List2,[H]).

shift([],L,L).


shift([H|T],List2,List3):-
    shift(T,List2,[H|List3]).

member(X,[X|_]).
member(X,[_|T]):-
    member(X,T).

append([],L,L).
append([H1|T1],L2,[H1|L3]):-
    append(T1,L2,L3).



means(0,zero).
means(1,one).
means(2,two).
means(3,three).
means(4,four).
means(5,five).
means(6,six).
means(7,seven).
means(8,eight).
means(9,nine).


translate([],List2,List2).
translate(List1,List2):-
    translate(List1,[],List2).

translate([H|T],ListAux,List2):-
    means(H,V),
    append(ListAux,[V],L),
    translate(T,L,List2).


dividelista([],[],[]).
dividelista([X],[X],[]).
dividelista([X,Y|L1], [X|L2], [Y|L3]):-
    dividelista(L1,L2,L3).

flatten2([Cabeca|Cauda],FlatLista):-
    flatten2(Cabeca,FlatCabeca),
    flatten2(Cauda,FlatCauda),
    append(FlatCabeca,FlatCauda,FlatLista).

flatten2([],[]).

flatten2(X,[X]).