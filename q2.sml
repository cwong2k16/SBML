fun gcd(n, m) = if n = m then n
else if m>n then gcd(m-n, n)
else gcd(m, n-m);

fun coprime(x, y) = gcd(x,y) = 1;

fun range(x, y) = if x = y then []
else x::range(x,y);

fun euler_helper(L, n) = if L = [] then 0
else if coprime(hd(L), n) then 1+euler_helper(tl(L), n)
else euler_helper(tl(L), n);

fun euler_totient(n) = euler_helper(range(1,n), n);

euler_totient(6);