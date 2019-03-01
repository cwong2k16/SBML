fun member(X, L) = 
if L=[] then false
else if X=hd(L) then true
else member(X, tl(L));

fun subset(L1, L2) = if L1 = [] then true
else if L2 = [] then false
else if member(hd(L1), L2)
then subset(tl(L1), L2)
else false;

fun remove(x, L) = 
if L = [] then []
else if x=hd(L) then remove(x, tl(L))
else hd(L)::remove(x, tl(L));

fun removedupl(L) = 
if L = [] then []
else hd(L)::removedupl(remove(hd(L), tl(L)));

fun authorizedRolesHelper2(User, L, RR : (''a * ''a) list) = 
if RR = [] then L
else if member(#1(hd(RR)), L) then authorizedRolesHelper2(User, #2(hd(RR)) :: L, tl(RR))
else authorizedRolesHelper2(User, L, tl(RR));

fun authorizedRolesHelper(User, L : (''a * ''a) list, RR : (''a * ''a) list) = 
if L = [] then []
else if User = #1(hd(L)) then #2(hd(L))::authorizedRolesHelper(User, tl(L), RR)
else authorizedRolesHelper(User, tl(L), RR);

fun authorizedRoles(User, L: (''a * ''a) list, RR : (''a * ''a) list) = 
authorizedRolesHelper2(User, authorizedRolesHelper(User, L, RR), RR);

val UR = [(1,1), (1,3)];
val RR = [(3,6), (1,2), (2, 7), (3,4), (99, 5)];
val la = authorizedRoles(1, UR, RR);