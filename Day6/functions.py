# Regular function
def my_function():
    print("Hello")
    print("Bye")

my_function()

# Function with parameters
def my_function_w_params(number):
    print(number)

my_function_w_params(6)

# # Reeborg function practice
# def move():
#     print("Moved forward")

# def turn_left():
#     print("Turned left")

# def turn_270_degrees():
#     turn_left()
#     turn_left()
#     turn_left()

# def over_one_hurdle():
#     move()
#     turn_left()
#     move()
#     turn_270_degrees()
#     move()
#     turn_270_degrees()
#     move()
#     turn_left()

# over_one_hurdle()
# over_one_hurdle()
# over_one_hurdle()
# over_one_hurdle()
# over_one_hurdle()
# over_one_hurdle()

# # Alternate solution for Reeborg using while loops
# def turn_270_degrees():
#     turn_left()
#     turn_left()
#     turn_left()

# def short_hop():
#     turn_left()
#     move()
#     turn_270_degrees()
#     move()
#     turn_270_degrees()
#     move()
#     turn_left()

# def at_goal():
#     print("Reeborg has arrived")

# def wall_in_front():
#     print("There is a wall here")

# while not at_goal():
#     if wall_in_front():
#         short_hop()
#     else:
#         move()

# # Of course, another alternative if the height of the hurdles are variable
# def turn_270_degrees():
#     turn_left()
#     turn_left()
#     turn_left()

# def short_hop():
#     turn_left()
#     move()
#     turn_270_degrees()
#     move()
#     turn_270_degrees()
#     move()
#     turn_left()

# def wall_on_right():
#     print("There is a wall on the right")

# while not at_goal():
#     if not wall_on_right():
#         turn_270_degrees()
#         move()
#     elif wall_in_front():
#         turn_left()
#     elif wall_on_right() and not wall_in_front():
#         move()
#     else:
#         turn_270_degrees()
#         move()

# # Code to get Reeborg through randomly generated maze
# def turn_270_degrees():
#     turn_left()
#     turn_left()
#     turn_left()

# moved_left = False
# while not at_goal():
#     if not wall_on_right():
#         turn_270_degrees()
#         move()
#     elif not wall_in_front():
#         move()
#     elif is_facing_north() and right_is_clear():
#         turn_270_degrees()
#         move()
#     else: 
#         turn_left()
    