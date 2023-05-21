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

def remove_friend(person, friend):
    person["friends"].remove(friend)

def total_money(people):
    tot_money = 0
    for person in people:
        tot_money += person["monies"]
    return tot_money
   
def lend_money(lender, lendee, loan_amount):
    lender["monies"] -= loan_amount
    lendee["monies"] += loan_amount

 #this is as far as we got   
def all_favourite_foods(people):
    favourite_foods = []
    for person in people:
        favourite_foods += (person["favourites"]["snacks"])
    return favourite_foods

def find_no_friends(people):
    no_friends = []
    for person in people:
        if len(person["friends"]) == 0:
            no_friends.append(person)
    return no_friends

def unique_favourite_tv_shows(people):
    favourite_shows = []
    for person in people:
        if person["favourites"]["tv_show"] not in favourite_shows:
            favourite_shows.append(person["favourites"]["tv_show"])
    return favourite_shows

    # monies = []
    # for money in bank:
    #     monies.append(money["monies"])
    #     money_total = sum(monies)

