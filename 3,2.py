import math
#ett program som talar om vad för area och omkrets en cirkel har efter man har hät in en radie
a = float(input('radie?' ))
if a > 0:#gör att man inte kan ha en radie under 0 för då går det till else
    b = 3.14
    area= b * a**2
    omkrets= 2 * b * a
    print('cirkelns area',area)
    print('cirkelns omkrets',omkrets) 
else:# och visar ett error för att det var mindre än 0 eller 0
    print('error radie mindre än 0')