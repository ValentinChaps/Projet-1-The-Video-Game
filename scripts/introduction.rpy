label introduction:
    voice "audio/1.mp3"
    un "PUTAIN !!! MERDE, Encore une ranked de perdue fais CHIE... !!! ATTENDS !!!! C'est à moi là ? !?"
    voice "audio/2.mp3"
    scene bg white with dissolve
    show prof at center with moveinleft
    play music "audio/pokemon.mp3" volume 0.3
    voice "audio/2.mp3"
    pr"Bien le bonjour !! Bienvenue dans le monde des Pokejean. Mon nom est {s}CHEN{/s} {color=#0080c0}{b}'Narrateur 1'{/b}{/color}. Mais les gens m'appelent le prof {color=#0080c0}{b}'Narrateur 1'{/b}{/color}."
    voice "audio/3.mp3"
    pr"Ce monde est peuplé de créatures du nom de Pokéjean ! Pour certains, ce sont des animaux domestiques, pour d'autres, ils sont un moyen de troller. Pour ma part, l’étude des Pokéjean est ma profession."

    python:
        renpy.play("audio/4.mp3")
        pr("Tout d’abord, quel est ton nom ?")

        name = renpy.input("Rentre ton nom ici :")
        name = name.strip()
        if (name == "jean") or (name == "Jean") or (name == "JEAN") :
            renpy.play("audio/6.mp3")
            pr("Félicitations Jean ! Tu viens de finir le ‘Projet numéro 1’. J’espère que ce jeu t’aura plus.")
            renpy.movie_cutscene("video/fake_ending.webm")
            renpy.jump("generic_fin_troll")
        if name == ""  :
            renpy.play("audio/7.mp3")
            pr("Wow, j’aurais jamais cru rencontrer quelqu’un avec aussi peu de personnalité. Mais c’est ton jour de chance ! Ce jeu en a autant que toi.")
        else :
            renpy.play("audio/5.mp3")
            pr("Ahahahaha !!!! Quel nom de merde ! T’as pas honte de t’appeler comme ça ? Tu sais quoi je vais t’appeler Jean Neutron, ça te va mieux quand même.")


    voice "audio/8.mp3"
    pr"Bon, il est temps de choisir ton Pokejean."

    $ N=0
    call screen pokemon with wiperight

label suite_pokemon:
    $ N = N+1

    if N<3:

        voice "audio/9.mp3"
        pr"Oh je vois tu as choisi Pikachu ! Très bon choix."
        voice "audio/intro1.mp3"
        pr"Ah mais il semblerait qu'il ne veuille pas de toi..."
        voice "audio/intro2.mp3"
        pr"Essayes de choisir un autre Pokéjean."

        call screen pokemon with wiperight

    voice "audio/10.mp3"
    pr"AH AH ! T’as cru que c’était un jeu Pokémon ? MDR ! Je te pensais plus intelligent que ça... Enfin bon, voici le VRAI jeu. Je te présente donc:"
    scene arc1
    $ renpy.movie_cutscene("video/trailer.webm")

    play music "audio/ameno.mp3" volume 0.5

    jei"Vite ! Je dois le trouver avant qu’il soit trop tard."



jump chapitre_1
