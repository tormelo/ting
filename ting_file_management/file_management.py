import sys


def txt_importer(path_file):
    if ".txt" not in path_file:
        print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file, "r") as my_file:
            return my_file.read().split("\n")
    except OSError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
