import filmek

filmek_lista=filmek.beolvas()



legrovidebb_index=filmek.legrovidebb(filmek_lista)
print(f"A legrövidebb film: {filmek_lista[legrovidebb_index].cim}")

# szamlalo=filmek.szaztiz(filmek_lista)
# print(f"A 110 percnél rövidebb filmek száma: {szamlalo}")  --->  nem tetszik neki a >= mert azt állítja hogy az egyik string a masik int és igy nem tudja elvegezni a dolgat :(

talalatok=filmek.szinesz_bekeres(filmek_lista)
# else ágon nem csak egyszer írja ki a kiírnivalóját :(
