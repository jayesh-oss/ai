convert(C,F):-
   F is 9*C/5 + 32,
   (C < 0 -> write('it is freezing'); write('it is not freezing')).
