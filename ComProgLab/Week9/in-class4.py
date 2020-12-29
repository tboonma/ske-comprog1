import csv

def find_lowest_highest_avg_city_temp(cities_data):
    country_temp = compute_ave_country_temp(cities_data)
    temp_list = []
    country_name = dict()
    for i in country_temp:
        temp_list.append(country_temp[i])
        country_name.update({country_temp[i]:i})
    return [country_name[min(temp_list)], country_name[max(temp_list)]]


def compute_ave_country_temp(cities_data):
    allcountry = dict()
    for i in range(len(cities_data)):
        temp = cities_data[i]
        try:
            temp_list = allcountry[temp['country']]
            temp_list.append(float(temp['temperature']))
            allcountry.update({temp['country']:temp_list})
        except:
            allcountry.update({temp['country']:[float(temp['temperature'])]})
    for i in allcountry:
        allcountry.update({i:sum(allcountry[i])/len(allcountry[i])})
    return allcountry

f = open("cities.csv", encoding="ISO-8859-1")
rows = csv.DictReader(f)
cities_data = []
for i in rows:
    cities_data.append(i)
print(find_lowest_highest_avg_city_temp(cities_data[:11]))
print(find_lowest_highest_avg_city_temp(cities_data[-10:]))
print(find_lowest_highest_avg_city_temp(cities_data))