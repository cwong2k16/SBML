fun remove(x, L) = if L = [] then []
else if x=hd(L) then remove(x, tl(L))
else hd(L)::remove(x, tl(L));

fun removedupl(L) = if L = [] then []
else hd(L)::removedupl(remove(hd(L), tl(L)));






fun addMember(Role, L, L2, RR : (''a * ''a) list) = if RR = [] then L2
else if hd(L) = #1(hd(RR)) then #2(hd(RR)) :: addMember(Role, L, L2, tl(RR))
else addMember(Role, L, L2, tl(RR));

fun authorizedRolesHelper2(User, L, L2, RR : (''a * ''a) list) = if L = [] then []
else L2 @ authorizedRolesHelper2(User, tl(L) , addMember(hd(L), L, L2, RR), RR);

fun authorizedRolesHelper(User, L : (''a * ''a) list, RR : (''a * ''a) list) = if L = [] then []
else if User = #1(hd(L)) then #2(hd(L))::authorizedRolesHelper(User, tl(L), RR)
else authorizedRolesHelper(User, tl(L), RR);

val UR = [(1,1), (1,3)];
val RR = [(1,2), (2, 7), (3,4), (1,99), (5, 1), (1,101)];
val res = authorizedRolesHelper(1, UR, RR);
val res2 = authorizedRolesHelper2(1, res, res, RR);