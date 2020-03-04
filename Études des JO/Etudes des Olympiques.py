import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

olymp = pd.read_csv("athlete_events.csv", sep = ";") #Charge le fichier sous le nom olympics.

"""
#----------------------------------------------------------------------------------
#Quelle a été l'évolution du nombre d'athlètes aux JO d'été depuis leur création ?
olymp_name_total = olymp.loc[olymp["Season"]!="NA",["Name", "Year"]].pivot_table(index="Year", aggfunc=len).fillna(0)
print(olymp_name_total) #Vérification
#Sur le même graphique (si possible) : quelle a été l'évolution du nombre d'athlètes aux JO d'hiver depuis leur création ?
olymp_name_winter = olymp.loc[olymp["Season"]=="Winter",["Name", "Year"]].pivot_table(index="Year", aggfunc=len).fillna(0)
print(olymp_name_winter) #Vérification
#Affichage du graphique.
dataframe = pd.concat([olymp_name_total, olymp_name_winter], axis=1)
dataframe = dataframe.plot()
plt.show()
#On constate notammment des sortes de montées et descente à partir de 1994. Cette date correspond à la séparation en saisons des Jeux. (Hiver - Été).
#Par ailleurs, on constate que la courbe orange (hiver) semble disparaître à partir de 1994. Elle ne disparait pas, seulement, les deux courbes sont superposées.
#----------------------------------------------------------------------------------
"""


"""
#----------------------------------------------------------------------------------
#Quelle a été l'évolution du nombre de femmes aux JO d'été depuis leur création ?
olymp_femme_total = olymp.loc[olymp["Sex"]=="F",["Name", "Year"]].pivot_table(index="Year", aggfunc=len).fillna(0)
print(olymp_femme_total)
olymp_femme_total.plot()
plt.show()
#Le nombre de femmes a beaucoup augmenté.
#----------------------------------------------------------------------------------
"""


"""
#----------------------------------------------------------------------------------
#Quelle a été l'évolution du nombre de disciplines aux JO d'été depuis leur création ?
olymp_discipline_total = olymp.loc[olymp["Season"]=="Summer",["Year", "Sport"]].pivot_table(index="Year", aggfunc="nunique").fillna(0)
olymp_discipline_total = olymp_discipline_total.drop(columns="Year") #Suppression de la colonne "Year" qui est une constante.
print(olymp_discipline_total) #Vérification
olymp_discipline_total.plot(style="bo", markersize="3")
plt.show()
#Le nombre de disciplines à lui aussi augmenté dans le binks.
#----------------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------------
#Il est aussi intéressant de voir le nombre de médailles gagnées par chaque pays au total des années.
olymp_medal = olymp.loc[olymp["Year"]!="NA",["Team", "Medal"]].pivot_table(index="Team", columns="Medal", aggfunc=len).fillna(0)
olymp_medal = olymp_medal.sort_values(by=["Gold"], ascending=False)
print(olymp_medal)
#Cependant, le nombre de médailles gagnées n'est pas forcément très utile, effectivement, un pays participant 
#à plus de disciplines peut avoir plus de médailles assez facilement.
#Il est donc préférable d'avoir un ratio.
#Voici donc une visualisation avec l'année 2012.
olymp_medal = olymp.loc[olymp["Year"]==2012,["Team", "Medal"]].pivot_table(index="Team", columns="Medal", aggfunc=len).fillna(0)
olymp_medal = olymp_medal.sort_values(by=["Gold"], ascending=False)
olymp_name = olymp.loc[olymp["Year"]==2012,["Team", "Name"]].pivot_table(index="Team", aggfunc="nunique").fillna(0).loc[:,["Name"]]
olymp_name = olymp_name.sort_values(by=["Name"], ascending=True)
dataframe = pd.concat([olymp_medal, olymp_name], axis=1).fillna(0)
dataframe = dataframe.div(dataframe["Name"], axis=0).fillna(0).sort_values(by="Gold") #Ratio entre les victoires et les participations.
print(dataframe)
#On constate qu'au final, l'équipe Olympique avec le meilleur ratio en 2012 et celle de Chine.
#----------------------------------------------------------------------------------
"""