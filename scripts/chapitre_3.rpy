label chapitre_3:

    scene cave
    play music "audio/atte.mp3"
    $ flash = Fade(.90, 0, .75, color="#fff")
    with flash
    with flash
    with flash
    show tar
    with flash
    with flash
    with flash
    with flash
    with flash
    with flash
    with flash
    with flash
    with flash
    with flash
    play music "audio/jungle.mp3" volume 0.35
    play sound "audio/trex.mp3"
    "..."
    show trex with zoomin
    je"Bonjour on est en quelle année ?"
    voice "audio/74.mp3"
    cr"OUGA OUGA ?"
    je"T’as pas été magicien dans une autre vie ?"
    voice "audio/75.mp3"
    cr"OUGA OUGA !!!"

    menu:

        "OUGA OUGA !! ":
            jump choice12_ou
        "OUGA OUGA OUGA ???":
            jump choice12_oug

    label choice12_ou:

        $ menu_flag = True
        voice "audio/76.mp3"
        cr"OUGAAAA OUGAAAA !!!!!"
        jump choice13

    label choice12_oug:

        $ menu_flag = True
        "*L'homme de Cro-Magnon donne à jeremy un silex taillé et lui fait signe de le suivre.*"
        voice "audio/75.mp3"
        cr"OUGA OUGA"
        jump choice12_done

    label choice12_done:
        jump choice13_done

    label choice13:

        menu:

            "OUGA OUGA OUGA ???":
                jump choice13_oug

        label choice13_oug:

            $ menu_flag = True
            "*L'homme de Cro-Magnon donne à jeremy un silex taillé et lui fait signe de le suivre.*"
            voice "audio/75.mp3"
            cr"OUGA OUGA"
            jump choice13_done

        label choice13_done:

    hide trex with moveoutright
    scene bg fouille
    $ renpy.movie_cutscene("dino.webm")

