#     I. Write a program that reads temperature in degree Celsius 
#     from console and converts it to Fahrenheit.
#      Display the result. Formula for conversion is given as follows:
#      Fahrenheit = (9/5) * Celsius + 32


celsius = float(input("Temperature in degree Celsius: " ))  
  

Fahrenheit = (celsius* 1.8) + 32  
    

print('The %.2f degree Celsius is equal to: %.2f Fahrenheit'  
      %(celsius, Fahrenheit))  
