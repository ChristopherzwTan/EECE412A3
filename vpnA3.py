#!/usr/bin/python

#
# EECE 412 Assignment 3 VPN
# 
# 
# 
# 
# Last Updated: October 5, 2014
# 

import gtk, sys

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
	
	self.set_title("EECE 412 VPN Group #9")        
        self.set_size_request(800, 500)
        self.set_position(gtk.WIN_POS_CENTER)

	# Buttons
	clientMode = gtk.Button("Client Mode")
        serverMode = gtk.Button("Server Mode")
        close = gtk.Button(stock=gtk.STOCK_CLOSE)
        #btn4 = gtk.Button("Button")

	vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox(True, 3)
        
        valign = gtk.Alignment(0, 1, 0, 0)
        vbox.pack_start(valign)
        
        hbox.add(clientMode)
	hbox.add(serverMode)
        hbox.add(close)
        
        halign = gtk.Alignment(1, 0, 0, 0)
        halign.add(hbox)
        
        vbox.pack_start(halign, False, False, 3)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)

        self.show_all()

PyApp()
gtk.main()
