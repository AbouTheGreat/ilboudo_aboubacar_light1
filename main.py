while True:
    
    #if light level is greater than 15, then set neopixels off
    print("light Level: " + input.light_level())
    if input.light_level() > 15:
        light.clear()
    
    #if light level is equal to or greater than 6, then set neopixels blue
    elif input.light_level() >= 6 :
        light.set_all(color.rgb(0, 0, 255))
    
    else:
        light.set_all(color.rgb(255,165,0))

  



















    #elif 9 >= input.light_level() > 3:
        #light.set_all(color.rgb(255,165,0))       
           
           
           #if light level is between 11 and 20 then set lights to yellow
    #print("light Level: " + input.light_level())
    #if 11 <= input.light_level() <= 20:
        #light.set_all(color.rgb(255, 255, 0))
