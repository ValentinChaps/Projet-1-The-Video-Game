screen toilette_map :

    imagemap:
        idle "images/BG/toilette.png"
        hover "images/BG/toilette_hover.png"

        hotspot (457, 445, 61, 92) clicked Jump("bouteille")
        ##hotspot (700, 363, 46, 72) clicked Jump("bouteille")
        #hotspot (908, 599, 74, 81) clicked Jump("bouteille")

        hotspot (657, 426, 306, 193) clicked Jump("cuvette")
        hotspot (196, 576, 179, 112) clicked Jump("revue")
        hotspot (1062, 340, 45, 38) clicked Jump("bouton")

label bouteille:
    scene toilette
    play sound "audio/pot.mp3"
    je "Oh tiens du jus d'orange !"
    call screen toilette_map
label cuvette:
    scene toilette
    je "J'ai pas envie de pisser alors que tout le monde regarde."
    call screen toilette_map
label revue:
    scene toilette
    je "Hummmm, faudrait que je le lise un jour."
    call screen toilette_map
label bouton:
    scene toilette
    je "Cette chasse me semble bizarre."
    je "{size=+10}AHHHHHHHHHHHHHH !!!!!!!"
    jump arc_final
