punctuations = '''!()-[|]{};:'"\,<>./?@#$%^&*_~`=+" "'''
rev=""
my_str = input("enter a sentence: ")
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char
for i in no_punct:
	rev = i + rev
if no_punct == rev:
	print("the sentence is reversible")
else:
	print("the sentence IS NOT reversible")