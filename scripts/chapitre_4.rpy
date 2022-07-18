
label chapitre_4:
    stop music


    scene bg tardis with pixellate
    with irisout
    je "Oh mince, je crois que ma machine à voyager dans le temps et celle du professeur Dorsong ont des problèmes, ce qui arrange bien les scénaristes. Olalalala, on dirait que je suis resté bloqué en 4242."

    je "Mais je suis sûr que ma machine fonctionne encore assez bien pour me donner des infos sur cette époque."

    scen ";)"
    $ renpy.movie_cutscene("video/intro_gintama.webm")

    je "Mais comment je vais me défendre sans raquette ? Il faut que je trouve de l’aide. J’espère que quelqu’un de cette époque pourra m’aider."

    #*Jeremy sort du tardis*
    $ flash = Fade(.25, 0, .75, color="#fff")

    ##*Flash avec gin intony qui apparait dans le salon des yorozujean*
    scene bg gin_salon
    show gin_venere at center
    with flash
    with flash
    play music "audio/gintama_home.mp3" volume 0.3
    voice "audio/gin_venere.mp3"
    gin  "Qu’est ce que vous faites chez moi ?! Qui vous a permis d’entrer avec votre cabine téléphonique dans mon salon ? C’est pas un endroit pour passer un coup de fil !!!"

    hide gin_venere
    show gin_blase at center

    voice "audio/gin_question_courte.mp3"
    gin   "J'espère au moins que vous êtes un client !"

    je  "Euhhh oui oui... Bien sûr, mais vous faites quoi exactement ?"

    voice "audio/gin_moyen.mp3"
    gin  "Je suis Jean Gintony Sakouthures et je dirige l'entreprise YorozuJean. On fait un peu de tout, t’as besoin de quoi ?"

    je  "C’est pas un vrai métier de faire un peu de tout."

    voice "audio/gin_insulte.mp3"
    gin  "Si c’en est un d’abord ! Explique-moi ton problème que je te montre."

    je " Bah il faut que je sauve le monde d’une invasion d’IA maléfiques."
    hide gin_blase
    show gin_etonne

    voice "audio/gin_oyo.mp3"
    gin  "Hum.... {i} ça à l’air d’être un bon pigeon, je vais l'arnaquer. {/i}"

    hide gin_etonne
    show gin_content
    voice "audio/gin_oyo.mp3"
    gin  "Ok pour 450 yens. {i} Mouhahahahahaha, il ne sait pas que dans l’anime ou je suis le héros, je suis payé bien moins cher pour sauver l’humanité.{/i} "

    hide gin_content

    je  "Alors tout commence par..."
    show bg "#000000"
    with Dissolve(0.2)

    $ renpy.movie_cutscene("video/titre.webm")
    play music "audio/gintama_home.mp3" volume 0.3
    show bg gin_salon
    je  "Et c’est pour ça que je suis dans ton salon."
    show gin_blase at center

    play sound "audio/gin_rien_a_voir.mp3"
    gin  "Humm je vois, simple comme histoire. Ca me rappelle que c’est mon arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrièrearrière arrière arrière arrière arrière arrière"
    gin  "arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière arrière"
    play sound "audio/gin_rien_a_voir_2.mp3"
    gin  "arrière arrière arrière arrière arrière arrière arrière grand père qui à découvert les homo superious couthurus."
    stop sound

    je  "Mais ça veut dire que tu en es un aussi ! Ca me paraissait bizarre aussi ce ton hautain. C’est super ! Grâce à notre supériorité intellectuelle nous allons pouvoir sauver la Terre."

    voice "audio/gin_cour_1.mp3"
    gin "Ah oui c’est sûr qu’on peut, mais dès que tu m’auras payer."

    je "Par contre j’ai pas d’argent..."

    hide gin_blase
    show gin_etonne at center

    voice "audio/ahh.mp3"
    gin "Ah !"# *Ah de Denis Brogin niat*"

    hide gin_etonne
    show gin_venere at center

    voice "audio/gin_venere.mp3"
    gin "Bah dégage alors. Reviens quand t’auras de l’argent ! Et sors ta machine de chez moi !!"

    hide gin_venere
    $ flash_black = Fade(.1, 0, .75, color="#000")
    scene bg ruegin
    with flash_black

    je  "..."
    stop music fadeout 1

    je  "Je vais essayer de trouver un job pour la journée, avec mes capacités supérieures ça devrait être d’une simplicité enfantine."

    $ renpy.movie_cutscene("video/jingle.webm")
    scene bg bar_otose
    jump start_game_perso

    # *Image d’un bar en fond

