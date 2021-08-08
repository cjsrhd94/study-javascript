word = input()
cro_al = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in cro_al:
    word = word.replace(i, '@') # i에 해당하는 크로아티아 알파벳을 @로 바꿔준다.
print(len(word))