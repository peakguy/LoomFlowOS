import tkinter as tk
import random
list = [
    ":[",
    ":(",
    ":<"
    
]
def crash(code,message):
    window = tk.Tk()
    window.title("Loomflow")
    window.geometry("600x400")
    emojicon = list[random.randint(0, len(list)-1)]
    label = tk.Label(window, text=f"loomflow crashed {emojicon}", font=("Spot Mono", 20))
    label.grid(row=0, column=0, padx=5, pady=5)
    error_code = tk.Label(window, text=f"Error code: {code}", font=("Spot Mono", 12))
    error_code.grid(row=0, column=1, padx=5, pady=5)
    frame = tk.Frame(window, bg="white", highlightbackground="white", highlightthickness=2)
    frame.grid(row=1, column=0, columnspan=1, padx=5, pady=5, rowspan=2)
    message_label = tk.Label(frame, text=f"{message}", font=("Spot Mono", 12))
    message_label.pack()
    button = tk.Button(window, text="Close", command=window.destroy)
    button.grid(row=0, column=2, padx=5, pady=5)
    
    window.mainloop()
    pass

