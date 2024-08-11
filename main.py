import os
import subprocess
import sys
import shutil


def check_git_repo():
    """Verifica si el directorio actual es un repositorio Git."""
    if not os.path.isdir(".git"):
        print("Este directorio no parece ser un repositorio Git.")
        return False
    print("Repositorio Git encontrado.")
    return True


def check_required_files():
    """Verifica si los archivos requeridos existen y los crea si no están presentes."""
    required_files = {
        "README.md": "# Proyecto\n\nDescripción del proyecto.",
        ".gitignore": "*.log\n*.pyc\n__pycache__/\nnode_modules/\n*.class\n*.jar\n",
    }

    for file, content in list(required_files.items()):
        if not os.path.exists(file):
            print(f"Advertencia: {file} no encontrado. Creando {file}...")
            create_file(file, content)
        else:
            print(f"{file} encontrado.")


def create_file(filename, content):
    """Crea un archivo con el contenido proporcionado."""
    try:
        with open(filename, "w") as f:
            f.write(content)
        print(f"{filename} creado con éxito.")
    except IOError as e:
        print(f"Error al crear el archivo {filename}: {e}")


def update_dependencies():
    """Actualiza las dependencias según los archivos de configuración presentes."""
    commands = {
        "requirements.txt": [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--upgrade",
            "-r",
            "requirements.txt",
        ],
        "package.json": ["npm", "update"],
        "Gemfile": ["bundle", "update"],
        "pom.xml": ["mvn", "versions:use-latest-releases"],
        "build.gradle": ["gradle", "dependencyUpdates"],
    }

    print("Actualizando dependencias...")
    for file, command in list(commands.items()):
        if os.path.exists(file):
            try:
                subprocess.run(command, check=True)
                print(f"Dependencias actualizadas para {file}.")
            except subprocess.CalledProcessError as e:
                print(f"Error al actualizar dependencias para {file}: {e}")


def handle_file_encoding(file_path):
    """Repara la codificación de archivos Python si es necesario."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            f.read()
    except UnicodeDecodeError:
        print(f"Reparando codificación en {file_path}...")
        try:
            shutil.copyfile(file_path, f"{file_path}.bak")
            with open(file_path, "rb") as f:
                content = f.read()
            with open(file_path, "wb") as f:
                f.write(content.decode("latin-1").encode("utf-8"))
            print(f"Codificación reparada en {file_path}.")
        except Exception as e:
            print(f"Error al reparar codificación en {file_path}: {e}")


def refactor_python_code():
    """Refactoriza y formatea código Python en el proyecto."""
    print("Refactorizando y formateando código Python...")

    try:
        # Convertir de Python 2 a 3
        subprocess.run([sys.executable, "-m", "lib2to3", "-w", "."], check=True)

        # Manejar archivos con problemas de codificación
        for root, _, files in os.walk("."):
            for file in files:
                if file.endswith(".py"):
                    handle_file_encoding(os.path.join(root, file))

        # Formateo con black y chequeo con flake8
        subprocess.run(["black", "."], check=True)
        subprocess.run(["flake8", "."], check=True)
        print("Código Python refactorizado y formateado con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al refactorizar código Python: {e}")


def refactor_java_code():
    """Refactoriza y actualiza código Java en el proyecto."""
    print("Refactorizando y actualizando código Java...")
    try:
        subprocess.run(["mvn", "spotless:apply"], check=True)
        subprocess.run(["mvn", "clean", "install"], check=True)
        print("Código Java refactorizado y actualizado con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al refactorizar código Java: {e}")


def run_tests():
    """Ejecuta pruebas dependiendo de los archivos de prueba disponibles."""
    print("Ejecutando pruebas...")
    try:
        if os.path.exists("tests"):
            subprocess.run(["pytest"], check=True)
        elif os.path.exists("src/test/java"):
            subprocess.run(["mvn", "test"], check=True)
        elif os.path.exists("spec"):
            subprocess.run(["rspec"], check=True)
        print("Pruebas ejecutadas con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar pruebas: {e}")


def detect_and_refactor_code():
    """Detecta y refactoriza código según el lenguaje utilizado."""
    detected_python = detected_java = False
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                detected_python = True
            elif file.endswith(".java"):
                detected_java = True

    if detected_python:
        refactor_python_code()
    if detected_java:
        refactor_java_code()


def git_create_branch(branch_name):
    """Crea una nueva rama Git o cambia a una existente."""
    try:
        result = subprocess.run(
            ["git", "branch", "--list", branch_name],
            capture_output=True,
            text=True,
            check=True,
        )
        if result.stdout.strip():
            print(f"La rama '{branch_name}' ya existe. Cambiando a ella...")
            subprocess.run(["git", "checkout", branch_name], check=True)
        else:
            subprocess.run(["git", "checkout", "-b", branch_name], check=True)
            print(f"Rama '{branch_name}' creada y cambiada a ella.")
    except subprocess.CalledProcessError as e:
        print(f"Error al gestionar ramas de Git: {e}")


def git_add_commit_push(message, branch="main"):
    """Añade, comitea y empuja los cambios a la rama especificada."""
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push", "-u", "origin", branch], check=True)
        print(f"Cambios comiteados y empujados a la rama '{branch}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al comitear o empujar cambios: {e}")


def git_status():
    """Muestra el estado actual del repositorio Git."""
    try:
        result = subprocess.run(
            ["git", "status"], capture_output=True, text=True, check=True
        )
        print((result.stdout))
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener el estado del repositorio Git: {e}")


def main():
    """Función principal que orquesta todas las operaciones."""
    if not check_git_repo():
        return

    check_required_files()
    git_create_branch("auto-update-and-refactor")

    update_dependencies()
    detect_and_refactor_code()
    run_tests()

    print("\nEstado del repositorio Git después de los cambios:")
    git_status()

    git_add_commit_push(
        "Auto update and refactor code to latest technologies",
        "auto-update-and-refactor",
    )

    print("Cambios realizados y empujados a la rama 'auto-update-and-refactor'.")


if __name__ == "__main__":
    main()
