screen salon :

    imagemap:
        idle "salon"
        hover "salon_hover"

        hotspot (220, 209, 92, 75) clicked Jump("wii_u")
        hotspot (896, 254, 134, 129) clicked Jump("linge")

        if Bool_linge and Bool_wii :
            hotspot (887, 554, 138, 75) clicked Jump("note")
