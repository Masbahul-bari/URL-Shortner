import tkinter as tk
from tkinter import messagebox
import pyshorteners

def shorten_url():
    long_url = url_entry.get()
    if not long_url:
        messagebox.showerror("Error", "Please enter a URL!")
        return
    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(long_url)
        result_label.config(text=f"Shortened URL: {short_url}", fg="green")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")


def copy_to_clipboard():
    short_url = result_label.cget("text").replace("Shortened URL: ", "")
    if short_url.startswith("http"):
        root.clipboard_clear()
        root.clipboard_append(short_url)
        root.update()  
        messagebox.showinfo("Copied", "Shortened URL copied to clipboard!")
    else:
        messagebox.showerror("Error", "No shortened URL to copy!")


root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x300")
root.resizable(False, False)


url_label = tk.Label(root, text="Enter URL:", font=("Arial", 12))
url_label.pack(pady=10)


url_entry = tk.Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=5)


shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url, bg="blue", fg="white", font=("Arial", 12))
shorten_button.pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=380)
result_label.pack(pady=10)


copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="green", fg="white", font=("Arial", 12))
copy_button.pack(pady=10)

root.mainloop()
