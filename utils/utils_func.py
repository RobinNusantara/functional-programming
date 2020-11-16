def printDictInsideList(dictList):
    for dictItem in dictList:
        for key in dictItem:
            print(f'{key} : {dictItem.get(key)}')
        print('-----')
    return dictList
    