
#haal storingen op

lijstVanStoringen = haalStoringenOp()

#bepaal voor elke storing de locatie

bepaalVoorStoringDeLocatie(lijstVanStoringen)

#bepaal de dichstbijzijnde monteur

lijstVanMonteurs = vullenLijstMetMonteurs()
bepaalDichstbijdzijndeMonteur(lijstVanMonteurs, lijstVanStoringen)

#dichtsbijzijnde monteur een bericht met de storing sturen

berichtMonteur = bepaalVoorStoringDeLocatie(lijstVanStoringen)