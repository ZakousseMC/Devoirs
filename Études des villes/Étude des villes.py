from math import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ville = pd.read_csv("villes_virgule.csv", sep = ",")
ville.info()

"""
#----------------------------------------------------------------------------------
ville_dens = ville.loc[ville["dep"]!="alpha",["nom", "dens"]].pivot_table(index="nom").fillna(0)
ville_dens = ville_dens.sort_values(by=["dens"], ascending=False)
print(ville_dens)
#----------------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------------
ville["evo"]= (ville["nb_hab_2012"]-ville["nb_hab_2010"])/ville["nb_hab_2010"]
ville_evo = ville.loc[ville["dep"]!="alpha",["nom", "evo"]].pivot_table(index="nom").fillna(0)
ville_evo = ville_evo.sort_values(by=["evo"], ascending=False)
print(ville_evo)
#----------------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------------
ville["evo"]= (ville["nb_hab_2012"]-ville["nb_hab_2010"])/ville["nb_hab_2010"]
ville_evo = ville.loc[ville["nb_hab_2010"]>=1000,["nom", "evo"]].pivot_table(index="nom").fillna(0)
ville_evo = ville_evo.sort_values(by=["evo"], ascending=False)
print(ville_evo)
#----------------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------------
ville["evo2"]= (ville["nb_hab_2012"]-ville["nb_hab_1999"])/ville["nb_hab_1999"]
ville_evo_beta = ville.loc[ville["dep"]!="alpha",["nom", "evo2"]].pivot_table(index="nom").fillna(0)
ville_evo_beta = ville_evo_beta.sort_values(by=["evo2"], ascending=False)
print(ville_evo_beta)
ville["evo2"]= (ville["nb_hab_2012"]-ville["nb_hab_1999"])/ville["nb_hab_1999"]
ville_evo_beta = ville.loc[ville["nb_hab_2010"]>=1000,["nom", "evo2"]].pivot_table(index="nom").fillna(0)
ville_evo_beta = ville_evo_beta.sort_values(by=["evo2"], ascending=False)
print(ville_evo_beta)
#----------------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------------
ville_dep = ville.loc[ville["lat"]!="NA",["dep", "nb_hab_2012"]].pivot_table(index="dep", aggfunc=sum).fillna(0)
ville_dep = ville_dep.sort_values(by=["nb_hab_2012"], ascending=False)
print(ville_dep)
#----------------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------------
ville_dep_beta = ville.loc[ville["lat"]!="NA",["dep", "nom"]].pivot_table(index="dep", aggfunc=len).fillna(0)
ville_dep_beta= ville_dep_beta.sort_values(by=["nom"], ascending=False)
print(ville_dep_beta)
#----------------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------------
ville_alt_min = ville.loc[ville["lat"]!="NA",["dep", "alt_min"]].pivot_table(index="dep").fillna(0)
ville_alt_min = ville_alt_min.sort_values(by=["alt_min"], ascending=False)
print(ville_alt_min)
#----------------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------------
ville["evo"]= (ville["nb_hab_2012"]-ville["nb_hab_2010"])/ville["nb_hab_2010"]
ville_evo = ville.loc[ville["dep"]!="alpha",["nom", "evo"]].pivot_table(index="nom").fillna(0)
ville_evo = ville_evo.sort_values(by=["evo"], ascending=False)
print(ville_evo)
ville_evo = ville.loc[ville["lat"]!="NA",["dep", "evo"]].pivot_table(index="dep").fillna(0)
ville_evo = ville_evo.sort_values(by=["evo"], ascending=False)
print (ville_evo)
#----------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------
ville["alt_moy"]= round((ville["alt_min"] + ville["alt_max"])/2)
ville_alt_moy = ville.loc[ville["dep"]!="alpha",["nb_hab_2012", "alt_moy"]].pivot_table(index="nb_hab_2012").fillna(0)
print(ville_alt_moy)
plt.plot(ville_alt_moy)
plt.show()

