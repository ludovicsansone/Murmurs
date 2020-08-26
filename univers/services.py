import datetime

def getAge(bornDate):
    diff = datetime.date.today() - bornDate
    days = diff.__getattribute__('days')
    age = int(days / 365)
    return age

def artisticTastesIsEmpty(univers):
    if "" in [univers.livrePrefere, univers.filmPrefere, univers.chansonPreferee]:
        return True
    else:
        return False

