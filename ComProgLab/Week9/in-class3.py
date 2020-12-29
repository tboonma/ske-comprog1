import csv
import matplotlib.pyplot as plt

def read_file(filename):
    f = open(filename, encoding="ISO-8859-1")
    cities_data = []
    rows = csv.DictReader(f)
    for i in rows:
        cities_data.append(i)
    return cities_data

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

cities_data = read_file('cities.csv')
region_list, region_freq_list = count_region_freq(cities_data)
# Set up bar colors in bar graph
# See more color names in the reference at the end of Exercise 6 
my_colors = ['red','blue','green','orange']
# Plot bar graph using x = unique region list
# y = region frequency
# Bar graph color is set to my_colors list
plt.bar(region_list, region_freq_list, color=my_colors) 
plt.xlabel('Region')
plt.ylabel('Frequency')
plt.savefig('region_freq.png')
plt.show()