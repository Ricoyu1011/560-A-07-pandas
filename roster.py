# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player = {"Last Name": ["Cadeau", "Ryan", "Davis"],
          "First Name": ["Elliot", "Cormac", "RJ"],
          "Height": [73, 77, 72],
          "Weight": [180, 195, 180]}


data = pd.DataFrame(player)

#bmi
data["bmi"] = ((data["Weight"])/((data["Height"]))**2) * 703

print(data)

data.to_csv("bmi.csv")