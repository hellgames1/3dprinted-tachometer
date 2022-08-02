# 3dprinted-tachometer
 scripts for tachometer design on thingiverse
 also pin wiring reference
 
 **Technical instructions:**
 
1. Get Raspberry Pi Imager and an SD card (8GB is enough)
2. Go to Choose OS -> Raspberry Pi OS Lite Legacy (Debian Buster)
3. Choose your SD card in Storage and press Write
4. Insert the card into your PI, connect it to HDMI and USB keyboard
It's also possible through SSH without needing mini-HDMI adapter and USB OTG cable, however you'll have to find instructions online
5. Boot your Pi and let it expand the filesystem
6. When you're done and in the terminal, first type "sudo raspi-config"
7. Go to System Options -> Wireless LAN
8. Enter your SSID (wi-fi name) and password
9. Then go to System Options -> Boot / Auto Login -> Console Autologin
10. Exit the config tool
11. Now type "sudo apt-get update" and wait for update
12. Type "sudo apt-get install python3-pigpio" and wait for installation
13. Type "sudo nano /boot/config.txt"
14. Go to the bottom of the file and add the line "enable_uart=1"
15. Save and exit with Ctrl+X
16. Type "sudo nano /etc/rc.local"
17. Go to the bottom but ABOVE the "exit 0" line!
18. Add these 3 lines and make sure to include the & symbols

    sudo pigpiod
    
    sudo python3 /home/pi/bshut.py &
    
    sudo python3 /home/pi/mai2n.py &
    

19. Save and exit again with Ctrl+X
20. Type "sudo shutdown 0" to shut down the Pi
21. Unplug the power, HDMI and keyboard
22. Wire up the servo, LEDs, display, button and power switch using the png reference images provided.
22. Assemble everything as in the Youtube video
https://www.youtube.com/watch?v=_IPluKo3RjY
