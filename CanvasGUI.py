from tkinter import *
from tkinter import ttk

root = Tk()

#event handler expects event parameter
def key_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('char: {}'.format(event.char))
    print('keysym: {}'.format(event.keysym))
    print('keycode: {}'.format(event.keycode))
'''bind method has two parameters: first is a string containing specially
formatted descriptions of events you want to act upon, second parameter is
name of callback function or method to be executed'''
#root.bind('<KeyPress>', key_press)



def shortcut(action):
    print(action)
'''below uses lambda events within the bind method (this is slighty diff
than the lambda functions we used for the callback functions because
we didnt need to pass in parameter e like we did for binding events'''
#root.bind('<Command-c>', lambda e: shortcut('Copy'))
#root.bind('<Command-v>', lambda e: shortcut('Paste'))


def mouse_press(event):
    global prev
    prev = event
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num))
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y ))
    #the underscore root is useful for creating right click drop-down menus
    print('x_root: {}'.format(event.x_root))
    print('y_root: {}'.format(event.y_root ))

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5)
    prev = event

canvas = Canvas(root, width = 640, height = 480, background = 'white')
canvas.pack()

canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)

root.mainloop()
