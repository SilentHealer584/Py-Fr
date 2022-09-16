import sys, os

arg = sys.argv[1]

with open(arg, 'r') as file:
    file = file.read()
    
    executable = file.replace('tant que ', 'while ').replace('si ', 'if ').replace('ou alors', 'elif ').replace('sinon:', 'else:').replace('importer ', 'import ').replace('classe ', 'class ').replace('essaie:', 'try:').replace('autrement:', 'except:').replace('pour ', 'for ').replace(' Vrai', 'True').replace('imprime(', 'print(').replace('saisie(', 'input(')
    
    exec(executable)