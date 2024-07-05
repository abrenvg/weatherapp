import requests



api_key='5d0dcb06586be28161e81737adde78e0'
user_input=input("enter city")
print(user_input)


weather_data= requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
if weather_data.status_code== '404':
    print("No City  Found")
else:
    print(weather_data.json())

weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])

print(f"The weather in {user_input} is: ",weather)
print(f"The temperature in {user_input} is:",temp)