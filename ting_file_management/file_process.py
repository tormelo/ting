from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    lines = txt_importer(path_file)

    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    data_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(data_dict)

    print(data_dict, file=sys.stdout)


def remove(instance: Queue):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        data = instance.dequeue()
        print(
            f"Arquivo {data['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout,
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
