import customtkinter as ctk
from PIL import Image


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Main page")
        self.geometry("1400x700")

        # Load the UI
        self.create_header()

        # Create tab view
        self.tabs = ctk.CTkTabview(self, 
                                   width=600,
                                   height=250,
                                   fg_color="#1d1065",
                                   segmented_button_fg_color="#7b8bae",
                                   segmented_button_selected_color="white",
                                   segmented_button_selected_hover_color=None,
                                   segmented_button_unselected_color="#7b8bae",
                                   segmented_button_unselected_hover_color="white",
                                   text_color="black")

        # self.tabs.grid(row=1, column=0)
        self.tabs.pack(fill="x", padx=10)
        
        self.create_hostel_view()
        self.create_search_view()

    def create_header(self):
        self.header_frame = ctk.CTkFrame(self)
        self.header_frame.pack(fill="x", pady=20, padx=10)
        # self.header_frame.grid(row= 0, column= 0, sticky= "nsew")
        ctk.CTkLabel(self.header_frame, text="Header", font=("Roboto", 14)).pack(fill="x")
        

    def create_hostel_view(self):
        # create frame and set position
        tab = self.tabs.add("View Hostels")
        # self.tab.grid(row= 1, column= 0)

        # Photos of hostels as buttons
        ceewus = ctk.CTkImage(light_image= Image.open("Images/CEEWUS.png"),
                              dark_image=Image.open("Images/CEEWUS.png"),
                              size=(401,245)) #WidthxHeight
        ceewus_button = ctk.CTkButton(tab,
                                      image=ceewus,
                                      text="",
                                      fg_color='transparent')
        ceewus_button.grid(row=0,column=0)



    def create_search_view(self):
        tab = self.tabs.add("Search")
        # tab.grid(row= 1, column= 0)
        



MainWindow().mainloop()