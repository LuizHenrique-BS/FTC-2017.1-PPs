import re
import sys

sys.setrecursionlimit(1000000)

def q0(fita, cabecote):
    if fita[cabecote] == 'b':
        cabecote += 1
        q0(fita, cabecote)
        return
    elif(fita[cabecote] == 'c'):
        cabecote += 1
        q0(fita, cabecote)
        return
    elif (fita[cabecote] == 'd'):
        cabecote += 1
        q0(fita, cabecote)
        return
    elif (fita[cabecote] == 'e'):
        cabecote += 1
        q0(fita, cabecote)
        return
    elif (fita[cabecote] == 'f'):
        cabecote += 1
        q0(fita, cabecote)
        return
    elif (fita[cabecote] == 'x'):
        cabecote += 1
        q0(fita, cabecote)
        return
    elif (fita[cabecote] == 'a'):
        fita[cabecote] = 'x'
        q1(fita, cabecote)
        return
    elif (fita[cabecote] == '0'):
        cabecote -= 1
        q12(fita, cabecote)
        return

def q1(fita, cabecote):
    if(fita[cabecote] == 'a'):
        cabecote -= 1
        q1(fita, cabecote)
        return
    elif (fita[cabecote]== 'b'):
        cabecote -= 1
        q1(fita, cabecote)
        return
    elif (fita[cabecote] == 'c'):
        cabecote -= 1
        q1(fita, cabecote)
        return
    elif (fita[cabecote] == 'd'):
        cabecote -= 1
        q1(fita, cabecote)
        return
    elif (fita[cabecote] == 'e'):
        cabecote -= 1
        q1(fita, cabecote)
        return
    elif (fita[cabecote] == 'f'):
        cabecote -= 1
        q1(fita, cabecote)
        return
    elif (fita[cabecote] == 'x'):
        cabecote -= 1
        q1(fita, cabecote)
        return
    elif (fita[cabecote] == '0'):
        cabecote += 1
        q2(fita, cabecote)
        return

def q2(fita, cabecote):
    if (fita[cabecote] == 'a'):
        cabecote += 1
        q2(fita, cabecote)
        return
    elif (fita[cabecote] == 'c'):
        cabecote += 1
        q2(fita, cabecote)
        return
    elif (fita[cabecote] == 'd'):
        cabecote += 1
        q2(fita, cabecote)
        return
    elif (fita[cabecote] == 'e'):
        cabecote += 1
        q2(fita, cabecote)
        return
    elif (fita[cabecote] == 'f'):
        cabecote += 1
        q2(fita, cabecote)
        return
    elif (fita[cabecote] == 'x'):
        cabecote += 1
        q2(fita, cabecote)
        return
    elif (fita[cabecote] == 'b'):
        fita[cabecote] = 'x'
        q3(fita, cabecote)
        return

def q3(fita, cabecote):
    if (fita[cabecote] == 'a'):
        cabecote -= 1
        q3(fita, cabecote)
        return
    elif (fita[cabecote] == 'b'):
        cabecote -= 1
        q3(fita, cabecote)
        return
    elif (fita[cabecote] == 'c'):
        cabecote -= 1
        q3(fita, cabecote)
        return
    elif (fita[cabecote] == 'd'):
        cabecote -= 1
        q3(fita, cabecote)
        return
    elif (fita[cabecote] == 'e'):
        cabecote -= 1
        q3(fita, cabecote)
        return
    elif (fita[cabecote] == 'f'):
        cabecote -= 1
        q3(fita, cabecote)
        return
    elif (fita[cabecote] == 'x'):
        cabecote -= 1
        q3(fita, cabecote)
        return
    elif (fita[cabecote] == '0'):
        cabecote += 1
        q4(fita, cabecote)
        return

def q4(fita, cabecote):
    if (fita[cabecote] == 'a'):
        cabecote += 1
        q4(fita, cabecote)
        return
    elif (fita[cabecote] == 'b'):
        cabecote += 1
        q4(fita, cabecote)
        return
    elif (fita[cabecote] == 'd'):
        cabecote += 1
        q4(fita, cabecote)
        return
    elif (fita[cabecote] == 'e'):
        cabecote += 1
        q4(fita, cabecote)
        return
    elif (fita[cabecote] == 'f'):
        cabecote += 1
        q4(fita, cabecote)
        return
    elif (fita[cabecote] == 'x'):
        cabecote += 1
        q4(fita, cabecote)
        return
    elif (fita[cabecote] == 'c'):
        fita[cabecote] = 'x'
        q5(fita, cabecote)
        return

def q5(fita, cabecote):
    if (fita[cabecote] == 'a'):
        cabecote -= 1
        q5(fita, cabecote)
        return
    elif (fita[cabecote] == 'b'):
        cabecote -= 1
        q5(fita, cabecote)
        return
    elif (fita[cabecote] == 'c'):
        cabecote -= 1
        q5(fita, cabecote)
        return
    elif (fita[cabecote] == 'd'):
        cabecote -= 1
        q5(fita, cabecote)
        return
    elif (fita[cabecote] == 'e'):
        cabecote -= 1
        q5(fita, cabecote)
        return
    elif (fita[cabecote] == 'f'):
        cabecote -= 1
        q5(fita, cabecote)
        return
    elif (fita[cabecote] == 'x'):
        cabecote -= 1
        q5(fita, cabecote)
        return
    elif (fita[cabecote] == '0'):
        cabecote += 1
        q6(fita, cabecote)
        return

