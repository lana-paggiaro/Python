people = [
    {"name": "Regina", "haircolor": "Blonde"},
    {"name": "Cady", "haircolor": "Ginger"},
    {"name": "Janis", "haircolor": "Black"},
]

def f(person):
    return person["name"]

people.sort(key=f)

# or people.sort(key=lambda person: person["name"])

print(people)