##### The game screen




init:
    python:
        def cards_shuffle(x):
            renpy.random.shuffle(x)
            return x

    ##### Images
    image A = im.Scale("images/button/ARAMdo.png", 127, 203)         # different card images
    image B = im.Scale("images/button/Grotadebave.png", 127, 203)
    image C = im.Scale("images/button/Pikachu.png", 127, 203)          # back of the card

screen memo_scr:

    ##### Timer
    timer 0.1 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("win_jeu") ) repeat True

    text str(memo_timer) xalign 0.5 yalign 0.05


    ##### Cards
    #
    # To use images, just comment out lines that show text and uncomment lines that show images
    grid 3 4:
            area (0.35,0.15, 600, 720)
            for card in cards_list:
                button:
                    if card["c_chosen"]:        # shows the face of the card
                        #text card["c_value"]    # will show text
                        add card["c_value"]    # will show image

                    else:                       # shows the back of the card
                        #text "X"                # will show text
                        add "C"                # will show image

                    action If ( (card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )



label memoria_game:

    #####
    #
    # At first, let's set the cards to play (the amount should match the grid size - in this example 12)
    $ values_list = ["A", "A", "G" ,"G", "G", "C", "C", "E", "F", "B",  "B", "D"]

    $ trap_cards = ["D", "E", "F"]

    # Then - shuffle them
    $ values_list = cards_shuffle(values_list)

    # And make the cards_list that describes all the cards
    $ cards_list = []
    python:
        for i in range (0, len(values_list) ):
            cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":False} )

    # Before start the game, let's set the timer
    $ memo_timer = 50.0

    # Shows the game screen
    show screen memo_scr

    # The game loop
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []

        # Let's set the amount of cards that should be opened each turn (all of them should match to win)
        $ turns_left = 2

        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append (cards_list[result]["c_number"])
                $ turned_cards_values.append (cards_list[result]["c_value"])
                if cards_list[result]["c_value"] in trap_cards:  #<----- check for trap-cards
                    jump turns_done
                $ turns_left -= 1
                jump turns_loop

        label turns_done:
            # To prevent further clicking befor chosen cards will be processed
            $ can_click = False
            # If not all the opened cards are matched or only one trap-card opened, will turn them face down after pause
            if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values) or len(turned_cards_values) == 1:
                $ renpy.pause (1.0, hard = True)
                python:
                    for i in range (0, len(turned_cards_numbers) ):
                        cards_list[turned_cards_numbers[i]]["c_chosen"] = False

            # If cards are matched, will check if player has opened all the cards
            else:
                $ renpy.pause (1.0, hard = True)
                python:

                    # Let's remove opened cards from game field
                    # But if you prefere to let them stay - just comment out next 2 lines
                    for i in range (0, len(turned_cards_numbers) ):
                        cards_list[turned_cards_numbers[i]]["c_value"] = Null()


                    for j in cards_list:
                        if j["c_chosen"] == False:
                            renpy.jump ("win_jeu")
                    renpy.jump ("win_jeu")



            jump memo_game_loop
