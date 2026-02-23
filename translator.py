import tkinter as tk
from tkinter import ttk, messagebox
import deep_translator
import pyttsx3 
import pyperclip

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        selected = language_select.get()
        tgt = lang_codes[selected]     

        translated = deep_translator.GoogleTranslator(source='auto', target=tgt).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", f"Translation Failed: {e}")


def speak_text():
    content = output_text.get("1.0", tk.END).strip()
    if content:
        engine.say(content)
        engine.runAndWait()
    else:
        messagebox.showinfo("Info", "Nothing to speak.")


def copy_text():
    content = output_text.get("1.0", tk.END).strip()
    if content:
        pyperclip.copy(content)
        messagebox.showinfo("Copied", "Text copied to clipboard!")
    else:
        messagebox.showinfo("Info", "Nothing to copy.")


def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


root = tk.Tk()
root.title("Beautiful Language Translator")
root.geometry("650x600")
root.configure(bg="#1F2024")

title = tk.Label(root, text="🌐 Language Translator",
                 font=("Segoe UI", 20, "bold"), fg="white", bg="#1F2024")
title.pack(pady=10)

box = tk.Frame(root, bg="#2A2C31", bd=2, relief="solid")
box.pack(pady=10, padx=20, fill="both", expand=True)

lang_label = tk.Label(box, text="Select Output Language",
                      font=("Segoe UI", 12), fg="white", bg="#2A2C31")
lang_label.pack(pady=5)

languages = [
    "English",
    "Hindi",
    "Marathi",
    "Spanish",
    "French",
    "German",
    "Italian",
]

lang_codes = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it"
}

language_select = ttk.Combobox(box, values=languages,
                               font=("Segoe UI", 12), state="readonly")
language_select.current(0)
language_select.pack(pady=5)

input_label = tk.Label(box, text="Enter Text",
                       font=("Segoe UI", 12), fg="white", bg="#2A2C31")
input_label.pack(pady=5)

input_text = tk.Text(box, height=6, font=("Segoe UI", 12),
                     bd=2, relief="ridge", wrap="word", bg="#F2F2F2")
input_text.pack(padx=10, pady=5, fill="x")

btn_frame = tk.Frame(box, bg="#2A2C31")
btn_frame.pack(pady=10)

translate_btn = tk.Button(btn_frame, text="Translate", command=translate_text,
                          font=("Segoe UI", 12, "bold"), bg="#4CAF50",
                          fg="white", padx=20, pady=5)
translate_btn.grid(row=0, column=0, padx=10)

speak_btn = tk.Button(btn_frame, text="Speak", command=speak_text,
                      font=("Segoe UI", 12, "bold"), bg="#2196F3",
                      fg="white", padx=20, pady=5)
speak_btn.grid(row=0, column=1, padx=10)

copy_btn = tk.Button(btn_frame, text="Copy", command=copy_text,
                     font=("Segoe UI", 12, "bold"), bg="#9C27B0",
                     fg="white", padx=20, pady=5)
copy_btn.grid(row=0, column=2, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_all,
                      font=("Segoe UI", 12, "bold"), bg="#FF5722",
                      fg="white", padx=20, pady=5)
clear_btn.grid(row=0, column=3, padx=10)

out_label = tk.Label(box, text="Translated Text",
                     font=("Segoe UI", 12), fg="white", bg="#2A2C31")
out_label.pack(pady=5)

output_text = tk.Text(box, height=6, font=("Segoe UI", 12),
                      bd=2, relief="ridge", wrap="word", bg="#F2F2F2")
output_text.pack(padx=10, pady=5, fill="x")

root.mainloop()