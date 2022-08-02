# 3dprinted-tachometer
 scripts for tachometer design on thingiverse
 
 also pin wiring reference
 
 Original post on thingiverse: https://www.thingiverse.com/thing:5447004
 
 **Technical instructions:**
 
1. Get Raspberry Pi Imager and an SD card (8GB is enough)
2. Go to Choose OS -> Raspberry Pi OS Lite Legacy (Debian Buster)
3. Choose your SD card in Storage and press Write
4. Insert the card into your PI, connect it to HDMI and USB keyboard

    *It's also possible through SSH without needing mini-HDMI adapter and USB OTG cable, however you'll have to find instructions online*

5. Boot your Pi and let it expand the filesystem
6. When you're done and in the terminal, first type "sudo raspi-config"
7. Go to System Options -> Wireless LAN
8. Enter your SSID (wi-fi name) and password
9. Then go to System Options -> Boot / Auto Login -> Console Autologin
10. Exit the config tool
11. Now type "sudo apt-get update" and wait for update
12. Type "sudo apt-get install python3-pigpio" and wait for installation
13. Now type the following commands

    wget https://raw.githubusercontent.com/hellgames1/3dprinted-tachometer/main/mai2n.py
    
    wget https://raw.githubusercontent.com/hellgames1/3dprinted-tachometer/main/showip.py
    
    wget https://raw.githubusercontent.com/hellgames1/3dprinted-tachometer/main/bshut.py
    

14. Type "sudo nano /boot/config.txt"
15. Go to the bottom of the file and add the line "enable_uart=1"
16. Save and exit with Ctrl+X
17. Type "sudo nano /etc/rc.local"
18. Go to the bottom but ABOVE the "exit 0" line!
19. Add these 3 lines and make sure to include the & symbols

    sudo pigpiod
    
    sudo python3 /home/pi/bshut.py &
    
    sudo python3 /home/pi/mai2n.py &
    

20. Save and exit again with Ctrl+X
21. Type "sudo shutdown 0" to shut down the Pi
22. Unplug the power, HDMI and keyboard
23. Wire up the servo, LEDs, display, button and power switch using the png reference images provided.
24. Assemble everything as in the Youtube video
https://www.youtube.com/watch?v=_IPluKo3RjY




How to set up Dirt Rally 2.0
1. Go to Documents\My Games\DiRT Rally 2.0\hardwaresettings\
2. Edit hardware_settings_config.xml
3. I'm not sure if all of this is needed, but this is how it looks like in my file

    ....
    
    </audio_card>
    
    <motion_platform>
    
        <dbox enabled="true" />
    
        <udp enabled="true" extradata="3" ip="192.168.0.108" port="30500" delay="5" />
    
        <custom_udp enabled="false" filename="packet_data.xml" ip="127.0.0.1" port="20777" delay="10" />
    
        <fanatec enabled="true" pedalVibrationScale="1.0" wheelVibrationScale="1.0" ledTrueForGearsFalseForSpeed="true" />
    
    </motion_platform>
    
    

Works best with delay at 5. The tachometer will display the IP address when it boots.
Check this video out as well https://www.youtube.com/watch?v=Hg7oHDs2x3s
