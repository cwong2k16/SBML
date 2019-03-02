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

fun addMember(L, RR : (''a * ''a) list) = 
if RR = [] then L
else if #1(hd(RR)) = hd(L) then addMember(L @ [#2(hd(RR))] , tl(RR))
else addMember(L, tl(RR));

fun authorizedRolesHelper2(User, L, RR : (''a * ''a) list) = 
if L = [] then []
else addMember(L, RR) @ authorizedRolesHelper2(User, tl(addMember(L, RR)), RR);

fun authorizedRolesHelper(User, L : (''a * ''a) list, RR : (''a * ''a) list) = 
if L = [] then []
else if User = #1(hd(L)) then #2(hd(L))::authorizedRolesHelper(User, tl(L), RR)
else authorizedRolesHelper(User, tl(L), RR);

fun authorizedRoles(User, L: (''a * ''a) list, RR : (''a * ''a) list) = 
removedupl(authorizedRolesHelper2(User, authorizedRolesHelper(User, L, RR), RR));

fun addMember2(L, RR : (''a * ''a) list) = 
if RR = [] then []
else if #1(hd(RR)) = hd(L) then #2(hd(RR)) :: addMember2(L, tl(RR))
else addMember2(L, tl(RR));

fun authorizedPermissions(User, L, RR : (''a * ''a) list) = 
if L = [] then []
else addMember2(L, RR) @ authorizedPermissions(User, tl(L), RR);
