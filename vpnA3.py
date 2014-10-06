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

#class VPN(gtk.Window):
class VPN(object):
    def __init__(self):
        super(VPN, self).__init__()
	
	# create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_usize(800, 500)
        self.window.set_title("EEVE 412 VPN Group #9")
        self.window.connect("delete_event", gtk.mainquit)

	hbox = gtk.HBox(gtk.FALSE, 0)
        vbox = gtk.VBox(gtk.FALSE, 0)
        self.window.add(hbox)
	hbox.add(vbox)
	
	mode_select = gtk.HBox(gtk.FALSE, 0)
        vbox.add(mode_select)

	server_info = gtk.HBox(gtk.FALSE, 0)
        vbox.add(server_info)

	# First HBox with mode select
	server_mode = gtk.RadioButton(None, "Server Mode")
	mode_select.pack_start(server_mode, gtk.TRUE, gtk.TRUE, 0)

	client_mode = gtk.RadioButton(server_mode, "Client Mode")
	mode_select.pack_start(client_mode, gtk.TRUE, gtk.TRUE, 0)

	
	# Second HBox with IPAddress and Port for server mode
	ip_label = gtk.Label("IP address")
	server_info.pack_start(ip_label, gtk.TRUE, gtk.TRUE, 0)

	ip_entry = gtk.Entry(15)
	server_info.pack_start(ip_entry, gtk.TRUE, gtk.TRUE, 0)

	port_label = gtk.Label("Port")
	server_info.pack_start(port_label, gtk.TRUE, gtk.TRUE, 0)

	port_entry = gtk.Entry(10)
	server_info.pack_start(port_entry, gtk.TRUE, gtk.TRUE, 0)

	
	# Sent assets
	shared_secret = gtk.Label("Shared Secret Value")
        vbox.pack_start(shared_secret, gtk.TRUE, gtk.TRUE, 0)

	self.shared_secret_entry = gtk.Entry(50)
        vbox.pack_start(self.shared_secret_entry, gtk.TRUE, gtk.TRUE, 0)

	plaintext = gtk.Label("Plain Text")
        vbox.pack_start(plaintext, gtk.TRUE, gtk.TRUE, 0)

	self.plaintext_entry = gtk.Entry(50)
        vbox.pack_start(self.plaintext_entry, gtk.TRUE, gtk.TRUE, 0)

	ciphertext = gtk.Label("Cipher Text")
        vbox.pack_start(ciphertext, gtk.TRUE, gtk.TRUE, 0)

	self.ciphertext_entry = gtk.Entry(50)
        vbox.pack_start(self.ciphertext_entry, gtk.TRUE, gtk.TRUE, 0)


	# Data Receive
	receive_data_box = gtk.VBox(gtk.FALSE, 0)
        receive_data_box.show()
	hbox.add(receive_data_box)

	received_ciphertext = gtk.Label("Received Ciphertext")
	receive_data_box.pack_start(received_ciphertext, gtk.TRUE, gtk.TRUE, 0)

	#scroll bars for received cipher text
        self.scrolled_cipher_window = gtk.ScrolledWindow(hadjustment=None, vadjustment=None)
        self.scrolled_cipher_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        receive_data_box.pack_start(self.scrolled_cipher_window, gtk.TRUE, gtk.TRUE, 0)
        self.scrolled_cipher_window.show()

        #recieved cipher textview
        self.received_cipher_textview = gtk.TextView()
        self.scrolled_cipher_window.add_with_viewport(self.received_cipher_textview)
        self.received_cipher_textview.show()


	received_plaintext = gtk.Label("Received Plaintext")
	receive_data_box.pack_start(received_plaintext, gtk.TRUE, gtk.TRUE, 0)

	 #scroll bars for received plain text
        self.scrolled_plain_window = gtk.ScrolledWindow(hadjustment=None, vadjustment=None)
        self.scrolled_plain_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        receive_data_box.pack_start(self.scrolled_plain_window, gtk.TRUE, gtk.TRUE, 0)
        self.scrolled_plain_window.show()

        #received plain textview
        self.received_plain_textview = gtk.TextView()
        self.scrolled_plain_window.add_with_viewport(self.received_plain_textview)        
        self.received_plain_textview.show()


	

	# Buttons
	send_button = gtk.Button("Send")
	vbox.pack_start(send_button, gtk.TRUE, gtk.TRUE, 0)
	
	server_start = gtk.Button("Server Start")
	vbox.pack_start(server_start, gtk.TRUE, gtk.TRUE, 0)

	


	self.window.show_all()
		


VPN()
gtk.main()
