def open_rock_list_window():
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
    content_window = canvas.create_window((0, 0), window=content_frame, anchor="nw")
    
    # Define the list of georocks
    rock_list = [
        "Granite", "Limestone", "Obsidian", "Sandstone", "Shale",
        "Basalt", "Marble", "Slate", "Gneiss", "Schist", "Quartzite",
        "Conglomerate", "Gabbro", "Dolomite", "Rhyolite", "Anorthosite",
        "Siltstone", "Gypsum", "Pumice", "Serpentine"
    ]
    
    # Create two frames inside the content frame for two columns
    left_column = tk.Frame(content_frame)
    right_column = tk.Frame(content_frame)
    left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    right_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Distribute georocks into two columns
    mid_index = len(rock_list) // 2
    for index, rock in enumerate(rock_list):
        parent = left_column if index < mid_index else right_column
        bullet_label = tk.Label(parent, text=f"• {rock}", font=("Arial", 12), anchor="w")
        bullet_label.pack(anchor="w", padx=5)