import csv

# get data file
data_file = list(csv.reader(open("guns.csv","r")))

# get data header
header = data_file[:1] 

# print header
print("1- Header : " + str(header) +"\n")

# get data without header
data = data_file[1:] 

# print firsts 5 guns data without header
print("2- First 5 guns data without header : " + str(data[:5]) +"\n")

# get and print number of deaths per year
years = [row[1] for i, row in enumerate(data)] 
year_counts = {}
for year in years:
    if year  not in year_counts:
        year_counts[year] = 0
    year_counts[year] += 1
    
print("3- Number of deaths per year : " + str(year_counts) +"\n")

# get and print number of deaths per month
import datetime

dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day = 1) for row in data]
dates_counts ={}
for date in dates:
    if date not in dates_counts:
        dates_counts[date] = 0
    dates_counts[date] += 1
    
print("4- Firsts 5 of deaths per month : " + str(dates_counts) +"\n")

# get and print number of deaths per sexe
sexes = [row[5] for row in data]
sexes_counts ={}
for sexe in sexes:
    if sexe not in sexes_counts:
        sexes_counts[sexe] = 0
    sexes_counts[sexe] += 1

print("5- Number of deaths per sexe : " + str(sexes_counts) +"\n")   

# get and print number of deaths per race
races = [row[7] for row in data]
races_counts ={}
for race in races:
    if race not in races_counts:
        races_counts[race] = 0
    races_counts[race] += 1

print("6- Number of deaths per race : " + str(races_counts) +"\n")   

# Calculte and  print ratio of deaths per race 
us_races_population = list(csv.reader(open("census.csv","r")))
mapping = {"Asian/Pacific Islander": int(us_races_population[1][14]) + int(us_races_population[1][15]), "White": int(us_races_population[1][10]) , "Native American/Native Alaskan": int(us_races_population[1][13]), "Black": int(us_races_population[1][12]), "Hispanic": int(us_races_population[1][11])}
races_ratio = {}
for k, v in races_counts.items():
    races_ratio[k] = (v / int(mapping[k])) * 100000

print("7- Ratio of deaths per race for 100 000 persons: " + str(races_ratio) +"\n")

# get and print homicide per race
intents = [row[3].lower()  for row in data]
races = [row[7] for row in data]
homicide_counts = {}
for  i, race in enumerate(races):
    if intents[i] == 'homicide':
        if race not in homicide_counts:
            homicide_counts[race] = 0
        homicide_counts[race] += 1    

print("8- Homicide per race: " + str(homicide_counts) +"\n")   

# Calculte and  print ratio of homicide per race 
homicide_ratio = {}
for k, v in homicide_counts.items():
    homicide_ratio[k] = (v / int(mapping[k])) * 100000

print("9- Ratio of homicide per race for 100 000 persons: " + str(homicide_ratio) +"\n")
