from autopy import bitmap
from autopy import mouse
from autopy.mouse import LEFT_BUTTON, RIGHT_BUTTON
from autopy import alert
from autopy import key
import time

ECLIPSE_COLLAPSE_ALL_IMG = "img/ecl_collapse_all.png"
ECLIPSE_SERVERS_ACTIVE_IMG = "img/ecl_servers_active.png"
ECLIPSE_JBOSS_LOGO_IMG = "img/ecl_jboss_logo.png"

#UTIL functions

def move_click(coordinates, button):
    """Moves the mouse to the specified coordinate and click the specified button."""
    print "moving mouse position to coordinates (X=%s , Y=%s) and click on this position!" % (coordinates[0],coordinates[1])
    mouse.move(coordinates[0], coordinates[1])
    mouse.click(button)

def click_bitmap(target_img_path, button):
    """Capture position of the target in the screen and click the specified mouse button on it."""
    screen = bitmap.capture_screen()
    target = bitmap.Bitmap.open(target_img_path)
    pos_target = screen.find_bitmap(target)
    move_click(pos_target, button)

def wait_target(target_img_path):
    """Try to capture position of the target in the screen until finds it and return his coordinates."""
    target = bitmap.Bitmap.open(target_img_path)
    pos_target = (0,0)

    while True:
        time.sleep(1)
        screen = bitmap.capture_screen()
        count = screen.count_of_bitmap(target)

        if count > 0:
            print "bitmap of image %s is found! Getting coordinates..." % target_img_path
            pos_target = screen.find_bitmap(target)
            break

        print "searching for bitmap of image %s ..." % target_img_path

    return pos_target

def wait_target_click(target_img_path, button):
    """Wait for the bitmap of the target appears in the screen and click the specified mouse button on it."""
    pos_target = wait_target(target_img_path)
    move_click(pos_target, button)

#OS and software dependent functions

def open_main_menu():
    """Open OS main menu whith META (SUPER,WINDOWS...) key."""
    key.tap(long(key.K_META))
    time.sleep(1) #wait for menu animation...

def open_eclipse():
    """Open eclipse typing string 'eclipse' in menu search."""
    open_main_menu()
    key.type_string("eclipse", 0)
    key.tap(long(key.K_RETURN))

def ecl_collapse_all():
    """Clicks on 'collapse all' in the eclipse."""
    wait_target_click(ECLIPSE_COLLAPSE_ALL_IMG, LEFT_BUTTON)

def ecl_servers():
    """Clicks on tab 'Servers' in the eclipse."""
    wait_target_click(ECLIPSE_SERVERS_ACTIVE_IMG, LEFT_BUTTON)

def ecl_jboss_clear():
    """Clicks on tab 'Servers' in the eclipse, and clean all published resources on JBOSS container."""
    ecl_servers()
    wait_target_click(ECLIPSE_JBOSS_LOGO_IMG, RIGHT_BUTTON)
    time.sleep(1)
    key.type_string("c", 0)
    time.sleep(1)
    key.tap(long(key.K_RETURN))

if __name__ == '__main__':
    print "Eclipse Automation Starts..."
    open_eclipse()
    ecl_collapse_all()
    ecl_jboss_clear()
    print "Eclipse Automation Finished!"
