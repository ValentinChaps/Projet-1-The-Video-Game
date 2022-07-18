transform roto_transform (roto_var):
    # ATL transform that will rotate our displayables to "roto_var" degrees
    rotate roto_var
    rotate_pad False

screen Madao :

    timer 1 action [Return("runing"), If( game_timer >1, If( madao_hit >= goal_madao_hit, Return("win"), SetVariable("game_timer", game_timer-1) ), Return("lose") )] repeat [If(game_timer >2, Return(True)), Return(False)]
    text "Timer : [game_timer]" size 25 xpos 10 ypos 10
    text "Score : [madao_hit] / [goal_madao_hit]" size 25 xpos 10 ypos 50

    imagebutton :
        idle "images/button/gin_blase.png"
        hover "images/button/gin_venere.png"
        # Also it is neccessary to comment out the next  4 lines.
        xpos gin_e_x
        ypos gin_e_y
        action SetVariable("madao_hit", madao_hit-1 )
        activate_sound "audio/ouch.mp3"


    imagebutton :

        idle "images/button/gin_blase.png"
        hover "images/button/gin_etonne.png"

        # Also it is neccessary to comment out the next  4 lines.

        xpos gin_v_x
        ypos gin_v_y
        action SetVariable("madao_hit", madao_hit+1 )
        activate_sound "audio/ah.mp3"





label start_game_perso:
    play music "audio/gintama_jeu.mp3" volume 0.3

    $ madao_hit = 0
    $ game_timer = 30
    $ goal_madao_hit = 100
    $ gin_v_x = (renpy.random.randint(80, 1050))
    $ gin_v_y = (renpy.random.randint(56, 520))
    $ gin_e_x = (renpy.random.randint(80, 1050))
    $ gin_e_y = (renpy.random.randint(56, 520))

    "Attrapes les Gintony étonnés et évites les rageux."
    pause
    window hide
    show screen Madao

    label loop_perso:
        $ gin_v_x = (renpy.random.randint(80, 1050))
        $ gin_v_y = (renpy.random.randint(56, 520))
        $ gin_e_x = (renpy.random.randint(80, 1050))
        $ gin_e_y = (renpy.random.randint(56, 520))
        $ result = ui.interact()
        if result == "runing":
            jump loop_perso

    if result == "lose":
        hide screen Madao
        $ renpy.pause (1.0, hard = True)
        stop music fadeout 1
        jump win_jeu

        return

    if result == "win":
        hide screen Madao
        $ renpy.pause (0.1, hard = True)
        $ renpy.pause (0.1, hard = True)
        $ renpy.pause (0.1, hard = True)
        $ renpy.pause (0.1, hard = True)
        "You win!"
        jump start_game_perso
        return
