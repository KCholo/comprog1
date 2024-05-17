import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk
from pathlib import Path
import os
from abc import ABC, abstractmethod

# Function to get the relative path of an asset
def relative_to_assets(path: str) -> Path:
    ASSETS_PATH = Path(__file__).parent / Path(r"C:\Users\amiel\Downloads\COMPROG SHIT\build\assets\frame0")
    return ASSETS_PATH / Path(path)

# Function to restore the main window
def restore_main_window():
    # Clear the current window widgets
    for widget in window.winfo_children():
        widget.destroy()

    # Create a canvas
    canvas = tk.Canvas(window, width=500, height=300)
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Load and place the image on the canvas
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(245.0, 58.0, image=image_image_1)
    canvas.image = image_image_1  # Retain reference to the image

    # Add some text elements to the canvas
    canvas.create_text(105.0, 0.0, anchor="nw", text="GEOROCK ANALYZER", fill="#000000", font=("Viga Regular", 26 * -1))
    canvas.create_text(170.0, 47.0, anchor="nw", text="What would you like to do?", fill="#000000", font=("Lexend Regular", 12 * -1))
    canvas.create_text(190.0, 100.0, anchor="nw", text="PLEASE SELECT", fill="#000000", font=("Lexend Regular", 15 * -1, "bold"))

    # Create and place button 1
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = tk.Button(window, image=button_image_1, borderwidth=0, highlightthickness=0, command=rock_database, relief="flat")
    button_1.place(relx=0.75, rely=0.5, anchor="center", width=234.0, height=25.0)  # Adjusted from 0.6 to 0.55
    button_1.image = button_image_1  # Retain reference to the image

    # Create and place button 2
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = tk.Button(window, image=button_image_2, borderwidth=0, highlightthickness=0, command=open_rock_list_window, relief="flat")
    button_2.place(relx=0.25, rely=0.5, anchor="center", width=236.0, height=25.0)  # Adjusted from 0.4 to 0.45
    button_2.image = button_image_2  # Retain reference to the image

    # Configure the grid
    window.rowconfigure(1, weight=1)  # Allow the canvas row to expand
    window.columnconfigure([0, 1], weight=1)  # Allow both columns to expand equally

