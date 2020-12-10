while (true) {
    // if light level is between 11 and 20 then set lights to yellow
    console.log("light Level: " + input.lightLevel())
    if (11 <= input.lightLevel() && input.lightLevel() <= 20) {
        light.setAll(color.rgb(255, 255, 0))
    } else if (input.lightLevel() <= 9) {
        // if light level is equal to or less than 9, then set neopixels blue
        console.log("light Level: " + input.lightLevel())
        light.setAll(color.rgb(0, 0, 255))
    } else if (input.lightLevel() >= 10) {
        // if light level is equal to or greater than 10 then set lights off    
        light.clear()
    }
    
}
