from Applets import Applets
from MyPy import io
import sys

while True:
    io.cls()
    print('Please choose one to continue:')
    for i, applet in enumerate(Applets):
        print('\t', i, applet.name())
    print('\t', 'e', 'Exit')

    c = io.getch()

    if c == 'e':
        sys.exit(0)
    else:
        Applet = Applets[int(c)]
        io.cls()    
        applet = Applet()
        applet.start()
