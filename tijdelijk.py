prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
reclame_tekst="Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding:.2f}"
reclame_tekst3=(reclame_tekst.format(aanbieding = prijzen["vanille"]*0.8))
reclame_tekst3=(reclame_tekst3.upper())
reclame_tekst4=(reclame_tekst3.split())
#print(reclame_tekst4)
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())