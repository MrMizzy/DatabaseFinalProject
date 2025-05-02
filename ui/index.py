import customtkinter as ctk
from PIL import Image
from models.hostel_model import get_hostel_details_by_name, get_room_types_by_hostel_name

class GenericHostelWindow(ctk.CTk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry("1400x700")

        # Get data
        self.hostel_info = get_hostel_details_by_name(title)
        self.room_info = get_room_types_by_hostel_name(title)

        self.create_content()

    def create_content(self):
        self.content_frame = ctk.CTkFrame(self, fg_color="#1d1065")
        self.content_frame.pack(fill="both", expand=True)

        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_columnconfigure(2, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(1, weight=1)

        # Left Column: Hostel Info
        about_frame = ctk.CTkFrame(self.content_frame, fg_color="#444444", border_color="white", border_width=1)
        about_frame.grid(row=0, column=0, sticky="nsew", padx=16, pady=(18, 8))

        manager_frame = ctk.CTkFrame(self.content_frame, fg_color="#444444", border_color="white", border_width=1)
        manager_frame.grid(row=1, column=0, sticky="nsew", padx=16, pady=(8, 18))

        # Right Section: Room Info
        result_frame = ctk.CTkFrame(self.content_frame, fg_color="#444444")
        result_frame.grid(row=0, rowspan=2, column=1, columnspan=2, sticky="nsew", padx=24, pady=24)

        # Fill in hostel info
        if self.hostel_info:
            ctk.CTkLabel(about_frame, text=self.hostel_info["Hostel_Name"], font=("Roboto", 24, "bold")).pack(pady=10)
            ctk.CTkLabel(about_frame, text=f"Location: {self.hostel_info['Location']}", font=("Roboto", 16)).pack(pady=5)
            ctk.CTkLabel(manager_frame, text=f"Manager: {self.hostel_info['Manager_Name']}", font=("Roboto", 16)).pack(pady=5)
            ctk.CTkLabel(manager_frame, text=f"Phone: {self.hostel_info['PhoneNo.']}", font=("Roboto", 16)).pack(pady=5)

        # Fill in room info as clickable buttons
        for room in self.room_info:
            info = f"{room['Room_Description']} - GHS {room['Price']} | Total: {room['Total_Rooms']} | Available: {room['Available_Rooms']}"
            button = ctk.CTkButton(result_frame, text=info, font=("Roboto", 12), fg_color="#666666",
                                   command=lambda r=room: self.show_room_instances(r))
            button.pack(anchor="w", pady=4, fill="x", padx=5)

    def show_room_instances(self, room_type):
        import tkinter.messagebox
        from models.hostel_model import get_room_instances_by_type

        rooms = get_room_instances_by_type(room_type['Room_Description'])
        if not rooms:
            tkinter.messagebox.showinfo("No Rooms", "No available room instances for this type.")
            return

        popup = ctk.CTkToplevel(self)
        popup.title(room_type["Room_Description"])
        popup.geometry("500x400")

        # Add a scrollable frame to the popup
        scroll_frame = ctk.CTkScrollableFrame(popup, fg_color="#333333")
        scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

        for r in rooms:
            label = ctk.CTkLabel(scroll_frame, text=f"Room: {r['Room_ID']} | Beds Available: {r['Available_Beds']}", font=("Roboto", 14))
            label.pack(pady=5, anchor="w")

class HostelWindow(ctk.CTk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry("1400x700")
        ctk.CTkLabel(self, text=title, font=("Roboto", 24)).pack(pady=20)

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Main page")
        self.geometry("1400x700")

        # Debounce variable for search
        self._search_after_id = None

        # Load the UI
        self.create_header()

        # Create tab view
        self.tabs = ctk.CTkTabview(self,
                                   fg_color="#1d1065",
                                   segmented_button_fg_color="#7b8bae",
                                   segmented_button_selected_color="white",
                                   segmented_button_selected_hover_color=None,
                                   segmented_button_unselected_color="#7b8bae",
                                   segmented_button_unselected_hover_color="white",
                                   text_color="black")

        # self.tabs.grid(row=1, column=0)
        self.tabs.pack(fill="both", padx=10, expand=True)
        
        self.create_hostel_view()
        self.create_search_view()


    def create_header(self):
        self.header_frame = ctk.CTkFrame(self,
                                         height=250)
        self.header_frame.pack(fill="x", pady=20, padx=10)
        # self.header_frame.grid(row= 0, column= 0, sticky= "nsew")
        ctk.CTkLabel(self.header_frame, text="Header", font=("Roboto", 14)).pack(fill="x")
        

    def create_hostel_view(self):
        # create frame and set position
        tab = self.tabs.add("View Hostels")
        self.hostel_section = ctk.CTkScrollableFrame(tab,
                                   fg_color="#1d1065")
        self.hostel_section.pack(fill="both", expand=True)

        # Create buttons for each hostel
        self.create_hostel_buttons(self.hostel_section)
    

    def create_hostel_buttons(self, master: ctk.CTkScrollableFrame):
        hostel_section = master

        # Configs for this view
        hostel_section.grid_columnconfigure(0, weight=1)
        hostel_section.grid_columnconfigure(1, weight=1)
        hostel_section.grid_columnconfigure(2, weight=1)

        # Photos of hostels as buttons
        ceewus = ctk.CTkImage(light_image= Image.open("Images/CEEWUS.png"),
                              dark_image=Image.open("Images/CEEWUS.png"),
                              size=(401,245)) #WidthxHeight
        ceewus_button = ctk.CTkButton(hostel_section,
                                      image=ceewus,
                                      text="",
                                      fg_color='transparent',
                                      command=self.ceewus_page)
        ceewus_button.grid(row=0,column=0, padx= 10, pady= 5)

        charlotte = ctk.CTkImage(light_image= Image.open("Images/Charlotte's_Court.png"),
                              dark_image=Image.open("Images/Charlotte's_Court.png"),
                              size=(401,245)) #WidthxHeight
        charlotte_button = ctk.CTkButton(hostel_section,
                                      image=charlotte,
                                      text="",
                                      fg_color='transparent',
                                      command=self.charlotte_page)
        charlotte_button.grid(row=0,column=1, padx= 10, pady= 5)

        columbiana = ctk.CTkImage(light_image= Image.open("Images/Columbiana.png"),
                              dark_image=Image.open("Images/Columbiana.png"),
                              size=(401,245)) #WidthxHeight
        columbiana_button = ctk.CTkButton(hostel_section,
                                      image=columbiana,
                                      text="",
                                      fg_color='transparent',
                                      command=self.columbiana_page)
        columbiana_button.grid(row=0,column=2, padx= 10, pady= 5)

        duf_ann = ctk.CTkImage(light_image= Image.open("Images/Dufie_Annex.png"),
                              dark_image=Image.open("Images/Dufie_Annex.png"),
                              size=(401,245)) #WidthxHeight
        duf_ann_button = ctk.CTkButton(hostel_section,
                                      image=duf_ann,
                                      text="",
                                      fg_color='transparent',
                                      command=self.duf_ann_page)
        duf_ann_button.grid(row=1,column=0, padx= 10, pady= 5)

        duf_gol = ctk.CTkImage(light_image= Image.open("Images/Dufie_Gold.png"),
                              dark_image=Image.open("Images/Dufie_Gold.png"),
                              size=(401,245)) #WidthxHeight
        duf_gol_button = ctk.CTkButton(hostel_section,
                                      image=duf_gol,
                                      text="",
                                      fg_color='transparent',
                                      command=self.duf_gol_page)
        duf_gol_button.grid(row=1,column=1, padx= 10, pady= 5)

        duf_pla = ctk.CTkImage(light_image= Image.open("Images/Dufie_Platinum.png"),
                              dark_image=Image.open("Images/Dufie_Platinum.png"),
                              size=(401,245)) #WidthxHeight
        duf_pla_button = ctk.CTkButton(hostel_section,
                                      image=duf_pla,
                                      text="",
                                      fg_color='transparent',
                                      command=self.duf_pla_page)
        duf_pla_button.grid(row=1,column=2, padx= 10, pady= 5)

        duf_pre = ctk.CTkImage(light_image= Image.open("Images/Dufie_Prestige.png"),
                              dark_image=Image.open("Images/Dufie_Prestige.png"),
                              size=(401,245)) #WidthxHeight
        duf_pre_button = ctk.CTkButton(hostel_section,
                                      image=duf_pre,
                                      text="",
                                      fg_color='transparent',
                                      command=self.duf_pre_page)
        duf_pre_button.grid(row=3,column=0, padx= 10, pady= 5)

        new_hos = ctk.CTkImage(light_image= Image.open("Images/New_Hosanna.png"),
                              dark_image=Image.open("Images/New_Hosanna.png"),
                              size=(401,245)) #WidthxHeight
        new_hos_button = ctk.CTkButton(hostel_section,
                                      image=new_hos,
                                      text="",
                                      fg_color='transparent',
                                      command=self.new_hos_page)
        new_hos_button.grid(row=3,column=1, padx= 10, pady= 5)

        new_mas = ctk.CTkImage(light_image= Image.open("Images/New_Masere.png"),
                              dark_image=Image.open("Images/New_Masere.png"),
                              size=(401,245)) #WidthxHeight
        new_mas_button = ctk.CTkButton(hostel_section,
                                      image=new_mas,
                                      text="",
                                      fg_color='transparent',
                                      command=self.new_mas_page)
        new_mas_button.grid(row=3,column=2, padx= 10, pady= 5)

        old_hos = ctk.CTkImage(light_image= Image.open("Images/Old_Hosanna.png"),
                              dark_image=Image.open("Images/Old_Hosanna.png"),
                              size=(401,245)) #WidthxHeight
        old_hos_button = ctk.CTkButton(hostel_section,
                                      image=old_hos,
                                      text="",
                                      fg_color='transparent',
                                      command=self.old_hos_page)
        old_hos_button.grid(row=4,column=0, padx= 10, pady= 5)

        old_mas = ctk.CTkImage(light_image= Image.open("Images/Old_Masere.png"),
                              dark_image=Image.open("Images/Old_Masere.png"),
                              size=(401,245)) #WidthxHeight
        old_mas_button = ctk.CTkButton(hostel_section,
                                      image=old_mas,
                                      text="",
                                      fg_color='transparent',
                                      command=self.old_mas_page)
        old_mas_button.grid(row=4,column=1, padx= 10, pady= 5)

        queen = ctk.CTkImage(light_image= Image.open("Images/Queenstar.png"),
                              dark_image=Image.open("Images/Queenstar.png"),
                              size=(401,245)) #WidthxHeight
        queen_button = ctk.CTkButton(hostel_section,
                                      image=queen,
                                      text="",
                                      fg_color='transparent',
                                      command=self.queen_page)
        queen_button.grid(row=4,column=2, padx= 10, pady= 5)

        tanko = ctk.CTkImage(light_image= Image.open("Images/Tanko.png"),
                              dark_image=Image.open("Images/Tanko.png"),
                              size=(401,245)) #WidthxHeight
        tanko_button = ctk.CTkButton(hostel_section,
                                      image=tanko,
                                      text="",
                                      fg_color='transparent',
                                      command=self.tanko_page)
        tanko_button.grid(row=5,column=1, padx= 10, pady= 5)
        
    def columbiana_page(self):
        GenericHostelWindow("Columbiana Hostel").mainloop()

    def duf_ann_page(self):
        GenericHostelWindow("Dufie Annex").mainloop()

    def duf_gol_page(self):
        GenericHostelWindow("Dufie Gold").mainloop()

    def duf_pla_page(self):
        GenericHostelWindow("Dufie Platinum").mainloop()

    def duf_pre_page(self):
        GenericHostelWindow("Dufie Prestige").mainloop()

    def new_hos_page(self):
        GenericHostelWindow("New Hosanna").mainloop()

    def new_mas_page(self):
        GenericHostelWindow("New Masere").mainloop()

    def old_hos_page(self):
        GenericHostelWindow("Old Hosanna").mainloop()

    def old_mas_page(self):
        GenericHostelWindow("Old Masere").mainloop()

    def queen_page(self):
        GenericHostelWindow("Queenstar").mainloop()

    def tanko_page(self):
        GenericHostelWindow("Tanko").mainloop()


    def ceewus_page(self):
        GenericHostelWindow("Ceewus").mainloop()
        
    def charlotte_page(self):
        GenericHostelWindow("Charlotte").mainloop()


    def create_search_view(self):
        tab = self.tabs.add("Search")
        self.search_tab = tab  # Store for callback access
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_columnconfigure(1, weight=1)
        tab.grid_columnconfigure(2, weight=1)
        tab.grid_columnconfigure(3, weight=1)
        tab.grid_rowconfigure(0, weight=1)
        tab.grid_rowconfigure(1, weight=1)

        self.create_price_section(tab)
        self.create_bed_section(tab)

        # Frame for results (scrollable)
        result_scroll_container = ctk.CTkScrollableFrame(tab, fg_color="#444444")
        result_scroll_container.grid(row=0, column=1, columnspan=3, rowspan=2, sticky="nsew", padx=20)
        self.result_section = result_scroll_container
        ctk.CTkLabel(self.result_section, text="Filter Results", font=("Roboto", 32)).pack(pady=10)
        self.refresh_search_results()


    def create_price_section(self, master: ctk.CTkFrame):
        tab = master

        # Frame for price
        price_section = ctk.CTkFrame(tab,
                                     fg_color="#444444")
        price_section.grid(row=0, column= 0, sticky="nsew")
        ctk.CTkLabel(price_section, text="Price", font=("Roboto", 32)).pack(pady=10)

        # Sliders for price
        minprice_frame = ctk.CTkFrame(price_section)
        minprice_frame.pack(fill="x", padx=5, pady=10)
        self.minprice = ctk.IntVar()
        ctk.CTkLabel(minprice_frame, text="Minimum Price", font=("Roboto", 30)).pack(pady=10)
        ctk.CTkLabel(minprice_frame, textvariable= self.minprice).pack(side="left", padx=5)
        minprice_slider = ctk.CTkSlider(minprice_frame,
                                        from_=2500,
                                        to=10000,
                                        number_of_steps=15,
                                        variable=self.minprice)
        minprice_slider.pack(side="right", fill="x", expand=True, padx=5, pady=10)
        minprice_slider.set(2500)
        minprice_slider.configure(command=self.refresh_search_results)
        self.minprice_slider = minprice_slider

        maxprice_frame = ctk.CTkFrame(price_section)
        maxprice_frame.pack(fill="x", padx=5, pady=10)
        self.maxprice = ctk.IntVar()
        ctk.CTkLabel(maxprice_frame, text="Maximum Price", font=("Roboto", 30)).pack(pady=10)
        ctk.CTkLabel(maxprice_frame, textvariable= self.maxprice).pack(side="left", padx=5)
        maxprice_slider = ctk.CTkSlider(maxprice_frame,
                                        from_=2500,
                                        to=10000,
                                        number_of_steps=15,
                                        variable=self.maxprice)
        maxprice_slider.pack(side="right", fill="x", expand=True, padx=5, pady=10)
        maxprice_slider.set(10000)
        maxprice_slider.configure(command=self.refresh_search_results)
        self.maxprice_slider = maxprice_slider

    def create_bed_section(self, master: ctk.CTkFrame):
        tab = master

        # Frame for beds
        bed_section = ctk.CTkFrame(tab,
                                     fg_color="#444444")
        bed_section.grid(row=1, column= 0, sticky= "nsew")
        ctk.CTkLabel(bed_section, text="Beds", font=("Roboto", 32)).pack(pady=10)

        # Sliders for beds
        minbed_frame = ctk.CTkFrame(bed_section)
        minbed_frame.pack(fill="x", padx=5, pady=10)
        self.minbed = ctk.IntVar()
        ctk.CTkLabel(minbed_frame, text="Minimum Beds", font=("Roboto", 30)).pack(pady=10)
        ctk.CTkLabel(minbed_frame, textvariable= self.minbed).pack(side="left", padx=5)
        minbed_slider = ctk.CTkSlider(minbed_frame,
                                        from_=1,
                                        to=4,
                                        number_of_steps=4,
                                        variable=self.minbed)
        minbed_slider.pack(side="right", fill="x", expand=True, padx=5, pady=10)
        minbed_slider.set(1)
        minbed_slider.configure(command=self.refresh_search_results)
        self.minbed_slider = minbed_slider

        maxbed_frame = ctk.CTkFrame(bed_section)
        maxbed_frame.pack(fill="x", padx=5, pady=10)
        self.maxbed = ctk.IntVar()
        ctk.CTkLabel(maxbed_frame, text="Maximum Beds", font=("Roboto", 30)).pack(pady=10)
        ctk.CTkLabel(maxbed_frame, textvariable= self.maxbed).pack(side="left", padx=5)
        maxbed_slider = ctk.CTkSlider(maxbed_frame,
                                        from_=1,
                                        to=4,
                                        number_of_steps=4,
                                        variable=self.maxbed)
        maxbed_slider.pack(side="right", fill="x", expand=True, padx=5, pady=10)
        maxbed_slider.set(4)
        maxbed_slider.configure(command=self.refresh_search_results)
        self.maxbed_slider = maxbed_slider


    def refresh_search_results(self, *args):
        # Debounce: cancel previous after, schedule new after 500ms
        if self._search_after_id:
            self.after_cancel(self._search_after_id)
        self._search_after_id = self.after(1000, self._perform_search)

    def _perform_search(self):
        from models.hostel_model import get_rooms_within_price_range, get_rooms_by_room_size

        # Clear previous results
        for widget in self.result_section.winfo_children():
            widget.destroy()

        min_price = self.minprice.get()
        max_price = self.maxprice.get()
        min_beds = self.minbed.get()
        max_beds = self.maxbed.get()

        price_filtered_rooms = get_rooms_within_price_range(min_price, max_price)
        bed_filtered_rooms = []
        for i in range(min_beds, max_beds + 1):
            bed_filtered_rooms.extend(get_rooms_by_room_size(i))

        # Filter intersection of both criteria
        matched_rooms = []
        seen = set()
        for room in price_filtered_rooms:
            for b_room in bed_filtered_rooms:
                if room["Room_ID"] == b_room["Room_ID"] and room["Room_ID"] not in seen:
                    matched_rooms.append(room)
                    seen.add(room["Room_ID"])

        if not matched_rooms:
            ctk.CTkLabel(self.result_section, text="No rooms match the selected criteria.", font=("Roboto", 16)).pack(pady=20)
            return

        # Avoid duplicate descriptions
        seen_descriptions = set()
        for room in matched_rooms:
            desc = room['Room_Description']
            if desc in seen_descriptions:
                continue
            seen_descriptions.add(desc)
            label = f"{desc} | GHS {room['Price']}"
            button = ctk.CTkButton(self.result_section, text=label, font=("Roboto", 12), fg_color="#666666",
                                   command=lambda r=room: self.show_room_instances({'Room_Description': r['Room_Description']}))
            button.pack(anchor="w", pady=4, fill="x", padx=10)
    
    def show_room_instances(self, room_type):
        import tkinter.messagebox
        from models.hostel_model import get_room_instances_by_type

        rooms = get_room_instances_by_type(room_type['Room_Description'])
        if not rooms:
            tkinter.messagebox.showinfo("No Rooms", "No available room instances for this type.")
            return

        popup = ctk.CTkToplevel(self)
        popup.title(room_type["Room_Description"])
        popup.geometry("500x400")

        # Scrollable frame for room list
        scroll_frame = ctk.CTkScrollableFrame(popup, fg_color="#333333")
        scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

        for r in rooms:
            label = ctk.CTkLabel(scroll_frame, text=f"Room: {r['Room_ID']} | Beds Available: {r['Available_Beds']}", font=("Roboto", 14))
            label.pack(pady=5, anchor="w")


MainWindow().mainloop()

