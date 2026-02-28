from tkinter import Tk, Frame, Label, Radiobutton, IntVar
from PIL import Image, ImageTk
import os

class FoodViewer:
    def __init__(self):
        # Main window
        self.root = Tk()
        self.root.title("Food Viewer")
        self.root.geometry("400x300")
        
        # Frames
        self.img_frame = Frame(self.root)
        self.img_frame.pack()
        self.rbdBtn_frame = Frame(self.root)
        self.rbdBtn_frame.pack()
        
        # Base path is the same folder as the script
        img_folder = os.path.dirname(__file__)
        
        # Load images
        self.imgOne = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, "chicken.jpg")).resize((400, 300)))
        self.imgTwo = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, "pie.jpg")).resize((400, 300)))
        self.imgThree = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, "pizza.jpg")).resize((350, 300)))
        self.imgFour = ImageTk.PhotoImage(Image.open(os.path.join(img_folder, "steak.jpg")).resize((300, 300)))
        
        # Label to show image
        self.lbl = Label(self.img_frame, image=self.imgOne)
        self.lbl.pack()
        
        # Variable for Radiobuttons
        self.var = IntVar()
        self.var.set(1)  # default is Chicken
        
        # Radiobuttons
        self.radio_a = Radiobutton(self.rbdBtn_frame, text="Chicken", variable=self.var, value=1,
                                   command=self.on_radio_select)
        self.radio_a.pack(side="left", padx=10)
        
        self.radio_b = Radiobutton(self.rbdBtn_frame, text="Pie", variable=self.var, value=2,
                                   command=self.on_radio_select)
        self.radio_b.pack(side="left", padx=10)
        
        self.radio_c = Radiobutton(self.rbdBtn_frame, text="Pizza", variable=self.var, value=3,
                                   command=self.on_radio_select)
        self.radio_c.pack(side="left", padx=10)
        
        self.radio_d = Radiobutton(self.rbdBtn_frame, text="Steak", variable=self.var, value=4,
                                   command=self.on_radio_select)
        self.radio_d.pack(side="left", padx=10)
        
        # Start main loop
        self.root.mainloop()
    
    def on_radio_select(self):
        choice = self.var.get()
        # Swap image based on selection
        if choice == 1:
            self.lbl.config(image=self.imgOne)
        elif choice == 2:
            self.lbl.config(image=self.imgTwo)
        elif choice == 3:
            self.lbl.config(image=self.imgThree)
        elif choice == 4:
            self.lbl.config(image=self.imgFour)

# Run the GUI
if __name__ == "__main__":
    app = FoodViewer()