def f(x): #Definer en funksjon
    return (x+7)/(2+x**2) #Funksjonen returnerer regnestykket med x som en variabel

x = 0 #Definerer variabelen x som 0
h = 0.001 #Definerer variabelen h som 0.001

while f(x) <= f(x+h):   #While loop som kjører enn så lenge f(x) er mindre eller lik f(x+h)
    x=x+h               #Øker x med h som er veldig lite, derav derivasjon

print (x)               #Skriver ut variabelen x 