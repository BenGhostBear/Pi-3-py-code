

# Function 1 - RGB_LED_Value_Converter
def RGB_LED_Value_Converter(RGB_LED_Value):
    # Define a dictionary of colors
    colors = {"RED": "100:0:0", "GREEN": "0:100:0", "BLUE": "0:0:100",
              "YELLOW": "100:100:0", "PURPLE": "100:0:100", "CYAN": "0:100:100",
              "WHITE": "100:100:100", "BLACK": "0:0:0"}

    # Check if the input is a number or a color
    if RGB_LED_Value in colors:
        # If it's a color, convert it to RGB values
        RGB_LED_Value = colors[RGB_LED_Value]
        RGB_LED_Value = list(map(int, RGB_LED_Value.split(":")))
    else:
        # If it's a number, convert it to RGB values
        if RGB_LED_Value[0] == "#":
            RGB_LED_Value = RGB_LED_Value[1:]
            RGB_LED_Value = list(map(int, (RGB_LED_Value[0:2], RGB_LED_Value[2:4], RGB_LED_Value[4:6])))
        elif len(RGB_LED_Value) == 6:
            RGB_LED_Value = list(map(int, RGB_LED_Value.split(":")))
        elif len(RGB_LED_Value) == 3:
            RGB_LED_Value = [int(RGB_LED_Value[i]*2) for i in range(3)] + [int(RGB_LED_Value[i]) for i in range(3)]
        else:
            raise ValueError("Invalid RGB LED value")

    # Normalize the RGB values to 0-100 range
    RGB_LED_Value = [min(max(x, 0), 100) for x in RGB_LED_Value]

    return RGB_LED_Value

# Function 2 - rgbWrite
def rgbWrite(r, g, b):
    # Convert the 0-100 values to 0-255 for the Raspberry Pi I/O
    r = int(r*2.55)
    g = int(g*2.55)
    b = int(b*2.55)

    # Write to the Raspberry Pi I/O for the 2 RGB LEDs
    redRGBPin = 11
    greenRGBPin = 13
    blueRGBPin = 15
    REDRGB = GPIO.PWM(redRGBPin, 100)
    GREENRGB = GPIO.PWM(greenRGBPin, 100)
    BLUERGB = GPIO.PWM(blueRGBPin, 100)
    REDRGB.start(0)
    GREENRGB.start(0)
    BLUERGB.start(0)
    REDRGB.ChangeDutyCycle(r)
    GREENRGB.ChangeDutyCycle(g)
    BLUERGB.ChangeDutyCycle(b)

# Example usage
RGB_LED_Value = "70:80:90"
RGB_LED_Value = RGB_LED_Value_Converter(RGB_LED_Value)
rgbWrite(RGB_LED_Value[0], RGB_LED_Value[1], RGB_LED_Value[2])
