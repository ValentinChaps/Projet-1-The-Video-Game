define r = Character('Moi', color="#B5B5B5")
define w = Character('Aurelius Maximus Aramus Couthurus', color="#CD0000")#CD0000

screen simple_stats_screen:
    frame:
        xalign 0.01 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Moi" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value jeremy_hp
                    range jeremy_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[jeremy_hp] / [jeremy_max_hp]" size 16


    frame:
        xalign 0.99 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Aurelius Maximus Aramus Couthurus" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value boss_hp
                    range boss_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[boss_hp] / [boss_max_hp]" size 16



# The game starts here.
label combat:
    #### Some variables that describes the game state.
    $ boss_max_hp = 30
    $ jeremy_max_hp = 50
    $ boss_hp = boss_max_hp
    $ jeremy_hp = jeremy_max_hp
    $ heal_left = 10

    scene bg boss with circleirisout


    jump battle_1_loop


label battle_1_loop:

    #### Let's show the game screen.
    #
    show screen simple_stats_screen

    #### The game loop.
    # It will exist till both enemies have more than 0 hp.
    #
    while (boss_hp > 0) and (jeremy_hp > 0):

        menu:
            "Raquette Justu":
                $ boss_hp -= 2
                play sound "audio/smashp.mp3"
                w "Tu crois que tu vas m'avoir avec des raquettes de ping pong alors que je peux lancer des boules d'énergies ?{vspace=30}(Il a pris 3hp en moins dans sa bouche)"

            "Boire un parfait au concerta (Il te reste [heal_left] parfaits.)" if heal_left > 0:
                play sound "audio/pot.mp3"
                $ jeremy_hp = min(jeremy_hp+5, jeremy_max_hp)
                $ heal_left -= 1
                r "Allez c'est reparti ! {vspace=30}(4hp en plus ça fait plaisir !)"

            "Avada Kedajean !":
                $ boss_hp -= 3
                play sound "audio/avada.mp3"
                w"Tu crois pourvoir me faire mal avec ton morceau de bois la ?{vspace=30}(Il a pris 3hp en moins dans sa bouche)"

            "F=ma":
                $ boss_hp -= 3
                $ renpy.movie_cutscene("revisions.webm")
                w"Ah mais ta gueule putain ! Tout le monde sait que la force c'est le produit de la masse par l'accelération.{vspace=30}(Il a pris 3hp en moins dans sa bouche)"



        $ boss_damage = renpy.random.randint(1, 6)

        $ jeremy_hp -= boss_damage

        $ boss_attack = renpy.random.randint(1,4)

        if boss_attack == 1:
            w"{i}*Aurelius vous prend de très très haut.*{/i}"
            w"Je n'ai même pas besoin de te toucher pour te blesser. Ma supériorité suffit.{vspace=30}(Merde j'ai pris [boss_damage]hp en moins)"

        if boss_attack == 2:
            play sound "audio/aram.mp3"
            w"Attaque du marathon de l'ARAM (C'est pas 42km mais 42h).{vspace=30}(Merde j'ai pris [boss_damage]hp en moins)"

        if boss_attack == 3:
            play sound link
            w"OOOOORILLAAAAAAAAAAA{vspace=30}(Merde j'ai pris [boss_damage]hp en moins)"

        if boss_attack == 4:
            play sound "audio/service.mp3"
            w"Service coupé.{vspace=30}(Merde j'ai pris [boss_damage]hp en moins)"
    #
    ####

    hide screen simple_stats_screen

    if boss_hp <= 0:
        if jeremy_hp <= 0:
            "AH merde on avait pas prévu ça... Bah j'imgagine que tu vas devoir refaire le jeu."
            jump introduction

        else:

            play music "audio/ff.mp3"
            r "No rage de ta supériorité inférieure."
            r "Bon... J'espère que la docteure va faire son taf. Je vais te renvoyer avec les Jean de ton niveau car je suis un être charitable. Profite bien."
            #$ renpy.movie_cutscene("revisions.webm")

    else:
        voice "audio/ok.mp3"
        w "No lage de ta lose."

        label boucle:
            scene bg juetc
            play music "audio/jean-petit-danse.mp3" volume 0.08
            voice "audio/14.mp3"
            ka "Tu crois que le bifidus ça peut mettre des bactéries dans le ventre pour maigrir ?"
            voice "audio/15.mp3"
            pe "Dans ton intestin t'as vraiment des bactéries ?"
            voice "audio/16.mp3"
            ka "Même moi des fois je comprend pas ce que je dis alors me pose pas la question."
            voice "audio/17.mp3"
            pe "Parfois je commence à comprendre la conversation puis après je comprend plus. Je comprend puis la seconde d'après je comprend plus rien c'est bizarre."
            voice "audio/18.mp3"
            ka "Même moi des fois je comprend pas ce que je dis alors ta gueule. Me pose pas la question et arrête de te foutre de ta gueule."
            voice "audio/19.mp3"
            pe "Moi je me fous de ma propre gueule ?! Toi ta gueule !"
            voice "audio/20.mp3"
            ka "Redis moi ta gueule encore une fois et tu vas voir ce que tu vas voir !"
            voice "audio/21.mp3"
            pe "J’y verrais rien je suis myope."
            voice "audio/22.mp3"
            ka "C’est pas faux."
            voice "audio/23.mp3"
            pe "De toute façon vous êtes tous des cons."
            voice "audio/24.mp3"
            ka "Tu connais l'histoire du yaourt Activia ?"
            voice "audio/25.mp3"
            pe "OUIIII J'ADOREEEEE !!!!!!"
            menu:
                "C'est quoi l'histoire du yaourt ?":
                            jump choice10_yaourt

                "*Ne rien dire":
                    jump choice10_riendire

            label choice10_yaourt:
                    $ menu_flag = True
                    voice "audio/14.mp3"
                    ka "Tu crois que le bifidus ça peut mettre des bactéries dans le ventre pour maigrir ?"
                    voice "audio/15.mp3"
                    pe "Dans ton intestin t'as vraiment des bactéries ?"
                    voice "audio/16.mp3"
                    ka "Même moi des fois je comprend pas ce que je dis alors me pose pas la question."
                    voice "audio/17.mp3"
                    pe "Parfois je commence à comprendre la conversation puis après je comprend plus. Je comprend puis la seconde d'après je comprend plus rien c'est bizarre."
                    voice "audio/18.mp3"
                    ka "Même moi des fois je comprend pas ce que je dis alors ta gueule. Me pose pas la question et arrête de te foutre de ta gueule."
                    voice "audio/19.mp3"
                    pe "Moi je me fous de ma propre gueule ?! Toi ta gueule !"
                    voice "audio/20.mp3"
                    ka "Redis moi ta gueule encore une fois et tu vas voir ce que tu vas voir !"
                    voice "audio/21.mp3"
                    pe "J’y verrais rien je suis myope."
                    voice "audio/22.mp3"
                    ka "C’est pas faux."
                    voice "audio/23.mp3"
                    pe "De toute façon vous êtes tous des cons."
                    voice "audio/24.mp3"
                    ka "Tu connais l'histoire du yaourt Activia ?"
                    voice "audio/25.mp3"
                    pe "OUIIII J'ADOREEEEE !!!!!!"

                    jump boucle

            label choice10_riendire:
                    $ menu_flag = True
                    voice "audio/14.mp3"
                    ka "Tu crois que le bifidus ça peut mettre des bactéries dans le ventre pour maigrir ?"
                    voice "audio/15.mp3"
                    pe "Dans ton intestin t'as vraiment des bactéries ?"
                    voice "audio/16.mp3"
                    ka "Même moi des fois je comprend pas ce que je dis alors me pose pas la question."
                    voice "audio/17.mp3"
                    pe "Parfois je commence à comprendre la conversation puis après je comprend plus. Je comprend puis la seconde d'après je comprend plus rien c'est bizarre."
                    voice "audio/18.mp3"
                    ka "Même moi des fois je comprend pas ce que je dis alors ta gueule. Me pose pas la question et arrête de te foutre de ta gueule."
                    voice "audio/19.mp3"
                    pe "Moi je me fous de ma propre gueule ?! Toi ta gueule !"
                    voice "audio/20.mp3"
                    ka "Redis moi ta gueule encore une fois et tu vas voir ce que tu vas voir !"
                    voice "audio/21.mp3"
                    pe "J’y verrais rien je suis myope."
                    voice "audio/22.mp3"
                    ka "C’est pas faux."
                    voice "audio/23.mp3"
                    pe "De toute façon vous êtes tous des cons."
                    voice "audio/24.mp3"
                    ka "Tu connais l'histoire du yaourt Activia ?"
                    voice "audio/25.mp3"
                    pe "OUIIII J'ADOREEEEE !!!!!!"

                    jump boucle

    jump battle_1_ending

label battle_1_ending:
    scen "The end."
    scen "Ah oui j'ai failli oublié !"
    scen "Bon anniversaire !"
    return
