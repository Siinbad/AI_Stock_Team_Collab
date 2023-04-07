import tkinter as tk

import OpenAI

from tkinter import messagebox


class MyGUI:

    def __init__(self):
        self.AIresponse = None
        self.root = tk.Tk()

        # Set the title and size of the chat box
        self.root.geometry("500x500")
        self.root.title("GUI")

        # Create the Menu
        self.menubar = tk.Menu(self.root)

        self.fileMenu = tk.Menu(self.menubar, tearoff=0)
        self.fileMenu.add_command(label="Close", command=self.on_closing)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Clear", command=self.on_clear)

        self.menubar.add_cascade(menu=self.fileMenu, label="File")

        self.root.config(menu=self.menubar)

        # Create a Label
        self.label = tk.Label(self.root, text="Chat Box", font=('Arial', 16))
        self.label.pack(pady=5)

        # Create Chat Window
        self.chatWindow = tk.Text(self.root, state='disabled', width=44, height=10)
        self.chatWindow.pack(padx=1, pady=5, fill='x')

        # Create TextBox
        # Configure the Columns
        self.textFrame = tk.Frame(self.root)
        self.textFrame.columnconfigure(0, weight=1)
        self.textFrame.columnconfigure(1, weight=10)
        # Create the Send Button
        self.sendBtn = tk.Button(self.textFrame, text='send', bg='light blue', activebackground='white', width=5,
                                 height=2,
                                 font=('Comic Sans', 20), command=self.display_message)
        self.sendBtn.grid(row=0, column=0, sticky=tk.W + tk.E)

        # Create the Text Box
        self.textBox = tk.Text(self.textFrame, width=44, height=3, font=('Arial', 18))
        self.textBox.bind("<KeyPress>", self.on_shortcut)
        self.textBox.grid(row=0, column=1, sticky=tk.W + tk.E)
        self.textFrame.pack(pady=5, fill='x')

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # MAKE SURE THIS IS AT THE END
        self.root.mainloop()

    # Will Display the Message on the Chat Logs
    def display_message(self):
        self.chatWindow.configure(state='normal')
        self.chatWindow.insert('end', "User: " + self.textBox.get('1.0', tk.END))
        self.AIresponse = OpenAI.write_prompt(self.textBox.get('1.0', tk.END))
        self.chatWindow.insert('end', "ChatBot: " + self.AIresponse["choices"][0]["text"] + "\n")  # Add the AI response here
        self.textBox.delete('1.0', tk.END)
        self.chatWindow.configure(state='disabled')

    # Will Close the Window
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to Quit?"):
            self.root.destroy()

    # Will Clear the Chat Logs
    def on_clear(self):
        self.chatWindow.configure(state='normal')
        self.chatWindow.delete('1.0', tk.END)
        self.chatWindow.configure(state='disabled')

    # Will set up a keybind for entering data
    def on_shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.display_message()


MyGUI()
