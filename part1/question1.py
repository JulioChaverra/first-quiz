################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

def get_city_temperature(city):
   if city == "Quito":
      return 22
   elif city == "Sao Paulo":
      return 17
   elif city == "San Francisco":
      return 16
   elif city == "New York":
      return 14
   else:
      "City not found"
      
def get_city_weather(city):

   sky_condition = None

   if city == "Quito":
      sky_condition = "sunny"
   elif city == "Sao Paulo":
      sky_condition = "cloudy"
   elif city == "San Francisco":
      sky_condition = "rainy"
   elif city == "New York":
      sky_condition = "rainy"
   else:
      "City not found"

   temperature = get_city_temperature(city)

   return str(temperature) + " degrees and " + sky_condition