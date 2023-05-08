from ting_file_management.queue import Queue


def get_occurrences(word, lines, include_content):
    occurrences = []
    for i in range(len(lines)):
        if word.lower() in lines[i].lower():
            occurrence = {"linha": i + 1}
            if include_content:
                occurrence["conteudo"] = lines[i]
            occurrences.append(occurrence)
    return occurrences


def get_occurences_in_files(word, instance, include_content=False):
    results = []
    for i in range(len(instance)):
        file_data = instance.search(i)
        lines = file_data["linhas_do_arquivo"]

        occurrences = get_occurrences(word, lines, include_content)

        if len(occurrences):
            results.append(
                {
                    "palavra": word,
                    "arquivo": file_data["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return results


def exists_word(word, instance: Queue):
    return get_occurences_in_files(word, instance)


def search_by_word(word, instance):
    return get_occurences_in_files(word, instance, True)
