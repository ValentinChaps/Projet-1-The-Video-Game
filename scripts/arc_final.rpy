label arc_final:


    #Call screen chiottes

    #Après qu'il ai appuyé sur le bouton
    play music "audio/oh.mp3" volume 0.15
    scene bg lab with pixellate
    show robcam
    voice "audio/camille1.mp3"

    db "Oh salut toi ! T’es vite revenu, j’ai juste eu le temps de fusionner avec mon robot afin de pouvoir survivre après l’explosion de mon labo et de me trouver un date sur..."

    je "TG ! On a pas le temps pour tes conneries. T’en as beaucoup des vibros qui m’ont fait parler comme dans l’arc ou on découvre que je suis une IA maléfique ?"
    voice"audio/camille2.mp3"

    db "Malheureusement les ¾ de ma collection ont explosé avec mon labo… Pourquoi ?"

    je "Eh merde. Tes vibros sont les seuls moyens pour detecter les homo superious couthurus. Si on arrivait à en distribuer à toute la population, la Terre serait sauvée."
    voice"audio/camille3.mp3"

    db "Attend t’es en train de me dire qu’il faudrait un vibro par habitant et qu’il se tape tous entre eux avec pour sauver le monde ?!!"

    je "Oui c’est exactement ça !"
    voice"audio/camille4.mp3"

    db "Ah bah c’est hyper simple en fait. Avec ce qui me reste de ma collection j’ai largement assez pour en donner à toute la population mondiale, et il m’en restera un peu pour moi en plus !"

    je "Sérieux ?! Mais c’est trop bien ! Heureusement que tu penses qu’à ça docteure. Mais on a quand même un problème."

    je "Comment va-t-on faire pour informer toute la population mondiale de l’invasion tout en leur fournissant tous des vibros ?"

    #Grosse explosion et arrivé d’Aurélien en boss final
    play sound "audio/exp.mp3"
    $ flash = Fade(.90, 0, .75, color="#fff")
    show aur at right with flash

    play music "audio/und.mp3" volume 0.1 fadeout 0.5
    "..."

    voice "audio/103.mp3"

    aur"Mouahahahahaha !! Tu as cru que tu pourrais sauver l’humanité de sa transformation en zoo pour le prince Baka. Tu n’es clairement pas le Couthures le plus supérieur de cette galaxie… Vu que tu l’as devant toi !"

    #Prince Baka qui pop
    show baka1 at left with moveinbottom

    voice baka_voice
    baka "Oh c’est gentil de dire ça Aurelius Aramus. J'ai toujours su que j'étais au dessus des autres macaques vivant dans cette galaxie."
    voice "audio/104.mp3"

    aur "Je ne parlais pas de toi espèce de con ! Euh je veux dire baka ! C’est moi l’être qui a été décerné le plus intelligent de la galaxie. Je connais déjà tout ce que tu vas faire à l’avance. Tu n’as aucune chance !"

    je "Non !!! J’étais si proche…"
    voice"audio/camille5.mp3"


    db "Tout n’est pas perdu ! Retiens le pendant que je me charge de distribuer les vibros et nous sauverons la Terre ensemble !"


    voice baka_voice
    baka "Non ne la pas laisse partir ! Sinon je ne pourrais pas mettre tous mes gentils petits Ewoks sur cette planète afin de les voir se faire dévorer par des lapins crétins !"

    voice "audio/105.mp3"
    aur "Ok je vais la {nw}rattra…"
    play music "audio/du.mp3"

    je "Pas si vite Kaïba ! C’est l’heure DU-DUDUDUDU-DUEL !"
    define circleirisout = ImageDissolve("images/imagedissolve_dream.png", 1.0, 8)



    jump combat

    #Lancement mini jeu de combat

    #O Si J gagne alors vidéo de fin badass que le noob veut faire ou les 2 se fight et J gagne. On voit à la fin Camille en robot qui distribue avec ses missiles des vibros sur toutes la Terre en leur disant de se foutre sur la gueule avec pour sauver le monde. Suivi de 2 personnes qui se battent avec des godes.

    #Si J perd il revient à l’écran ou Karamouille et Percenoob parlent et ne peut plus en sortir mais juste avant A dit :
    voice "audio/106.mp3"
    aur "No rage de ta loose. Je vais te renvoyer avec les Jean de ton niveau. Je suis un être charitable. Profite bien."
