import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    data_privacy = data_privacy_var.get()
    if data_privacy=="I Accept":

    # First Frame Variable
        first_name = first_name_input.get()
        last_name = last_name_input.get()
        customer_title = customer_title_combobox.get()
        full_name = (customer_title + first_name + last_name)
        full_name_2 = (customer_title + " " + first_name + " " + last_name)
        customer_address = customer_address_input.get()
        customer_age = customer_age_spinbox.get()
        customer_nationality = customer_nationality_combobox.get()

        # Second Frame Variable
        good_deeds = num_of_good_deeds_spinbox.get()
        rate_yourself = rate_yourself_spinbox.get()
        good_citizen = good_deeds_var.get()

        if first_name and last_name:
            alpha_validation = (full_name + customer_nationality)
            if alpha_validation.isalpha():
                num_validation = (customer_age + good_deeds + rate_yourself)
                if num_validation.isdigit():

                    #Clearing entries after submission
                    first_name_input.delete(0, 'end')
                    last_name_input.delete(0, 'end')
                    customer_title_combobox.delete(0, 'end')
                    customer_age_spinbox.delete(0, 'end')
                    customer_address_input.delete(0, 'end')
                    customer_nationality_combobox.delete(0, 'end')
                    num_of_good_deeds_spinbox.delete(0, 'end')
                    rate_yourself_spinbox.delete(0, 'end')

                    # RESPONSE 
                    print("First name: ", first_name, "  Last name: ", last_name)
                    print("Title: ", customer_title, "Age: ", customer_age, "  Nationality: ", customer_nationality, " Address: ", customer_address)
                    print("The customer believes that he/she is", good_citizen, "The customer as well claims to have done:", good_deeds, " good deeds. ", "Moreover the customer believes to be a/an ", rate_yourself)
                    print("-------------------------------------------------------------------------------------------------------")
                    tk.messagebox.showinfo(title="Greetings!", message=("Hello! " + full_name_2 + ", " + good_citizen + ", you are currently " + customer_age + "  years old. From " + customer_nationality + "(" + customer_address + ")" + ". You believe you are a " + rate_yourself + " with " + good_deeds + " good deeds. What a remarkable confidence done right. Because of that the Christmas Corps will ensure you receive a deserving gift from Claus himself!"))
                else:
                    tk.messagebox.showwarning(title="INVALID", message="Age, Number of Good Deeds, and Self Rating should contain numbers only.")    
            else:
                tk.messagebox.showwarning(title="INVALID", message="Title, First Name, Last Name and Nationality should contain letters only.")
        else:
            tk.messagebox.showerror(title="ERROR", message="Please fill up the First Name and Last Name.")
    else:
     tk.messagebox.showerror(title="ERROR" , message="You cannot proceed without giving permision for data use of your personal data.")

# FOR LAYOUT AND BASE WINDOW ----------------------------------------------------------------------------------------------------------------------------
base_window = tk.Tk()
base_window.title("Merry Christmas! application for santa gift")

frame_of_bw = tk.Frame(base_window)
frame_of_bw.pack()
frame_of_bw.configure(bg='#EAC6BB')

# FIRST FRAME----------------------------------------------------------------------------------------------------------------------------
customer_info_frame = tk.LabelFrame(frame_of_bw, text="Please complete the necessary details.")
customer_info_frame.grid(row=0, column=0, padx=20, pady=10)
customer_info_frame.configure(bg='#F1EAD0')

