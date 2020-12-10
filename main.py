while True:
    #if light level is between 11 and 20 then set lights to yellow
    print("light Level: " + input.light_level())
    if 11 <= input.light_level() <= 20:
           light.set_all(color.rgb(255, 255, 0))

    #if light level is equal to or less than 9, then set neopixels blue
    elif input.light_level() <= 9  :
        print("light Level: " + input.light_level())
        light.set_all(color.rgb(0, 0, 255))

    #if light level is equal to or greater than 10 then set lights off    
    elif input.light_level() >= 10 :
           light.clear()