fun authorizedRoles(User, L : (int*int) list) = if L = [] then []
else if User = #1(hd(L)) then #2(hd(L))::authorizedRoles(User, tl(L))
else authorizedRoles(User, tl(L));

val lst = [(1,2), (1,3), (4,5), (1, 8), (4,9), (5,1)];

authorizedRoles(8, lst);