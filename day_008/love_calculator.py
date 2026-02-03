
def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    true_count = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + \
                 name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
    love_count = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") + \
                 name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
    love_score = int(str(true_count) + str(love_count))
    return love_score
    
print(calculate_love_score("Angela Yu", "Jack Bauer"))
print(calculate_love_score("Kanye West", "Kim Kardashian"))
