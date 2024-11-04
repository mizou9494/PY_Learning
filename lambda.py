people = [
    {"name": "harry", "house": "Gryffindor"},
    {"name": "draco", "house": "Slytherin"},
    {"name": "cho", "house": "Ravenclaw"}
]

# it will return the value correspondant to the value given inside the brackets []
def f(person):
    return person["house"]

# people.sort(key=f)
# this is the shorthand version of the function above
# it will sort the people dictionary ascendently based on parameter passed inside the brackets []
people.sort(key=lambda person: person['house'])
print(people)