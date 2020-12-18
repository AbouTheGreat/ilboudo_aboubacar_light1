let A: number;
while (true) {
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
    // if light level is less than 5, then set neopixels blue
    console.log("light Level: " + input.lightLevel())
    if (input.lightLevel() < 5) {
        light.setAll(color.rgb(0, 0, 255))
    } else if (input.lightLevel() >= 6) {
        light.clear()
    } else {
        light.setAll(color.rgb(255, 165, 0))
    }
    
}
