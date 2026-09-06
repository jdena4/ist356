# write a sentinel controlled loop to input a color until quit
#add the color to a list and print the list each time
# do not add a color if its already in the list
colors = []
while True:
    color = input("Enter a color (or 'quit' to exit): ")
    if color == "quit":
        break
    if color not in colors:
        colors.append(color)
    print(f"You entered the color: {color}")
    print(f"The list of colors is: {colors}")