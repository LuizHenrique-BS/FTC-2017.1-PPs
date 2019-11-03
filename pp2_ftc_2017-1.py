import re

def validaCaractere(entrada):
    res = False
    if re.match(r'^(\(|\)|\[|\]|\{|\}|\s)+$', entrada):
        res = True
    return res

def converteEntrada(ent):
    ent = ent.replace('(', ' ( ')
    ent = ent.replace(')', ' ) ')
    ent = ent.replace('{', ' { ')
    ent = ent.replace('}', ' } ')
    ent = ent.replace('[', ' [ ')
    ent = ent.replace(']', ' ] ')
    ent = ent.split()
    return ent

def checarString(ent):
    pilha = []
    for char in ent:
        if re.match(r'^(\(|\[|\{)$', char):
            pilha.append(char)
        else:
            try:
                aux = pilha.pop()
            except:
                return False
            if char == ')' and aux != '(':
                pilha.append(aux)
            elif char == ']' and aux != '[':
                pilha.append(aux)
            elif char == '}' and aux != '{':
                pilha.append(aux)
    if len(pilha) == 0:
        res = True
    else:
        res = False
    return res

def main(ent):
    teste = False
    if (validaCaractere(ent) == teste):
        return teste
    elif(checarString(converteEntrada(ent)) == teste):
        return teste
    else:
        return True


try:
    entrada = input()
    print(main(entrada))
except:
    print('True')
