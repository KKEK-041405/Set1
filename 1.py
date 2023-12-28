sentence = input("Enter sentence")

vowel = ['a','e','i','o','u']

cnt=0

for i in str(

vowel).lower():

 if i in sentence:

 cnt+=1

if cnt==5:

 print("All vowels exist in given sentence")

else:

 print("All vowels do not ex

ist")
