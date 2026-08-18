print("Word analyzer")
sentence= input("Enter Your Sentence").lower()
words= sentence.split()
print(len(words))
print(words[0:-1])
search = input("Enter what you're searching for").lower()
word2= "sakshiiiiii"
if word2 in search:
	print("Found her")
else:
	print("couldn't find her")
print(f"your {sentence} has found {word2} ")
print(f"your sentence: {sentence} has {len(words)}words , first : {words[0]} ,last: {words[-1]}")

#"Your sentence has 5 words. First word: hello. Last word: world."