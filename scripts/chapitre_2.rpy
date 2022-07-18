label chapitre_2:
    scene fac with pixellate
    jei "Je dois donc trouver le labo du Dr Camouille."
    play music "audio/dieu.mp3" fadeout 1
    show dieu
    with moveintop
    di"Grâce à mes pouvoirs extraordinaires, j'ai pu sentir ton immense détresse et avec mes pouvoirs divins je peux t’aider à résoudre n’importe quel problème !"
    $ x=0
    label choix8:
        $ x = x+1
        menu:
            di"Grâce à mes pouvoirs extraordinaires, j'ai pu sentir ton immense détresse et avec mes pouvoirs divins je peux t’aider à résoudre n’importe quel problème !"

            "J’aimerais acquérir le savoir de toute chose.":
                jump choice8_sav

            "Tu peux nous sortir de la crise du covid?":
                jump choice8_covid

        label choice8_sav:

            di"Et puis quoi encore tu voudrais que je te spoil la fin de ton histoire ?!"

            if x<2:
                jump choix8
            else:
                jump choice8_done

        label choice8_covid:

            di"Ah tu crois encore au Père Noël toi ?"

            if x<2:
                jump choix8
            else:
                jump choice8_done

        label choice8_done:

    label choix9:
        menu:
            di"Grâce à mes pouvoirs extraordinaires, j'ai pu sentir ton immense détresse et avec mes pouvoirs divins je peux t’aider à résoudre n’importe quel problème !"
            "J’aimerais acquérir le savoir de toute chose.":
                jump choice9_sav

            "Tu peux nous sortir de la crise du covid?":
                jump choice9_covid

            "En fait tu sers a rien, tu peux faire quoi ?":
                jump choice9_cam

        label choice9_sav:

            di"Et puis quoi encore tu voudrais que je te spoil la fin de ton histoire ?!"

            $ menu_flag = True
            jump choix9

        label choice9_covid:

            di"Ah tu crois encore au Père Noël toi ?"
            $ menu_flag = True
            jump choix9

        label choice9_cam:
            di"Je peux t’indiquer la salle où se trouve le Dr Camouille."
            $ menu_flag = True
            jump choice9_done

        label choice9_done:

    scene bg lab
    play music "audio/labo.mp3" volume 0.2 fadeout 0.5
    show dr:
        xalign 0.99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        yalign 0.25
    je"Excusez-moi je cherche le Dr Camouille."
    voice "audio/61.mp3"
    dr"Ah oui comme ça tu me cherche ?! Vas y je t’attends gamin !!"
    je"On m’a dit que tu étais une professionnelle.."
    voice "audio/62.mp3"
    dr"Ça dépend, pour toi je prends 50€ de l’heure !"
    je"Wahou c’est pas cher pour une péripatéticienne."
    voice "audio/63.mp3"
    pr"(Aucune travailleuse du sexe n’a été blessée pendant la réalisation de ce projet.)"
    voice "audio/64.mp3"
    dr"Merci du compliment, mais je parlais de mes tarifs en tant que docteure en psychologie."
    je"Mais je pensais que vous étiez une éminente chercheuse en IA ?"
    voice "audio/65.mp3"
    dr"Évidemment ! Il n’y a pas plus grande que moi dans le domaine de l’intelligence artificielle, je te présente le LGBT++ Mark 2.69."
    play music "audio/oh.mp3" volume 0.15 fadeout 0.1
    show robot:
        xalign 0.000001
        yalign 0.4
    with moveinleft
    rb"..."
    voice "audio/1robot.mp3"
    rb"Bonjour, quel est votre genre et votre orientation sexuelle ?"

    menu:
        rb"Bonjour, quel est votre genre et votre orientation sexuelle ?"

        "Homme cisgenre.":
            jump choice10_cis
        "Bah j’ai une bite quoi":
            jump choice10_cis
        "Je peux pas vraiment dire que je rentre dans une catégorie. Je me retrouve dans chaque catégorie.":
            jump choice10_queer

    label choice10_cis:

        voice "audio/2robot.mp3"
        rb"Cible reconnue, sortie des missiles."
        $ menu_flag = True
        jump choice10_done

    label choice10_queer:
        voice "audio/3robot.mp3"
        rb"Individu queer reconnu."
        rb"..."
        voice "audio/4robot.mp3"
        rb"Tu fais quoi ce soir ? ;)"
        $ menu_flag = True
        jump choice10_done

    label choice10_done:

    voice "audio/5robot.mp3"
    rb"Erreur système, problème d’analyse de donnée, surplus capacitielle, générateur secon..."
    voice "audio/6robot.mp3"
    rb"Bzzzz djdnzmd"
    rb"..."
    voice "audio/7robot.mp3"
    rb"I'm so gay for you"
    voice "audio/66.mp3"
    dr"Bon il est possible qu’ils aient encore quelques bugs, assez légers toutefois."
    voice "audio/8robot.mp3"
    rb"AUTO DESTRUCTION IMMINENTE !!!"
    voice "audio/67.mp3"
    dr"Vraiment rien de bien grave."
    je"Quel langage de code t'utilises pour tes IA ?"
    voice "audio/68.mp3"
    dr"De quoi tu me parles ? D’habitude je tape dessus avec mon vibro et après ça marche."
    je"Mais tu as utilisé quel logiciel pour coder ?"
    voice "audio/69.mp3"
    dr"Mon vibro ?"
    je"Je peux voir comment tu fais ?"
    play sound "audio/coup.mp3"
    "*La docteure donne un coup de vibro au personnage principal.*"
    je"Mise à jour système disponible, que voulez-vous faire ?"
    voice "audio/70.mp3"
    dr"Accès code source."
    je"Le code source est trop maléfique pour que vous puissiez y accéder."
    je"Wahou il vient de se passer quoi là ?"
    voice "audio/71.mp3"
    dr"Tu es une IA maléfique, mais j’ai modifié ton code ça manquait de LGBT."
    je"Pfff n'importe quoi ! Je le saurais si j'étais une IA, je suis pas con, j'ai eu 42/20 à mon baccalauréat. Si c’est comme ça je me casse."
    voice "audio/9robot.mp3"
    rb"AUTO DESTRUCTION IMMINENTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    #Video explosion avec les images du robot et de Camouille mortel
    $ renpy.movie_cutscene("des_lab.webm")

    #Ruines du labo
    scene bg delab
    je"Tout cela me paraît étrange, je dois en avoir le cœur net."
    voice "audio/72.mp3"
    pr"Jeremy récupère des pièces dans les décombres du labo de Camouille et commence à construire quelque chose."
    je"Ça devrait le faire comme ça."
    voice "audio/73.mp3"
    pr"Bruit sourd."
    show tar

    #Vrai bruit sourd puis rajout de la cabine à voyager dans le temps

    je"C’est terminé. Ma toute nouvelle machine à voyage dans le temps va me permettre d'enquêter sur mes origines."
    window hide
    label tardis:

        play music "audio/deco.mp3" fadeout 0.3
        $ flash = Fade(.90, 0, .75, color="#fff")
        show tar with flash
        show tar with flash
        show tar with flash
        show tar with flash
        show tar with flash
        show tar with flash
        show tar with flash
        show tar with flash
        show tar with flash
        hide tar
        with flash
        with flash

jump chapitre_3

      #Image "Arc Final"
      #Jeremy de retour dans la maison mère couthure et il a de nouveau le choix entre plusieurs objets: un jouet de t-rex ,Jeremy pense ça me rappelle de belle rencontre, ce choix lance la suite de l'histoire ; ou un autre truc
