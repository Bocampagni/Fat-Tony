objetivo(2,0).
objetivo(2,1).
objetivo(2,2).
objetivo(2,3).

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