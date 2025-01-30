# apt_install_locally

## Description
Le projet `apt_install_locally` permet d'installer localement un package Debian (`.deb`) et ses dépendances via `apt-get`. Il vérifie d'abord si le package est déjà installé, puis procède à son téléchargement, son extraction et l'installation de ses dépendances de manière récursive.

## Prérequis
- Python 3.x

## Installation et Utilisation

### 1. Télécharger le script

Téléchargez le script `apt_install_locally` dans le répertoire souhaité sur votre machine.

### 2. Ajoutez une entrée à votre `.bashrc`

Pour faciliter l'exécution du script, vous pouvez ajouter un alias dans votre fichier `.bashrc`. Ouvrez votre fichier `.bashrc` dans un éditeur de texte et ajoutez la ligne suivante :

```bash
alias apt_install='function _apt_install(){ python /<path_repo>/apt_install.py $1 $2;}; _apt_install'
PATH="$PATH:/<path_repo>/usr/bin"
export LD_LIBRARY_PATH=$(find /<path_repo>/usr/lib -type d | tr '\n' ':')$LD_LIBRARY_PATH
```

N'oubliez pas de remplacer `/<path_repo>` par le chemin réel où vous avez téléchargé le script.

Après avoir ajouté ces lignes, rechargez votre fichier `.bashrc` avec la commande suivante :

```bash
source ~/.bashrc
```

### 3. Utilisation

#### Pour installer un package :

```bash
apt_install <package_name>
```

Exemple d'utilisation :

```bash
apt_install vim
```

#### Option `--force`

Si vous souhaitez forcer l'installation d'un package, même s'il est déjà installé, vous pouvez ajouter l'option `--force` :

```bash
apt_install <package_name> --force
```

### 4. Fonctionnement du script

- **Vérification de l'installation** : Le script vérifie si le package est déjà installé avant de procéder à son installation.
- **Téléchargement** : Si le package n'est pas installé, le script utilise `apt-get download` pour télécharger le package `.deb`.
- **Extraction et Installation** : Une fois le package téléchargé, il est extrait à l'aide de `dpkg --extract` et installé localement.
- **Gestion des dépendances** : Le script analyse les dépendances du package via `apt-cache depends` et les installe récursivement.

## Limitations

- Ce script ne gère pas directement les installations depuis un dépôt personnalisé, il fonctionne avec les packages disponibles via les dépôts Debian standards.
- L'installation se fait localement, ce qui signifie que les fichiers sont extraits dans le répertoire actuel, et non installés globalement dans le système. Si vous avez besoin de déplacer des fichiers ou de les installer de manière globale, vous devrez le faire manuellement après l'extraction.

## Exemples d'utilisation

### Exemple 1 : Installer un package

```bash
apt_install curl
```

### Exemple 2 : Forcer l'installation d'un package

```bash
apt_install curl --force
```

### Exemple 3 : Installer un package avec ses dépendances

Le script résoudra automatiquement les dépendances et installera tous les packages nécessaires.
