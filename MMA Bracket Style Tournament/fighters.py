from classes import *

fighter1 = Fighter("Jon Jones", 99, 0) #0 = striker, 1 = grappler
fighter2 = Fighter("Max Holloway", 87, 0)
fighter3 = Fighter("George St. Piere", 96, 0)
fighter4 = Fighter("Connor Mcgreggor", 90, 0)
fighter5 = Fighter("Khabib Nurmagomedhov", 92, 1)
fighter6 = Fighter("Illia Topuria", 93, 0)
fighter7 = Fighter("Demitrius Johnson", 98, 0)
fighter8 = Fighter("Charles Olivera", 89, 1)
fighter9 = Fighter("Justin Gaethje", 85, 0)
fighter10 = Fighter("Alexander Volkanovski", 91, 0)
fighter11 = Fighter("Islam Makachev", 93, 1)
fighter12 = Fighter("Tom Aspinal", 89, 0)
fighter13 = Fighter("Michael Chandler", 79, 0)
fighter14 = Fighter("Maricio Ruffy", 84, 0)
fighter15 = Fighter("Sean Strickland", 86, 0)
fighter16 = Fighter("Khamzat Chimaev", 88, 1)

fighters = [fighter1, fighter2, fighter3, fighter4, fighter5, fighter6, fighter7, fighter8, fighter9, fighter10, fighter11, fighter12, fighter13, fighter14, fighter15, fighter16]

seededfighters = sorted(fighters, key=lambda x: x.skillLevel, reverse=True)
