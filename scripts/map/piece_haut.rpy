screen piece_haut_map :

    imagemap:
        if Bool_chambre and Bool_piece_du_fond and Bool_imprimante and Bool_lampe :
            idle "images/BG/piece_haut_robot.png"
            hover "images/BG/piece_haut_robot_hover.png"

            hotspot (601, 207, 105, 274) clicked Jump("robot")
        else :
            idle "images/BG/piece_haut.png"
            hover "images/BG/piece_haut_hover.png"

        hotspot (895, 330, 84, 88) clicked Jump("imprimante")
        hotspot (785, 267, 74, 46) clicked Jump("lampe")
        hotspot (219, 186, 217, 284) clicked Jump("piece_du_fond")

        hotspot (72, 138, 156, 468) clicked Jump("chambre")

        hotspot (698, 533, 380, 186) clicked Jump("boite_vis")

label boite_vis:
    if Bool_chambre and Bool_piece_du_fond and Bool_imprimante and Bool_lampe :
        scene bg piece_haut_robot
    else :
        scene bg piece_haut
    $ Bool_chambre = True
    je "Les vis là dedans sont toutes mélangées..."
    call screen piece_haut_map

label chambre:
    if Bool_chambre and Bool_piece_du_fond and Bool_imprimante and Bool_lampe :
        scene bg piece_haut_robot
    else :
        scene bg piece_haut
    $ Bool_chambre = True
    je "Bah c'est ma chambre... Je me demande si je pourrais la voir dans ce jeux à 2 balles."
    call screen piece_haut_map
label piece_du_fond:
    if Bool_chambre and Bool_piece_du_fond and Bool_imprimante and Bool_lampe :
        scene bg piece_haut_robot
    else :
        scene bg piece_haut
    $ Bool_piece_du_fond = True
    je "C'est pas assez ranger pour que je puisse y aller."
    call screen piece_haut_map

label imprimante:
    if Bool_chambre and Bool_piece_du_fond and Bool_imprimante and Bool_lampe :
        scene bg piece_haut_robot
    else :
        scene bg piece_haut
    $ Bool_imprimante = True

    je "J'ai rien imprimer en 3D depuis un moment, je devrais essayer de trouver un prototype de TARDIS en .stl"
    call screen piece_haut_map

label lampe:
    if Bool_chambre and Bool_piece_du_fond and Bool_imprimante and Bool_lampe :
        scene bg piece_haut_robot
    else :
        scene bg piece_haut
    $ Bool_lampe = True

    je "C'est la lampe que Anthony m'as piqué ..."
    call screen piece_haut_map

label robot:
    scene piece_haut_robot
    je "Ce truc me rappelle de bon souvenir de quand j'était à la fac de sciences !"
    jump chapitre_2
