# Handling Command-Line Arguments
import sys

for arg in sys.argv:
    print arg


# C:\Users\Graham\Desktop\Graham\CIT\git\DiveIntoPython\Chapter 10 - Scripts and S
# treams>python IntroducingSysargv.py
# IntroducingSysargv.py

# C:\Users\Graham\Desktop\Graham\CIT\git\DiveIntoPython\Chapter 10 - Scripts and S
# treams>python IntroducingSysargv.py abc def
# IntroducingSysargv.py
# abc
# def

# C:\Users\Graham\Desktop\Graham\CIT\git\DiveIntoPython\Chapter 10 - Scripts and S
# treams>python IntroducingSysargv.py --help
# IntroducingSysargv.py
# --help

# C:\Users\Graham\Desktop\Graham\CIT\git\DiveIntoPython\Chapter 10 - Scripts and S
# treams>python IntroducingSysargv.py -m.kant.xml
# IntroducingSysargv.py
# -m.kant.xml

# C:\Users\Graham\Desktop\Graham\CIT\git\DiveIntoPython\Chapter 10 - Scripts and S
# treams>python IntroducingSysargv.py -m kant.xml
# IntroducingSysargv.py
# -m
# kant.xml