def q6(fita, cabecote):
    if (fita[cabecote] == 'a'):
        cabecote += 1
        q6(fita, cabecote)
        return
    elif (fita[cabecote] == 'b'):
        cabecote += 1
        q6(fita, cabecote)
        return
    elif (fita[cabecote] == 'c'):
        cabecote += 1
        q6(fita, cabecote)
        return
    elif (fita[cabecote] == 'e'):
        cabecote += 1
        q6(fita, cabecote)
        return
    elif (fita[cabecote] == 'f'):
        cabecote += 1
        q6(fita, cabecote)
        return
    elif (fita[cabecote] == 'x'):
        cabecote += 1
        q6(fita, cabecote)
        return
    elif (fita[cabecote] == 'd'):
        fita[cabecote] = 'x'
        q7(fita, cabecote)
        return

def q7(fita, cabecote):
    if (fita[cabecote] == 'a'):
        cabecote -= 1
        q7(fita, cabecote)
        return
    elif (fita[cabecote] == 'b'):
        cabecote -= 1
        q7(fita, cabecote)
        return
    elif (fita[cabecote] == 'c'):
        cabecote -= 1
        q7(fita, cabecote)
        return
    elif (fita[cabecote] == 'd'):
        cabecote -= 1
        q7(fita, cabecote)
        return
    elif (fita[cabecote] == 'e'):
        cabecote -= 1
        q7(fita, cabecote)
        return
    elif (fita[cabecote] == 'f'):
        cabecote -= 1
        q7(fita, cabecote)
        return
    elif (fita[cabecote] == 'x'):
        cabecote -= 1
        q7(fita, cabecote)
        return
    elif (fita[cabecote] == '0'):
        cabecote += 1
        q8(fita, cabecote)
        return

def q8(fita, cabecote):
    if (fita[cabecote] == 'a'):
        cabecote += 1
        q8(fita, cabecote)
        return
    elif (fita[cabecote] == 'b'):
        cabecote += 1
        q8(fita, cabecote)
        return
    elif (fita[cabecote] == 'c'):
        cabecote += 1
        q8(fita, cabecote)
        return
    elif (fita[cabecote] == 'd'):
        cabecote += 1
        q8(fita, cabecote)
        return
    elif (fita[cabecote] == 'f'):
        cabecote += 1
        q8(fita, cabecote)
        return
    elif (fita[cabecote] == 'x'):
        cabecote += 1
        q8(fita, cabecote)
        return
    elif (fita[cabecote] == 'e'):
        fita[cabecote] = 'x'
        q9(fita, cabecote)
        return

def q9(fita, cabecote):
    if (fita[cabecote] == 'a'):
        cabecote -= 1
        q9(fita, cabecote)
        return
    elif (fita[cabecote] == 'b'):
        cabecote -= 1
        q9(fita, cabecote)
        return
    elif (fita[cabecote] == 'c'):
        cabecote -= 1
        q9(fita, cabecote)
        return
    elif (fita[cabecote] == 'd'):
        cabecote -= 1
        q9(fita, cabecote)
        return
    elif (fita[cabecote] == 'e'):
        cabecote -= 1
        q9(fita, cabecote)
        return
    elif (fita[cabecote] == 'f'):
        cabecote -= 1
        q9(fita, cabecote)
        return
    elif (fita[cabecote] == 'x'):
        cabecote -= 1
        q9(fita, cabecote)
        return
    elif (fita[cabecote] == '0'):
        cabecote += 1
        q10(fita, cabecote)
        return

def q10(fita, cabecote):
    if (fita[cabecote] == 'a'):
        cabecote += 1
        q10(fita, cabecote)
        return
    elif (fita[cabecote] == 'b'):
        cabecote += 1
        q10(fita, cabecote)
        return
    elif (fita[cabecote] == 'c'):
        cabecote += 1
        q10(fita, cabecote)
        return
    elif (fita[cabecote] == 'd'):
        cabecote += 1
        q10(fita, cabecote)
        return
    elif (fita[cabecote] == 'e'):
        cabecote += 1
        q10(fita, cabecote)
        return
    elif (fita[cabecote] == 'x'):
        cabecote += 1
        q10(fita, cabecote)
        return
    elif (fita[cabecote] == 'f'):
        fita[cabecote] = 'x'
        q11(fita, cabecote)
        return

def q11(fita, cabecote):
    if (fita[cabecote] == 'a'):
        cabecote -= 1
        q11(fita, cabecote)
        return
    elif (fita[cabecote] == 'b'):
        cabecote -= 1
        q11(fita, cabecote)
        return
    elif (fita[cabecote] == 'c'):
        cabecote -= 1
        q11(fita, cabecote)
        return
    elif (fita[cabecote] == 'd'):
        cabecote -= 1
        q11(fita, cabecote)
        return
    elif (fita[cabecote] == 'e'):
        cabecote -= 1
        q11(fita, cabecote)
        return
    elif (fita[cabecote] == 'f'):
        cabecote -= 1
        q11(fita, cabecote)
        return
    elif (fita[cabecote] == 'x'):
        cabecote -= 1
        q11(fita, cabecote)
        return
    elif (fita[cabecote] == '0'):
        cabecote += 1
        q0(fita, cabecote)
        return

def q12(fita, cabecote):
    if fita[cabecote] == 'x':
        cabecote -= 1
        q12(fita, cabecote)
        return
    elif(fita[cabecote] == '0'):
        cabecote += 1
        q13()
        return

def q13():
    global resultado
    resultado = "ACEITA"
    return resultado

cabecote = 2
branco = '00'

try:
    global resultado
    resultado = "REJEITA"
    entrada = input()
    entrada2 = branco+entrada+branco
    fita = re.findall(".", entrada2)
    q0(fita, cabecote)

    entrada = entrada + ' ' + resultado
    print(entrada)
except:
    print(' ACEITA')