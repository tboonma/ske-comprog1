import csv
import statistics

# open Cities.csv file with csv.DictReader and read its content into a list of dictionary, cities_data
cities_data = []
with open('Cities.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)

# open Countries.csv file with csv.DictReader and read its content into a list of dictionary, countries_data
countries_data = []
with open('Countries.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries_data.append(r)


def min_max_temp(cities_data):
    """Returns a list whose first and second elements are the min and the max temperatures of all the
    cities in cities_data.
    """
    temps = []
    for r in cities_data:
        temps.append(float(r['temperature']))
    return [min(temps), max(temps)]


def country_list(cities_data):
    """Returns a list of all the countries represented in cities_data.
    """
    countries = []
    for r in cities_data:
        if r['country'] not in countries:
            countries.append(r['country'])
    return countries


def average_country_temp(cities_data):
    """
    Return a dictionary whose key:value pair is country name:its average temp. The size of the
    returned dictionary must equal the number of countries represented.
    """
    d = dict()
    for country in country_list(cities_data):
        t = []
        for r in cities_data:
            if r['country'] == country:
                t.append(float(r['temperature']))
        d[country] = sum(t) / len(t)
    return d


def country_max_diff_temperature(cities_data):
    """Returns a tuple with information about a country whose minimum and maximum city temperatures differ the most in the following format: (the country whose minimum and maximum city temperatures differ the most, min temperature, max temperature, max temperature - min temperature)
    """
    country_temp = dict()
    for country in cities_data:
        try:
            temp = country_temp[country['country']]
            temp.append(float(country['temperature']))
            country_temp.update({country['country']: temp})
        except:
            country_temp.update({country['country']: [float(country['temperature'])]})
    max_diff = int()
    max_diff_info = []
    for i in country_temp:
        temp = round(max(country_temp[i]) - min(country_temp[i]), 14)
        if temp > max_diff:
            max_diff = temp
            max_diff_info = [i, min(country_temp[i]), max(country_temp[i]), temp]
    return tuple(max_diff_info)


def northern_sounthern_most_cities(cities_data):
    """Returns a list of tuples with information about the northernmost and southernmost cities together with their associated countries in the following format: [(northernmost city, its country), (southernmost city, its country)]
    """
    northmost = -90.00
    southmost = 90.00
    for city in cities_data:
        if float(city['latitude']) > northmost:
            northmost = float(city['latitude'])
            northernmost = (city['city'], city['country'])
        if float(city['latitude']) < southmost:
            southmost = float(city['latitude'])
            southernmost = (city['city'], city['country'])
    return [northernmost, southernmost]


def population_countries_no_coastline_in_EU(countries_data):
    """Returns a dictionary whose keys are countries in EU but do not have coastline; the value associated with each key is the population of that country
    """
    country_pop = dict()
    for country in countries_data:
        if country['EU'] == 'yes' and country['coastline'] == 'no':
            country_pop.update({country['country']: float(country['population'])})
    return country_pop


def cities_in_EU(cities_data, countries_data):
    """Returns a dictionary whose key:value pair is "name of city":"EU membership", e.g., "Graz":"yes" or 'Aalborg':'no'; the size of the dictionary must equal the number of cities represented in cities_data
    """
    cities_eu = dict()
    # Hint:
    # Use nested for in loops to generate the dictionary:
    #
    for city in cities_data:
        for country in countries_data:
            if city['country'] == country['country']:
                cities_eu.update({city['city']: country['EU']})
                break
    return cities_eu

# for i in range(len(cities_data)):
#     if

def average_EU_city_temperature(cities_data, countries_data):
    """Returns a tuple with two elements: (the average temperature of all the cities in EU countries, the average temperature of all the cities not in EU countries)
    """
    avg_eu_temp = [[], []]
    for city in cities_data:
        for country in countries_data:
            if city['country'] == country['country']:
                if country['EU'] == 'yes':
                    avg_eu_temp[0].append(float(city['temperature']))
                else:
                    avg_eu_temp[1].append(float(city['temperature']))
    temp = statistics.mean(avg_eu_temp[0])
    temp2 = statistics.mean(avg_eu_temp[1])
    avg_city_temp = (temp, temp2)
    return avg_city_temp


# open Players.csv file with csv.DictReader and read its content into a list of dictionary, players_data
players_data = []
with open('Players.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        players_data.append(r)

# open Teams.csv file with csv.DictReader and read its content into a list of dictionary, teams_data
teams_data = []
with open('Teams.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        teams_data.append(r)


def average_passes(players_data):
    """Returns a tuple with four elements; the first, second, third, and fourth elements show the average number of passes made by defenders, midfielders, forwards, and goalkeepers, respectively
    """
    players_passes = [[], [], [], []]
    for player in players_data:
        if player['position'] == 'defender':
            players_passes[0].append(float(player['passes']))
        elif player['position'] == 'midfielder':
            players_passes[1].append(float(player['passes']))
        elif player['position'] == 'forward':
            players_passes[2].append(float(player['passes']))
        elif player['position'] == 'goalkeeper':
            players_passes[3].append(float(player['passes']))
    for i in range(len(players_passes)):
        players_passes[i] = statistics.mean(players_passes[i])
    return tuple(players_passes)


def max_GF_GA_ratio(teams_data):
    """Returns the string name of a team with highest ratio of goalsFor to goalsAgainst
    """
    max_ratio = float()
    for team in teams_data:
        if float(team['goalsFor']) / float(team['goalsAgainst']) > max_ratio:
            max_team = team['team']
            max_ratio = float(team['goalsFor']) / float(team['goalsAgainst'])
    return max_team


def whose_player_list(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a player who is on a team ranked in the top 20, plays less than 200 minutes and makes more than 100 passes; the format for each tuple is (player's surname, team played for, team ranking, minutes played, number of passes)
    """

    # Reminder: Convert minutes and passes to integers before comparing to values
    player_list = []
    for team in teams_data:
        if int(team['ranking']) > 20:
            continue
        for player in players_data:
            if player['team'] == team['team'] and int(player['minutes']) < 200 and int(player['passes']) > 100:
                player_list.append((player['surname'], player['team'], int(team['ranking']), int(player['minutes']),
                                    int(player['passes'])))
    return player_list


def team_list_passes_per_minute(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a team and its passes per minute value generated by its players
    """
    team_passes = dict()
    team_minutes = dict()
    team_ppm = []
    for player in players_data:
        try:
            team_passes.update({player['team']: team_passes[player['team']] + int(player['passes'])})
            team_passes.update({player['team']: team_passes[player['team']] + int(player['minutes'])})
        except:
            team_passes.update({player['team']: int(player['passes'])})
            team_minutes.update({player['team']: int(player['minutes'])})
    for team in team_passes:
        team_ppm.append((team, team_passes[team] / team_minutes[team]))
    return team_ppm


# open Titanic.csv file with csv.DictReader and read its content into a list of dictionary, titanic_data
titanic_data = []
with open('Titanic.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        titanic_data.append(r)


def number_married_women_embarked(place_embarked, age_threshold, titanic_data):
    """Returns the number of married women over age_threshold embarked at place_embarked

    Your test code must include at least five test cases with different combinations of place_embarked and age_threshold
    >>> number_married_women_embarked('Southampton', 20, titanic_data)
    96
    >>> number_married_women_embarked('Cherbourg', 18, titanic_data)
    101
    >>> number_married_women_embarked('Cherbourg', 40, titanic_data)
    38
    >>> number_married_women_embarked('Queenstown', 30, titanic_data)
    68
    >>> number_married_women_embarked('Cherbourg', 'n', titanic_data)
    Traceback (most recent call last):
        ...
    TypeError: Value Error
    """
    if not isinstance(place_embarked, str) or not isinstance(age_threshold, int) or not isinstance(titanic_data, list):
        raise TypeError('Value Error')
    number = 0
    for passenger in titanic_data:
        try:
            if passenger['gender'].upper() == 'M':
                continue
            if float(passenger['age']) < age_threshold:
                continue
            if passenger['first'].title().startswith('Mrs'):
                number += 1
        except:
            continue
    return number


def class_survival_rate(passenger_class, titanic_data):
    """Returns the survival rate of a given passenger_class

    Your test case must test all the three passenger classes
    >>> class_survival_rate(1, titanic_data)
    62.96296296296296
    >>> class_survival_rate(2, titanic_data)
    47.28260869565217
    >>> class_survival_rate(3, titanic_data)
    24.236252545824847
    >>> class_survival_rate(4, titanic_data)
    Traceback (most recent call last):
        ...
    Exception: No passenger in this class
    """
    all_passengers = 0
    survived = 0
    for passesnger in titanic_data:
        if int(passesnger['class']) == passenger_class:
            if passesnger['survived'] == 'yes':
                survived += 1
            all_passengers += 1
    if all_passengers <= 0:
        raise Exception('No passenger in this class')
    return survived / all_passengers * 100


def gender_survival_number(passenger_gender, titanic_data):
    """Returns the number of survivors for a given gender, M (male) or F (female)

    Your test case must test both genders
    >>> gender_survival_number('F', titanic_data)
    233
    >>> gender_survival_number('M', titanic_data)
    109
    >>> gender_survival_number('m', titanic_data)
    109
    >>> gender_survival_number(1, titanic_data)
    Traceback (most recent call last):
        ...
    Exception: Gender must be M or F
    """
    if not isinstance(passenger_gender, str):
        raise Exception('Gender must be M or F')
    number = 0
    for passenger in titanic_data:
        if passenger['gender'].upper() == passenger_gender.upper() and passenger['survived'] == 'yes':
            number += 1
    return number


def twin_list(titanic_data):
    """Returns a list of tuples of pairs of passengers who are likely to be twin children, i.e., same last name, same age, same place of embarkment, and age is under 18; each tuple has the following format: (person1's "last name" + "first name", person2's "last name" + "first name")
    """
    twin = []
    for i in range(len(titanic_data)):
        for next_passenger in titanic_data[i + 1:]:
            try:
                if titanic_data[i]['last'] == next_passenger['last'] and float(titanic_data[i]['age']) < 18:
                    if titanic_data[i]['age'] == next_passenger['age'] or titanic_data[i]['embarked'] == next_passenger[
                        'embarked']:
                        twin.append((titanic_data[i]['last'] + ', ' + titanic_data[i]['first'],
                                     next_passenger['last'] + ', ' + next_passenger['first']))
            except:
                continue
    return twin


if __name__ == "__main__":
    import doctest

    doctest.testmod()
