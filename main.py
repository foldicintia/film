import filmek

filmek_lista=filmek.beolvas()

legrovidebb_index=filmek.legrovidebb(filmek_lista)
print(f"A legrövidebb film: {legrovidebb_index}")

szamlalo=filmek.szaztiz(filmek_lista)
print(f"A 110 percnél rövidebb filmek száma: {szamlalo}")
