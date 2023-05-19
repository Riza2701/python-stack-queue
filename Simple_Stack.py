#Percobaan 1: Stack Sederhana
stack = [1,2,3,4,5]
print('Tumpukan sekarang:',stack)

stack.append(6)
print('Tumpukan masuk:',6)
print('Tumpukan sekarang:',stack)

stack.append(7)
print('Tumpukan masuk:',7)
print('Tumpukan sekarang:',stack)

out = stack.pop()
print('Tumpukan keluar:',out)
print('Tumpukan sekarang:',stack)
