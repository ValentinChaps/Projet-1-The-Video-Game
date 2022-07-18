init:
    $ style.default.font = "mikachanALL.ttf"
    $ style.default.language = "eastasian"

# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Menu devellopeur : shift + D (jeu lancé)
# Recharger le jeu ouvert : shift + R

# Déclarez les personnages utilisés dans le jeu.
define Ant = Character('Anthony', color="#c8ffc8")
define pe = Character('Percenoob', color="#c8ffc8")
define Val = Character('Judas', color="#c8ffc8")
define Rob = Character('Robin', color="#c8ffc8")
define ka = Character('Karamouille', color="#c8ffc8")
define je = Character('Moi', color="#c8ffc8")
define pr = Character('Prof Narrateur 1' , color="#c8ffc8")
define un = Character('Un rageux qui perd sa game de LOL')
define me = Character('Merlirobin')
define jei = Character('Moi' , what_italic=True)
define bu = Character('Judas, Roi Burgonde')
define vn = Character('Le fameux porc silver 2')
define jf = Character('Moi du futur')
define mei = Character('Merlirobin' , what_italic = True)
define shin = Character('Jerepanchi')
define scen = Character('Les Scénaristes')
define gin = Character('Gintony')
define maj = Character('Majordome')
define baka = Character('Prince Baka')
define katsu = Character('Zuralentin')
define gin_sensei = Character('Gintony Seinsei !!!', who_outlines=[( 1.5, "#000000", 0, 0 )] , what_outlines=[( 2, "#000000", 0, 0 )] , window_background=None , what_xalign=0.5, what_textalign=0.5, what_layout='subtitle' )

define shini = Character('Jerepanchi' ,  what_italic = True)
define di = Character('Jeremy Christ, alias J.C. dans le milieu')
define dr = Character('Docteure Camouille')
define rb = Character('LGBT++ Mark 2.69')
define cr = Character('Homme de Jeanmagnon')
define az = Character('Rilexia Dorsong')
define os = Character('Oui ce sont bien des os qui parlent')
define db = Character('Docteure LGBT++ Camouille Version 69.69')
define aur = Character('Aurelius Maximus Aramus Couthurus')
# Le jeu commence ici
label start:

    jump introduction
    jump chapitre_1
    jump chapitre_2
    jump chapitre_3
    jump chapitre_4
    jump arc_final
    jump generic_fin
    return

#BG

image bg white = "images/BG/white.png"
image bg parc_devant = "images/BG/parc.png"
image bg pong field= "images/BG/pong_field.png"
image bg salon = "images/BG/salon.png"
image bg salon_hover = "images/BG/salon_hover.png"
image bg juetc = "images/BG/juetc.png"
image bg intechat = "images/BG/intechateau.png"
image bg fondmerlin = "images/BG/fondmerlin.png"
image bg pelerin = "images/BG/pelerin_jeremy.png"
image bg lab = "images/BG/fond_labo.png"
image bg delab = "images/BG/labo_delabre.png"
image bg fouille = "images/BG/fouille.png"
image bg ruegin = "images/BG/fondruegin1.png"
image bg gin_salon = "images/BG/gin_salon.png"
image bg fac = "images/BG/fac.png"
image bg bar_otose = "images/BG/bar.png"
image bg parc_gin = "images/BG/parc_gin.png"
image bg gin_brisee = "images/BG/gin_brisee.png"
image bg tardis = "images/BG/tardis_interior.png"
image bg gintony_sensei_intro = "images/BG/gintony_sensei_intro.png"
image bg gintony_sensei_image = "images/BG/gintony_sensei.png"
image bg blue = "images/BG/blue.png"
image bg boss = "images/BG/fond_boss.png"
image bg ruegin_maison = "images/BG/rue_gin_maison.png"


image bg cuisine = "images/BG/cuisine.png"
image bg cuisine_pong = "images/BG/cuisine_pong.png"
image bg piece_haut = "images/BG/piece_haut.png"
image bg piece_haut_robot = "images/BG/piece_haut_robot.png"


image arc1 = "images/BG/arc1.png"
image arc2 = "images/BG/arc2.png"
image arc3 = "images/BG/arc3.png"
image arc4 = "images/BG/arc4.png"
#Personnages

image prof =  "Image_professeur.png"
image porckam = "Porc_mongol.png"
image merlin = "merlin.png"
image note = "note.png"
image table1 = "table1.png"
image ginrage = "gintonyrage.png"
image ginrage1 = "gintonyrage1.png"
image ginrage2 = "gintonyrage2.png"
image ginrage3 = "gintonyrage3.png"
image robot = "robot_lgbt.png"
image dr = "camille_doc.png"
image jdufut = "jdufut1.png"
image tar = "TARDIS.png"
image cave = "cave.png"
image alex = "alex2.png"
image dieu = "jeremy_dieu.png"
image robcam = "robot_camouille.png"

image baka = "images/baka.png"
image maj = "images/majordome.png"
image maj_venere = "images/majordome_venere.png"
image gin_venere = "images/gintony_venere.png"
image gin_etonne = "images/gintony_etonne.png"
image gin_blase = "images/gintony_blase.png"
image gin_blase_g = "images/gintony_blase_g.png"
image gin_content = "images/gintony_content.png"
image zura = "images/zura.png"
image aur = "aurelius.png"
image gin_couilles = "images/gin_couilles.png"
image gin_inquiet = "images/gintony_inquiet.png"
image parfait = "images/parfait_au_concerta.png"
#Films
image trailer = Movie(play="trailer.webm")
image park = Movie(play="paarmelott.webm")
image pongvid = Movie(play="pongvid.webm")
image dino = Movie(play="dino.webm")




#Audio
