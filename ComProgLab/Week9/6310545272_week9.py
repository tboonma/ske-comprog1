# 1.1
# import csv
# cities_data = []
# f = open('cities.csv', encoding="ISO-8859-1")
# rows = csv.reader(f)
# for i in rows:
#     cities_data.append(i)
# # print(cities_data[0:10])
# # print(cities_data[8:10])

# 1.2
import csv
cities_data = []
with open('cities.csv',encoding="ISO-8859-1") as f:
    rows = csv.DictReader(f) 
    for r in rows:
        cities_data.append(r) 
# print(cities_data[0:10]) 
# print(cities_data[8:10])

# 2
# city_temp_tuple = []
# for i in range(1,len(cities_data)):
#     city_temp_tuple.append((cities_data[i][0],float(cities_data[i][4])))
# print(city_temp_tuple)

# 3
def list_countries(cities_data):
    countries = []
    for i in range(len(cities_data)):
        temp = cities_data[i]
        if temp['country'] not in countries:
            countries.append(temp['country'])
    return countries


# countries = list_countries(cities_data) 
# print(len(countries))
# print(countries)

# 4
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

# country_temps = compute_ave_country_temp(cities_data) 
# print(len(country_temps))
# print(country_temps)

# 5
import matplotlib.pyplot as plt

def read_file(filename):
    f = open(filename, encoding="ISO-8859-1")
    rows = csv.DictReader(f)
    cities_data = []
    for i in rows:
        cities_data.append(i)
    return cities_data

def extract_to_list(data,name):
    lst = []
    for country in data:
        lst.append(float(country[name]))
    return lst

# cities_data = read_file('cities.csv')
# lat = extract_to_list(cities_data,'latitude') 
# long = extract_to_list(cities_data,'longitude') 
# temps = extract_to_list(cities_data,'temperature') 
# high = extract_to_list(cities_data,'highest')
# # Plot scatter plot using x = latitude,
# # y = temperature,
# # color=longitude 
# plt.scatter(lat,temps,c=long)
# # Add x-axis label 
# plt.xlabel('Latitude')
# # Add y-axis label 
# plt.ylabel('Temperatures')
# # Add label for color bar 
# plt.colorbar().ax.set_title('Longtitude') 
# # Save plot as image file 
# plt.savefig('lat_temps_long.png')
# # Show plot
# plt.show()

# plt.scatter(long,temps,c=lat) 
# plt.xlabel('Longitude') 
# plt.ylabel('Temperatures') 
# plt.colorbar().ax.set_title('Latitude') 
# # Set colormap to the selected one
# # See more colormap selection in the reference at the end of Exercise 5
# plt.set_cmap('RdBu')
# plt.savefig('long_temps_lat.png')
# plt.show()

# 6
def count_region_freq(cities_data):
    region_list = []
    region_freq_list = []
    for country in cities_data:
        if country['region'] in region_list:
            pos = region_list.index(country['region'])
            region_freq_list[pos] += 1
        else:
            region_list.append(country['region'])
            region_freq_list.append(1)
    return region_list, region_freq_list

# cities_data = read_file('cities.csv')
# region_list, region_freq_list = count_region_freq(cities_data)
# # Set up bar colors in bar graph
# # See more color names in the reference at the end of Exercise 6 
# my_colors = ['red','blue','green','orange']
# # Plot bar graph using x = unique region list
# # y = region frequency
# # Bar graph color is set to my_colors list
# plt.bar(region_list, region_freq_list, color=my_colors) 
# plt.xlabel('Region')
# plt.ylabel('Frequency')
# plt.savefig('region_freq.png')
# plt.show()

# 7
def find_lowest_highest_avg_city_temp(cities_data):
    country_temp = compute_ave_country_temp(cities_data)
    temp_list = []
    country_name = dict()
    for i in country_temp:
        temp_list.append(country_temp[i])
        country_name.update({country_temp[i]:i})
    return [country_name[min(temp_list)], country_name[max(temp_list)]]

# f = open("cities.csv", encoding="ISO-8859-1")
# rows = csv.DictReader(f)
# cities_data = []
# for i in rows:
#     cities_data.append(i)
# print(find_lowest_highest_avg_city_temp(cities_data[:11]))
# print(find_lowest_highest_avg_city_temp(cities_data[-10:]))
# print(find_lowest_highest_avg_city_temp(cities_data))

# 8
def compute_ave_region_highest(cities_data):
    reg_highest = []
    reg_list = []
    reg_avg_highest = []
    for country in cities_data:
        if country['region'] in reg_list:
            reg_highest[reg_list.index(country['region'])].append(float(country['highest']))
        else:
            reg_list.append(country['region'])
            reg_highest.append([float(country['highest'])])
    for i in reg_highest:
        reg_avg_highest.append(sum(i)/len(i)) 
    return reg_list, reg_avg_highest

cities_data = read_file('cities.csv')
reg_list, reg_highest = compute_ave_region_highest(cities_data)
reg_colors = ['#F3DECA','#FA9483','#2D4057','#4097AA']
plt.bar(reg_list, reg_highest, color=reg_colors) 
plt.xlabel('Region')
plt.ylabel('AVG Highest')
plt.savefig('region_avg_highest.png')
plt.show()