label win_jeu:
    scene bg bar_otose
    show maj_venere at center with zoomin

    voice "audio/majordome_1.mp3"
    maj "C’est ce que je dis imbécile, ce n’est pas ça ! C’est là ! Là !! Vraiment, même un chimpanzé peut faire ce genre de choses ! Et toi, t’es humain !"

    je "Désolé. J’ai seulement pratiqué le ping pong jusqu’à maintenant."

    voice "audio/majordome_1.mp3"
    maj "Idiot ! Tu t’occupes encore de tes raquettes de ping-pong ?! Les Jeans et les raquettes ont disparu depuis un bon moment maintenant ! Combien de temps vas-tu garder tes accessoires de ping-pong, enfoiré !"

    #*Apparition du prince Baka et de sa musique
    play music "audio/baka.mp3" volume 0.3
    show baka at center behind maj_venere with moveinbottom

    voice "audio/baka_voice.mp3"
    baka "Laissez tomber docteur Fabre... J’ai acheté cet endroit pour le bien de mes animaux. On vient juste vérifier l’avancement des travaux, pas besoin de se battre avec la faune locale."

    hide maj_venere with moveoutleft
    show maj at left with moveinleft

    voice "audio/majordome_2.mp3"
    maj "Désolé mon prince, je ne vous manquerez jamais de respect. {i}Prince baka de mes deux.{/i}"

    voice "audio/majordome_3.mp3"
    maj "Désolé monsieur le singe, voilà 450 Yens pour vous dédommager d'être un tel chimpanzé."

    hide baka with moveoutright

    hide maj with moveoutright

    #    *effet transition*
    #(*image devant le bar d’otose de nuit* )

    je "{i}J’ai rien compris de ce qui vient de se passer mais l’important c’est que j’ai l’argent pour le Couthures “à tout faire”.{/i}"
    stop music


    scene bg ruegin
    $ renpy.movie_cutscene("video/jingle.webm")
    pause
    voice "audio/101.mp3"
    pr "Le lendemain chez Gintony."

    #*salon YorozuJean*
    scene bg gin_salon
    show gin_etonne at center with moveinleft
    voice "audio/gin_rien_a_voir.mp3"
    gin "T’es enfin revenu ! Et t’as toujours pas sorti ta merde. D’ailleurs en parlant de ça faudrait que tu nettoie l’intérieur, j’avais encore jamais vu une cabine qui pouvait servir de toilettes."

    "*Je donne les 450Y à Gintony*"
    hide gin_etonne
    show gin_content
    voice "audio/gin_cour_2.mp3"

    gin "Ah, enfin je vais pouvoir m’acheter le JUMP de cette semaine. "
    hide gin_content
    show gin_blase
    voice "audio/gin_moyen.mp3"
    gin "Bon vas-y suis moi, on va chercher le carburant dont j’ai besoin : Le parfait au concerta 54mg LP."

    scene bg ruegin
    with dissolve
    show gin_blase
    voice "audio/gin_moyen_2.mp3"
    gin "Il n’y a qu’une seule personne parmi les Jeans du royaume qui peut me fournir ça sans ordonnance d’un psy. On va devoir aller le voir."
    hide gin_blase with moveoutright
    scene bg parc_gin
    $ renpy.movie_cutscene("video/jingle.webm")

    #*Image Katsuralentin et Gintony
    #*musique Katsura*
    play music "audio/katsurap.mp3" volume 0.4
    show gin_blase_g at left with moveinleft
    voice "audio/gin_oyo.mp3"
    gin "Yo Zuratin ! Ça va ou quoi ?"
    show zura with moveinright
    voice "audio/zura_janai.mp3"
    katsu "ZuraTin djanaï ! Katsuralentin da !"

    #Audio de Katsura qui dit :”Zura djanaï, Katsura da”
    voice "audio/gin_question_courte_2.mp3"
    gin "Si tu veux, si tu veux Zuratin. Est ce que tu as ma dose ?"

    voice "audio/zura_janai.mp3"
    katsu "Comme tu le sais je ne prend que des balles de ping pong."
    hide zura
    hide gin_blase_g
    $ flash_black = Fade(.1, 0, .1, color="#000")
    stop music fadeout 1.0

    scene bg blue with dissolve
    show gin_inquiet
    #*Ecran Gintony brisé*
    play music "audio/gintama_madao.mp3" volume 0.1
    play sound "audio/gin_rien_a_voir.mp3" volume 0.8
    queue sound "audio/gin_rien_a_voir_2.mp3" volume 0.8
    queue sound "audio/gin_rien_a_voir.mp3" volume 0.8
    gin "{i}Je peux pas lui acheter des balles j’ai vraiment besoin de mes 450 Yens, je ne peux pas revenir en arrière..."
    gin "{i}Je vais devoir lui donner mes boules c’est la seule solution."
    gin "{i}Mais j’ai pas envie de perdre mes précieuses boules... ça  doit faire super mal."
    gin "{i}En plus, mon personnage n’aura plus de profondeur et les scénaristes vont me remplacer par un personnage secondaire comme l’autre Madao ou même Zuratin."
    gin "{i}Je vais me retrouver à la rue si je perd ce petit boulot, j’ai déjà pas assez d’argent avec la série."
    gin "{i}Mais je vais leur dire que finalement on annule et qu'au pire le monde peut être détruit c’est pas mes affaires. En plus, je ne le connais même pas ce ..."
    stop sound
    stop music fadeout 1.0
    #*Gintony se fait arracher les boules, on voit une image de 2 balles de ping pong censurés.

    #*Gintony par terre*
    scene bg gin_brisee
    play sound "audio/vol_de_couille.mp3" volume 0.5
    with vpunch
    with flash_black
    with vpunch
    with flash
    show zura with moveinright
    window hide
    pause
    window show
    scene bg parc_gin with dissolve
    play music "audio/gintama_katsura.mp3" volume 0.1
    show zura
    show gin_couilles with moveinbottom:
        xalign 0.0
        yalign 0.60

    voice "audio/zura_janai.mp3"
    katsu "J’espère que tu ne m’en veux pas je me suis servi."

    voice "audio/gin_plie_1.mp3"
    gin "{size=-10}Non pas du tout... Toujours un plaisir de faire affaire avec toi..."

    voice "audio/zura_janai.mp3"
    katsu "Mais j’en ai pas besoin de deux, celle-ci ne sert plus à rien."
    play sound "audio/ecrasement.mp3" volume 0.5

    gin "*Katsuralentin écrase une boule sur le sol* {vspace=30} {size=+5}"
    with vpunch

    play sound "audio/gin_cri.mp3"
    gin"NOOOOONNN !!! Ma précieuse boule..."

    gin "..."

    je "..."

    scen "..."

    voice "audio/gin_plie_2.mp3"
    gin "{size=-10}Je peux avoir mon parfait au concerta 54 mg Lp maintenant ?"
    show parfait behind zura, gin_couilles with zoomin
    voice "audio/zura_janai.mp3"
    katsu "Ah oui tiens, prends le."
    stop music fadeout 1.0

    scene bg gintony_sensei_intro
    $ renpy.movie_cutscene("video/jingle.webm")
    ##*Jingle milieu épisode*
    play sound "audio/gintony_sensei_intro.mp3"
    "GINTONY SENSEIIIIIII !!!!"
    scene bg gintony_sensei_image
    #*Jingle Gintonyyyyyyyyy senseiiiiiiiiiiiiiii*
    $ _skipping = False
    play sound "audio/gintony_sensei_voice.mp3"



    gin_sensei  "Bon, ça faisait longtemps que je n\'avais pas pris de concerta.{w=5.0} {nw}"
    gin_sensei  "Passons directement à la seule question.{w=3.0} {nw}"

    gin_sensei  "Elle provient d’un de mes fans qui vient de France.{w=4.0} {nw}"

    gin_sensei  "Bonjour Gintony, j’aimerai bien sauver la terre de l’invasion de mon peuple, pouvez vous me dire comment faire s’il vous plaît ?{w=18.0} {nw}"

    gin_sensei  "Bien voilà ta réponse.{w=4.0} {nw}"

    gin_sensei  "C’est très simple, tu dois trouver la maison mère Couthures et appuyer sur le bouton.{w=8.0} {nw}"

    gin_sensei  "Si jamais tu te demandes où est la maison mère Couthures, elle est là où elle a toujours été..{w=10.0} {nw}"

    gin_sensei "{font=mikachanALL.ttc}丸字の手書きフォント。同じ部首でも書き方が違かったりと、とてもアバウトでゆるいフォントです。{w=7.0} {nw}"

    scen "Merde qu'est ce qu'il se passe ?!{w=3.0} {nw}"
    gin_sensei "{font=mikachanALL.ttc}しかし、私は私の貴重なボールを失いたくありません…それは多くを傷つけるに違いありません。さらに、私のキャラクターはもはや深みがなく、{w=10.0} {nw}"
    scen "Le stagiaire japonais s'est barré !!! {w=3.0} {nw}"
    gin_sensei "{font=mikachanALL.ttc}作家は私を他のマダオやズラティンのような二次的なキャラクターに置き換えます。{w=7.0} {nw}"

    scen "Merde qu'est qu'on peut mettre ?! Je comprend rien à ce qu'il dit ce con ! {w=4.0} {nw}"
    gin_sensei "{font=mikachanALL.ttc}この奇妙な仕事を失うとホームレスになります。ショーにはまだ十分なお金がありません。{w=7.0} {nw}"
    scen "Vite une idée !!! {w=2.0} {nw}"
    scen "J'ai trouvé !!!{w=2.0} {nw}"
    $ _skipping = True
    gin_sensei  "La maison est au fond de ton cœur ! <3"

    play sound "audio/gintony_sensei.mp3"
    scene bg gintony_sensei_intro
    window hide
    pause
    ###*GINTONY SEENSEI*

    scene bg ruegin
    show gin_content
    voice "audio/gin_moyen_2.mp3"
    gin "Bah tu vois c’était pas si compliqué comme question."

    je "Mais par contre, elle est où en vrai la maison ?"
    hide gin_content with moveoutright


    #*bruit de vomi*

    scene bg ruegin
    show ginrage with moveinright:
        xalign 0.99999999999999999999999999
        yalign 0.18
    voice "audio/gin_cour_1.mp3"
    gin "Bah moi je la vois là, juste retournes toi."