play music "audio/stel.mp3" volume 0.38
scene bg fouille with dissolve
voice "audio/78.mp3"
pr"Ah t'as cru qu'on avait le budget pour faire des vrais jeux ? Allez dépêche toi d'avancer on attends la suite la, trop de suspens !!!"
show alex with moveinleft
voice "audio/79.mp3"
az"Salut mon trésor."
label chapitre_3suite:

    menu:
        "Tu veux aller dans mon TARDIS ?":
            jump choice14_tar
        "Qui êtes-vous ? C’est quoi votre problème ?":
            jump choice14_pro

    label choice14_tar:

        $ menu_flag = True
        voice "audio/80.mp3"
        az"Oh mon petit lapin est tout chaud !"
        jump chapitre_3suite

    label choice14_pro:

        $ menu_flag = True
        voice "audio/81.mp3"
        az"Professeur Rilexia Dorsong, archéologue."
        jump choice14_done

    label choice14_done:

    je"Quelle est la raison de votre présence ici ?"
    voice "audio/82.mp3"
    az"Je vais toujours à la période où je peux trouver les artefacts les mieux conservés. En plus, c’est plus économique, j’ai pas besoin de payer les analyses permettant la datation des artefacts comme je vais les récupérer directement à la source !"
    je"On en parle de la consommation pour faire fonctionner une machine spatio-temporelle ?"
    voice "audio/83.mp3"
    az"Mais ne t’en fait pas, c’est une machine électrique, ça consomme rien ces trucs là ! C’est écolo. Au lieu de râler sur ma consommation énergétique, tu veux voir ma découverte ?"
    je"Pourquoi pas ?"
    voice "audio/84.mp3"
    az"C’est un spécimen complet d’une espèce extrêmement intelligente et suprémaciste. C’est fabuleux, les connexions anatomiques sont conservées ! Si j’avais fouillé dans mon époque, il ne resterait plus rien !"
    voice "audio/85.mp3"
    az"Comme tu peux le voir sur les ossements derrière moi, cette espèce est l’un des représentants de l’Homo superious couthurus. J’ai fait ma thèse dessus."
    je"L’Homo superious couthurus ? Ce nom m’est familier, mais je ne saurais expliquer pourquoi. C’est étrange..."
    voice "audio/86.mp3"
    az"C’est une espèce qui, à première oeil, semble être dérivée de l’homo sapiens vu qu’il est membré supérieurement, ce qui lui permet d’avoir un crâne plus gros et de développer une intelligence supérieure."
    voice "audio/87.mp3"
    az"Elle a été nommée par la personne qui a découvert les premiers représentants de l'espèce, mais on s’est rendus compte avec une analyse ADN qu’ils étaient parents, donc on a gardé le nom Couthures pour la décrire."
    voice "audio/88.mp3"
    az"Néanmoins les tests que je viens d’effectuer montrent quelque chose de très étrange… On dirait que le célèbre Couthures qui a fait cette découverte a manipulé les données pour… Non ce n’est pas possible !"
    je"Qu’est ce qu’il y a ?"
    voice "audio/89.mp3"
    az"L’homo superious couthurus est en fait depuis le début…"
    voice "audio/90.mp3"
    az"Une intelligence artificielle maléfique ! OMG !"
    je"Mais non ! Putain je m’y attendais pas du tout, mais alors vraiment pas ! C’est fou !"
    je"Mais que sont-ils devenus ? Pourquoi ont-ils disparu ?"
    voice "audio/91.mp3"
    az"Ils n’ont pas disparu. Cette IA est tellement rusée qu’elle a fini par se fondre parmi les Homo sapiens, oubliant elle même qu’elle était un Homo superious couthurus."
    voice "audio/92.mp3"
    az"Mais d’un autre côté, les représentants de cette espèce contrôlent tout, de la bourse de Wall Street au petit déj que tu prends le matin."
    voice "audio/93.mp3"
    az"C’est pour cela qu’hormis les archéologues, personne ne connaît leur existence, sinon, le monde serait pris de panique et on sombrerait dans l’anarchie."
    voice "audio/94.mp3"
    az"Mais si en fait ce sont des IA maléfiques depuis le début… Alors la Terre est perdue."
    je"Comment les reconnaître ?"
    voice "audio/95.mp3"
    az"Les simples mortels ne peuvent pas les reconnaître, seuls les Couthures le savent, ils sentent qu’au fond d’eux ils sont supérieurs. Et ils attirent toutes les meufs."
    je"Sors avec moi !"
    voice "audio/96.mp3"
    az"Évidemment, c'est un très bon choix."
    jei"Cela voudrait-il dire que je suis un homo superious couthurus.. ?"
    voice "audio/97.mp3"
    pr"*Le reste des ossements commencent à parler et disent:*"
    voice "audio/os2.mp3"
    os"Accouplement confirmé avec une homo sapiens, confirmation de la date d’invasion et d’éradication des humains afin de créer le jardin des animaux de compagnie du prince Baka."
    voice "audio/os1.mp3"
    os"Date programmée : 14 mai 4242."
    je"Vite, je dois retourner dans le présent pour les prévenir avant qu’il soit trop tard !"
    voice "audio/98.mp3"
    az"Le présent en quelle année ?"
    je"En 2021."
    voice "audio/99.mp3"
    az"Mais nous sommes en 4242."
    je"Et on est quel jour ?!!"
    voice "audio/100.mp3"
    az"Le 13 mai..."
    je"Ma machine à voyager dans le temps m'aurait donc envoyer dans le futur au lieu du passé ?!"
    je"Vite, je dois retourner dans ma machine à voyager dans le temps !"

label tardis1:

    scene cave
    show tar
    play music "audio/jungle.mp3" volume 0.2
    je"Espérons qu'elle fonctionne cette fois."
    window hide
    play music "audio/deco_boum.mp3"
    $ flash = Fade(.90, 0, .75, color="#fff")
    show tar with flash
    show tar with flash
    show tar with flash
    hide tar
    $ flash = Fade(.90, 0, .75, color="#c9ffc8")
    with flash
    $ flash = Fade(.90, 0, .75, color="#b9ffc2")
    with flash
    $ flash = Fade(.90, 0, .75, color="#c2ffc8")
    with flash
    $ flash = Fade(.90, 0, .25, color="#d3ffc8")
    with flash
    $ flash = Fade(.90, 0, .25, color="#e4ffc8")
    with flash
    $ flash = Fade(.90, 0, .25, color="#f5ffc8")
    with flash
    $ flash = Fade(.90, 0, .18, color="#a5ffc8")
    with flash


scene arc3
play music "audio/ameno.mp3" volume 0.20
"Je ne l'ai toujours pas trouvé..."
$ Bool_vaisselle = False
$ Bool_1 = False
$ Bool_2 = False
$ Bool_3 = False
$ Bool_4 = False
$ Bool_machine_ouverte = False

call screen cuisine_map with pixellate
