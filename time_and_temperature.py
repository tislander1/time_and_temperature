
from requests_html import HTMLSession


s = HTMLSession()
lat = 40
long = -102

url_time = 'https://www.timeanddate.com/worldclock/@' + str(lat) + ',' + str(long)
url_weather = 'https://forecast.weather.gov/MapClick.php?lat=' + str(lat) + '&lon=' + str(long)

time_page = s.get(url_time)
current_time = time_page.html.find('span#ct')[0].text
timezone = time_page.html.find('span#cta')[0].text
date = time_page.html.find('span#ctdat')[0].text
print('Time: ' + current_time + ' ' + timezone)
print(date)

# <p class="myforecast-current-lrg">62&deg;F</p>
weather_page = s.get(url_weather)
current_weather = weather_page.html.find('p.myforecast-current')[0].text
current_temp = weather_page.html.find('p.myforecast-current-lrg')[0].text
current_weather_details = weather_page.html.find('div#current_conditions_detail')[0].text
current_weather_dict = {}
details = current_weather_details.split('\n')
print('Weather: ' + current_weather + ' and ' + current_temp)

for ix in range(0, len(details), 2):
    current_weather_dict[details[ix]] = details[ix+1]
for key in current_weather_dict:
    if key not in ['Last update']:
        print(key + ': ' + current_weather_dict[key])

url_sunset = 'https://sunrise-sunset.org/search?location=' + str(lat) + '%2C+'+ str(long)
sunset_page = s.get(url_sunset)
sunrise = sunset_page.html.find('div.sunrise')[0].text
sunrise = '; '.join(sunrise.split('\n'))
sunset = sunset_page.html.find('div.sunset')[0].text
sunset = '; '.join(sunset.split('\n'))
print(sunrise)
print(sunset)

url_spaceweather = 'https://www.swpc.noaa.gov/'
spaceweather_page = s.get(url_spaceweather)
spaceweather_predicted = spaceweather_page.html.find('div.noaa_scale_block.scale_G.day_1')[0].text
spaceweather_predicted = '; '.join(spaceweather_predicted.split('\n'))
spaceweather_observed = spaceweather_page.html.find('div.noaa_scale_block.scale_G.day_0')[0].text
spaceweather_observed = '; '.join(spaceweather_observed.split('\n'))
print('Observed aurora: ' + spaceweather_observed)
print('Predicted aurora: ' + spaceweather_predicted)

url_nationalday = 'https://www.daysoftheyear.com/today/'
nationalday_page = s.get(url_nationalday)
national_days = nationalday_page.html.find('div.banner__content')[0].text
print(national_days)
x = 2