#!/bin/bash
# This script toggles the virtual keyboard
# borrowed from https://forums.raspberrypi.com/viewtopic.php?t=358147
# this file is in /usr/bin/toggle-wvkbd.sh
#

PID="$(pidof wvkbd-mobintl)"

if [  "$PID" != ""  ]; then
  killall wvkbd-mobintl
else
 wvkbd-mobintl -L 250 -fg 111111 -fg-sp 6364ff --text ffffff --text-sp ffffff -fn "Manrope Variable 25"

# use wvkbd-mobintl --help for options
# our options:
# -L 250 = landscape, 250 pixels tall
# -fg 111111 = foreground color dark grey
# -fg-sp 6364ff = special keys foreground brand purple
# -text ffffff = text color white
# -text-sp ffffff = special keys text color white
# -fn "Manrope Variable 40" = font Manrope size 40

fi
