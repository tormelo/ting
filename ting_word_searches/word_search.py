from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    word_lower = word.lower()

    results = []
    for i in range(len(instance)):
        file_data = instance.search(i)
        lines = file_data["linhas_do_arquivo"]

        occurrences = []
        for j in range(len(lines)):
            if word_lower in lines[j].lower():
                occurrences.append({"linha": j + 1})

        if len(occurrences):
            results.append(
                {
                    "palavra": word,
                    "arquivo": file_data["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
