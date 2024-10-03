import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
from PIL import Image, ImageTk

# Create the root window or login form
window = tk.Tk()
window.title("Travelista Tours - Login")
window.geometry("600x400")
window.config(bg = "#E0F7FF")
window.resizable(False, False)


# function for hide and show password
def toggle_password():
    if password_entry.cget('show') == '*':  # If password is hidden
        password_entry.config(show = '')    # Show password
    else:
        password_entry.config(show = '*')   # Hide password       
    
# Define the login function
def login(): 
    email = email_entry.get()
    password = password_entry.get()
    if email == "it5" and password == "python": 
        messagebox.showinfo("Login", "Login Successful!")
        window.destroy()  # Closes the login window
        open_booking_form()  # Opens the booking form window
        
    elif email == "" or password == "":
        messagebox.showerror("Login", "Please input username and password") 
    else:
        messagebox.showerror("Login", "Invalid credentials!")

# define for log out button
def logout(booking_form):
    booking_form.destroy()  # Close the booking form window  
    
 # function list form   
def view_list_form():
    listform = tk.Tk()
    listform.title("List of Bookings") 
    listform.geometry("1400x700") 
    listform.config(bg = "#E0F7FF")
    listform.resizable(False, False)
    
    # Frame for the table and buttons
    viewlist_frame = tk.Frame(listform, bg = "gray")
    viewlist_frame.pack(pady = 20, padx = 20, fill = tk.BOTH, expand = True)

    # Creating Treeview (Table)
    columns = ("Booking ID", "First Name", "Last name", "Contac Number", "Email", "Arrival", "Departure","Number of adults", "Number of kids", "Number of Nights", "Room Preferences", "Special Request")
    tree = ttk.Treeview(viewlist_frame, columns=columns, show="headings", height=10)
    
    # Define the column headers
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor=tk.CENTER)
    
    # this is only a sample data(@everyone)
    bookings = [
        (1, "John", "Doe", "09507465749", "johnDoe@gamil.com", "2023-09-10", "2023-09-12", "2", "1", "3", "Single Room"),
        (2, "Jane", "Smith", "09074794592", "janesmith@gmail.com", "2023-09-15", "2023-09-18", "4", "0", "2", "Double Room")
    ]
    
    for booking in bookings:
        tree.insert('', tk.END, values = booking)
    
    tree.pack(fill=tk.BOTH, expand=True)

    # Buttons for Update and Delete actions
    button_frame = tk.Frame(listform, bg="gray")
    button_frame.pack(pady=10, fill=tk.X)
    
    update_button = tk.Button(button_frame, text = "Update", font = ("Arial", 12), bg="blue", fg="white", width=15)
    update_button.pack(side=tk.LEFT, padx=20)
    
    delete_button = tk.Button(button_frame, text="Delete", font=("Arial", 12), bg="red", fg="white", width=15)
    delete_button.pack(side=tk.LEFT, padx=20)

    # Close button to exit the view list form
    close_button = tk.Button(button_frame, text="Close", font=("Arial", 12), bg="gray", fg="white", width=15, command=listform.destroy)
    close_button.pack(side=tk.RIGHT, padx=20)
    
    listform.mainloop()
     
                  
