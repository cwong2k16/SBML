fun authorizedRolesHelper(User, L : (''a * ''a) list) = if L = [] then []
else if User = #1(hd(L)) then #2(hd(L))::authorizedRoles(User, tl(L))
else authorizedRoles(User, tl(L));

fun authorizedRolesHelper2(User, L : (''a * ''a) list, RR : (''a * ''a) list) = if L = [] then []
else if(hd(L))

fun addMember(Role, RR) = if RR = [] then []
else if Role = #1(hd(RR)) then #2(hd(RR))::addMember(Role, tl(RR))
else authorizedRoles(Role, tl(RR));