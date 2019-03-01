fun addMember(Role, RR) = if RR = [] then []
else if Role = #1(hd(RR)) then #2(hd(RR))::addMember(Role, tl(RR))
else addMember(Role, tl(RR));

fun authorizedRolesHelper2(User, L : (''a * ''a) list, RR : (''a * ''a) list) = if L = [] then []
else authorizedRolesHelper2(User, addMember(hd(L), RR), RR);

fun authorizedRolesHelper(User, L : (''a * ''a) list, RR : (''a * ''a) list) = if L = [] then []
else if User = #1(hd(L)) then #2(hd(L))::authorizedRolesHelper(User, tl(L), RR)
else authorizedRolesHelper(User, tl(L), RR);

