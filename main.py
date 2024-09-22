import tkinter as tk
import os
import cryptocode

window = tk.Tk()
window.config(padx=30, pady=30)
window.minsize(width=400, height=500)

file_path ="C:\\Users\\umuto\\OneDrive\\Masaüstü\\pyCharm\\secretNotes\\Notes.txt"

def openTxt():
    if os.path.exists(file_path):
        pass
    else:
        file = open("Notes.txt","a")

def write_Notes():
    openTxt()
    title = title_entry.get()
    text = text_text.get("1.0",tk.END)
    key = pass_entry.get()
    encoded = cryptocode.encrypt(text, key)
    with open("Notes.txt","a") as file:
        file.write(title)
        file.write("\n")
        file.write(encoded)
        file.write("\n")
    title_entry.delete(0, tk.END)
    text_text.delete("1.0",tk.END)
    pass_entry.delete(0, tk.END)

def decryption():
    message = text_text.get("1.0", tk.END)
    key = pass_entry.get()
    decoded = cryptocode.decrypt(message, key)
    text_text.delete("1.0",tk.END)
    text_text.insert("1.0",decoded)

title_label = tk.Label(text="Metin başlığı giriniz")
title_label.pack()

title_entry = tk.Entry(width=30)
title_entry.pack()

text_label = tk.Label(text="Metninizi giriniz")
text_label.pack()

text_text = tk.Text(width=30)
text_text.pack()

pass_label = tk.Label(text="Anahtar Kelimenizi girin")
pass_label.pack()

pass_entry = tk.Entry(width=30)
pass_entry.pack()

enc_button = tk.Button(text="Encrypt and Save", command=write_Notes)
enc_button.pack()

dec_button = tk.Button(text="Decrypt",command=decryption)
dec_button.pack()

tk.mainloop()