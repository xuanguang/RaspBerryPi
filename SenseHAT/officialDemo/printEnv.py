from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

tempUnit = ' Celsius'
temp = round(sense.get_temperature(), 1)
#sense.show_message(str(int(temp))+"#")
print(str(temp)+tempUnit)

humidityUnit = ' %'
humidity = round(sense.get_humidity(),1)
#sense.show_message(str(int(humidity))+"%")
print(str(humidity)+humidityUnit)

pressureUnit = ' millibars'
pressure = round(sense.get_pressure(),1)
print(str(pressure)+pressureUnit)