def open_rock_list_window():
    # Nested functions for event handling
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_canvas_configure(event):
        canvas_width = event.width
        frame_width = content_frame.winfo_reqwidth()
        new_x = max(0, (canvas_width - frame_width) // 2)
        canvas.coords(content_window, new_x, 0)
        canvas.itemconfig(content_window, width=canvas_width)

    def show_tooltip(event, text):
        tooltip = tk.Toplevel(window)
        tooltip.wm_overrideredirect(True)
        tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
        label = tk.Label(tooltip, text=text, background="white", relief="solid", borderwidth=1, font=("Calibri", 10))
        label.pack()
        event.widget.tooltip = tooltip

    def hide_tooltip(event):
        if hasattr(event.widget, 'tooltip'):
            event.widget.tooltip.destroy()

    # Clear the main window by removing all existing widgets
    for widget in window.winfo_children():
        widget.destroy()

    # Update the main window title and set a fixed size
    window.title("Available Georocks")
    window.geometry("400x400")

    # Add a label to the main window
    label = tk.Label(window, text="Available Georocks", font=("Arial", 14))
    label.pack(anchor="n", pady=10)

    # Create a frame to hold the scrollable content and center it in the window
    scroll_frame = tk.Frame(window)
    scroll_frame.pack(fill=tk.BOTH, expand=True)

    # Create a canvas inside the frame
    canvas = tk.Canvas(scroll_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a vertical scrollbar and link it to the canvas
    scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to hold the content
    content_frame = tk.Frame(canvas)

    # Create a window in the canvas to host the content frame
    content_window = canvas.create_window((0, 0), window=content_frame, anchor="n")

    # Create a centered frame inside the content frame
    centered_frame = tk.Frame(content_frame)
    centered_frame.pack(anchor="center")

    # Define the list of georocks
    rock_list = [
        "Granite", "Limestone", "Obsidian", "Sandstone", "Shale",
        "Basalt", "Marble", "Slate", "Gneiss", "Schist", "Quartzite",
        "Conglomerate", "Gabbro", "Dolomite", "Rhyolite", "Anorthosite",
        "Siltstone", "Gypsum", "Pumice", "Serpentine"
    ]

    # Create columns dynamically based on the number of rocks
    num_columns = 2
    columns = [tk.Frame(centered_frame) for _ in range(num_columns)]
    for column in columns:
        column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Distribute georocks into columns
    rock_properties = {
        "Granite": {"hardness": 6, "color": "Beige"},
        "Limestone": {"hardness": 3, "color": "Dirty White"},
        "Obsidian": {"hardness": 5, "color": "Black"},
        "Sandstone": {"hardness": 6, "color": "Tan"},
        "Shale": {"hardness": 3, "color": "Gray"},
        "Basalt": {"hardness": 7, "color": "Black"},
        "Marble": {"hardness": 4, "color": "White"},
        "Slate": {"hardness": 4, "color": "Gray"},
        "Gneiss": {"hardness": 7, "color": "Light Gray"},
        "Schist": {"hardness": 7, "color": "Green"},
        "Quartzite": {"hardness": 7, "color": "Light Brown"},
        "Conglomerate": {"hardness": 7, "color": "Brown"},
        "Gabbro": {"hardness": (6,7), "color": "Dark Green"},
        "Dolomite": {"hardness": (3,4), "color": "White"},
        "Rhyolite": {"hardness": 6, "color": "Light Gray"},
        "Anorthosite": {"hardness": 6, "color": "Gray"},
        "Siltstone": {"hardness": 3, "color": "Brown"},
        "Gypsum": {"hardness": 2, "color": "Dirty White"},
        "Pumice": {"hardness": 2, "color": "White"},
        "Serpentine": {"hardness": 4, "color": "Yellow-Green"}
    }

    for index, rock in enumerate(rock_list):
        parent = columns[index % num_columns]
        bullet_label = tk.Label(parent, text=f"• {rock}", font=("Arial", 12), anchor="w")
        bullet_label.pack(anchor="w", padx=5, pady=2)  # Left-align the labels with padding
        tooltip_text = f"Hardness: {rock_properties[rock]['hardness']}, Color: {rock_properties[rock]['color']}"
        bullet_label.bind("<Enter>", lambda event, text=tooltip_text: show_tooltip(event, text))
        bullet_label.bind("<Leave>", hide_tooltip)

    # Bind events to update the canvas scroll region
    content_frame.bind("<Configure>", on_frame_configure)
    canvas.bind("<Configure>", on_canvas_configure)

    # Add a back button
    back_button = tk.Button(window, text="Back", command=restore_main_window)
    back_button.pack(anchor="w", padx=10, pady=10)
    
def rock_database():
    
    # Clear the main window by removing all existing widgets
    for widget in window.winfo_children():
        widget.destroy()
    
    window.title("Rock Database")
    window.geometry("500x300")  # Adjust the size as needed

    label = tk.Label(window, text="ROCK IDENTIFIER", font=("Arial", 14, "bold"))
    label.pack(padx=20, pady=20)

    class RockDatabase(ABC):
        @abstractmethod
        def search(self, physical_characteristics):
            raise NotImplementedError("Subclass must implement this method")
 
    # Step 2: Implement the interface with a specific database
    class SimpleRockDatabase(RockDatabase):
        def __init__(self):
            self.database = {
                "granite": {
                    "color": "Beige",
                    "hardness": 6,
                    "formation": "Igneous",
                    "picture": "granite.jpg",
                    "texture": "Coarse-Grained",
                    "commonly_found" : "Mountain ranges and continental crust.", 
                    "formation_process" : "It develops from magma cooling and solidifying beneath the Earth's surface."
                },
                "limestone": {
                    "color": "Dirty White",
                    "hardness": 3,
                    "formation": "Sedimentary",
                    "picture": "limestone.jpg",
                    "texture": "Fine-grained",
                    "commonly_found": "Marine waters",
                    "formation_process": "It primarily formed from the accumulation of marine organisms such as coral, shells, and algae."
                },
                "obsidian": {
                    "color": "Black",
                    "hardness": 5,
                    "formation": "Igneous",
                    "picture": "obsidian.jpg",
                    "texture": "Glassy",
                    "commonly_found": "Areas with recent volcanic activity",
                    "formation_process": "It originates from the rapid cooling of lava, which hinders mineral crystal growth."
                },
                "sandstone": {
                    "color": "Tan",
                    "hardness": 6,
                    "formation": "Sedimentary",
                    "picture": "sandstone.jpg",
                    "texture": "Medium-grained",
                    "commonly_found": "Ocean floor, desert dunes, beaches",
                    "formation_process": "It forms from the accumulation and cementation of sand grains."
                },
                "shale": {
                    "color": "Gray",
                    "hardness": 3,
                    "formation": "Sedimentary",
                    "picture": "shale.jpg",
                    "texture": "Fine-grained",
                    "commonly_found": "Lakes, river deltas",
                    "formation_process": "It develops through the compression of clay, silt, and other fine-grained sediments."
                },
                "basalt": {
                    "color": "Black",
                    "hardness": 7,
                    "formation": "Igneous",
                    "picture": "basalt.jpg",
                    "texture": "Fine-grained",
                    "commonly_found": "Ocean floors, rift zones",
                    "formation_process": "It forms from the rapid cooling of lava on the Earth's surface."
                },
                "marble": {
                    "color": "White",
                    "hardness": 4,
                    "formation": "Metamorphic",
                    "picture": "marble.jpg",
                    "texture": "Granular",
                    "commonly_found": "Mountainous areas with significant tectonic activity",
                    "formation_process": "When it is under heat and pressure, the minerals in limestone recrystallize, resulting in the formation of marble."
                },
                "slate": {
                    "color": "Gray",
                    "hardness": 4,
                    "formation": "Metamorphic",
                    "picture": "slate.jpg",
                    "texture": "Fine-grained",
                    "commonly_found": "Mountainous areas with intense tectonic pressure",
                    "formation_process": "It originates through the transformation of shale or sedimentary rocks rich in clay."
                },
                "gneiss": {
                    "color": "Light Gray",
                    "hardness": 7,
                    "formation": "Metamorphic",
                    "picture": "gneiss.jpg",
                    "texture": "Foliated",
                    "commonly_found": "Mountain ranges",
                    "formation_process": "It develops through the metamorphic process of pre-existing rocks like granite, shale, or basalt."
                },
                "schist": {
                    "color": "Green",
                    "hardness": 7,
                    "formation": "Metamorphic",
                    "picture": "schist.jpg",
                    "texture": "Medium to coarse-grained",
                    "commonly_found": "Mountainous areas with significant tectonic pressure",
                    "formation_process": "It forms from the metamorphism of shale, mudstone, or volcanic rocks."
                },
                "quartzite": {
                    "color": "Light Brown",
                    "hardness": 7,
                    "texture": "Granular",
                    "formation": "Metamorphic",
                    "picture": "quartzite.jpg",
                    "commonly_found": "Mountains and hillsides",
                    "formation_process": "It is formed when sedimentary sandstone is subjected to high temperature and pressure along collisional tectonic plate boundaries."
                },
                "conglomerate": {
                    "color": "Brown",
                    "hardness":7,
                    "texture": "Coarse-grained",
                    "picture" : "conglomerate.jpg",
                    "formation": "Sedimentary",
                    "commonly_found": "Riverbeds, beaches, and ancient shorelines",
                    "formation_process": "It is formed by the river movement or ocean wave action."
                },
                "gabbro": {
                    "color": "Dark Green",
                    "hardness": (6,7),
                    "texture": "Coarse-grained",
                    "picture": "gabbro.jpg",
                    "formation": "Igneous",
                    "commonly_found": "Oceanic crust, deep within the Earth",
                    "formation_process": "It is formed from the slow cooling of magnesium-rich and iron-rich magma into a holocrystalline mass deep beneath the Earth's surface."
                },
                "dolomite": {
                    "color": "White",
                    "hardness": (3,4),
                    "texture": "Very Fine-grained",
                    "picture": "dolomite.jpg",
                    "formation": "Sedimentary",
                    "commonly_found": "Hydrothermal veins, pore-filling mineral in carbonate rocks",
                    "formation_process": "Dolomite forms in hydrothermal veins or as a pore-filling mineral in carbonate rocks, and more rarely as an accessory component in igneous pegmatites or altered mafic igneous rocks."
                },
                "rhyolite": {
                    "color": "Light Gray",
                    "hardness": 6,
                    "texture": "Fine grained",
                    "picture": "rhyolite.jpg",
                    "formation": "Igneous",
                    "commonly_found": "Volcanic flows, domes",
                    "formation_process": "It is formed by the rapid cooling of magma, usually when it erupts onto the Earth's surface."
                },
                "anorthosite": {
                    "color": "Gray",
                    "hardness": 6,
                    "texture": "Coarse-grained",
                    "picture": "anorthosite.jpg",
                    "formation": "Igneous",
                    "commonly_found": "Oceanic crust, layered intrusions in the Earth's crust",
                    "formation_process": "Anorthosites form through a combination of magmatic differentiation and the crystallization of magma."
                },
                "siltstone": {
                    "color": "Brown",
                    "hardness": 3,
                    "texture": "Fine-grained",
                    "picture": "siltstone.jpg",
                    "formation": "Sedimentary",
                    "commonly_found": "Riverbeds, lakes, and seas",
                    "formation_process": "It is formed when grains of sand are compacted and cemented together over thousands or millions of years."
                },
                "gypsum": {
                    "color": "Dirty White",
                    "hardness": 2,
                    "texture": "Fine-grained",
                    "picture": "gypsum.jpg",
                    "formation": "Sedimentary",
                    "commonly_found": "Evaporite deposits in arid regions",
                    "formation_process": "Gypsum forms when water evaporates in mineral-rich marine soil environments."
                },
                "pumice": {
                    "color": "White",
                    "hardness": 2,
                    "texture": "Rough-textured",
                    "picture": "pumice.jpg",
                    "formation": "Igneous",
                    "commonly_found": "Volcanic vents, ash deposits",
                    "formation_process": "Pumice is formed when volcanoes erupt explosively. It comes from the same kind of magma that forms granite or rhyolite, which is high in silica."
                },
                "serpentine": {
                    "color": "Yellow-Green",
                    "hardness": 4,
                    "texture": "Fine-grained",
                    "picture": "serpentine.jpg",
                    "formation": "Metamorphic",
                    "commonly_found": "Oceanic crust, near tectonic plate boundaries",
                    "formation_process": "It is formed when sea water penetrates the crust and reacts with olivine and pyroxenes to form serpentine, a process known as serpentinization."
                }
        
            }
            # Normalize rock names to title case
            self.database = {rock.capitalize(): characteristics for rock, characteristics in self.database.items()}

        def search(self, physical_characteristics):
            matches = []
            user_color = physical_characteristics.get("color")
            user_hardness = physical_characteristics.get("hardness")

            for rock, characteristics in self.database.items():
                match = True

                # Compare color
                if characteristics.get("color") != user_color:
                    match = False

                # Compare hardness
                rock_hardness = characteristics.get("hardness")
                if isinstance(rock_hardness, tuple):
                    if user_hardness not in rock_hardness:
                        match = False
                else:
                    if rock_hardness != user_hardness:
                        match = False

                # Add matching rock to the list
                if match:
                    matches.append((rock, characteristics))

            return matches
    class GeoRockApp:
        def __init__(self, window):
            self.window = window
            self.database = SimpleRockDatabase()
            
            # Create a center frame for search widgets
            self.center_frame = tk.Frame(self.window)
            self.center_frame.pack(side=tk.TOP, pady=20)  # Center frame with padding at the top

            # Create widgets in the center frame
            self.create_center_widgets()
            
            # Create a frame to hold the canvas and scrollbar
            self.frame = tk.Frame(self.window)
            self.frame.pack(expand=True, fill=tk.BOTH)
            
            # Create canvas and other contents
            self.create_main_content()

        def create_center_widgets(self):
            # Create a label to display error messages and search results above the widgets
            self.message_text = tk.StringVar()
            self.message_label = tk.Label(self.center_frame, textvariable=self.message_text, fg='red')
            self.message_label.pack(anchor='center', pady=0)
            
            # Create search widgets
            self.color_label = tk.Label(self.center_frame, text="Select a Color:")
            self.color_label.pack(anchor='center', pady=0)

            self.style_var = tk.StringVar()
            style_options = ["None", "Black", "Beige", "Brown", "Dark Green", "Dirty White", "Gray", "Green", "Light Gray", "Pink", "Tan", "White", "Yellow-Green", "Light Brown"]
            self.style_combobox = ttk.Combobox(self.center_frame, textvariable=self.style_var, values=style_options, state="readonly")
            self.style_combobox.set("Choose your Color")
            self.style_combobox.pack(anchor='center', pady=0)

            self.hardness_label = tk.Label(self.center_frame, text="Enter hardness of the rock (1-10):")
            self.hardness_label.pack(anchor='center', pady=0)
            
            self.hardness_entry = tk.Entry(self.center_frame)
            self.hardness_entry.pack(anchor='center', pady=0)

            self.back_button = tk.Button(window, text="Back", command=restore_main_window)
            self.back_button.pack(side="left", anchor="sw", padx=10, pady=10)

            self.search_again_button = tk.Button(self.center_frame, text="Search Again", command=self.search_again)
            self.search_again_button.pack_forget()  # Initially hide the "Search Again" button

        def create_main_content(self):
            # Create a Canvas to hold the content
            self.canvas = tk.Canvas(self.frame)
            self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Add a scrollbar to the canvas
            self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.canvas.yview)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Attach the scrollbar to the canvas
            self.canvas.config(yscrollcommand=self.scrollbar.set)

            # Create a frame within the canvas to hold the main content
            self.content_frame = tk.Frame(self.canvas)
            self.content_window = self.canvas.create_window((0, 0), window=self.content_frame, anchor='nw')

            # Bind the canvas to handle scrolling
            self.content_frame.bind("<Configure>", self.on_configure)
            self.canvas.bind("<Configure>", self.on_canvas_configure)

            # Image label for displaying rock images
            self.image_label = tk.Label(self.content_frame)
            self.image_label.pack(anchor='center')

            # Display results label
            self.result_text = tk.StringVar()
            self.result_label = tk.Label(self.content_frame, textvariable=self.result_text, justify=tk.LEFT, wraplength=300)
            self.result_label.pack(anchor='center')
            
            self.search_button = tk.Button(self.center_frame, text="Search", command=self.search_button_click)
            self.search_button.pack(anchor='center', pady=5)

        def on_configure(self, event):
            # Resize the canvas to fit the content frame
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        def on_canvas_configure(self, event):
            # Resize the canvas width
            canvas_width = event.width
            self.canvas.itemconfig(self.content_window, width=canvas_width)

        def search_button_click(self):
            # Clear previous messages and results
            self.message_text.set("")
            self.result_text.set("")
            self.image_label.config(image=None)

            # Get user inputs
            selected_color = self.style_var.get()
            hardness_input = self.hardness_entry.get()

            # Validate inputs
            if selected_color == "Choose your Color":
                self.message_text.set("Error: Please select a color.")
                return

            if not hardness_input:
                self.message_text.set("Error: Please enter a hardness value.")
                return

            # Convert hardness input to float and validate range
            try:
                hardness_value = float(hardness_input)
                if hardness_value < 1 or hardness_value > 10:
                    self.message_text.set("Error: Hardness must be a number between 1 and 10.")
                    return
            except ValueError:
                self.message_text.set("Error: Hardness must be a number between 1 and 10.")
                return

            # Search for matching rocks
            physical_characteristics = {
                "color": selected_color,
                "hardness": hardness_value
            }
            matches = self.database.search(physical_characteristics)

            if matches:
                # Display the first match
                rock, characteristics = matches[0]
                self.display_results(rock, characteristics)
                
                # Hide search widgets after search is performed
                self.hide_search_widgets()
                
                # Show the "Search Again" button since there is a match
                self.search_again_button.pack(anchor='center', pady=0)
            else:
                # No matching rock found
                self.message_text.set("No matching rock found.")

        def display_results(self, rock, characteristics):
            # Preprocess the characteristics text to add indentation in multi-line descriptions
            def format_description(description):
                # Split the description into lines
                lines = description.split('\n')
                # Add indentation to subsequent lines
                formatted_lines = [lines[0]] + [' ' * 5 + line for line in lines[1:]]
                return '\n'.join(formatted_lines)
            
            # Format the rock information text, using the function to format multi-line descriptions
            formatted_text = (
                f"Rock: {rock}\n"
                f"Color: {characteristics['color']}\n"
                f"Hardness: {characteristics['hardness']}\n"
                f"Formation: {characteristics['formation']}\n"
                f"Texture: {characteristics['texture']}\n"
                f"Commonly Found: {characteristics['commonly_found']}\n"
                f"Formation Process: {format_description(characteristics['formation_process'])}\n"
            )

            # Set the formatted text to the result text variable
            self.result_text.set(formatted_text)

            # Configure the Label widget for wrap length and justification
            self.result_label.config(wraplength=300, justify='left')
            
            # Load and display rock image
            image_path = os.path.join(os.path.dirname(__file__), characteristics.get("picture"))
            try:
                image = Image.open(image_path)
                image.thumbnail((200, 200))
                photo = ImageTk.PhotoImage(image)
                self.image_label.config(image=photo)
                self.image_label.photo = photo  # Keep a reference to the image

            except FileNotFoundError:
                self.result_text.set("No matching rock found.")
                self.image_label.config(image=None)

        def hide_search_widgets(self):
            # Hide all search widgets in the center frame
            self.color_label.pack_forget()
            self.style_combobox.pack_forget()
            self.hardness_label.pack_forget()
            self.hardness_entry.pack_forget()
            self.search_button.pack_forget()

        def search_again(self):
            # Clear previous results
            self.result_text.set("")  # Clear any previous results
            self.image_label.config(image=None)  # Clear the displayed image
            self.image_label.photo = None  # Clear image reference
            
            # Reset the combobox to its default value
            self.style_combobox.set("Choose your Color")

            # Clear the hardness entry
            self.hardness_entry.delete(0, tk.END)
            
            # Repack the search widgets in the center frame
            self.color_label.pack(anchor='center', pady=0)
            self.style_combobox.pack(anchor='center', pady=0)
            self.hardness_label.pack(anchor='center', pady=0)
            self.hardness_entry.pack(anchor='center', pady=0)
            self.search_button.pack(anchor='center', pady=5)

            # Hide the "Search Again" button
            self.search_again_button.pack_forget()

            # Repack the back button
            self.back_button.pack(side='left', anchor='sw', padx=10, pady=10)
            
        def back_to_main_screen(self):
            # Reset the application to its initial state
            self.result_text.set("")
            self.image_label.config(image=None)
            self.image_label.photo = None  # Clear image reference

            # Hide the "Search Again" button
            self.search_again_button.pack_forget()

            # Repack all search widgets
            for widget in self.search_widgets:
                widget.pack(anchor='center')

            self.style_combobox.set("Choose your Color")
    
        def run(self):
            self.window.mainloop()
                
    # Create an instance of GeoRockApp with the existing main application window
    app = GeoRockApp(window)

    # Call the function to display the rock database interface
    app.run()

# Create the main window
window = tk.Tk()
window.geometry("500x300")
window.title("GEOROCK ANALYZER")
window.minsize(500, 500)  # Set minimum size of the window

# Create a canvas
canvas = tk.Canvas(window, width=500, height=300)
canvas.place(relx=0.5, rely=0.5, anchor="center")

# Load and place the image on the canvas
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(245.0, 58.0, image=image_image_1)
canvas.image = image_image_1  # Retain reference to the image

# Add some text elements to the canvas
canvas.create_text(105.0, 0.0, anchor="nw", text="GEOROCK ANALYZER", fill="#000000", font=("Viga Regular", 26 * -1))
canvas.create_text(170.0, 47.0, anchor="nw", text="What would you like to do?", fill="#000000", font=("Lexend Regular", 12 * -1))
canvas.create_text(190.0, 100.0, anchor="nw", text="PLEASE SELECT", fill="#000000", font=("Lexend Regular", 15 * -1, "bold"))

# Create and place button 1
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = tk.Button(window, image=button_image_1, borderwidth=0, highlightthickness=0, command=rock_database, relief="flat")
button_1.place(relx=0.75, rely=0.5, anchor="center", width=234.0, height=25.0)  # Adjusted from 0.6 to 0.55
button_1.image = button_image_1  # Retain reference to the image

# Create and place button 2
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = tk.Button(window, image=button_image_2, borderwidth=0, highlightthickness=0, command=open_rock_list_window, relief="flat")
button_2.place(relx=0.25, rely=0.5, anchor="center", width=236.0, height=25.0)  # Adjusted from 0.4 to 0.45
button_2.image = button_image_2  # Retain reference to the image

# Configure the grid
window.rowconfigure(1, weight=1)  # Allow the canvas row to expand
window.columnconfigure([0, 1], weight=1)  # Allow both columns to expand equally

window.resizable(True, True)  # Allow window to be resizable
window.mainloop()