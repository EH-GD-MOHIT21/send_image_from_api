'''

        ##############################################################################################################################################

        # Make sure you have all three files copy_to_clipboard.py , main_sender.py , random_image.py in same folder / directory.....

        ##############################################################################################################################################


        <<<<<<<<<<<-----------------------------------------------WORKING OF CODE----------------------------------------------------------->>>>>>>>>>>


        ##################### random_image.py request a random image through api , copy_to_clipboard helps it to copy on your pc's clipboard #########

        #################### pyautogui or main_sender does the remaining stuff.

        ###################### YOU JUST HAVE TO RUN ONLY main_sender.py make sure you are using web.whatsapp.com or whats app desktop or some other
        ###################### stuff so you can switch between them easily...

'''
from time import sleep
import pyautogui as pag
from random_image import my_image
from copy_to_clipboard import *

print("Get Set Go......")
sleep(15)       # Get set ready switch between tabs/windows your code is ready to execute.

for i in range(10):                 # set any finite number of images you want to send
    image_bytes , img = my_image()
    work_bench()
    # img.show()
    pag.hotkey('ctrl', 'v')
    sleep(0.8)      ### Because whats app takes some time to process that image
    pag.keyDown("enter")
    sleep(0.5)      ### cooldown time for image