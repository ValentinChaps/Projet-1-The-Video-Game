transform roto_transform (roto_var):
    # ATL transform that will rotate our displayables to "roto_var" degrees
    rotate roto_var
    rotate_pad False

##### The game screen
screen numbers_scr:

    ##### Timer
    #
    # It returns "smth" every second and "win" (if all buttons were clicked) or "lose" (if time was up)
    timer 200 action [Return("smth"), If( game_timer>1, If( numbers_buttons[-1]["b_to_show"] == False, Return("win"), SetVariable("game_timer", game_timer-1) ), Return("lose") ) ] repeat True
    text "[game_timer]" size 25 xpos 10 ypos 10


    for each_b in sorted(numbers_buttons, reverse=True):
        if each_b["b_to_show"]:
            $ text_var = each_b["b_value"]
            $ i = each_b["b_number"] - 1
            button:

                # Will show image if "b_value" was set as file name or displayable.
                background None
                add each_b["b_value"]
                # Also it is neccessary to comment out the next  4 lines.


                xminimum 100 xmaximum 100
                yminimum 100 ymaximum 100
                xpos each_b["b_x_pos"]
                ypos each_b["b_y_pos"]
                anchor (0.5, 0.5)
                action If (i == -1, SetDict(numbers_buttons[each_b["b_number"] ], "b_to_show", False),
                    If (numbers_buttons[i]["b_to_show"] == False,
                        SetDict(numbers_buttons[each_b["b_number"] ], "b_to_show", False),
                        SetVariable("game_timer", game_timer-1) )  )          # Wrong click reduces the time left by 1 second
                at roto_transform (renpy.random.randint (0, 10)*36)



    # It might be usefull to show the order of buttons to click if it's not obvious.
    side "c b":
        area (150, 05, 640, 70)         # The size of hint's area

        viewport id "vp":
            draggable False

            hbox:
                xalign 1.0

                # The same buttons declaration, but they will be scaled down
                for each_b in numbers_buttons:
                    $ text_var = each_b["b_value"]

                    button:

                        # Will show image if "b_value" was set as file name or displayable.
                        background None
                        add each_b["b_value"]
                        # Also it is neccessary to comment out the next  4 lines.

                        #background "image.png"          # Sets button's appearance
                        xminimum 100 xmaximum 100
                        yminimum 100 ymaximum 100
                        action If (each_b["b_to_show"], Hide("nonexistent_screen"), None)
                        at Transform(zoom=0.5)           # Size

        bar value XScrollValue("vp")




label start_game:

    #####
    #
    # At first, let's set the values for buttons
    $ numbers_buttons = []
    $ buttons_values = ["images/button/Pikachu.png", "images/button/Grotadebave.png", "images/button/Grotadebave.png"]

    # This might be numbers,
    #python:
    #    for i in range (1, renpy.random.randint (10, 15) ):
    #       buttons_values.append (str(i) )

    # or letters,
    #$ buttons_values = [u"а", u"б", u"в", u"г", u"д", u"е", u"ё", u"ж", u"з", u"и", u"й", u"к", u"л", u"м", u"н", u"о", u"п", u"р", u"с", u"т", u"у", u"ф", u"х", u"ц", u"ч", u"ш", u"щ", u"ъ", u"ы", u"ь", u"э", u"ю", u"я" ]

    #or images,


    # This will make the description for all buttons (numbers, values and positions)


    python:
        for i in range (0, len(buttons_values) ):
            numbers_buttons.append ( {"b_number":i, "b_value":buttons_values[i], "b_x_pos":(renpy.random.randint (10, 70))*10, "b_y_pos":(renpy.random.randint (15, 50))*10, "b_to_show":True} )

    "To win the game - click all the buttons one after another (start from \"1\")."

    # Before start the game, let's set the timer
    $ game_timer = 20

    # Shows the game screen
    show screen numbers_scr

    # The loop will exist untill game screen returns win or lose
    label loop:
        $ result = ui.interact()
        $ game_timer = game_timer
        if result == "smth":
            jump loop

    if result == "lose":
        hide screen numbers_scr
        $ renpy.pause (0.1, hard = True)
        $ renpy.pause (0.1, hard = True)
        $ renpy.pause (0.1, hard = True)
        $ renpy.pause (0.1, hard = True)
        "You lose! Try again."
        jump numbers_game

    if result == "win":
        hide screen numbers_scr
        $ renpy.pause (0.1, hard = True)
        $ renpy.pause (0.1, hard = True)
        $ renpy.pause (0.1, hard = True)
        $ renpy.pause (0.1, hard = True)
        "You win!"
        return
