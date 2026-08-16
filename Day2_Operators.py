'''
#comparision operator

a = 110
b = 90
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#logical operator
# and / or / not

100 - 200 ->true
165 ->true
93  ->false
201 ->false
 
cond1	cond2	op-and	
TRUE	TRUE	TRUE	
TRUE	FALSE	FALSE	
FALSE	TRUE	FALSE			
FALSE	FALSE	FALSE	

cond1	cond2	op-or	
TRUE	TRUE	TRUE	
TRUE	FALS	TRUE	
FALSE	TRUE	TRUE		
FALSE	FALSE	FALSE		

cond	op-not
TRUE	FALSE
FALSE	TRUE

print(29>=100 and 29<=200)
print(29>=100 or 29<=200)
print(not(29>=100))

#bitwise operator

		2^7	2^6	2^5	2^4	2^3	2^2	2^1	2^0			
		128	64	32	16	8	4	2	1			
		0	0	0	0	0	1	0	1	5		
		0	0	0	0	0	0	1	1	3		
		0	0	0	0	0	0	0	1	5&3		
		0	0	0	0	0	1	1	1	5|3		
		0	0	0	0	0	1	1	0	5^3		
												
2^9	2^8	2^7	2^6	2^5	2^4	2^3	2^2	2^1	2^0	2^-1	2^-2	
512	256	128	64	32	16	8	4	2	1			
		0	0	0	0	0	1	0	1			5
				0	0	0	0	0	1	0	1	5>>2
0	0	0	0	0	1	0	1					 

+ve -> -(n+1)
5 -> -(5+1)-> -(6) -> -6
12 -> -(12+1) -> -13

-ve -> +(n-1)
-5 -> +(5-1) -> +(4) -> 4
-21 -> +(21-1) -> 20

print(5&3)
print(5|3)
print(5^3)
print(~5)
print(~(-5))
print(5<<2)
print(5>>2)

#membership operator
a = [1,2,3,4,5,6,7,8,9]
print(6 in a)
print(10 in a)

print(10 not in a)
print(6 not in a)

#identity operator
x = 10
y = 20
z = 10
print(x is y)
print(x is z)

print(x is not y)
print(x is not z)

'''





