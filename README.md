## Overview
We are making a pokemon-like pedomoeter with the look and fel of the 1998 Pocket Pikachu. It will have different animations and allow you to choose from a number of creatures. 
## Expected features
- Dynamic moods
- Step counter / resource converter
- Feeding resources to the creature
- Set date / time
- Set date of birth (for a special animation)
- Set alarms
## Harware
This is a rough idea.
- Microcontroler
- Tiny color LCD or OLED, around **128×128** resolution.
- Input: D-pad, A, B, Select, and Start buttons
- I2C accerometer
- USB-C port
### Performance budget
We are assuming:
- a CPU speed in the tens to hundreds of MHz.
- memory in the tens to hundreds of KB for logic/assets.
- low‑frequency updates between 5–20 FPS for animations
## Software
- Prototype will be in Python.
- Device will be in MicroPython
    - if MicroPython is too heavy, we'll switch to C/C++

## Notes
1. For now all code will be for a desktop prototype. I'll name files, folders, and functions accordingly.
2. We may make a mobile app later, since we'll already have the logic.