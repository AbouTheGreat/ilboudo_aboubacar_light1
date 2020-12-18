while True:
    A = 5
    A = 4
    A = 6
    A = 3 
    A = 7
    A = 8
    A = 9
    A = 10
    A = 14
    A = 16
    
    
    #if light level is less than 5, then set neopixels blue
    print("light Level: " + input.light_level())
    if input.light_level() < 5:
         light.set_all(color.rgb(0, 0, 255))
    

    
    elif input.light_level() >= 6 :
         light.clear()
    
    else:
        light.set_all(color.rgb(255,165,0))

  






    #elif 9 >= input.light_level() > 3:
        #light.set_all(color.rgb(255,165,0))       
           
           
           #if light level is between 11 and 20 then set lights to yellow
    #print("light Level: " + input.light_level())
    #if 11 <= input.light_level() <= 20:
        #light.set_all(color.rgb(255, 255, 0))
