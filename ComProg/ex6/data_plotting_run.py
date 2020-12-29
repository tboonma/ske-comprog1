import data_processing as dp
import matplotlib.pyplot as plt

# Scatter plot of cities showing latitudes versus temperatures
x = []
y = []
for city in dp.cities_data:
    x.append(float(city['latitude']))
    y.append(float(city['temperature']))
plt.xlabel('latitude')
plt.ylabel('temperature')
plt.scatter(x, y)
plt.show()

# Bar chart showing average temperatures of all cities in each country
bars = []  # list of countries
temperature = []  # average temperature of each country
dict = dp.average_country_temp(dp.cities_data)
for key, value in dict.items():
    bars.append(key)
    temperature.append(value)

numbars = len(bars)
width = .75
plt.bar(range(numbars), temperature, width, align='center')
plt.xlabel('country')
plt.ylabel('temperature')
plt.xticks(range(numbars), bars, rotation='vertical')
print(bars)
print(temperature)
plt.show()

# Pie chart showing number of EU countries versus non-EU countries
numEU = 0
numNotEU = 0
for country in dp.countries_data:
    if country['EU'] == 'yes':
        numEU += 1
    else:
        numNotEU += 1
plt.pie([numEU, numNotEU], labels=['EU', 'not EU'], autopct='%1.1f%%')
plt.show()

# Bar chart showing population of countries that are in EU but do not have coastline

# your code here
EU_countries_name = list(dp.population_countries_no_coastline_in_EU(dp.countries_data).keys())
EU_countries_pop = list(dp.population_countries_no_coastline_in_EU(dp.countries_data).values())
numbars = len(EU_countries_name)
plt.bar(range(numbars), EU_countries_pop, .50, align="center")
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(range(numbars), EU_countries_name)
plt.title('Population of countries that are in EU but do not have coastline')
print(EU_countries_name)
print(EU_countries_pop)
plt.show()

# Pie chart showing number of EU cities versus non-EU cities

# your code here
all_cities = list(dp.cities_in_EU(dp.cities_data, dp.countries_data).values())
eu_cities = all_cities.count('yes')
not_eu = all_cities.count('no')
plt.pie([eu_cities, not_eu], labels=['EU', 'Not EU'], autopct='%1.1f')
plt.title("EU cities vs. non-EU cities")
print(eu_cities)
print(not_eu)
plt.show()

# Scatter plot of players showing minutes played versus passes made;
# color each player based on their position (goalkeeper, defender, midfielder, forward)

# your code here
passes = []
mins = []
pos = []
pos_name = ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']
i = 1
for player in dp.players_data:
    passes.append(float(player['passes']))
    mins.append(float(player['minutes']))
    if player['position'] == 'goalkeeper':
        pos.append(1)
    elif player['position'] == 'defender':
        pos.append(2)
    elif player['position'] == 'midfielder':
        pos.append(3)
    elif player['position'] == 'forward':
        pos.append(4)
    i += 1
plt.scatter(passes, mins, c=pos)
plt.xlabel('Passes')
plt.ylabel('Minutes played')
# plt.colorbar().ax.set_title('position')
cb = plt.colorbar()
tick_pos = [1, 2, 3, 4]
cb.set_ticks(tick_pos)
cb.set_ticklabels(pos_name)
cb.ax.set_title('Position')
plt.title('Players passes minutes played vs. passes made')
plt.show()

# Bar chart showing average number of passes made by each player postion (defender, midfielder, forward, goalkeeper)

# your code here
bars = ['defender', 'midfielder', 'forward', 'goalkeeper']
avg_pass = dp.average_passes(dp.players_data)
plt.bar(range(len(bars)), avg_pass, width=0.5, align='center')
plt.xlabel('Position')
plt.ylabel('Average passes')
plt.xticks(range(len(bars)), bars)
print(bars)
print(avg_pass)
plt.title('Average number of passes made by each player postion')
plt.show()

# Bar chart showing the survival rate in each passenger class; the three bars should be labeled 'first', 'second', 'third'

# your code here
bars = ['First', 'Second', 'Third']
survive_rate = [dp.class_survival_rate(1, dp.titanic_data), dp.class_survival_rate(2, dp.titanic_data),
                dp.class_survival_rate(3, dp.titanic_data)]
plt.bar(range(len(bars)), survive_rate, width=0.5, align='center')
plt.xlabel('Passenger class')
plt.ylabel('Survival rate')
plt.xticks(range(len(bars)), bars)
print(bars)
print(survive_rate)
plt.title('survival rate in each passenger class')
plt.show()

# Pie chart showing the number of male survivors versus female survivors

# your code here
male_survive = dp.gender_survival_number('M', dp.titanic_data)
female_survive = dp.gender_survival_number('F', dp.titanic_data)
plt.pie([male_survive, female_survive], labels=['Male', 'Female'], autopct='%1.1f')
print(male_survive)
print(female_survive)
plt.title('Number of male survivors vs. female survivors')
plt.show()
