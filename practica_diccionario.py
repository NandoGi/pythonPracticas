midiccionario={"Francia":"Paris", "Alemania":"Berlin", "Peru":"Lima", "Colombia":"Bogota" }
midiccionario["Italia"]="Roma"
midiccionario1={2:"Francia", "Ecuador":1, "Bolivia":"La Paz"}
print(midiccionario1.keys())
print(midiccionario1.values())
print(len(midiccionario1))
print(midiccionario["Peru"])
print(midiccionario)
del midiccionario["Francia"]
print(midiccionario)
print(midiccionario1[2])
mitupla=("Chile", "Argentina", "Usa")
midiccionario2={mitupla[0]:"Santiago", mitupla[1]:"Buenos Aires", mitupla[2]:"Washintong"}
print(midiccionario2)
midiccionario3={89:"vida", "Cuero":"Vaca", "Campeones futbol":{"temporadas":[2000,2001,2002,2003]}}
print(midiccionario3["Campeones futbol"])