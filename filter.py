import database
def cleanFilter(filter, template):

    for key in template.keys():#Creates key-value pairs for non declared keys. Makes sure in the worst case all variables is None
        try:
            template[key] = filter[key]
        except:
            continue

    return template

def executeStatement(statement):
    session = database.Session(database.engine, future=True)

    result = session.execute(statement).scalars().all()

    return result

def encode_to_json(objects):
    lst = []
    for obj in objects:
        lst.append(obj.to_dict())
    return lst

