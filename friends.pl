friend(nunew,zee).
friend(joke,pond).
friend(diya,siya).
friend(siya,diya).
mutual_friend(X,Y):- friend(X,Y),friend(Y,X).
