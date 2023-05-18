def get_name(person):
    name = person["name"]
    return name

def get_favourite_tv_show(person):
    tv_show = person["favourites"]["tv_show"]
    return tv_show

def likes_to_eat(person, food):
    if food in person["favourites"]["snacks"]:
        return True
    else:
        return False
    
def add_friend(person, friend):
    person["friends"].append(friend)



