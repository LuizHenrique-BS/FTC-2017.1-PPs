import re


def validaUsuario(usuario):
    if re.match(r'^[a-z]([a-z]|[A-Z])*$', usuario):
        return 'True'
    else:
        return 'False'


def dv1Cpf(cpf):
    soma = 0
    j = 0
    while (j < 9):
        soma = soma + (cpf[j] * (10 - j))
        j += 1
    if ((soma % 11) < 2):
        a = 0
    else:
        a = (11 - (soma % 11))
    return a


def dv2Cpf(cpf, digito1):
    soma = 0
    j = 0
    while (j < 9):
        soma = soma + (cpf[j] * (11 - j))
        j += 1
    soma = soma + (digito1 * (11 - j))
    if (soma % 11 < 2):
        a = 0
    else:
        a = (11 - (soma % 11))
    return a


def validaCpf(cpfInt):
    x = dv1Cpf(cpfInt)
    y = dv2Cpf(cpfInt, dv1Cpf(cpfInt))

    if x == cpfInt[9] and y == cpfInt[10]:
        a = 'True'
    else:
        a = 'False'
    return a


def converteCpf(pCpf):
    pCpf = pCpf.replace('.', '')
    pCpf = pCpf.replace('-', '')
    cpfInt = []
    cpfInt = [int(x) for x in pCpf]
    return cpfInt


def vPadraoCpf(pCpf):
    if re.match(r'^[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}$', pCpf):
        return 'True'
    else:
        return 'False'


def validaEmail(email):
    if re.match(r'^([a-z]|[A-Z])([a-z]|[A-Z]|[0-9]|[._%+-])*\@[a-z]*\.+([a-z]|\.)*$', email):
        return 'True'
    else:
        return 'False'


def validaSenha(senha):
    r = 'False'
    if re.match(r'^((\d{2}|\d[A-F]|[A-F]\d)\.){3}(\d{2}|\d[A-F]|[A-F]\d)$', senha):
        if re.match(r'^([0]{2}|[1]{2}|[2]{2}|[3]{2}|[4]{2}|[5]{2}|[6]{2}|[7]{2}|[8]{2}|[9]{2}).*$', senha):
            return r
        elif re.match(r'^.{2}\.([0]{2}|[1]{2}|[2]{2}|[3]{2}|[4]{2}|[5]{2}|[6]{2}|[7]{2}|[8]{2}|[9]{2}).*$', senha):
            return r
        elif re.match(r'^.{2}\..{2}\.([0]{2}|[1]{2}|[2]{2}|[3]{2}|[4]{2}|[5]{2}|[6]{2}|[7]{2}|[8]{2}|[9]{2}).*$', senha):
            return r
        elif re.match(r'^.{2}\..{2}\..{2}\.([0]{2}|[1]{2}|[2]{2}|[3]{2}|[4]{2}|[5]{2}|[6]{2}|[7]{2}|[8]{2}|[9]{2})$', senha):
            return r
        else:
            return 'True'
    else:
        return r


def nomeApp(app):
    if re.match(r'^([a-z]|[A-Z])+$', app):
        return 'True'
    else:
        return 'False'


def versaoApp(versao):
    if re.match(r'^\d+\.\d+$', versao):
        lista = versao.split('.')
        vp = int(lista[0])
        sbv = int(lista[1])
        if vp >= sbv:
            return 'True'
        else:
            return 'False'
    else:
        return 'False'


def plataforma(plat):
    if re.match(r'^(windows|mac|linux|ios|android|windowsPhone)$', plat):
        return 'True'
    else:
        return 'False'


def main(ent):
    s = 'False'
    if len(ent) % 2 == 0:
        return s
    elif len(ent) < 7:
        return s
    elif len(ent) == 7:
        if validaUsuario(ent[0]) == s:
            return s
        elif vPadraoCpf(ent[1]) == s:
            return s
        elif validaCpf(converteCpf(ent[1])) == s:
            return s
        elif validaEmail(ent[2]) == s:
            return s
        elif validaSenha(ent[3]) == s:
            return s
        elif nomeApp(ent[4]) == s:
            return s
        elif versaoApp(ent[5]) == s:
            return s
        elif plataforma(ent[6]) == s:
            return s
        else:
            return 'True'
    else:
        if validaUsuario(ent[0]) == s:
            return s
        elif vPadraoCpf(ent[1]) == s:
            return s
        elif validaCpf(converteCpf(ent[1])) == s:
            return s
        elif validaEmail(ent[2]) == s:
            return s
        elif validaSenha(ent[3]) == s:
            return s
        elif nomeApp(ent[4]) == s:
            return s
        elif versaoApp(ent[5]) == s:
            return s
        elif plataforma(ent[6]) == s:
            return s
        else:
            j = (len(ent) - 1)
            while(j > 6):
                if j % 2 == 0:
                    if validaEmail(ent[j]) == s:
                        return s
                else:
                    if validaUsuario(ent[j]) == s:
                        return s
                j -= 1
        return 'True'
try:
    entrada = input().split()
    print(main(entrada))

except:
    print('False')