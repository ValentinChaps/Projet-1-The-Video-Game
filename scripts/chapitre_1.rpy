label chapitre_1:

    $ Bool_linge = False
    $ Bool_wii = False

 #Parc
    scene bg salon
    call screen salon


    label wii_u:
        $ Bool_wii = True
        play sound "audio/link.mp3"
        jei "Tiens ça fait longtemps que je n'ai pas joué Link Cartoon."
        call screen salon

    label linge :
        if Bool_linge == False:
            $ Bool_linge = True
            jei "Pas de vêtements à moi... J'ai vraiment plus de chaussettes et de caleçons..."
        else :
            jei "Mais j'ai déjà regarder ici, toujours pas de caleçons."
        call screen salon

    label note :
        show note:
            xalign 0.5
            yalign 2

        jei "Ça me rappelle mes années de lycée à Paarkmelott tout ça... "
        scene bg parc_devant
        $ renpy.movie_cutscene("paarkmelott.webm")

    stop music

    label park:
        play music "audio/jean-petit-danse.mp3" volume 0.08 fadeout 1
        scene bg parc_devant with pixellate
        show porckam with moveinbottom

        voice "audio/11.mp3"
        bu "Jeremy… CUILLIÈRE !!!!"
        menu:

            "Cuillière ? ":
                jump choice1_cuilliere

            "Fourchette ? ":
                jump choice1_fourchette

        label choice1_cuilliere:

            $ menu_flag = True
            voice "audio/12.mp3"
            bu "CUILLIÈRE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"


            jump choice1_done

        label choice1_fourchette:

            $ menu_flag = False
            voice "audio/13.mp3"
            bu "AAAAAAAAAAAAAH !!! CUILLIÈRE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"


            jump choice1_done

        label choice1_done:
            je "Euh.. Je vais rentrer dans le château, je dois aller parler à Merlin. "

    $ x=0

    label danslepark:
        scene bg juetc with wipeleft
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
                jump choice2_yaourt

            "*Ne rien dire":
                jump choice2_riendire

        label choice2_yaourt:
            $ x = x+1

        if x<2:
            jump danslepark
        else:
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

            jump choice2_done

        label choice2_riendire:
            $ x = x+1

        if x<2:
            jump danslepark
        else:
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

            jump choice2_done

        label choice2_done:

            label danslepark1:

                        menu:
                            "C'est quoi l'histoire du yaourt ?":
                                        jump choice6_yaourt

                            "*Ne rien dire":
                                jump choice6_riendire

                            "*Partir":
                                jump choice6_partir

                        label choice6_yaourt:
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

                                jump danslepark1

                        label choice6_riendire:
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

                                jump danslepark1

                        label choice6_partir:
                            $ menu_flag = True
                            jei "Et dire que je pensais que les autres êtres humains étaient des animaux… C’est peut être pire que ce que j’imaginais. Je vais voir Merlin."

                            jump choice6_done


                        label choice6_done:


    label bac:
        scene bg fondmerlin with irisout
        show merlin with moveinright
        voice "audio/26.mp3"
        me "Oh bonjour Jeremy ! J’espère que tu as bien révisé ton baccalauréat réservé exclusivement aux êtres supérieurs. Quelle note penses-tu avoir ?"

        label bac1:
            menu:

                "42/20":
                    jump choice3_42

                "20/20 facile":
                    jump choice3_20

            label choice3_42:

                $ menu_flag = True
                voice "audio/27.mp3"
                me "Ahahahaha ! Cette note est humainement impossible. Arrête de te foutre de ma gueule ou je te transforme en suricate."

                jump bac1

            label choice3_20:

                $ menu_flag = False
                voice "audio/28.mp3"
                me "Tu es le meilleur élève du château de Paarkmelott. Tu as même réussi à dépasser les résultats de Jean Perceval qui était resté imbattu car il n’avait redoublé son baccalauréat que 6 fois."
                voice "audio/28-29.mp3"
                me "Si tu réussis l’examen aujourd’hui, tu marqueras l’histoire de tout le royaume des United Jeans."

                jump choice3_done

            label choice3_done:
                je "Et toi tu as eu combien au bac ?"
                voice "audio/29.mp3"
                me "Euh… Ce n’est pas la question !"
                jei "Attend mais il l’a pas eu son bac ce singe ?"
                voice "audio/30.mp3"
                me "C’est toi le singe !"
                voice "audio/31.mp3"
                me "Commençons donc l’examen maintenant."
                voice "audio/32.mp3"
                me "Camille a 42 pilules de Concerta. Elle doit en prendre 2 par jour pendant 2 jours. A la fin des 2 jours, combien lui reste-t-il de Concerta ?"

                menu:
                    me"Camille a 42 pilules de Concerta. Elle doit en prendre 2 par jour pendant 2 jours. A la fin des 2 jours, combien lui reste-t-il de Concerta ?"
                    "Pas assez.":
                        voice "audio/33.mp3"
                        me "Bien vu l’aveugle ! Cette question était facile, mais la prochaine va te donner du fil à retordre."
                    "Suffisamment.":
                        voice "audio/33.mp3"
                        me "Bien vu l’aveugle ! Cette question était facile, mais la prochaine va te donner du fil à retordre."
                    "42 parce qu’elle a oublié de les prendre.":
                        voice "audio/33.mp3"
                        me "Bien vu l’aveugle ! Cette question était facile, mais la prochaine va te donner du fil à retordre."

            voice "audio/34.mp3"
            me "Question culturelle maintenant. Quels types de poissons sont les plus communs dans la mer sucrée ?"
            $ n=0

            label bacmerlin:
                menu:
                    me "Question culturelle maintenant. Quels types de poissons sont les plus communs dans la mer sucrée ?"

                    "Les moulagaufres.":
                        jump choice4_42

                    "Les hommes crabes.":
                        jump choice4_20

                    "Le saumon.":
                        jump choice4_ez

                label choice4_42:
                    $ n = n+1

                    if n<3:
                        voice "audio/35.mp3"
                        me "Oui oui oui oui oui.. !!"
                        voice "audio/36.mp3"
                        me "C’est pas du tout ça !!"
                        jump bacmerlin

                    else:
                        voice "audio/35.mp3"
                        me "Oui oui oui oui oui.. !!"
                        voice "audio/36.mp3"
                        me "C’est pas du tout ça !!"
                        jump choice4_done

                label choice4_20:
                    $ n = n+1

                    if n<3:
                        voice "audio/35.mp3"
                        me "Oui oui oui oui oui.. !!"
                        voice "audio/36.mp3"
                        me "C’est pas du tout ça !!"
                        jump bacmerlin

                    else:
                        voice "audio/35.mp3"
                        me "Oui oui oui oui oui.. !!"
                        voice "audio/36.mp3"
                        me "C’est pas du tout ça !!"
                        jump choice4_done

                label choice4_ez:
                    $ n = n+1

                    if n<3:
                        voice "audio/35.mp3"
                        me "Oui oui oui oui oui.. !!"
                        voice "audio/36.mp3"
                        me "C’est pas du tout ça !!"
                        jump bacmerlin

                    else:
                        voice "audio/35.mp3"
                        me "Oui oui oui oui oui.. !!"
                        voice "audio/36.mp3"
                        me "C’est pas du tout ça !!"
                        jump bacmerlin1

            

            label bacmerlin1:
                menu:
                    me "Question culturelle maintenant. Quels types de poissons sont les plus communs dans la mer sucrée ?"

                    "Les moulagaufres.":
                        jump choice5_42

                    "Les hommes crabes.":
                        jump choice5_20

                    "Le saumon.":
                        jump choice5_ez

                    "La bonne réponse ?":
                        jump choice5_bon

                label choice5_42:

                    $ menu_flag = True

                    voice "audio/35.mp3"
                    me "Oui oui oui oui oui.. !!"
                    voice "audio/36.mp3"
                    me "C’est pas du tout ça !!"
                    jump bacmerlin1


                label choice5_20:

                    $ menu_flag = True

                    voice "audio/35.mp3"
                    me "Oui oui oui oui oui.. !!"
                    voice "audio/36.mp3"
                    me "C’est pas du tout ça !!"
                    jump bacmerlin1

                label choice5_ez:

                    $ menu_flag = True

                    voice "audio/35.mp3"
                    me "Oui oui oui oui oui.. !!"
                    voice "audio/36.mp3"
                    me "C’est pas du tout ça !!"
                    jump bacmerlin1

                label choice5_bon:

                    $ menu_flag = True
                    voice "audio/37.mp3"
                    me "Bonne réponse ! Wow ! Celle-là n'était pas facile. La dernière personne qui a réussi à répondre à cette question c’était moi et j’ai copié sur mon voisin.. Et mon voisin c’était toi !"
                    jump choice5_done

                label choice5_done:

                voice "audio/38.mp3"
                me "Tu arrives maintenant à la dernière épreuve qui décidera si tu es un être supérieur ou un simple mortel."
                voice "audio/39.mp3"
                me"Pour réussir cette dernière épreuve tu devras faire preuve de détermination, de stratégie, d’agilité, d’ingéniosité mais surtout… de supériorité !"
                voice "audio/40.mp3"
                me"Je pense que tu l’as bien compris. Nous allons jouer au Ping PONG."
                $ renpy.movie_cutscene("pongvid.webm")
            stop music

