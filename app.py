# Import tkinter
import tkinter as tk

# Import customtkinker
import customtkinter as ctk

# Import Youtube from Pytube
from pytube import YouTube

# Import os
import os


# Functions
# Cancel video download
def cancel_download():
    print("Download Cancelled")


# Downloading the video
def download_video():
    url = url_entry.get()
    resolution = resolution_variable.get()

    try:
        yt = YouTube(url=url)
        stream = yt.streams.filter(res=resolution).first()

        stream.download()
    except Exception as e:
        print(e)



# Create root window
root_ctk = ctk.CTk()

# Set Appearanace Mode
ctk.set_appearance_mode("dark")

# Set the default color theme
ctk.set_default_color_theme("blue")

# Set the size of the window
root_ctk.geometry("720x480")

# Set the title of the window
root_ctk.title("My Youtube Downloader")

# Create a frame to hold the contents
content_frame = ctk.CTkFrame(root_ctk)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)


# Create label and entry
url_label = ctk.CTkLabel(content_frame, text="Enter Youtube url here: ")
url_entry = ctk.CTkEntry(content_frame, width=300, height=30)

# Pack on content frame
url_label.pack(pady=(10, 5))
url_entry.pack(pady=(10, 5))

# Create doownload and Cancel/clear button
button_clear = ctk.CTkButton(content_frame, text="Cancel", command=cancel_download)
button_download = ctk.CTkButton(content_frame, text="Download", command=download_video)

# pack on content frame
button_clear.pack(pady=(10, 5))
button_download.pack(pady=(10, 5))


# Create download progressbar
progressbar_download = ctk.CTkProgressBar(content_frame, orientation="horizontal")


# Pack on content frame
progressbar_download.pack(pady=(10, 5))


# Resolutions
resolutions = ["720px", "480px", "360px", "240px"]
resolution_variable = ctk.StringVar()
resolution_comboxbox = ctk.CTkComboBox(content_frame, values=resolutions, variable=resolution_variable)
resolution_comboxbox.pack(pady=(10, 5))
resolution_comboxbox.set("720px")


root_ctk.mainloop()
