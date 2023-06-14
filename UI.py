import tkinter as tk
import os
from data_former import new_plant_creator
from tkinter import messagebox
from tkinter import ttk
from predict import start_process

window_m = tk.Tk()
window_m.title("CropStageRegressor")

style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 10))

folder_path = 'C:/Users/soni2/Desktop/Shreyans/AI/Crop/Control/workbooks'

# Create a frame for content
content_frame = ttk.Frame(window_m)
content_frame.pack(pady=20)

loading_label = None

def select_file():
    file_list = os.listdir(folder_path)
    xlsx = [file for file in file_list if file.endswith('.xlsx')]

    if xlsx:
        clear_frame(content_frame)

        label = ttk.Label(content_frame, text="Following plant models were found:", font=("Arial", 14))
        label.pack(pady=10)

        for i, file in enumerate(xlsx):
            plant_name = file[:-5]
            plant_button = ttk.Button(content_frame, text=plant_name, command=lambda name=plant_name: select_plant(name), width=30)
            plant_button.pack(pady=5)

        new_plant_button = ttk.Button(content_frame, text="Create a new plant", command=create_new_plant, width=30)
        new_plant_button.pack(pady=5)

        hide_start_button()

    else:
        label = ttk.Label(content_frame, text="No plant data exists. Creating a new plant.", font=("Arial", 10))
        label.pack()

        create_new_plant()

def hide_title_label():
    home_label.pack_forget()

home_label = ttk.Label(window_m, text="CropStageRegressor", font=("Arial", 24, "bold"))
home_label.pack(pady=20)

# Start process button
start_button = ttk.Button(window_m, text="Start Process", command=lambda: (select_file(), hide_title_label()), width=30, style="Custom.TButton")
start_button.pack(pady=10)

start_button_visible = True

def select_plant(name):
    label = ttk.Label(content_frame, text=f"Your Plant: {name}", font=("Arial", 14))
    label.pack(pady=10)

    name = name.lower()
    clear_frame(content_frame)
    if name is not None:
        _label = ttk.Label(content_frame, text=f"Your plant is: {name}", font=("Arial", 10, "bold"))
        _label.pack(pady=10)

        # Entry widgets for average height and leaf count
        labelh = ttk.Label(content_frame, text="Enter Average Height value:", font=("Arial", 10))
        labelh.pack(pady=5)
        entryh = ttk.Entry(content_frame, width=25, font=("Arial", 10))
        entryh.pack(pady=5)

        labell = ttk.Label(content_frame, text="Enter Average Leaf count value:", font=("Arial", 10))
        labell.pack(pady=5)
        entryl = ttk.Entry(content_frame, width=25, font=("Arial", 10))
        entryl.pack(pady=5)

        def enter_values():
            loading_label = None
            show_loading_message()
            h_value = entryh.get()
            l_value = entryl.get()
            window_m.update()
            try: 
                tdata = start_process(name, h_value, l_value)
                if tdata == -1:
                    result = messagebox.askquestion("Error", "The CSV file is locked.\nDo you want to restart:", icon="error")
                    if result == "yes":
                        select_file()
                        pass
                    else:
                        window_m.destroy()
                        pass
                elif tdata[0] != None:
                    hide_loading_message()
                    display_results(tdata)
                    hide_title_label()  # Hide the title label after displaying results
            except Exception:
                messagebox.showerror("Error", "Error Occurred")
                select_file()
            hide_start_button()

        button_s = ttk.Button(content_frame, text="Enter", command=enter_values, width=30, style="Custom.TButton")
        button_s.pack(pady=10)

    else:
        label = ttk.Label(content_frame, text="Name not found.", font=("Arial", 10))
        label.pack(pady=10)

def create_new_plant():
    clear_frame(content_frame)

    label = ttk.Label(content_frame, text="Enter the name of the new plant:", font=("Arial", 10))
    label.pack(pady=5)

    entry = ttk.Entry(content_frame, width=30, font=("Arial", 10))
    entry.pack(pady=5)

    def save_new_plant():
        new_plant = str(entry.get())
        if os.path.exists(folder_path + "/" + new_plant + ".xlsx"):
            messagebox.showerror("Error", "This file already exists in the folder.")
        else:
            path = folder_path + "/" + new_plant + ".xlsx"
            new_plant_creator(new_plant, path)
            messagebox.showinfo("Success", f"New file called {new_plant}.xlsx created!")
        select_file()
        hide_start_button()

    button = ttk.Button(content_frame, text="Save", command=save_new_plant, width=30, style="Custom.TButton")
    button.pack(pady=5)

def display_results(tdata):
    clear_frame(content_frame)
    result_label = ttk.Label(content_frame, text="Results:", font=("Arial", 14))
    result_label.pack(pady=10)

    def show():

        stage_label = ttk.Label(content_frame, text=f"Growth Stage: {str(tdata[0][0])}", font=("Arial", 10))
        stage_label.pack(pady=5)

        temperature_label = ttk.Label(content_frame, text=f"Temperature: {tdata[0][1]}", font=("Arial", 10))
        temperature_label.pack(pady=5)

        humidity_label = ttk.Label(content_frame, text=f"Humidity: {tdata[0][2]}", font=("Arial", 10))
        humidity_label.pack(pady=5)

        light_label = ttk.Label(content_frame, text=f"Light: {tdata[0][3]}", font=("Arial", 10))
        light_label.pack(pady=5)

        co2_label = ttk.Label(content_frame, text=f"CO2 Levels: {tdata[0][4]}", font=("Arial", 10))
        co2_label.pack(pady=5)

        ec_label = ttk.Label(content_frame, text=f"EC: {tdata[0][5]}", font=("Arial", 10))
        ec_label.pack(pady=5)

        ph_label = ttk.Label(content_frame, text=f"pH: {tdata[0][6]}", font=("Arial", 10))
        ph_label.pack(pady=5)

        btn = ttk.Button(content_frame, text="Restart", command=select_file, width=30, style="Custom.TButton")
        btn.pack(pady=10)

    if tdata:
        show()
    else:
        result_label.config(text="No results found.")
        result_label.pack(pady=10)

def show_loading_message():
    global loading_label
    loading_label = ttk.Label(content_frame, text="Loading...", font=("Arial", 10))
    loading_label.pack(pady=10)
    window_m.update()
    import time
    time.sleep(1)  # Delay for 1 second

    loading_label.config(text="Label Encoding Categorical Values...")
    window_m.update()

    time.sleep(1)  # Delay for 1 second

    loading_label.config(text="Training and Predicting...")
    window_m.update()

def hide_loading_message():
    global loading_label
    if loading_label:
        loading_label.pack_forget()
        loading_label = None

def clear_frame(frame):
    for child in frame.winfo_children():
        child.destroy()

def hide_start_button():
    global start_button_visible
    if start_button_visible:
        start_button.pack_forget()
        start_button_visible = False

# Home page label

# Set window size and center it on the screen
window_m.geometry("500x400")
window_m.eval('tk::PlaceWindow . center')
window_m.mainloop()
