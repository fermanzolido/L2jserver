import os
import subprocess
import sys


def check_git_repo():
    if not os.path.isdir(".git"):
        print("Este directorio no parece ser un repositorio Git.")
        return False
    print("Repositorio Git encontrado.")
    return True


def check_required_files():
    required_files = ["README.md", ".gitignore"]
    for file in required_files:
        if not os.path.exists(file):
            print(f"Advertencia: {file} no encontrado. Creando {file}...")
            create_file(file)
        else:
            print(f"{file} encontrado.")


def create_file(filename):
    if filename == "README.md":
        with open(filename, "w") as f:
            f.write("# Proyecto\n\nDescripción del proyecto.")
    elif filename == ".gitignore":
        with open(filename, "w") as f:
            f.write("*.log\n*.pyc\n__pycache__/\nnode_modules/")


def update_dependencies():
    print("Actualizando dependencias...")
    # Aquí puedes actualizar el código específico según el gestor de dependencias:
    # Para Python (pip):
    if os.path.exists("requirements.txt"):
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--upgrade",
                "-r",
                "requirements.txt",
            ]
        )

    # Para Node.js (npm):
    if os.path.exists("package.json"):
        subprocess.run(["npm", "update"])

    # Para Ruby (Bundler):
    if os.path.exists("Gemfile"):
        subprocess.run(["bundle", "update"])


def refactor_code():
    print("Refactorizando y formateando el código...")

    # Formateo automático de código con black (Python)
    subprocess.run(["black", "."])

    # Análisis estático con flake8 para encontrar problemas comunes (Python)
    subprocess.run(["flake8", "."])


def run_tests():
    print("Ejecutando pruebas para asegurar que la funcionalidad se mantiene...")
    # Ejecutar pruebas unitarias
    if os.path.exists("tests"):
        subprocess.run(["pytest"])  # Para Python
    elif os.path.exists("spec"):
        subprocess.run(["rspec"])  # Para Ruby


def git_create_branch(branch_name):
    subprocess.run(["git", "checkout", "-b", branch_name])
    print(f"Rama {branch_name} creada y cambiada a ella.")


def git_add_commit_push(message, branch="main"):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push", "-u", "origin", branch])


def main():
    if not check_git_repo():
        return

    check_required_files()

    git_create_branch("auto-update-and-refactor")

    update_dependencies()
    refactor_code()
    run_tests()

    print("\nEstado del repositorio Git después de los cambios:")
    git_status()

    git_add_commit_push(
        "Auto update and refactor code to latest technologies",
        "auto-update-and-refactor",
    )

    print("Cambios realizados y empujados a la rama 'auto-update-and-refactor'.")


def git_status():
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    print(result.stdout)


if __name__ == "__main__":
    main()
