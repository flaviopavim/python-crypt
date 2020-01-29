from array import *
import math
def cc(s, n, rev, m):
    r = '';
    for i in range(len(s)):
        p = m.find(s[i])
        if p >= 0:
            if rev:
                soma=p-n
            else: 
                soma = p + n
            while (soma >= 52):
                soma -= 26
            while (soma < 0):
                soma += 26
            r=r+''+m[soma]
        else:
            r=r+''+s[i]
    return r
def caesar(s, n, rev):
    m1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    m2 = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    return cc(cc(s,n,rev,m1),n,rev,m2)

s='testando uma frase bem grande pra ver o que vira disso aqui. Python? No problem!'
c=caesar(s,3,0);
print('CAE:   '+c)
print('UNCAE: '+caesar(c,3,1))

def charVal(c):
    m = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    p = m.find(c)
    if (p > 0):
        return p
    return 0

def viginere(string, key, reverse):
    kl = len(key);
    count = 0;
    r = '';
    for i in range(len(string)):
        if (count == kl):
            count = 0
        if (reverse):
            c = -(charVal(key[count]))
        else:
            c = charVal(key[count])
        r = r+''+caesar(string[i], c,0)
        count=count+1;
    return r

print('VG:    '+viginere(s,'aloha',0))
print('UNVG:  '+viginere(viginere(s,'aloha',1),'aloha',0))

def sh(s, l):
    g = 0
    b = 0
    arr=[0]*l
    for i in range(len(s)):
        if g == l:
            g = 0
        arr[g]=''
        g=g+1
    g = 0
    b = 0
    for i in range(len(s)):
        if g == l:
            g = 0
        arr[g]=str(arr[g])+''+str(s[i])
        g=g+1 
    r = ''
    for f in arr:
        r=r+''+f
    return r

def unsh(s, l):
    c = a = 0
    arr=[0]*100
    for i in range(len(s)):
        arr[c] = s[i]
        if (c < (len(s) - l)):
            c=c+l
        else:
            a=a+1
            c = a
    r = ''
    for i in range(len(s)):
        r=r+''+arr[i]
    return r

level=7
sh_=sh(s,level)
print('SH'+str(level)+':   '+sh_)
print('UNSH'+str(level)+': '+unsh(sh_,level))

