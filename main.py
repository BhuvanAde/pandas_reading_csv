import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey =len(data[data["Primary Fur Color"]=="Gray"])
black = len(data[data["Primary Fur Color"]=="Black"])
red = len(data[data["Primary Fur Color"]=="Cinnamon"])
# print(grey)
# print(black)
# print(red)
#
# data_dict = {
#     "Fur Color" : ["Gray", "Cinnamon", "Black"],
#     "Count" : [grey, black, red]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("new.csv")

print(pandas.read_csv("new.csv"))