first_name_label = tk.Label(customer_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(customer_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_input = tk.Entry(customer_info_frame)
first_name_input.grid(row=1, column=0)
last_name_input = tk.Entry(customer_info_frame)
last_name_input.grid(row=1, column=1)

customer_address_label = tk.Label(customer_info_frame, text="Address")
customer_address_label.grid(row=2,column=2)
customer_address_input = tk.Entry(customer_info_frame)
customer_address_input.grid(row=3, column=2)

customer_title_label = tk.Label(customer_info_frame, text="What would you prefer to be called?")
customer_title_label.grid(row=0, column=2)
customer_title_combobox = ttk.Combobox(customer_info_frame, values=["", "Mister", "Mistress", "Miss", "Doctor", "Engineer"])
customer_title_combobox.grid(row=1, column=2)

customer_age_label = tk.Label(customer_info_frame, text="Select Your Age.")
customer_age_label.grid(row=2, column=0)
customer_age_spinbox = tk.Spinbox(customer_info_frame, from_=0, to ='infinity')
customer_age_spinbox.grid(row=3, column=0)

customer_nationality_label = tk.Label(customer_info_frame, text="Which country do you live?")
customer_nationality_label.grid(row=2, column=1)
customer_nationality_combobox = ttk.Combobox(customer_info_frame, values=["UnitedStates", "Canada", "Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "AntiguaAndOrBarbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "BosniaAndHerzegovina", "Botswana", "Bouvet Island", "Brazil", "BritishIndianOceanTerritory", "BruneiDarussalam", "Bulgaria", "BurkinaFaso", "Burundi", "Cambodia", "Cameroon", "CapeVerde", "CaymanIslands", "CentralAfricanRepublic", "Chad", "Chile", "China", "ChristmasIsland", "Cocos(Keeling)Islands", "Colombia", "Comoros", "Congo", "CooIslands", "CostaRica", "Croatia(Hrvatska)", "Cuba", "Cyprus", "CzechRepublic", "Denmark", "Djibouti", "Dominica", "DominicanRepublic", "EastTimor", "Ecuador", "Egypt", "ElSalvador", "EquatorialGuinea", "Eritrea", "Estonia", "Ethiopia", "FalklandIslands(Malvinas)", "FaroeIslands", "Fiji", "Finland", "France", "France, Metropolitan", "FrenchGuiana", "FrenchPolynesia", "FrenchSouthernTerritories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "GuineaBissau", "Guyana", "Haiti", "HeardandMcDonaldIslands", "Honduras", "HongKong", "Hungary", "Iceland", "India", "Indonesia", "Iran(IslamicRepublicof)", "Iraq", "Ireland", "Israel", "Italy", "IvoryCoast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, DemocraticPeople'sRepublicof", "Korea, Republicof", "Kuwait", "Kyrgyzstan", "LaoPeople'sDemocraticRepublic", "Latvia", "Lebanon", "Lesotho", "Liberia", "LibyanArabJamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "MarshallIslands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia,FederatedStatesof", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "NetherlandsAntilles", "NewCaledonia", "NewZealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "NorthernMarianaIslands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "PapuaNewGuinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "PuertoRico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "SaintKittsandNevis", "SaintLucia", "SaintVincentandtheGrenadines", "Samoa", "SanMarino", "SaoTomeandPrincipe", "SaudiArabia", "Senegal", "Seychelles", "SierraLeone", "Singapore", "Slovakia", "Slovenia", "SolomonIslands", "Somalia", "SouthAfrica", "SouthGeorgiaSouthSandwichIslands", "Spain", "SriLanka", "StHelena", "StPierreandMiquelon", "Sudan", "Suriname", "SvalbardandJanMayenIslands", "Swaziland", "Sweden", "Switzerland", "SyrianArabRepublic", "Taiwan", "Tajikistan", "TanzaniaUnitedRepublicof", "Thailand", "Togo", "Tokelau", "Tonga", "TrinidadandTobago", "Tunisia", "Turkey", "Turkmenistan", "TurksandCaicosIslands", "Tuvalu", "Uganda", "Ukraine", "UnitedArabEmirates", "UnitedKingdom", "UnitedStatesminoroutlyingislands", "Uruguay", "Uzbekistan", "Vanuatu", "VaticanCityState", "Venezuela", "Vietnam", "VirginIslands(British)", "VirginIslands(U.S.)", "WallisandFutunaIslands", "WesternSahara", "Yemen", "Yugoslavia", "Zaire", "Zambia", "Zimbabwe"])
customer_nationality_combobox.grid(row=3, column=1)

for widget in customer_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# SECOND FRAME --------------------------------------------------------------------------------------------------------------------
customer_second_frame = tk.LabelFrame(frame_of_bw)
customer_second_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
customer_second_frame.configure(bg='#F1EAD0')

customer_moral_label = tk.Label(customer_second_frame, text="Have you been a good this year?")
customer_moral_label.grid(row=0, column=0)
good_deeds_var = tk.StringVar(value="Not a Good Citizen")
customer_moral_checkbutton = tk.Checkbutton(customer_second_frame, text="A good citizen", variable=good_deeds_var, onvalue= "Good Citizen", offvalue= "Not a Good Citizen")
customer_moral_checkbutton.grid(row=1, column=0)

num_of_good_deeds_label = tk.Label(customer_second_frame, text="# of your good deeds?")
num_of_good_deeds_label.grid(row=0, column=1)
num_of_good_deeds_spinbox = tk.Spinbox(customer_second_frame, from_=0, to='infinity')
num_of_good_deeds_spinbox.grid(row=1, column=1)

rate_yourself_label = tk.Label(customer_second_frame, text="What would you rate yourself?")
rate_yourself_label.grid(row=0, column=2)
rate_yourself_spinbox = tk.Spinbox(customer_second_frame, from_=0, to=10)
rate_yourself_spinbox.grid(row=1, column=2)

for widget in customer_second_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# THIRD FRAME ----------------------------------------------------------------------------------------------------------------------------------
customer_third_frame = tk.LabelFrame(frame_of_bw, text="RA 10173: Data Privacy Act of 2012, all of your given information will be at utmost confidentiality.")
customer_third_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)
customer_third_frame.configure(bg='#F1EAD0')

data_privacy_var = tk.StringVar(value="Not Accepted")
data_privacy_check = tk.Checkbutton(customer_third_frame, text="I understand and accept", variable=data_privacy_var, onvalue="I Accept", offvalue="Not Accepted")
data_privacy_check.grid(row=0, column=0)

enter_button = tk.Button(frame_of_bw, text="Enter", command= enter_data)
enter_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
enter_button.configure(bg='#F1EAD0')

base_window.mainloop()