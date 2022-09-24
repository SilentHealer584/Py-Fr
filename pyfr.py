import sys, getopt, os

def translate(content: str) -> str:
    return content.replace('tant que ', 'while ').replace('si ', 'if ').replace('ou alors', 'elif ').replace('sinon:', 'else:').replace('importer ', 'import ').replace('classe ', 'class ').replace('essaie:', 'try:').replace('autrement:', 'except:').replace('pour ', 'for ').replace(' Vrai', 'True').replace('imprime(', 'print(').replace('saisie(', 'input(')

try:
    with open(sys.argv[2], 'r', encoding='utf-8') as file:

        content = file.read()
        executable = translate(content)

        arguments, values = getopt.getopt(sys.argv[1:], "cfhm", ["Console", "Translate", "Help", "File"])

        for currentArgument, currentValue in arguments:
            if currentArgument in ("-c", "--Console"):
                print(executable)
            elif currentArgument in ("-f", "--Translate"):
                with open(f"{str(sys.argv[2]).removesuffix('.py')}-compiled.py", "x", encoding="utf-8") as f:
                    f.write(executable)
                    f.close()
                print(f"Translated file -> {os.getcwd()}\{str(sys.argv[2]).removesuffix('.py')}-compiled.py")
            elif currentArgument in ("-h", "--Help"):
                print("""
usage: python pyfr.py [option] [file]
options:    
-c --Console    : Display the translated code in the terminal.
-f --Translate  : Translate the code and write it in a new file.
-h --Help       : Display the help message.
-m --File       : Read the file and execute it.
                """)
            elif currentArgument in ("-m", "--File"):
                exec(executable)

        file.close()
except IndexError:
    print("""
usage: python pyfr.py [option] [file]
options:    
-c --Console    : Display the translated code in the terminal.
-f --Translate  : Translate the code and write it in a new file.
-h --Help       : Display the help message.
-m --File       : Read the file and execute it.
    """)
