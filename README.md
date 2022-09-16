# Py-Fr
Ce module vous permet de coder en Francais tout en etant capables d'executer vos programmes normalement.<br/>
Par exemple:
```
x = 0

tant que x < 10:
    imprime(x)
    x = x + 1

variable = saisie("Comment t'appelle-tu ? ")

imprime(variable)
```

Est traduit en:
 
```
x = 0

while x < 10:
    print(x)
    x = x + 1

variable = input("Comment t'appelle-tu ? ")

print(variable)
```
Puis exécuté par la ligne de commande

Pour executer:<br/>
- Naviguer dans le dossier ou se trouve le code source 
- Créer votre fichier français ou copiez le dans le même dossier que le code source (fichier: `traducteur.py`)
- Dans l'Explorateur de Fichiers, naviguez vers le dossier contenant vos fichiers
- Tapper `cmd` dans la barre d'adresse
- Dans la fenêtre CMD, tapper la ligne suivante: `python traducteur.py nom_de_votre_fichier.py`

A noter: Si vous exécutez le script dans votre IDE directement, il est normal que le programme ne marche pas.<br/>
La méthode ci-dessus est recommandée.