label play_pong:

    window hide  # Hide the window and  quick menu while in pong
    $ quick_menu = False

    call screen pong

    $ quick_menu = True
    window show

    if _return == "Moi":

        voice "audio/41.mp3"
        me"Incroyable.. Une telle perfection ne peut être humaine. Je n’ai jamais vu quelqu’un d’aussi supérieur ! Mais qui es tu ? Ce qui est sûr c’est que tu ne viens pas d’ici…"

    else:
        voice "audio/42.mp3"
        me "YES !! Je t’ai niqué !!! Je suis trop fort putain, DTC !"
        je "Elle était faute."
        voice "audio/43.mp3"
        me"Quoi ?!!!!!!!! Ce n’est pas possible.. Personne n’a jamais réussi à vaincre mon coup droit légendaire. Cela veut dire que tu es l’être qui dépasse tous les autres dans ce royaume ?"
        voice "audio/44.mp3"
        me"Une telle perfection ne peut être humaine. Je n’ai jamais vu quelqu’un d’aussi supérieur ! Mais qui es tu ? Ce qui est sûr c’est que tu ne viens pas d’ici…"


play music "audio/ff.mp3" volume 0.18 fadeout 1
voice "audio/45.mp3"

me"Félicitations, tu es désormais l’être le plus supérieur parmi tous les êtres supérieurs du royaume. Voici ton baccalauréat !"
voice "audio/46.mp3"
me"Néanmoins je vais devoir te demander de quitter les United Jeans immédiatement. Nous ne pouvons pas tolérer qu’un être soit supérieur à notre roi, le grand Jean Sympa Le Lion III."
voice "audio/47.mp3"
me"Ce fut un honneur de t’avoir comme élève. Bon voyage à toi."
voice "audio/48.mp3"
mei"Par contre il a intérêt à bouger son cul sinon j’appelle les gardes."
je"Ok ok je m’en vais n’appel pas les gardes !"
voice "audio/49.mp3"
mei"Quoi il a lu dans mes pensées ?!!"
je"Non."
voice "audio/50.mp3"
me"Ah ça va alors. Allez salut."
play music "audio/jt.mp3" volume 0.32 fadeout 0.5


