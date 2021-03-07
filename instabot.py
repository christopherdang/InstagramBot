# 1. Mouse position to middle of pic (x=746, y=569)
# 2. Double-click to like
# 3. Mouse position to comment box (x=1095, y=845)
# 4. Click on comment box
# 5. Random-type in text
# 6. Press enter
# 8. Random wait time
# 8. Mouse position to right-arrow (x=1449, y=570)
# 9. Click

#top-left 576, 403
#top-right 940, 403
#bottom-left 576, 735
#bottom-right 940, 735

#comment 1238, 842 - 1322, 845

# general x-coordinate 624
# general y-coordinate 650

# Out of post x coordinate = 70
# Out of post y coordinate = 500

# Username = patrickenbows
# Password = patrickenbows123

# Search bar coordinates 909, 130

import os
import time
import pyautogui
import random

random_comment_list = ["nice!", "cool", "dope", "niccccceeee", "run ittt", "i like this"]
random_hashtag_list = []

time.sleep(5)

for i in range(2):
    for x in range(3):
        #temp values for coordinates
        picX = random.randint(600, 645)
        picY = random.randint(600, 650)

        commentX = random.randint(1238, 1322)
        commentY = random.randint(841, 845)

        # Moves to pic to like it
        pyautogui.moveTo(picX, picY, duration=(2 / random.randint(1, 10)))
        pyautogui.click(picX, picY)
        time.sleep(2)
        randomLike = random.randint(1, 2)
        if randomLike == 1:
            pyautogui.doubleClick(picX, picY)
            time.sleep(1)

        # Moves to comment and comments
        randomComment = random.randint(1, 3)
        if randomComment == 1:
            pyautogui.moveTo(commentX, commentY,  duration=(2 / random.randint(1, 10)))
            pyautogui.click(commentX, commentY)
            pyautogui.typewrite(random.choice(random_comment_list), (2 / random.randint(1, 10)))
            pyautogui.typewrite(["enter"])
            time.sleep(2)

        # Click out of post and scroll
        pyautogui.moveTo(70, 500, duration=(2 / random.randint(1, 10)))
        pyautogui.doubleClick(70, 500)
        pyautogui.scroll(-300)

    # Move to search bar and look up different hashtag
    pyautogui.moveTo(909, 130, duration=(2 / random.randint(1, 10)))
    pyautogui.click(909, 130)
    time.sleep(1)
    pyautogui.typewrite("#food", (2 / random.randint(1, 10)))
    pyautogui.typewrite(["enter"])
    time.sleep(1)
    pyautogui.typewrite(["enter"])
    time.sleep(2)