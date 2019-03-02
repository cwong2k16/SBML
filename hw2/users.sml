fun member(X, L) = 
if L=[] then false
else if X=hd(L) then true
else member(X, tl(L));

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

val UR = [(1,2), (1,3)];
val RR = [(1,7),(2,6),(3,4),(4,5)];
authorizedRoles(1, [(1,1), (1,2), (6,5)], [(1,2), (1,3), (2,4), (2,6)]);