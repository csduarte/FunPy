"""
Goal: To build a game similar to ex35
Map: Map.png
"""

import os

s_desc = '''
You wake in a fiery inferno. Luckily you're surrounded by doors.
You try all the door knobs. They are are all cool to the touch.
'''

a_desc = '''
If you thought the fire was bad, this room is crazy. Clowns. Nothing
but wall-to-wall clowns. You can't take it much longer. Move it!
'''

b_desc = '''
More doors, this has to be a joke. What is with this? You question how
you got here. One second you were at the batting cages and now you're
in your ex-girlfriends room. Time to get out.
'''

c_desc = '''
It seems like you're going in circles. If only there was something
you haven't tried.
'''

d_desc = '''
This room is pleasant. Nothing but the sound of rain and forrest
animals. While it doesn't sound like a bad hike, probably not where
you want to stop.
'''


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')


class Room:

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.options = []

    def __len__(self):
        return len(self.options)

    def add(self, option):
        if isinstance(option, list):
            self.options.extend(option)
        else:
            self.options.append(option)

    def __options__(self):
        count = 1
        for option in self.options:
            print "%d) %s" % (count, option.title)
            count += 1

    def __str__(self):
        return self.description

    def __getitem__(self, index):
        return self.options[index - 1]


def start():
    s = Room("Start", s_desc)
    a = Room("The Brown Door", a_desc)
    b = Room("The Red Door", b_desc)
    c = Room("The Blue Door", c_desc)
    d = Room("The Green Door", d_desc)
    e = Room("The Blue Door", "The Sneaky Exit")

    s.add([a, b, c, d])
    a.add([b, c, d])
    b.add([a, c, d])
    c.add([a, b, d])
    d.add([a, b, e])

    exited = False
    room = s
    count = 0
    while not exited:
        room = prompt_room(room)
        count += 1
        if room == e:
            exited = True
    clr()
    print "Whew! That was fun to watch. It only took you %d moves." \
          " Good job getting out of there. Hope you weren't burnt so bad that you won't play again" % count
    exit(0)


def prompt_room(room, retry=False):

    clr()

    if not retry:
        print room
        print "Which will you try?"
    else:
        print "You're panicking. Take a deep breath and select an actual option. Try again."

    print_options(room)

    try:
        selection = int(raw_input("> "))
        sel_room = room[selection]
    except (ValueError, NameError):
        return room, True
    else:
        return sel_room


def print_options(room):
    room.__options__()

start()
