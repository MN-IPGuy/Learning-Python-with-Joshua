import subprocess
import curses, os #curses is the interface for capturing key presses on the menu, os launches the files
screen = curses.initscr() #initializes a new window for capturing key presses
curses.noecho() # Disables automatic echoing of key presses (prevents program from input each key twice)
curses.cbreak() # Disables line buffering (runs each key as it is pressed rather than waiting for the return key to pressed)
curses.start_color() # Lets you use colors when highlighting selected menu option
screen.keypad(1) # Capture input from keypad

# Change this to use different colors when highlighting
curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) # Sets up color pair #1, it does black text with white background 
h = curses.color_pair(1) #h is the coloring for a highlighted menu option
n = curses.A_NORMAL #n is the coloring for a non highlighted menu option

def menu():
    curses.init_pair(1,curses.COLOR_RED, curses.COLOR_WHITE)
    screen.keypad(1)
    pos = 1
    x = None
    # I'm going to be lazy and save some typing here.
    h = curses.color_pair(1)
    n = curses.A_NORMAL
    while x != ord('\n'):
        # Gotta reset the screen from the root or lose the border, window, etc.
        screen.clear()
        screen.border(0)
        screen.addstr(2,2, "Dan's Arcade Cabinet", curses.A_STANDOUT)
        screen.addstr(4,2, "Please select an option...", curses.A_BOLD)
        # Detect what is highlighted by the 'pos' variable.
        if pos == 1:
            screen.addstr(5,4, "1 - Classic Arcade Games",h)
        else:
            screen.addstr(5,4, "1 - Classic Arcade Games",n)
        if pos == 2:
            screen.addstr(6,4, "2 - C64 Jumpman",h)
        else:
            screen.addstr(6,4, "2 - C64 Jumpman",n)
        if pos == 3:
            screen.addstr(7,4, "3 - Restart",h)
        else:
            screen.addstr(7,4, "3 - Restart",n)
        if pos == 4:
            screen.addstr(8,4, "4 - Turn Off",h)
        else:
            screen.addstr(8,4, "4 - Turn Off",n)
        screen.refresh()
        x = screen.getch()
        # Is 'x' 1-4 or arrow up, arrow down?
        if x == ord('1'):
            pos = 1
        elif x == ord('2'):
            pos = 2
        elif x == ord('3'):
            pos = 3
        elif x == ord('4'):
            pos = 4
        elif x == 258:
            if pos < 4:
                pos += 1
            else:
                pos = 1
        elif x == 259:
            if pos > 1:
                pos += -1
            else:
                pos = 4
        elif x != ord('\n'):
            curses.flash()
            # show_error() is my custom function for displaying a message:
            # show_error(str:message, int:line#, int:seconds_to_display)
            show_error('Invalid Key',11,1)

    return (pos)
    
# Main
while True:
	Choice = menu()
	if Choice == 1:
		print("/home/pi/emulators/mame4all-pi/mame")
	if Choice == 2:
		print("x64 -autostart ~/roms/JUMPMAN.D64")
	if Choice == 3:
		print("sudo reboot")
	if Choice == 4:
		print("sudo poweroff")    
curses.endwin()
