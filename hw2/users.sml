fun authorizedRoles(User, L : (''a * ''a) list) = if L = [] then []
else if User = #1(hd(L)) then #2(hd(L))::authorizedRoles(User, tl(L))
else authorizedRoles(User, tl(L));

val lst = [("a","president"), ("a","citizen"), ("b","agf"), ("b", "dsa"), ("c","asdsd"), ("d","asdsad")];

authorizedRoles("a", lst);