import tkinter as tk
from PIL import Image,ImageTk
import PyPDF2
import time

from tkinter.filedialog import askopenfile

#define root UI
root = tk.Tk()

#define canvas
canvas = tk.Canvas(root, height = 600, width = 300)
canvas.grid(columnspan=4,rowspan=4)

#open Image
logo = Image.open("./logos/logo1.jpg")
logo = ImageTk.PhotoImage(logo)

logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

#instructions
instructions = tk.Label(root, text="Select a pdf file from a computer to extract its text:")
instructions.grid(columnspan=3, column=0, row=1)

#function
def open_file():
    browse_text.set("Loading...")
    filename = askopenfile(parent=root, mode="rb", title = "Choose a pdf file", filetypes = [("Pdf file","*.pdf")] )
    if filename:
        print("File was succesfully loaded")
        read_pdf = PyPDF2.PdfFileReader(filename)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        #text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        print(page_content)
        #sleep before changing value from loading to browse
        time.sleep(1)
        browse_text.set("Browse")
    


#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text, command=lambda:open_file(), bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1,row=2)

canvas = tk.Canvas(root, height = 600, width = 300)
canvas.grid(columnspan=3)
#start display
root.mainloop()
#if __name__ == '__main__':
#    ui()

