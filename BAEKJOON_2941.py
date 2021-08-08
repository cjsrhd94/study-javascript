word = input()
cro_al = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in cro_al:
    word = word.replace(i, '@')
print(len(word))