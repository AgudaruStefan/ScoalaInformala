# 1. Se dă un şir cu cel mult 10 caractere. Să se determine câte vocale conţine. (1 punct)
sirCaractere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def justVoc(x):
    l = []
    vocale = ['a', 'e', 'i', 'o', 'u', 'ă']
    for i in x:
        if i in vocale:
            l.append(i)
    print(len(l))

print(justVoc(sirCaractere))
