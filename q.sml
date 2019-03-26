fun length(L) = if L=[] then 0
    else 1+length(tl(L));

fun helper(L1, L2, rem, x) = 
	if L1=[] then ~1
    else if length(rem) = 0 then x-length(L2)
    else if hd(L1) = hd(rem) then helper(tl(L1),L2,tl(rem),x+1)
    else helper(tl(L1),L2,L2,x+1);

fun first(S,Sub) =
    helper(S,Sub,Sub,0);
    
first(["c","a","t","c","o","w","c","a","t"], ["m","a","t"]);