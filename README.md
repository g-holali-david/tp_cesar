# Chiffre de César en Python

## Auteur : GAVI Holali David

Ce programme implémente l'algorithme classique du Chiffre de César, une méthode de chiffrement par substitution  
qui déplace chaque lettre d'un message d'un nombre fixe de positions dans l'alphabet. 
Ce projet a évolué pour supporter le chiffrement de **tous les caractères Unicode**, y compris les caractères accentués, les chiffres, et les symboles.

### Fichiers

- `cesar.py` : Contient la logique de chiffrement et de déchiffrement.
- `ui.py` : Gère l'interface utilisateur et la gestion des entrées.
- `main.py` : Point d'entrée du programme pour démarrer l'application.

### Fonctionnalités

1. **Chiffrement de messages** :
   - Le programme chiffre des messages en utilisant un décalage donné. Chaque caractère du message est décalé dans sa représentation Unicode.
   - Les caractères accentués, comme les lettres françaises, sont désormais également chiffrés correctement, 
   contrairement à la première version qui ne gérait que les lettres de l'alphabet standard.

2. **Déchiffrement de messages** :
   - Le programme permet également de déchiffrer des messages en appliquant un décalage inverse.
   - Cette fonctionnalité fonctionne pour tous les caractères, y compris ceux accentués et les symboles Unicode.

3. **Attaque brute-force** :
   - Une fonctionnalité d'attaque brute-force a été ajoutée pour casser le chiffrement sans connaître le décalage. 
   Le programme essaie toutes les valeurs possibles de décalage de 1 à 25 pour déchiffrer un message chiffré.

### Améliorations Progressives

Le projet a connu plusieurs améliorations majeures :

1. **Prise en charge des caractères accentués** :
   - La première version du programme ne gérait que les lettres non accentuées. 
   Cette limitation a été surmontée en appliquant le décalage directement sur le **code Unicode** de chaque caractère. 
   Ainsi, même des caractères accentués comme `é`, `à`, `è` sont maintenant chiffrés et déchiffrés correctement.
   
2. **Chiffrement de tous les caractères Unicode** :
   - Contrairement à la version originale qui se concentrait sur l'alphabet, la version améliorée chiffre tous les caractères (y compris les symboles, les chiffres et les espaces) en utilisant leur code Unicode. Cela permet de traiter une plus grande variété de messages, avec tous types de caractères.

3. **Gestion des erreurs** :
   - Le programme vérifie désormais que les entrées sont bien des chaînes de caractères valides avant de procéder à l'opération de chiffrement ou de déchiffrement. Cela améliore la robustesse et empêche les erreurs dues à des entrées incorrectes.

4. **Amélioration de l'attaque brute-force** :
   - L'attaque brute-force permet maintenant d'essayer tous les décalages possibles, de 1 à 25, pour retrouver le message original sans connaître le décalage. 
   Un message sera déchiffré avec chaque valeur de décalage, offrant ainsi une méthode simple pour casser un chiffrement de César faible.

### Instructions d'utilisation

1. **Lancer le programme** :
   - Ouvrez un terminal et exécutez le fichier `main.py` :
     ```bash
     python main.py
     ```

2. **Menu principal** :
   - Choisissez une option :
     - `1` : Chiffrer un message
     - `2` : Déchiffrer un message
     - `3` : Attaque brute-force sur un message chiffré
     - `4` : Quitter le programme

3. **Chiffrement d'un message** :
   - Entrez le message à chiffrer et le décalage à utiliser. Le message sera chiffré en fonction du décalage Unicode.

4. **Déchiffrement d'un message** :
   - Entrez un message chiffré et le décalage utilisé lors du chiffrement pour récupérer le message original.

5. **Attaque brute-force** :
   - Si vous ne connaissez pas le décalage, vous pouvez utiliser l'attaque brute-force pour essayer 
   tous les décalages possibles et voir si l'un d'eux vous donne un message lisible.
