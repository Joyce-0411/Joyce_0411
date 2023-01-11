import re
text = "Iam not feeling well.Iam so sad.I want some chocolate."

max_words = 0 
sentences = re.split("[.!?]", text)
for sentence in sentences:
 max_words = max( len( sentence.split() ), max_words ) 


print(f"max_words: {max_words}")
