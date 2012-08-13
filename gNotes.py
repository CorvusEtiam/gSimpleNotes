#!/usr/bin/python 
from gi.repository import Gtk
import Notes
class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="gNotes")
        self.set_border_width(10)
        hbox = Gtk.Box(spacing=6)
        self.add(hbox)
        
        button = Gtk.Button(label="Add")
        button.connect("clicked", self.add_on_click)
        hbox.pack_start(button, True, True, 0)
        

        button = Gtk.Button(label="Delete")
        button.connect("clicked", self.del_on_click)
        hbox.pack_start(button,True, True, 0)

        button = Gtk.ToggleButton("Read")
        button.connect("toggled", self.on_button_toggled, "1")
        hbox.pack_start(button, True, True, 0)

        button = Gtk.ToggleButton("Write", use_underline=True)
        button.set_active(True)
        button.connect("toggled", self.on_button_toggled, "2")
        hbox.pack_start(button, True, True, 0)

        
    def add_on_click(self, widget):
        pass
    def del_on_click(self,widget):
        pass
    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print "Button", name, "was turned", state
win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

