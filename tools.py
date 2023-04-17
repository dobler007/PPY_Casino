
def remove_odds(lists):

    new = []
    for i in range(len(lists)):
        if(lists[i]%2!=0):
            new.append(lists[i])
        else:
            continue

    return new



