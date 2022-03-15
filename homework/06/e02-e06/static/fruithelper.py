import random
def generate_fruit():
    random_fruit = random.randint(0, 3)
    if random_fruit == 1:
        return '<img src="lemon.png" width="200px" height="200px">'
    elif random_fruit == 2:
        return """<img src="orange.png" width="200px" height="200px">"""
    elif random_fruit == 3:
        return """<img src="pineapple.png" width="200px" height="200px">"""