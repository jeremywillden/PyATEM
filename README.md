# PyATEM library

## Install

    python3 setup.py

## Test run
on raspberry-pi connected to ATEM switcher optionally with leds connected

    python3 atem.py

## Run on startup

    # sudo crontab -e

add this row

    @reboot sh /home/pi/tally/startup.sh
