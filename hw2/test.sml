fun max(x:int, y:int, z:int):int = 
if((x > y) andalso (x > z)) then x
else (if((y>z)) then y
else z);

fun factorial(x) = if x = 1 then 1
else x * factorial(x-1);

fun gcd(x, y) = if x = y then x
else if y > x then gcd(y, x)
else gcd(x - y, y);
gcd(15, 9);

fun firstThird(Tuple: 'a * 'b * 'c): 'a * 'b = (#1(Tuple), #3(Tuple));
firstThird(10, "Aaa", 12);

fun id x = x;
id(10);

