#!/usr/bin/env python3
import sys
from tkinter import *
from collections import OrderedDict

# This program creates a guitar scale gui from grid elements, and fills them in color-coded appropriately. 
# https://github.com/crawsome/GuitarScaleChart
# 2017 Colin Burke, et al contributors from Github :-)

TUNINGS = {
    'Standard': {
        'Labels': ['E', 'B', 'G', 'D', 'A', 'E'],
        'Offset': [0, 7, 3, 10, 5, 0]
    },
    'Drop D': {
        'Labels': ['E', 'B', 'G', 'D', 'A', 'D'],
        'Offset': [0, 7, 3, 10, 5, 10]
    },
    'DADGAD': {
        'Labels': ['D', 'A', 'G', 'D', 'A', 'D'],
        'Offset': [10, 5, 3, 10, 5, 10]
    }
}
NOTES = ['E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb']
SCALES = OrderedDict([
    ('Major', [0, 2, 2, 1, 2, 2, 2, 1]),
    ('Natural minor', [0, 2, 1, 2, 2, 1, 2, 2]),
    ('Harmonic minor', [0, 2, 1, 2, 2, 1, 3, 1]),
    ('Melodic minor', [0, 2, 1, 2, 2, 2, 2, 2]),
    ('Dorian mode', [0, 2, 1, 2, 2, 2, 1, 2]),
    ('Mixolydian mode', [0, 2, 2, 1, 2, 2, 1, 2]),
    ('Ahava raba mode', [0, 1, 3, 1, 2, 1, 2, 2]),
    ('Minor pentatonic', [0, 3, 2, 2, 3, 2]),
    ('Pentatonic', [0, 2, 2, 3, 2, 3]),
    ('5 chord', [0, 7]),
    ('Major chord', [0, 4, 3]),
    ('Minor chord', [0, 3, 4]),
    ('Diminished chord', [0, 3, 3]),
    ('Augmented chord', [0, 4, 4]),
    ('Sus2 chord', [0, 2, 5]),
    ('Sus4 chord', [0, 5, 2]),
    ('Maj7 chord', [0, 4, 3, 4]),
    ('min7 chord', [0, 3, 4, 3]),
    ('7 chord', [0, 4, 3, 3]),
    ('dim7 chord', [0, 3, 3, 3]),
    ('9 chord', [0, 4, 3, 3, 4]),
    ('Maj9 chord', [0, 4, 3, 4, 3]),
    ('m9 chord', [0, 3, 4, 3, 4])
    ])

def get_tuning_labels():
    return TUNINGS[str(variable3.get())]['Labels']

def get_tuning_offset():
    return TUNINGS[str(variable3.get())]['Offset']

# Get Note name from a 0-11 INT
def getnotename(tonename):
    return NOTES[tonename % 12]


# Contains int offsets, based on note string, added for convenience, which is simply offset relative to C.
def getoffset_tonename(tonename):
    return NOTES.index(tonename)


# Return array that is rotated circular
def rotate(l, n):
    return l[-n:] + l[:-n]

# returns a scale of 16 notes, from the key tonic + 24
def makescale(keyroot, keyopt):
    keywheel = []
    keywheel.extend(SCALES[keyopt])
    filler = 0
    # fill array with 16 notes relevant to key and option.
    ourscale = []
    lenvar = len(keywheel)  # of notes we use (2 octaves of key notes)
    for inte in range(lenvar):
        filler += keywheel[inte % len(keywheel)]
        ourscale.append(int(filler + getoffset_tonename(keyroot)))
    return ourscale



# default e Major
chartgui = Tk()
# our callback variables that change when menu options are selected
variable = StringVar(chartgui)
variable.set('E')
variable2 = StringVar(chartgui)
variable2.set('Major')
variable3 = StringVar(chartgui)
variable3.set("Standard")

# variable3 = StringVar(chartgui)
# variable3.set('View 1')

# for clearing all our values, used for the "Reset" button.
def resettable():
    print("Tried to reset!")
    offset = get_tuning_offset()
    for i in range(0, 25):
        for gss in range(0, 6):
            Label(chartgui, text=getnotename(i + offset[gss])).grid(row=gss + 2, column=i + 1, padx=0, pady=0)


# redraw our whole scale, the action for the "Apply" button
def redraw_fretboard():
    print("Trying to apply!")
    # print("var1 = %s"%variable.get())
    # print("var2 = %s"%variable2.get())
    # print("var3 = %s"%variable3.get())
    ourtonic = str(variable.get())
    ourkey = str(variable2.get())
    print(ourtonic)
    print(ourkey)

    ourscale = makescale(ourtonic, ourkey)
    print(ourscale)
    ournotes = []

    for notes in ourscale:
        ournotes.append(getnotename(notes))

    print (ournotes)

    # For our string (row) labels
    offset = get_tuning_offset()
    for gss in range(0, 6):
        Label(chartgui, text=offset[gss], font="comicsans").grid(row=gss + 2, column=0, padx=10, pady=0)

    # draw our whole scale
    for i in range(0, 25):
        for gss in range(0, 6):
            start = get_tuning_offset()[gss]

            # draw red for roots
            if ourtonic == getnotename(i + start % 12):
                Label(chartgui, text=getnotename(i + start), bg='red').grid(row=gss + 2, column=i + 1,
                                                                                       padx=0, pady=0)
            # draw yellow for notes in the scale
            elif getnotename(i + start) in ournotes:
                Label(chartgui, text=getnotename(i + start), bg='yellow').grid(row=gss + 2, column=i + 1,
                                                                                          padx=0, pady=0)
            # only write notename
            else:
                Label(chartgui, text=getnotename(i + start)).grid(row=gss + 2, column=i + 1, padx=0, pady=0)


if __name__ == "__main__":
    chartgui.geometry('640x280+400+300')
    chartgui.title('GuitarScaleChart - Colin Burke, 2017')
    ourx = 40
    oury = 20

    # For our fret (column) labels on top and bottom
    for i in range(0, 25):
        Label(chartgui, text=i, font='helvetica').grid(row=0, column=i + 1, padx=0, pady=10)
        Label(chartgui, text=i, font='helvetica').grid(row=9, column=i + 1, padx=0, pady=10)

    keymenu = OptionMenu(chartgui, variable, *NOTES).place(x=ourx * 2, y=oury * 12)
    scalemenu = OptionMenu(chartgui, variable2, *SCALES.keys()).place(x=ourx * 4, y=oury * 12)
    tuningmenu = OptionMenu(chartgui, variable3, *TUNINGS.keys()).place(x=ourx * 6.5, y=oury * 12)
    submitbutton = Button(chartgui, text=' Apply ', command=redraw_fretboard).place(x=ourx * 10, y=oury * 12)
    resetbutton = Button(chartgui, text=' Reset ', command=resettable).place(x=ourx * 12, y=oury * 12)

    # draw our whole scale
    redraw_fretboard()
    chartgui.mainloop()

