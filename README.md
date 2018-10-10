# PyATEM library

## Install

    sudo apt install python3-gpiozero

## Test run
on raspberry-pi connected to ATEM switcher optionally with leds connected

    python3 atem.py

## Run on startup with crontab

    # sudo crontab -e

add this row

    @reboot sh /home/pi/tally/startup.sh
