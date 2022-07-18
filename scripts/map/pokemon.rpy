screen pokemon:

    imagemap:
        idle "table1"
        hover "table1"

        imagebutton:
            idle "button/ARAMdo.png"
            hover "button/Pikachu.png"
            xalign 0.50
            yalign 0.43
            action Jump("suite_pokemon") # Si aucune action n'est déclaré le bouton n'apparaitra pas avec la souris en surbrillance

        imagebutton:
            idle "button/Grotadebave.png"
            hover "button/Pikachu.png"
            xalign 0.20
            yalign 0.40
            action Jump("suite_pokemon") # Si aucune action n'est déclaré le bouton n'apparaitra pas avec la souris en surbrillance

        imagebutton:
            idle "button/Machopierre.png"
            hover "button/Pikachu.png"
            xalign 0.80
            yalign 0.38
            action Jump("suite_pokemon") # Si aucune action n'est déclaré le bouton n'apparaitra pas avec la souris en surbrillance



        text "{color=#000000}Grotadebave{/color}":
            size 25
            xalign 0.20
            yalign 0.30

        text "{color=#000000}ARAMdo{/color}":
            size 25
            xalign 0.50
            yalign 0.30

        text "{color=#000000}Machopierre{/color}":
            size 25
            xalign 0.77
            yalign 0.15
