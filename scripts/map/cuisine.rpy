screen cuisine_map :

    imagemap:
        if Bool_vaisselle :
            idle "images/BG/cuisine_pong.png"
            hover "images/BG/cuisine_pong_hover.png"

            hotspot (578, 358, 63, 57) clicked Jump("raquette")
        else :
            idle "images/BG/cuisine.png"
            hover "images/BG/cuisine_hover.png"
        if Bool_machine_ouverte and (Bool_vaisselle==False) :
            hotspot (914, 457, 154, 34) clicked Jump("assiettes_1")
            hotspot (298, 465, 200, 83) clicked Jump("assiettes_2")
            hotspot (736, 284, 108, 65) clicked Jump("casserole")
            hotspot (850, 337, 94, 100) clicked Jump("couverts")
        hotspot (645, 376, 186, 233) clicked Jump("lave_vaisselle")



label couverts:
    if Bool_vaisselle :
        scene bg cuisine_pong
    else :
        scene bg cuisine
    $ Bool_4 = True
    je "J'ai failli oublier les couverts."
    call screen cuisine_map

label assiettes_1:
    if Bool_vaisselle :
        scene bg cuisine_pong
    else :
        scene bg cuisine
    $ Bool_1 = True
    je "Je sais pas de quand date cette assiette."
    call screen cuisine_map

label assiettes_2:
    if Bool_vaisselle :
        scene bg cuisine_pong
    else :
        scene bg cuisine
    $ Bool_2 = True
    je "C'est Aurelien qui a du les mettre ici... "
    call screen cuisine_map

label casserole:
    if Bool_vaisselle :
        scene bg cuisine_pong
    else :
        scene bg cuisine
    $ Bool_3 = True
    je "Je vais mettre ces casserole pour les laver."
    call screen cuisine_map

label lave_vaisselle:
    if Bool_vaisselle :
        scene bg cuisine_pong
    else :
        scene bg cuisine
    if Bool_1 and Bool_2 and Bool_3 and Bool_4 :
        $ Bool_vaisselle = True
        je "La machine est remplie mais je ne sais pas la lancer... Je vais attendre que quelqu'un le fasse pour moi."
    elif Bool_1 or Bool_2 or Bool_3 :
        je "Il reste de la place, je vais mettre d'autres choses dedans."
    else :
        $ Bool_machine_ouverte = True
        je "La machine est sale, je vais la remplir."

    call screen cuisine_map

label raquette:
    if Bool_vaisselle :
        scene bg cuisine_pong
    else :
        scene bg cuisine
    $ Bool_raquette = True

    je "L'époque des Jeans me manque."
    jump chapitre_4
