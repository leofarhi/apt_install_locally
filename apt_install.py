import subprocess
import os
import sys

file_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(file_dir)

def is_installed(package):
    """Vérifie si un package ou une librairie est déjà installé."""
    try:
        result = subprocess.run(["dpkg", "-s", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        if b"Status: install ok installed" in result.stdout:
            return True
    except subprocess.CalledProcessError:
        pass
    return False
allready_installed = []
def install(package, force=False):
    global allready_installed
    if package in allready_installed:
        print(f"Package {package} is already installed.")
        return
    allready_installed.append(package)
    if not force:
        """Télécharge et installe un package et ses dépendances."""
        if is_installed(package):
            print(f"Package {package} is already installed.")
            return

    print(f"Installing {package}...")
    val = subprocess.call(["apt-get", "download", package])
    if val != 0:
        print(f"Error downloading package: {package}.")
        return

    lst = os.listdir(file_dir)
    package_file = None
    for item in lst:
        if item.startswith(package):
            package_file = item
            break

    if package_file is None:
        print(f"Error finding package file for {package}.")
        return

    # Extraire le package
    subprocess.call(["dpkg", "--extract", package_file, "."])
    print(f"Extracted {package_file}.")

    # Supprimer le fichier de package téléchargé
    os.remove(package_file)

    # Gérer les dépendances
    try:
        print(f"Checking dependencies for {package}...")
        output = subprocess.check_output(["apt-cache", "depends", package]).decode("utf-8")
        for line in output.splitlines():
            if "  Depends:" in line:
                dependency = line.split(":")[1].strip()
                print(f"Found dependency: {dependency}")
                install(dependency, force=force)  # Installation récursive des dépendances
    except subprocess.CalledProcessError:
        print(f"Could not resolve dependencies for {package}.")

if len(sys.argv) < 2:
    print("Usage: python3 apt_install.py <package>")
    sys.exit(1)
force = False
if len(sys.argv) > 2 and sys.argv[2] == "--force":
    force = True
install(sys.argv[1], force=force)
