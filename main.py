import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
canvas.config(bg = 'black')

rootpath = "C:\\Users\KIIT\OneDrive\Desktop\MUSIC"
pattern = "*.mp3"

mixer .init()

prev_img = tk.PhotoImage(file = "prev_img.png")
next_img = tk.PhotoImage(file = "next_img.png")
pause_img = tk.PhotoImage(file = "pause_img.png")
play_img = tk.PhotoImage(file = "play_img.png")
stop_img = tk.PhotoImage(file = "stop_img.png")

def select():
    label.config(text = listBox.get("anchor")) #to show the song name inside the label and listbox is to get the selected songs and anchor is to get selected songs
    mixer.music.load(rootpath + "\\" + listBox.get("anchor")) #to play the song
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active') #to clear the selected songs and active is for deselect the active song after stopping it

def play_next():
    next_song = listBox.curselection()#to return the currently selected song  
    next_song = next_song[0] + 1 #to get the index of the next song
    next_song_name = listBox.get(next_song) #to get and show the song name of the next song inside the label
    label.config(text = next_song_name) #to show the next song inside the label
    mixer.music.load(rootpath + "\\" + next_song_name) #to play the song
    mixer.music.play() #to play the song

    listBox.select_clear(0, 'end') #so thar selection gets clear
    listBox.activate(next_song) #to active the next song
    listBox.select_set(next_song) #to activate the next song

def play_prev():
    next_song = listBox.curselection()#to return the currently selected song  
    next_song = next_song[0] - 1 #to get the index of the next song
    next_song_name = listBox.get(next_song) #to get and show the song name of the next song inside the label
    label.config(text = next_song_name) #to show the next song inside the label
    mixer.music.load(rootpath + "\\" + next_song_name) #to play the song
    mixer.music.play() #to play the song

    listBox.select_clear(0, 'end') #so thar selection gets clear
    listBox.activate(next_song) #to active the next song
    listBox.select_set(next_song) #to activate the next song

def pause_song():
    #to check if the song is paused it will play else it will play
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"

    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause" 

listBox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = 100, font = ('poppins', 14))
listBox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text = '', bg = 'black', fg = 'yellow', font = ('poppins', 18))
label.pack(pady = 15)

top = tk.Frame(canvas, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center')

prevButton = tk.Button(canvas, text = "Prev", image = prev_img, bg = 'black', borderwidth = 0, command = play_prev)
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(canvas, text = "Stop",  image = stop_img, bg = 'black', borderwidth = 0, command = stop)
stopButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(canvas, text = "Play",  image = play_img, bg = 'black', borderwidth = 0, command = select)
playButton.pack(pady = 15, in_ = top, side = 'left')

pauseButton = tk.Button(canvas, text = "Pause",  image = pause_img, bg = 'black', borderwidth = 0, command = pause_song)
pauseButton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(canvas, text = "Next",  image = next_img, bg = 'black', borderwidth = 0, command = play_next)
nextButton.pack(pady = 15, in_ = top, side = 'left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()