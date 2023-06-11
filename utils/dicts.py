def get_val(collection, key, default='git'):
    """
    Извлекает из словаря значение по указанному ключу, если ключ существует.
    Если ключ не существует, возвращает значение по умолчанию.
    :param collection: исходный словарь.
    :param key: ключ извлекаемого элемента.
    :param default: значение по-умолчанию.
    :return: значение по ключу или значение по-умолчанию.
    """
    if key in collection.keys():
        return collection[key]
    else:
        return default