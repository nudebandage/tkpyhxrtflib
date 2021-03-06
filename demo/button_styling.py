import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
import os
import glob

colors = {
    "frame": "#efefef",
    "disabledfg": "#aaaaaa",
    "selectbg": "#657a9e",
    "selectfg": "#ffffff"
}

imgs = {}
def _load_imgs(imgdir):			# Images without any references are garbage collected by python
	imgdir = os.path.expanduser(imgdir)
	if not os.path.isdir(imgdir):
		raise Exception("%r is not a directory, can't load images" % imgdir)
	for f in glob.glob("%s/*.gif" % imgdir):
		img = os.path.split(f)[1]
		name = img[:-4]
		imgs[name] = PhotoImage(name, file=f, format="gif89")

def install(root, imgdir):
	_load_imgs(imgdir)
	style=ttk.Style(root)
	ttk.Style().theme_create("toggle", "default", settings={
		"ToggleButton": {
			"configure": {"width": 10, "anchor": "center"},
			"layout": [
				("ToggleButton.button", {"children":
					[("ToggleButton.focus", {"children":
						[("ToggleButton.padding", {"children":
				[("ToggleButton.label", {"side": "left", "expand": 1})]
						})]
					})]
				})
			]
		},
		"ToggleButton.button": {"element create":
			("image", 'button-n',
		("pressed", 'button-p'), ("active","!alternate", 'button-h'),
				("alternate", "button-s"),	#THIS IS THE MAGIC tbutton-p
				{"border": [4, 10], "padding": 4, "sticky":"ewns"}
			)
		}
	}
	)
	style.theme_use('toggle')
