# How to modify global scope within local scope; DON'T NORMALLY DO THIS -> MORE PRONE TO BUGS SINCE AWAY FROM INITIAL DECLARATION
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(enemies)

increase_enemies()

# Instead something like this
enemies2 = 1
def increase_enemies2():
    enemies = 2
    return enemies

enemies2 = increase_enemies2()