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
        #btn4.set_size_request(80, 40)

	vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox(False, 3)
        
	hbox.add(clientMode)
	hbox.add(serverMode)

	hboxLeft = gtk.HBox(False,0)
	hboxRight = gtk.HBox(False,0)
	#vbox.pack_start(halign, False, False, 3)

	vbox.add(hboxLeft)
	#self.add(hbox)
	#self.add(vbox)
        self.connect("destroy", gtk.main_quit)

        self.show_all()

PyApp()
gtk.main()
