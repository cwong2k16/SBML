fun addMember(Role, L, L2, RR : (''a * ''a) list) = if RR = [] then L2
else if Role = #1(hd(RR)) then #2(hd(RR)) :: addMember(Role, L, L2, tl(RR))
else addMember(Role, L, L2, tl(RR));

fun authorizedRolesHelper2(User, L, L2, RR : (''a * ''a) list) = if L = [] then []
else L2 @ authorizedRolesHelper2(User, tl(L) , addMember(hd(L), L, L2, RR), RR);

fun authorizedRolesHelper(User, L : (''a * ''a) list, RR : (''a * ''a) list) = if L = [] then []
else if User = #1(hd(L)) then #2(hd(L))::authorizedRolesHelper(User, tl(L), RR)
else authorizedRolesHelper(User, tl(L), RR);

val lst = [(1,2), (1,3), (4,5), (1, 8), (4,9), (5,1)];
val lst2 = [(1,77), (1, 78), (3,45), (1,80), (2, 123)];
val res = authorizedRolesHelper(1, lst, lst2);
val res2 = authorizedRolesHelper2(1, res, res, lst2);
