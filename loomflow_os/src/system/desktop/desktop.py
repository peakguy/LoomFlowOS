import tkinter as tk
import json
apps = json.load(open("apps/app_key.json", "r"))
def main():
    window = tk.Tk()

    window.attributes("-fullscreen", True)
    window.title("Loomflow Desktop")
    bg_image = tk.PhotoImage(file="src/system/desktop/desktop.png")
    background_picture = tk.Label(window, image=bg_image)
    background_picture.place(relx=0, rely=0, relwidth=1, relheight=1)  # Use place instead of pack

    def setup_taskbar():
        bgcolor = "gray"  # Set the background color for the taskbar
        taskbar = tk.Frame(window, bg=bgcolor, height=100)
        taskbar.pack(side=tk.BOTTOM, fill=tk.X)
        taskbar_label = tk.Label(taskbar, text="Loom", fg="lightgreen",bg=bgcolor, font=("Big Bad Blocks", 20))
        taskbar_label.pack(side=tk.LEFT, padx=10)
        for app in apps.get("apps", {}).values():
            app_button = tk.Button(taskbar, text=app["name"], bg=bgcolor, fg="black", font=("Big Bad Blocks", 12))
            app_button.pack(side=tk.LEFT, padx=5, pady=5)
            
        
    setup_taskbar()
    window.mainloop()