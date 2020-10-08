"""enter a sentence and the output will be its pglatin form...
   eg: input: nevermind youve got them
       output: evermindnay ouveyay otgay hemtay

       taking the first letter of a word at the end and adding 'ay' at the end """

#sentence input
s=input("enter a sentence \n")       

#function to convert a word into its piglatin form
def pig(x):
	#x is the string word parameter
	r=x[1:]+x[0]+"ay"

	return r


#splitting the words of the sentence in a list p
p=s.split()

#traversing through all the words and converting them into their piglatin form
#also storing the piglatin forms in another empty list z
z=[]

for i in p:
	y=pig(i)
	z.append(y)

#joining the words of list z to form a sentence of the piglatin form and then printing it
a=" ".join(z)
print(f"Piglatin form is: {a}")
