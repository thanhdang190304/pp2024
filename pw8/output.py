import curses

def display_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr("Students:\n")
    for student in students:
        stdscr.addstr(student.display_info() + "\n")
    stdscr.refresh()

def run_curses():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    while True:
        stdscr.addstr("--- MENU ---\n")
        # Menu options and code for handling user input
        # ...

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()