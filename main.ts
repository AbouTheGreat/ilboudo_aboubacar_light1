while (true) {
    // if light level is equal to or less than 5, then set neopixels blue
    console.log("light Level: " + input.lightLevel())
    if (input.lightLevel() <= 5) {
        console.log("light Level: " + input.lightLevel())
        light.setAll(color.rgb(0, 0, 255))
    } else if (input.lightLevel() >= 6) {
        // if light level is equal to or greater than 6 then set lights off    
        light.clear()
    }
    
}
