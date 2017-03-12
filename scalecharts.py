import sys
from tkinter import *


#This program creates a guitar scale gui from grid elements, and fills them in color-coded appropriately.


# Get Note name from a 0-11 INT
def getnotename(tonename):
    notedict = ['E ', 'F ', 'F#', 'G ', 'Ab', 'A ', 'Bb', 'B ', 'C ', 'Db', 'D ', 'Eb']
    return notedict[tonename % 12]


# Contains int offsets, based on note string, added for convenience, which is simply offset relative to C.
def getoffset_tonename(tonename):
    scaleref = {'E ': 0, 'F ': 1, 'F#': 2, 'G ': 3, 'Ab': 4., 'A ': 5, 'Bb': 6, 'B ': 7, 'C ': 8, 'Db': 9, 'D ': 10, \
                'Eb': 11}
    return scaleref[tonename]


# Return array that is rotated circular
def rotate(l, n):
    return l[-n:] + l[:-n]


# returns a scale of 16 notes, from the key tonic + 24
def makescale(keyroot, keyopt):
    keywheel = []
    if 'Major' == keyopt:
        keywheel.extend([0, 2, 2, 1, 2, 2, 2, 1])
    if 'Natural minor' == keyopt:
        keywheel.extend([0, 2, 1, 2, 2, 1, 2, 2])
    if 'Harmonic minor' == keyopt:
        keywheel.extend([0, 2, 1, 2, 2, 1, 3, 1])
    if 'Melodic minor' == keyopt:
        keywheel.extend([0, 2, 1, 2, 2, 2, 2, 2])
    if 'Dorian mode' == keyopt:
        keywheel.extend([0, 2, 1, 2, 2, 2, 1, 2])
    if 'Mixolydian mode' == keyopt:
        keywheel.extend([0, 2, 2, 1, 2, 2, 1, 2])
    if 'Ahava raba mode' == keyopt:
        keywheel.extend([0, 1, 3, 1, 2, 1, 2, 2])
    if 'Minor pentatonic' == keyopt:
        keywheel.extend([0, 3, 2, 2, 3, 2])
    if 'Pentatonic' == keyopt:
        keywheel.extend([0, 2, 2, 3, 2, 3])
    filler = 0
    # fill array with 16 notes relevant to key and option.
    ourscale = []
    lenvar = len(keywheel)  # of notes we use (2 octaves of key notes)
    for inte in range(lenvar):
        filler += keywheel[inte % len(keywheel)]
        ourscale.append((filler + getoffset_tonename(keyroot)))
    return ourscale


# fetches a default scale
ourscale = makescale('E ', 'Major')

# Used for note offsets
e = 0

# high e = (e+4), b = (e-1), g = (e+7), d = (e+2),a = (e+9), low e = (e+4)
# added to each string to offset and identify the notes.
offsetArray = [e, e + 7, e + 3, e + 10, e + 5, e]

# default e Major
chartgui = Tk()

# our callback variables that change when menu options are selected
variable = StringVar(chartgui)
variable.set('E ')
variable2 = StringVar(chartgui)
variable2.set('Major')


# variable3 = StringVar(chartgui)
# variable3.set('View 1')


# for clearing all our values, used for the "Reset" button.
def resettable():
    print("Tried to reset!")
    for i in range(0, 25):
        for gss in range(0, 6):
            Label(chartgui, text=getnotename(i + offsetArray[gss])).grid(row=gss + 2, column=i + 1, padx=0, pady=0)


# redraw our whole scale, the action for the "Apply" button
def applyit():
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

    # draw our whole scale
    for i in range(0, 25):
        for gss in range(0, 6):
            start = offsetArray[gss]

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


def __main():
    chartgui.geometry('640x280+400+300')
    chartgui.title('GuitarScaleChart - Colin Burke, 2017')
    ourx = 40
    oury = 20

    # For our fret (column) labels on top and bottom
    for i in range(0, 25):
        Label(chartgui, text=i, font='helvetica').grid(row=0, column=i + 1, padx=0, pady=10)
        Label(chartgui, text=i, font='helvetica').grid(row=9, column=i + 1, padx=0, pady=10)

    # For our string (row) labels
    stringarray = ['E', 'B', 'G', 'D', 'A', 'E']
    for gss in range(0, 6):
        Label(chartgui, text=stringarray[gss], font="comicsans").grid(row=gss + 2, column=0, padx=10, pady=0)

    print(ourscale)

    # draw our whole scale
    applyit()

    keymenu = OptionMenu(chartgui, variable, 'E ', 'F ', 'F#', 'G ', 'Ab', 'A ', 'Bb', 'B ', 'C ', 'Db', 'D ',
                         'Eb', ).place(x=ourx * 2, y=oury * 12)
    scalemenu = OptionMenu(chartgui, variable2, 'Major', 'Natural minor', 'Harmonic minor', 'Melodic minor',
                           'Dorian mode', 'Mixolydian mode', 'Ahava raba mode', 'Minor pentatonic', 'Pentatonic').place(
        x=ourx * 4, y=oury * 12)
    submitbutton = Button(chartgui, text=' Apply ', command=applyit).place(x=ourx * 8, y=oury * 12)
    resetbutton = Button(chartgui, text=' Reset ', command=resettable).place(x=ourx * 10, y=oury * 12)

    chartgui.mainloop()


__main()
