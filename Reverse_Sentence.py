#Percobaaan 3: Membalikkan Kata/Kalimat(Stack)
def reverse_sentence(sentece):
    stack = []
    reverse_sentence = ""
    
    for word in sentece.split():
        stack.append(word)
        
    while len(stack)>0:
        reverse_sentence += stack.pop()+""
        
    return reverse_sentence.strip()

sentence = "Selamat Pagi, bagaimana kabar anda?"
print(reverse_sentence(sentence))