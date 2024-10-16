/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Emre Guzel
 * Created on: Oct 16 2024
 * This program measures the distance  
*/

let  distanceToObject:number = 0

// Setup
basic.showIcon(IconNames.Happy)

// Find the distance 
input.onButtonPressed(Button.A,function(){
    basic.clearScreen()
    distanceToObject = sonar.ping(
       DigitalPin.P1,
       DigitalPin.P2,
       PingUnit.Centimeters
    )
    basic.showNumber(distanceToObject)
    basic.showIcon(IconNames.Happy)
})