# Function for Hompage Panel
def open_booking_form():
    # Booking form panel
    booking_form = tk.Tk()
    booking_form.title("Hotel Booking Form")
    booking_form.geometry("1040x540")
    booking_form.config(bg="#E0F7FF")
    booking_form.resizable(False, False) 
    
    # background image booking form main frame
    bg_image = ImageTk.PhotoImage(Image.open(r"C:\\Users\\HUAWEI\\OneDrive\Documents\\Python_LabActivity\\hotel_pool.jpg"))
    bg_label = tk.Label(booking_form, image = bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # main frame for booking form
    main_frame = tk.Frame(booking_form, bg = "gray")
    main_frame.pack(pady = 20, padx = 20, fill = tk.BOTH, expand = False)

    # Frame for 'Personal Details' and 'Make a Reservation'
    personal_details_frame = tk.Frame(main_frame, bg = "black")
    personal_details_frame.grid(row = 0, column = 0, padx = 20, pady = 20, ipadx = 25, sticky = "nw")

    reservation_frame = tk.Frame(main_frame, bg = "black")
    reservation_frame.grid(row = 0, column = 1, padx = 20, pady = 20, ipadx = 25, ipady = 8, sticky = "nw")
    
    # Add section titles
    personal_title = tk.Label(personal_details_frame, text="Personal Details", font = ("Arial", 16), fg="yellow", bg="black")
    personal_title.grid(row = 0, column = 0, columnspan = 2, pady = 10)

    reservation_title = tk.Label(reservation_frame, text="Make a Reservation", font = ("Arial", 16), fg="yellow", bg="black")
    reservation_title.grid(row=0, column=0, columnspan=2, pady=10)

    # Personal Details Section
    labels_personal = ["First Name", "Last Name", "Email", "Phone Number", "Street Address", "City", "State", "Pin Code"]
    entries_personal = []

    for idx, text in enumerate(labels_personal):
        label = tk.Label(personal_details_frame, text=text, font=("Arial", 12), bg="black", fg="white")
        label.grid(row = idx + 1, column = 0, padx = 10, pady = 5, sticky = "w")

        entry = tk.Entry(personal_details_frame, font = ("Arial", 12), width = 25)
        entry.grid(row = idx + 1, column = 1, padx = 10, pady = 5)
        entries_personal.append(entry)

    # Country selection dropdown
    country_label = tk.Label(personal_details_frame, text = "Select Country", font = ("Arial", 12), bg = "black", fg = "white")
    country_label.grid(row = 9, column = 0, padx = 10, pady = 5, sticky = "w")

    country_options = ["Philippines","Korea", "Japan", "USA", "Canada", "Australia", "India", "Other"]
    country_var = tk.StringVar()
    country_dropdown = ttk.Combobox(personal_details_frame, textvariable = country_var, values = country_options, width = 23, font=("Arial", 12))
    country_dropdown.grid(row = 9, column = 1, padx = 10, pady = 5)

    # Reservation Section
    labels_reservation = ["Arrival Date", "Departure Date", "No of Adult", "No of Kids", "No of Nights at Hotel", "Room Preference"]
    entries_reservation = []

    for idx, text in enumerate(labels_reservation):
        label = tk.Label(reservation_frame, text=text, font = ("Arial", 12), bg = "black", fg = "white")
        label.grid(row = idx + 1, column = 0, padx = 10, pady = 5, sticky = "w")

        if "No of" in text:
            entry = ttk.Combobox(reservation_frame, values=[str(i) for i in range(1, 11)], font = ("Arial", 12), width=23)
        else:
            entry = tk.Entry(reservation_frame, font = ("Arial", 12), width=25)

        entry.grid(row = idx + 1, column = 1, padx = 10, pady = 5)
        entries_reservation.append(entry)

    # Special Request Text Box
    special_label = tk.Label(reservation_frame, text = "Any Special Request...", font = ("Arial", 12), bg = "black", fg = "white")
    special_label.grid(row = 7, column = 0, padx = 10, pady = 5, sticky="nw")

    special_entry = tk.Text(reservation_frame, height = 4, width = 25, font = ("Arial", 12))
    special_entry.grid(row = 7, column = 1, padx = 10, pady=5)

    # Frame of the 3 buttons
    button_frame = tk.Frame(main_frame, bg="gray")
    button_frame.grid(row=1, column=0, columnspan=2, pady=20, sticky="ew")  

    # submit button
    submit_button = tk.Button(button_frame, text="SUBMIT", font=("Arial", 14), bg="#00A1E4", fg="white", width=20)
    submit_button.pack(side=tk.LEFT, padx=10, pady=10)

    # view bookings button
    view_booking_button = tk.Button(button_frame, text="VIEW BOOKINGS", font=("Arial", 14), bg="green", fg="white", width=20, command = view_list_form)
    view_booking_button.pack(side=tk.LEFT, padx=10, pady=10)

    
    # Booking history button
    booking_history_button = tk.Button(button_frame, text="BOOKING HISTORY", font=("Arial", 14), bg="purple", fg="white", width=20)
    booking_history_button.pack(side=tk.LEFT, padx=10, pady=10)

    # logout button
    logout_button = tk.Button(button_frame, text="LOG OUT", font=("Arial", 14), bg="red", fg="white", width=20, command=lambda: logout(booking_form))
    logout_button.pack(side=tk.LEFT, padx=10, pady=10)

    booking_form.mainloop()
    
    


# left frame in login panel
left_frame = tk.Frame(window, width = 300, height = 400)
left_frame.grid(row = 0, column = 0, padx = 0, pady = 0)
left_frame.grid_propagate(False)

# background image login form left frame
bg_image = Image.open(r"C:\\Users\\HUAWEI\\OneDrive\\Documents\\Python_LabActivity\\Hotel_beach.jpg")
bg_image = bg_image.resize((300, 400))  # Resize the image to match frame size

# Convert to PhotoImage
bg_image_tk = ImageTk.PhotoImage(bg_image)

# Add image to left frame using a label
bg_label = tk.Label(left_frame, image=bg_image_tk)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Adjust to cover the frame

# right frame in login panel
right_frame = tk.Frame(window, width = 300, height = 400, bg="white")
right_frame.grid(row = 0, column = 1, padx = 0, pady = 0)
right_frame.grid_propagate(False)

# Add "Welcome" text
welcome_label = tk.Label(right_frame, text = "Welcome", font = ("Arial", 24), bg = "white", fg = "blue")
welcome_label.pack(pady = (30, 10))

# Email label and entry
email_label = tk.Label(right_frame, text = "Email ", font = ("Arial", 12), bg = "white", fg = "black")
email_label.pack(pady = (10, 5))
email_entry = tk.Entry(right_frame, font = ("Arial", 12), width=30)
email_entry.pack(pady = (0, 10))

# Password label and entry
password_label = tk.Label(right_frame, text = "Password", font = ("Arial", 12), bg = "white", fg = "black")
password_label.pack(pady = (10, 5))
password_entry = tk.Entry(right_frame, font = ("Arial", 12), width = 30, show = "*")
password_entry.pack(pady = (0, 10))

# "Show Password" checkbox
show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(right_frame, text = "Show Password", variable = show_password_var,
                                        onvalue = True, offvalue = False, command = toggle_password, bg = "white")
show_password_checkbox.pack(pady = (5, 10))

# Login button
login_button = tk.Button(right_frame, text = "LOGIN", font = ("Arial", 12), bg = "blue", fg = "white", command = login)
login_button.pack(pady=(20, 5))

# Register text
register_label = tk.Label(right_frame, text = "Don't have an account? Register Now", font = ("Arial", 10), bg = "white", fg = "blue")
register_label.pack(pady = (50, 0))

window.mainloop()
