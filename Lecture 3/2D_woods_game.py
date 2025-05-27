# initialize the backgrounds 
wood_background = "Woods"
exit_background = "Exit"
background = wood_background

while (background == wood_background) : 
    background = input ("Enter the direction to go(Right or Left):").strip()
    if background.capitalize() == "Right" :
        background = wood_background
        print("trapped in the woods")
    elif background.capitalize() == "Left":
        background = exit_background
    else :
        print("Invalid direction. Please enter Right or Left.")
        background = wood_background
else :
    print("you successfully escaped from the woods")
