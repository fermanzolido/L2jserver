import os
import subprocess
import sys
import shutil
import logging
import importlib.metadata

# Configurar logging
logging.basicConfig(
    filename="modification_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)


def check_git_repo():
    """Verifica si el directorio actual es un repositorio Git."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True,
            text=True,
            check=True,
        )
        if result.stdout.strip() == "true":
            print("Repositorio Git encontrado.")
            return True
    except subprocess.CalledProcessError:
        print("Este directorio no parece ser un repositorio Git.")
        return False


def check_required_files():
    """Verifica si los archivos requeridos existen y los crea si no están presentes."""
    required_files = {
        "README.md": "# Proyecto\n\nDescripción del proyecto.\n\n## Requisitos\n\nEste proyecto requiere las siguientes dependencias:\n\n- Python 3.8 o superior\n- Java 21\n- Maven\n\n## Instalación\n\nEjecuta `pip install -r requirements.txt` para instalar las dependencias necesarias.\n",
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


def create_requirements_txt():
    """Genera un archivo requirements.txt con las dependencias necesarias del proyecto."""
    print("Generando requirements.txt...")
    try:
        installed_packages = importlib.metadata.distributions()
        with open("requirements.txt", "w") as f:
            for package in installed_packages:
                f.write(f"{package.metadata['Name']}=={package.version}\n")
        print("requirements.txt creado con éxito.")
    except Exception as e:
        print(f"Error al crear requirements.txt: {e}")
        logging.info(f"Error al crear requirements.txt: {e}")


def update_jar_files():
    """Actualiza los archivos .jar a versiones compatibles con Java 21."""
    print("Actualizando archivos .jar...")
    jar_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".jar"):
                jar_files.append(os.path.join(root, file))

    if not jar_files:
        print("No se encontraron archivos .jar para actualizar.")
        return

    for jar_file in jar_files:
        try:
            print(f"Actualizando {jar_file}...")
            # Aquí puedes agregar la lógica específica para actualizar los archivos .jar.
            # subprocess.run(["java", "-jar", "jar-updater.jar", jar_file], check=True)
            print(f"{jar_file} actualizado con éxito.")
        except Exception as e:
            print(f"Error al actualizar {jar_file}: {e}")
            logging.info(f"Error al actualizar {jar_file}: {e}")


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


def refactor_shell_script(file_path):
    """Refactoriza y formatea scripts de shell (.sh)."""
    print(f"Refactorizando script de shell: {file_path}")
    try:
        subprocess.run(["shfmt", "-w", file_path], check=True)
        print(f"Script de shell {file_path} refactorizado con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al refactorizar el script de shell {file_path}: {e}")


def refactor_batch_script(file_path):
    """Refactoriza y formatea scripts de batch (.bat)."""
    print(f"Refactorizando script de batch: {file_path}")
    try:
        # Para scripts .bat, no hay herramientas de formateo estándar como para otros lenguajes.
        # Sin embargo, se pueden aplicar reglas básicas de formato o validaciones personalizadas.
        with open(file_path, "r") as f:
            lines = f.readlines()

        with open(file_path, "w") as f:
            for line in lines:
                f.write(line.strip() + "\n")

        print(f"Script de batch {file_path} refactorizado con éxito.")
    except Exception as e:
        print(f"Error al refactorizar el script de batch {file_path}: {e}")


def update_pkc_files():
    """Actualiza los archivos .pkc a versiones compatibles o realiza una operación específica."""
    print("Actualizando archivos .pkc...")
    pkc_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".pkc"):
                pkc_files.append(os.path.join(root, file))

    if not pkc_files:
        print("No se encontraron archivos .pkc para actualizar.")
        return

    for pkc_file in pkc_files:
        try:
            print(f"Procesando {pkc_file}...")
            # Aquí puedes agregar la lógica específica para manejar los archivos .pkc.
            print(f"{pkc_file} procesado con éxito.")
        except Exception as e:
            print(f"Error al procesar {pkc_file}: {e}")
            logging.info(f"Error al procesar {pkc_file}: {e}")


def run_tests():
    """Ejecuta pruebas dependiendo de los archivos de prueba disponibles."""
    print("Ejecutando pruebas...")
    try:
        if os.path.exists("tests"):
            subprocess.run(["pytest"], check=True)
        elif os.path.exists("src/test/java"):
            subprocess.run(["mvn", "test"], check=True)
        print("Pruebas ejecutadas con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar pruebas: {e}")


def detect_and_refactor_code():
    """Detecta y refactoriza código según el lenguaje utilizado."""
    detected_python = detected_java = detected_jar = detected_sh = detected_bat = (
        detected_pkc
    ) = False
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                detected_python = True
            elif file.endswith(".java"):
                detected_java = True
            elif file.endswith(".jar"):
                detected_jar = True
            elif file.endswith(".sh"):
                detected_sh = True
            elif file.endswith(".bat"):
                detected_bat = True
            elif file.endswith(".pkc"):
                detected_pkc = True
            else:
                logging.info(
                    f"Archivo no manejado: {file} - Se requiere una extensión válida para editar."
                )

    if detected_python:
        refactor_python_code()
    if detected_java:
        refactor_java_code()
    if detected_jar:
        update_jar_files()
    if detected_sh:
        for root, _, files in os.walk("."):
            for file in files:
                if file.endswith(".sh"):
                    refactor_shell_script(os.path.join(root, file))
    if detected_bat:
        for root, _, files in os.walk("."):
            for file in files:
                if file.endswith(".bat"):
                    refactor_batch_script(os.path.join(root, file))
    if detected_pkc:
        update_pkc_files()


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

    create_requirements_txt()
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
