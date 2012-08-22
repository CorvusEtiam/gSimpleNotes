from gi.repository import Gtk
import Notes

class Handler(object):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("gNotes.glade")
        self.window = builder.get_object("gNotes")
        self.about_button = builder.get_object("About")
        self.textview = builder.get_object("textview1")
        self.treeview = builder.get_object("treeview1")
        self.about = builder.get_object("Dialog")
        self.add_button = builder.get_object("Add")
        builder.connect_signals(self)
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
    def onAddClick(self, textview):
        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        content = self.textbuffer.get_text()
        Notes.Core.append(content)
        
    def onDeleteClick(self):
        pass
    def UpClick(self):
        pass
    def DownClick(self):
        pass
    def onAboutClick(self,about_button):
        self.about.run()
        self.about.hide()

#        self.textview = Gtk.TextView()
#        self.textbuffer = self.textview.get_buffer()
#        self.textbuffer.set_text("This is some text inside of a Gtk.TextView. "
#            + "Select text and click one of the buttons 'bold', 'italic', "
#            + "or 'underline' to modify the text accordingly.")
#        scrolledwindow.add(self.textview)
        

if __name__ == "__main__":
    window = Handler()
    window.window.show()
    Gtk.main()
    