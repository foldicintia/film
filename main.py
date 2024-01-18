import filmek

filmek_lista=filmek.beolvas()

legrovidebb_index=filmek.legrovidebb(filmek_lista)
print(f"A legrövidebb film: {filmek_lista[legrovidebb_index].cim}")

szamlalo=filmek.szaztiz(filmek_lista)
print(f"A 110 percnél rövidebb filmek száma: {szamlalo}")  

valasz= filmek.szinesz_bekeres(filmek_lista)

filmek.kiiras(valasz)