scene bg pelerin with dissolve


#Image de J avec le sac ou le baluchon qui marche

voice "audio/51.mp3"
pr"Jeremy du haut de ses 23 ans, considéré comme l’être le plus supérieur du royaume, se retrouve aujourd’hui sans domicile fixe."
voice "audio/52.mp3"
pr"Ce qu’il ne savait pas c’est que quelque chose d’incroyable allait lui arriver, quelque chose d'inoubliable, d’unique, de fantastique !"
voice "audio/53.mp3"
pr" Et cette chose c’est l'arrivée de son.."
voice "audio/54.mp3"
vn"Eh noob ! Tu viens faire une ranked ou quoi ?"
voice "audio/55.mp3"
pr"Euh je peux pas vraiment la, je suis en plein milieu de mon histoire. Fais pas chier revient plus tard !"
voice "audio/56.mp3"
vn"Ton histoire ? Ah mais tu lis un texte et tout ! Vas-y laisse moi faire ça ira plus vite qu’avec toi. Donne moi ça."
voice "audio/57.mp3"
pr"Non lache ça c’est mon job ! Va jouer Veigar tout seul !"
voice "audio/58.mp3"
vn"Donne je te dis ! Alors t’en étais où..?"
je"Il était à :”Et cette chose c’est l’arrivée de son..”"
voice "audio/59.mp3"
vn"Ah merci. Alors nanananana et.. Ah oui c’est bon j’y suis !"
voice "audio/60.mp3"
vn"Et cette chose c’est l'arrivée de son…"
voice "audio/60-61.mp3"
vn"Lui du futur !"
play sound "audio/dbz.mp3"

define teleport = ImageDissolve("imagedissolveteleport.png", 1.2, 0)


show jdufut at right with teleport

#J du futur ici
play music "audio/retour.mp3" volume 0.8
jf"Bonjour moi même. Nous n’avons que très peu de temps pour discuter car les auteurs de ce chef-d'œuvre n’ont pas le temps pour créer des dialogues très longs."
jf"Je pense que tu viens de comprendre que tu étais clairement supérieur aux autres. Mais tu dois certainement te demander pourquoi."
jf"Va parler à la célèbre Camouille qui se trouve dans l’université des LGBTQIA+-/*VersionRougeBleuJauneEtSaphir. Sinon voila ce qui va se passer !"
jf"Tu pourras pas finir le jeu."
jf"C’est toujours un plaisir de me voir, à bientôt."
play music "audio/ameno.mp3" volume 0.5

scene arc2
jei"Je dois me dépêcher avant qu'il soit trop tard !"
$ Bool_chambre = False
$ Bool_piece_du_fond = False
$ Bool_imprimante = False
$ Bool_lampe = False
window hide
call screen piece_haut_map with pixellate