label gintama2:

    scene bg ruegin
    show ginrage1 with moveinleft:
        xalign 0
        yalign 0.18
    voice "audio/gin_question_courte.mp3"
    gin "Non pas comme ça ... Et comment as-tu fait ça ?"

label gintama3:

    scene bg ruegin
    show ginrage2 with moveintop:
        xalign 0.99999999999999999999999999
        yalign 0
    voice "audio/gin_retourner_1.mp3"
    gin "Mais tu le fais exprès ou quoi ? Pourquoi je suis à l’envers ?!"

label gintama4:

    scene bg ruegin
    show ginrage3 with moveintop:
        xalign 0
        yalign 0


    voice "audio/gin_venere.mp3"
    gin "Mais tu te fous de ma gueule ou quoi ? Je sais pas ce que tu fais mais arrête c’est horrible !! Tu veux pas juste te retourner plutôt ?!!"
    scene rue_gin_maison
    show gintony_venere with moveinbottom
    voice "audio/gin_insulte.mp3"
    gin "C’est pas trop tôt ! J’ai envie de vomir maintenant..."
    hide gintony_venere
    show gin_couilles:
        xalign 0.0
        yalign 0.60
    voice "audio/gin_plie_1.mp3"
    gin "Je me sens vraiment pas bien en vrai, mes couilles me manque, tu vas devoir y aller tout seul Patsuan."

    je "Le démon blanc mon cul, c’est vraiment un incapable sans son concerta."
    call screen rue_gin_map

label arc_4:
    scene arc4
    play music "audio/ameno.mp3" volume 0.20

scene arc4
play music "audio/ameno.mp3" volume 0.5
"C'est maintenant ou jamais. Puis cette musique commence vraiment à me souler. J'espère que c'est le dernier arc parce qu'on s'amuse pas beaucoup pour l'instant !"
"De toute façon j'ai fais toutes les pièces de la maison mère Couthures, le bouton pour remonter le temps et sauver le monde doit être ici."


call screen toilette_map with pixellate
