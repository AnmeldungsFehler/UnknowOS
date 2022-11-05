import ctypes
import os
from pathlib import Path
#--------------------------------------------------------------------

user = os.getlogin()


#--------------------------------------------------------------------

#Set Wallpaper

SPI_SETDESKTOPWALLPAPER=20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0 , "C:\\Users\\" + user + "\\Desktop\\UnknowOS\\src\\Wallpaper\\default-wallpaper.png" , 3)

#--------------------------------------------------------------------

#Run Modules

#CacheCleaner
os.system("C:\\Users\\" + user + "\\Desktop\\UnknowOS\\src\\ProgramData\\CacheCleaner.py")
print("[*] Clearing the system cache. Please be patient, takes a moment!")
os.system("color f")


#AutoApps
os.system("C:\\Users\\" + user + "\\Desktop\\UnknowOS\\src\\Modules\\AutoApps\\AppsInstaller.py")
print("[*] Installing Auto Apps for UnknowOS. Please be patient, takes a moment!")
os.system("color f")

#Install Drivers
#os.system("src\\Desktop\\SetupDrivers\\drivers.py")
#print("[*] Installing Drivers for UnknowOS. Please be patient, takes a moment!")
#os.system("color f")




#--------------------------------------------------------------------

#End of the program

#del this

#--------------------------------------------------------------------




