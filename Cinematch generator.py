import random 
import tkinter as tk  
from tkinter import ttk


#-------------------------------
# Movie database 
#-------------------------------
movies = {
    "Netflix": {
        "Action": ["Extraction", "The Gray Man","6 Underground"],
        "Comedy": ["Murder Mystery", "The Wrong Missy", "Holidate"],
        "Animation": ["The Mitchells vs The Machines", "Klaus", "Over the Moon"]
    },
    "Disney +":{
        "Action": ["Avengers: Endgame","Black Panther", "Shang-Chi"],
        "Comedy": ["Jungle Cruise", "Free Guy", "Cheaper by the Dozen"],
        "Animation": ["Moana", "Frozen", "Encanto"]
    },
    "Amazon": {
        "Action": ["The Tomorrow War", "Without Remorse", "Jack Ryan"],
        "Comedy": ["Coming 2 America", "The Big Sick", "Late Night"], 
        "Animation": ["Hotel Transylvania", "Rumble", "The Lorax"]
    }
}
#----------------------------
#Setup Tkinter Window 
#----------------------------
root = tk.Tk()
root.title("CineMatch:Movie Generator")
root.geometry("400x350")

#-----------------------------
#Dropdowns for service and genre 
#-----------------------------
tk.Label(root, text="Choose a streaming service:").pack(pady=5)
service_var = tk.StringVar()
service_dropdown = ttk.Combobox(root, textvariable=service_var)
service_dropdown['values'] = list(movies.keys())
service_dropdown.pack(pady=5)

tk.Label(root,text="Choose a genre").pack(pady=5)
genre_var = tk. StringVar()
genre_dropdown = ttk.Combobox(root, textvariable=genre_var)
genre_dropdown ['values'] = ["Action", "Comedy", "Animation"]
genre_dropdown.pack(pady=5)

#----------------------------
# Label for recommendation 
#----------------------------
result_label = tk.Label(root, text ="", font =("Arial", 12))
result_label.pack(pady=20)

#---------------------------
#Function to recommend movie 
def recommend_movie():
    service = service_var.get()
    genre = genre_var.get()
    if service in movies and genre in movies [service]:
        choice = random.choice(movies[service][genre])
        result_label.config(text=f"We recommend:{choice} ({service}), {genre}")
    else:
        result_label.config(text="Please select both streaming service and genre")

#-------------------------------
# Button to generate recommendation 
#-------------------------------
tk.Button(root, text="Generate Movie", command=recommend_movie).pack(pady=10)

#------------------------------
# Run the window 
#------------------------------
root.mainloop()



print("Avaliable streaming services: Netflix, Disney, Amazon")
service = input("Choose a streaming service:").strip()

print("Available genres:Action, Comedy, Animation")
genre = input("Choose a genre:").strip()

service = service.capitalize()
genre = genre.capitalize()

if service in movies and genre in movies [service]:
    choice = random.choice(movies[service][genre])
    print(f"\n We recommend: {choice} ({service}, {genre})")
else:
    print("\n Invalid choice. Please type exactly as shown (e.g., Netflix, Action).")