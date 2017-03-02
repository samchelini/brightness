#!/usr/bin/python

import sys

def main():
    """
    Read the brightness file and perform the operation on it
    then write the new brightness to the file
    """
    if len(sys.argv) != 4:  # check number of args, print usage statement if incorrect
        print('usage: ' + sys.argv[0] + '  path_to_brightness_file operation brightness')
        print('possible operations: set, inc, or dec')
        print('possible brightness: 0 - 100')
        sys.exit()

    # get the args
    FILE = sys.argv[1]
    OP = sys.argv[2]
    BRIGHTNESS = int(sys.argv[3]) * 10  # get brightness and convert

    with open(FILE, 'w+') as f:

        current_brightness = int(f.readline())  # read current brightness

        # set the brightness
        if OP == 'set':
            current_brightness = BRIGHTNESS
            if current_brightness < 0:
                current_brightness = 0
            elif current_brightness > 937:
                current_brightness = 937

        # increment the brightness
        elif OP == 'inc':
            current_brightness += BRIGHTNESS
            if current_brightness > 937:
                current_brightness = 937
    
        # decrement the brightness
        elif OP == 'dec':
            current_brightness -= BRIGHTNESS
            if current_brightness < 0:
                current_brightness = 0

        # write to file
        f.write(str(current_brightness))

    return

if __name__ == "__main__":
    main()

