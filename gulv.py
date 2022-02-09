# Få input på rommets lengde og gulvbordets bredde som float
rommets_lengde = float(input("Rommets lengde i CM: "))
gulvbordets_bredde = float(input("Gulvbordets bredde i CM: "))

# Regn ut antall gulvbord som går i rommmets lengde og hent ut desimalene fra resultat
antall_gulvbord_desimal = (rommets_lengde / gulvbordets_bredde) % 1

# Regn ut hvor bredt siste gulvbord blir
siste_gulvbord = gulvbordets_bredde * antall_gulvbord_desimal

# Regn ut ny bredde på første og siste gulvbord
første_og_siste_bord = (gulvbordets_bredde + siste_gulvbord) / 2

# Print resultat
print("Bredde på første og siste bord:", round(første_og_siste_bord, 2), "CM")