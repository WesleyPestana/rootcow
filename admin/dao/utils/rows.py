def row_to_dict(description, row) -> dict:
    dic = {}
    for i in range(0, len(row)):
        dic[description[i][0]] = row[i]

    return dic


def rows_to_dict(description, rows) -> list:
    lista = []
    for row in rows:
        lista.append(row_to_dict(description, row))
    
    return lista
