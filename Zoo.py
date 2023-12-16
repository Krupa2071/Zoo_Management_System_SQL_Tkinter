import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import cx_Oracle
import datetime

# Assuming sd_p is a datetime.date object

#---------------------------------------Connection-----------------------------------------------------

username = 'hp578'
password = '11_Oraclesql'
host = 'prophet.njit.edu'
port = 1521
sid = 'course'
dsn = cx_Oracle.makedsn(host, port, sid)
try:
    connection = cx_Oracle.connect(username,password,dsn)
    print("Connection successful!")
    # Add your code to work with the database here
except cx_Oracle.DatabaseError as e:
    print(f"Error connecting to the Oracle database: {e}")

#-----------------------------------------Connection-----------------------------------------------------
class zoo:
    def __init__(self, root):
        self.root = root
        self.root.title("Asset Management")
        
        # -------------------------------------------------Creating main tabs---------------------------------------------

        self.tab_control = ttk.Notebook(root)
        self.asset_management = ttk.Frame(self.tab_control)
        self.daily_zoo_activity = ttk.Frame(self.tab_control)
        self.management_reporting = ttk.Frame(self.tab_control)

        #----------------------------------------------------- Adding main tabs ------------------------------------------------

        self.tab_control.add(self.asset_management, text='Asset Management')
        self.tab_control.add(self.daily_zoo_activity, text='Daily Zoo Activity')
        self.tab_control.add(self.management_reporting, text='Management and Reporting')

        self.tab_control.pack(expand=1, fill='both')
        
        #--------------------------------------------------- Adding sub-tabs under Tab Asset-------------------------------------------

        self.sub_tab_control_asset = ttk.Notebook(self.asset_management)
        self.sub_tab_animal = ttk.Frame(self.sub_tab_control_asset)
        self.sub_tab_building = ttk.Frame(self.sub_tab_control_asset)
        self.sub_tab_attraction = ttk.Frame(self.sub_tab_control_asset)
        self.sub_tab_employees = ttk.Frame(self.sub_tab_control_asset)
        self.sub_tab_hourly = ttk.Frame(self.sub_tab_control_asset)


        self.sub_tab_control_asset.add(self.sub_tab_animal, text='Animal')
        self.sub_tab_control_asset.add(self.sub_tab_building, text='Building')
        self.sub_tab_control_asset.add(self.sub_tab_attraction, text='Attractions')
        self.sub_tab_control_asset.add(self.sub_tab_employees, text='Employees')
        self.sub_tab_control_asset.add(self.sub_tab_hourly, text='Hourly Wages')

        self.sub_tab_control_asset.pack(expand=1, fill='both')

        #--------------------------------------------------- Adding sub-tabs under Tab Animal -------------------------------------------

        self.view_animal_id_label = tk.Label(self.sub_tab_animal, text='Animal_ID')
        self.view_animal_id_entry = tk.Entry(self.sub_tab_animal)
        self.view_animal_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.view_animal_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        self.view_animal_status_label = tk.Label(self.sub_tab_animal, text='Status')
        self.view_animal_status_entry = tk.Entry(self.sub_tab_animal)
        self.view_animal_status_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.view_animal_status_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        self.view_animal_birth_label = tk.Label(self.sub_tab_animal, text='Birth Year')
        self.view_animal_birth_entry = tk.Entry(self.sub_tab_animal)
        self.view_animal_birth_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.view_animal_birth_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        self.view_animal_spc_id_label = tk.Label(self.sub_tab_animal, text='Species Id')
        self.view_animal_spc_id_entry = tk.Entry(self.sub_tab_animal)
        self.view_animal_spc_id_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.view_animal_spc_id_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        self.view_animal_enc_id_label = tk.Label(self.sub_tab_animal, text='Encloser Id')
        self.view_animal_enc_id_entry = tk.Entry(self.sub_tab_animal)
        self.view_animal_enc_id_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.view_animal_enc_id_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        
        self.view_animal_build_id_label = tk.Label(self.sub_tab_animal, text='Building ID')
        self.view_animal_build_id_entry = tk.Entry(self.sub_tab_animal)
        self.view_animal_build_id_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.view_animal_build_id_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        self.insert_animal_button = tk.Button(self.sub_tab_animal, text = "Insert Animal", command=self.add_animal)
        self.insert_animal_button.grid(row=6, column=0, columnspan=2, pady=10, sticky="w")

        self.upd_animal_button = tk.Button(self.sub_tab_animal, text = "Update Animal", command=self.update_animal)
        self.upd_animal_button.grid(row=6, column=1, columnspan=2, pady=10, sticky="w")

        self.message_label = tk.Label(root, text="")
        self.message_label.pack()

        columns = ("Animal_ID", "Status", "Birth Year", "Species Id", "Encloser Id", "Building ID")
        tree = ttk.Treeview(self.sub_tab_animal, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            tree.heading(col, text=col)

        # Grid the Treeview
        tree.grid(row=7, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb = ttk.Scrollbar(self.sub_tab_animal, orient="vertical", command=tree.yview)
        vsb.grid(row=7, column=2, pady=10, sticky="ns")
        tree.configure(yscrollcommand=vsb.set)

        # hsb = ttk.Scrollbar(self.sub_tab_animal, orient="horizontal", command=tree.xview)
        # hsb.grid(row=8, column=0, padx=10, sticky="ew")
        # tree.configure(xscrollcommand=hsb.set)
        cursor2 = connection.cursor()
        query = "SELECT * FROM HP578.ANIMAL"
        cursor2.execute(query)

        # Fetch all rows from the result
        rows = cursor2.fetchall()
        # Insert data into the Treeview
        for row in rows:
            tree.insert("", "end", values=row)
        
        def on_treeview_select(event):
    # Get the selected item
            selected_item = tree.selection()

            # Check if any item is selected
            if selected_item:
                # Clear the entries
                self.view_animal_id_entry.delete(0, 'end')
                self.view_animal_status_entry.delete(0, 'end')
                self.view_animal_birth_entry.delete(0, 'end')
                self.view_animal_spc_id_entry.delete(0, 'end')
                self.view_animal_enc_id_entry.delete(0, 'end')
                self.view_animal_build_id_entry.delete(0, 'end')

                # Get values from the selected item and fill the entries
                values = tree.item(selected_item)['values']
                if values:
                    self.view_animal_id_entry.insert(0, values[0])  # Assuming name is the first column
                    self.view_animal_status_entry.insert(0, values[1])
                    self.view_animal_birth_entry.insert(0, values[2])
                    self.view_animal_spc_id_entry.insert(0, values[3])
                    self.view_animal_enc_id_entry.insert(0, values[4])
                    self.view_animal_build_id_entry.insert(0, values[5])  
        tree.bind('<ButtonRelease-1>', on_treeview_select) 
        
        #--------------------------------------------------- Adding sub-tabs under Tab Building -------------------------------------------
        
        self.view_building_id_label = tk.Label(self.sub_tab_building, text='Building ID')
        self.view_building_id_entry = tk.Entry(self.sub_tab_building)
        self.view_building_id_label.grid(row=0, column=0, padx=5, pady=5)
        self.view_building_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.view_building_name_label = tk.Label(self.sub_tab_building, text='Building Name')
        self.view_building_name_entry = tk.Entry(self.sub_tab_building)
        self.view_building_name_label.grid(row=1, column=0, padx=5, pady=5)
        self.view_building_name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.view_building_type_label = tk.Label(self.sub_tab_building, text='Building Type')
        self.view_building_type_entry = tk.Entry(self.sub_tab_building)
        self.view_building_type_label.grid(row=2, column=0, padx=5, pady=5)
        self.view_building_type_entry.grid(row=2, column=1, padx=5, pady=5)
        
        self.view_building_button = tk.Button(self.sub_tab_building, text='Insert Building', command=self.add_building)
        self.view_building_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.view_building_button = tk.Button(self.sub_tab_building, text='Update Building', command=self.upd_building)
        self.view_building_button.grid(row=3, column=1, columnspan=2, pady=10)

        self.message_label = tk.Label(root, text="")
        self.message_label.pack()

        columns_build = ("Building_ID", "Building_Name", "Building_Type")
        tree_build = ttk.Treeview(self.sub_tab_building, columns=columns_build, show="headings")

        # Set column headings
        for col in columns_build:
            tree_build.heading(col, text=col)

        # Grid the Treeview
        tree_build.grid(row=4, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_build = ttk.Scrollbar(self.sub_tab_building, orient="vertical", command=tree_build.yview)
        vsb_build.grid(row=4, column=2, pady=10, sticky="ns")
        tree_build.configure(yscrollcommand=vsb_build.set)

        hsb_build = ttk.Scrollbar(self.sub_tab_building, orient="horizontal", command=tree_build.xview)
        hsb_build.grid(row=6, column=0, padx=10, sticky="ew")
        tree_build.configure(xscrollcommand=hsb_build.set)
        cursor3 = connection.cursor()
        query1 = "SELECT * FROM HP578.BUILDING"
        cursor3.execute(query1)

        # Fetch all rows from the result
        rows_build = cursor3.fetchall()
        # Insert data into the Treeview
        for row in rows_build:
            tree_build.insert("", "end", values=row)
        
        def on_treeview_select_b(event):
    # Get the selected item
            selected_item_build = tree_build.selection()

            # Check if any item is selected
            if selected_item_build:
                # Clear the entries
                self.view_building_id_entry.delete(0, 'end')
                self.view_building_name_entry.delete(0, 'end')
                self.view_building_type_entry.delete(0, 'end')

                # Get values from the selected item and fill the entries
                values = tree_build.item(selected_item_build)['values']
                if values:
                    self.view_building_id_entry.insert(0, values[0])  # Assuming name is the first column
                    self.view_building_name_entry.insert(0, values[1])
                    self.view_building_type_entry.insert(0, values[2]) 
        tree_build.bind('<ButtonRelease-1>', on_treeview_select_b)
        
        #--------------------------------------------------- Adding sub-tabs under Tab Attraction -------------------------------------------

        self.view_attraction_c_p_label = tk.Label(self.sub_tab_attraction, text='Child Price')
        self.view_attraction_c_p_entry = tk.Entry(self.sub_tab_attraction)
        self.view_attraction_c_p_label.grid(row=0, column=0, padx=5, pady=5)
        self.view_attraction_c_p_entry.grid(row=0, column=1, padx=5, pady=5)

        self.view_attraction_s_p_label = tk.Label(self.sub_tab_attraction, text='Senior Price')
        self.view_attraction_s_p_entry = tk.Entry(self.sub_tab_attraction)
        self.view_attraction_s_p_label.grid(row=1, column=0, padx=5, pady=5)
        self.view_attraction_s_p_entry.grid(row=1, column=1, padx=5, pady=5)

        self.view_attraction_a_p_label = tk.Label(self.sub_tab_attraction, text='Adult Price')
        self.view_attraction_a_p_entry = tk.Entry(self.sub_tab_attraction)
        self.view_attraction_a_p_label.grid(row=2, column=0, padx=5, pady=5)
        self.view_attraction_a_p_entry.grid(row=2, column=1, padx=5, pady=5)

        self.view_attraction_per_day_label = tk.Label(self.sub_tab_attraction, text='Per Day')
        self.view_attraction_per_day_entry = tk.Entry(self.sub_tab_attraction)
        self.view_attraction_per_day_label.grid(row=3, column=0, padx=5, pady=5)
        self.view_attraction_per_day_entry.grid(row=3, column=1, padx=5, pady=5)

        self.view_attraction_rev_id_label = tk.Label(self.sub_tab_attraction, text='Revenue Type ID')
        self.view_attraction_rev_id_entry = tk.Entry(self.sub_tab_attraction)
        self.view_attraction_rev_id_label.grid(row=4, column=0, padx=5, pady=5)
        self.view_attraction_rev_id_entry.grid(row=4, column=1, padx=5, pady=5)

        self.view_attraction_button = tk.Button(self.sub_tab_attraction, text='Insert Attraction', command=self.add_attraction)
        self.view_attraction_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.view_attraction_button = tk.Button(self.sub_tab_attraction, text='Update Attraction', command=self.upd_attraction)
        self.view_attraction_button.grid(row=5, column=1, columnspan=2, pady=10)

        self.message_label = tk.Label(root, text="")
        self.message_label.pack()

        columns_att = ("Child Price", "Senior Price", "Adult Price", "Per Day", "Revenue Type ID")
        tree_att = ttk.Treeview(self.sub_tab_attraction, columns=columns_att, show="headings")

        # Set column headings
        for col in columns_att:
            tree_att.heading(col, text=col)

        # Grid the Treeview
        tree_att.grid(row=6, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_att = ttk.Scrollbar(self.sub_tab_attraction, orient="vertical", command=tree_att.yview)
        vsb_att.grid(row=6, column=2, pady=10, sticky="ns")
        tree_att.configure(yscrollcommand=vsb_att.set)

        hsb_att = ttk.Scrollbar(self.sub_tab_attraction, orient="horizontal", command=tree_att.xview)
        hsb_att.grid(row=8, column=0, padx=10, sticky="ew")
        tree_att.configure(xscrollcommand=hsb_att.set)
        cursor4 = connection.cursor()
        query2 = "SELECT * FROM HP578.ANIMAL_SHOW"
        cursor4.execute(query2)

        # Fetch all rows from the result
        rows_att = cursor4.fetchall()
        # Insert data into the Treeview
        for row in rows_att:
            tree_att.insert("", "end", values=row)
        
        def on_treeview_select_b(event):
    # Get the selected item
            selected_item_att = tree_att.selection()

            # Check if any item is selected
            if selected_item_att:
                # Clear the entries
                self.view_attraction_rev_id_entry.delete(0, 'end')
                self.view_attraction_c_p_entry.delete(0, 'end')
                self.view_attraction_s_p_entry.delete(0, 'end')
                self.view_attraction_a_p_entry.delete(0, 'end')
                self.view_attraction_per_day_entry.delete(0, 'end')

                # Get values from the selected item and fill the entries
                values = tree_att.item(selected_item_att)['values']
                if values:
                    self.view_attraction_rev_id_entry.insert(0, values[4])  # Assuming name is the first column
                    self.view_attraction_c_p_entry.insert(0, values[0])
                    self.view_attraction_s_p_entry.insert(0, values[1])
                    self.view_attraction_a_p_entry.insert(0, values[2])
                    self.view_attraction_per_day_entry.insert(0, values[3]) 
        tree_att.bind('<ButtonRelease-1>', on_treeview_select_b)

        #--------------------------------------------------- Adding sub-tabs under Tab Employee -------------------------------------------

        self.view_employee_id_label = tk.Label(self.sub_tab_employees, text='Employee ID')
        self.view_employee_id_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_id_label.grid(row=0, column=0, padx=5, pady=5,sticky='w' )
        self.view_employee_id_entry.grid(row=0, column=1, padx=5, pady=5,sticky='w')

        self.view_employee_start_label = tk.Label(self.sub_tab_employees, text='Start Date')
        self.view_employee_start_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_start_label.grid(row=1, column=0, padx=5, pady=5,sticky='w')
        self.view_employee_start_entry.grid(row=1, column=1, padx=5, pady=5,sticky='w')

        self.view_employee_job_label = tk.Label(self.sub_tab_employees, text='Job Type')
        self.view_employee_job_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_job_label.grid(row=2, column=0, padx=5, pady=5,sticky='w')
        self.view_employee_job_entry.grid(row=2, column=1, padx=5, pady=5,sticky='w')

        self.view_employee_f_label = tk.Label(self.sub_tab_employees, text='First')
        self.view_employee_f_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_f_label.grid(row=3, column=0, padx=5, pady=5,sticky='w')
        self.view_employee_f_entry.grid(row=3, column=1, padx=5, pady=5,sticky='w')

        self.view_employee_m_label = tk.Label(self.sub_tab_employees, text='Middle initial')
        self.view_employee_m_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_m_label.grid(row=4, column=0, padx=5, pady=5,sticky='w')
        self.view_employee_m_entry.grid(row=4, column=1, padx=5, pady=5,sticky='w')

        self.view_employee_l_label = tk.Label(self.sub_tab_employees, text='Last')
        self.view_employee_l_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_l_label.grid(row=5, column=0, padx=5, pady=5,sticky='w')
        self.view_employee_l_entry.grid(row=5, column=1, padx=5, pady=5,sticky='w')

        self.view_employee_st_label = tk.Label(self.sub_tab_employees, text='Street')
        self.view_employee_st_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_st_label.grid(row=6, column=0, padx=5, pady=5,sticky='w')
        self.view_employee_st_entry.grid(row=6, column=1, padx=5, pady=5,sticky='w')

        self.view_employee_city_label = tk.Label(self.sub_tab_employees, text='City')
        self.view_employee_city_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_city_label.grid(row=7, column=0, padx=5, pady=5,sticky='w')
        self.view_employee_city_entry.grid(row=7, column=1, padx=5, pady=5,sticky='w')

        self.view_employee_state_label = tk.Label(self.sub_tab_employees, text='State')
        self.view_employee_state_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_state_label.grid(row=8, column=0, padx=5, pady=5,sticky='w')
        self.view_employee_state_entry.grid(row=8, column=1, padx=5, pady=5,sticky='w')

        self.view_employee_zip_label = tk.Label(self.sub_tab_employees, text='Zip')
        self.view_employee_zip_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_zip_label.grid(row=9, column=0, padx=5, pady=5,sticky='w')
        self.view_employee_zip_entry.grid(row=9, column=1, padx=5, pady=5,sticky='w')

        self.view_employee_hr_id_label = tk.Label(self.sub_tab_employees, text='HR ID')
        self.view_employee_hr_id_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_hr_id_label.grid(row=10, column=0, padx=5, pady=5,sticky='w')
        self.view_employee_hr_id_entry.grid(row=10, column=1, padx=5, pady=5,sticky='w')

        self.view_employee_sup_id_label = tk.Label(self.sub_tab_employees, text='Super ID')
        self.view_employee_sup_id_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_sup_id_label.grid(row=11, column=0, padx=5, pady=5,sticky='w')
        self.view_employee_sup_id_entry.grid(row=11, column=1, padx=5, pady=5,sticky='w')

        self.view_employee_rev_id_label = tk.Label(self.sub_tab_employees, text='Revenue Type ID')
        self.view_employee_rev_id_entry = tk.Entry(self.sub_tab_employees)
        self.view_employee_rev_id_label.grid(row=12, column=0, padx=5, pady=5,sticky='w')
        self.view_employee_rev_id_entry.grid(row=12, column=1, padx=5, pady=5,sticky='w')

        self.add_employee_button = tk.Button(self.sub_tab_employees, text='Insert Employee', command=self.add_employee)
        self.add_employee_button.grid(row=13, column=0, columnspan=2, pady=10 ,sticky='w')

        self.upd_employee_button = tk.Button(self.sub_tab_employees, text='Update Employee', command=self.upd_employee)
        self.upd_employee_button.grid(row=13, column=1, columnspan=2, pady=10,sticky='w')

        self.message_label = tk.Label(root, text="")
        self.message_label.pack()

        columns_em = ("Employee ID", "Start Date", "Job Type", "First","Middle initial", "Last", "Street","City","State","Zip","HR ID","Super ID","Revenue Type ID")
        tree_em = ttk.Treeview(self.sub_tab_employees, columns=columns_em, show="headings")

        # Set column headings
        for col in columns_em:
            tree_em.heading(col, text=col)

        # Grid the Treeview
        tree_em.grid(row=14, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar

        # vsb_em = ttk.Scrollbar(root, orient="vertical", command=tree_em.yview)
        # tree_em.configure(yscrollcommand=vsb_em.set)

        def on_h(*args):
            tree_em.xview(*args)

        def on_v(*args):
            tree_em.yview(*args)    

        vsb_em = ttk.Scrollbar(self.sub_tab_employees, orient="vertical", command=on_v)
        vsb_em.grid(row=14, column=2, pady=10, sticky="ns")
        tree_em.configure(yscrollcommand=vsb_em.set)

        hsb_em = ttk.Scrollbar(self.sub_tab_employees, orient="horizontal", command=on_h)
        tree_em.configure(xscrollcommand=hsb_em.set)
        hsb_em.grid(row=16, column=0, padx=0, sticky="ew")
        
        self.sub_tab_employees.grid_rowconfigure(0, weight=1)
        self.sub_tab_employees.grid_columnconfigure(0, weight=1)

        cursor6 = connection.cursor()
        query4 = "SELECT * FROM HP578.EMPLOYEE"
        cursor6.execute(query4)

        # Fetch all rows from the result
        rows = cursor6.fetchall()
        # Insert data into the Treeview
        for row in rows:
            tree_em.insert("", "end", values=row)
        
        def on_treeview_select_em(event):
    # Get the selected item
            selected_item = tree_em.selection()

            # Check if any item is selected
            if selected_item:
                # Clear the entries
                self.view_employee_id_entry.delete(0, 'end')
                self.view_employee_start_entry.delete(0, 'end')
                self.view_employee_job_entry.delete(0, 'end')
                self.view_employee_f_entry.delete(0, 'end')
                self.view_employee_m_entry.delete(0, 'end')
                self.view_employee_l_entry.delete(0, 'end')
                self.view_employee_st_entry.delete(0, 'end')
                self.view_employee_city_entry.delete(0, 'end')
                self.view_employee_state_entry.delete(0, 'end')
                self.view_employee_zip_entry.delete(0, 'end')
                self.view_employee_hr_id_entry.delete(0, 'end')
                self.view_employee_sup_id_entry.delete(0, 'end')
                self.view_employee_rev_id_entry.delete(0, 'end')
                

                # Get values from the selected item and fill the entries
                values = tree_em.item(selected_item)['values']
                if values:
                    self.view_employee_id_entry.insert(0, values[0])
                    self.view_employee_start_entry.insert(0, values[1])
                    self.view_employee_job_entry.insert(0, values[2]) 
                    self.view_employee_f_entry.insert(0, values[3])  # Assuming name is the first column
                    self.view_employee_m_entry.insert(0, values[4])
                    self.view_employee_l_entry.insert(0, values[5])
                    self.view_employee_st_entry.insert(0, values[6])
                    self.view_employee_city_entry.insert(0, values[7])
                    self.view_employee_state_entry.insert(0, values[8])
                    self.view_employee_zip_entry.insert(0, values[9])  # Assuming name is the first column
                    self.view_employee_hr_id_entry.insert(0, values[10])
                    self.view_employee_sup_id_entry.insert(0, values[11])
                    self.view_employee_rev_id_entry.insert(0, values[12])
        tree_em.bind('<ButtonRelease-1>', on_treeview_select_em)
        
        # #--------------------------------------------------- Adding sub-tabs under Tab Hourly -------------------------------------------
        
        self.view_hourly_id_label = tk.Label(self.sub_tab_hourly, text='HR ID')
        self.view_hourly_id_entry = tk.Entry(self.sub_tab_hourly)
        self.view_hourly_id_label.grid(row=0, column=0, padx=5, pady=5)
        self.view_hourly_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.view_hourly_rate_label = tk.Label(self.sub_tab_hourly, text='Rate')
        self.view_hourly_rate_entry = tk.Entry(self.sub_tab_hourly)
        self.view_hourly_rate_label.grid(row=1, column=0, padx=5, pady=5)
        self.view_hourly_rate_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_hourly_button = tk.Button(self.sub_tab_hourly, text='Insert Hourly Wages', command=self.add_hourly)
        self.add_hourly_button.grid(row=2, column=0, columnspan=2, pady=10, sticky='w')

        self.upd_hourly_button = tk.Button(self.sub_tab_hourly, text='Update Hourly Wages', command=self.upd_hourly)
        self.upd_hourly_button.grid(row=2, column=1, columnspan=2, pady=10)

        self.message_label = tk.Label(root, text="")
        self.message_label.pack()

        columns_hw = ("HR ID", "Rate")
        tree_hw = ttk.Treeview(self.sub_tab_hourly, columns=columns_hw, show="headings")

        # Set column headings
        for col in columns_hw:
            tree_hw.heading(col, text=col)

        # Grid the Treeview
        tree_hw.grid(row=3, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_hw = ttk.Scrollbar(self.sub_tab_hourly, orient="vertical", command=tree_hw.yview)
        vsb_hw.grid(row=3, column=2, pady=10, sticky="ns")
        tree_hw.configure(yscrollcommand=vsb_hw.set)

        hsb_hw = ttk.Scrollbar(self.sub_tab_hourly, orient="horizontal", command=tree_hw.xview)
        hsb_hw.grid(row=5, column=0, padx=10, sticky="ew")
        tree_hw.configure(xscrollcommand=hsb_hw.set)
        cursor5 = connection.cursor()
        query3 = "SELECT * FROM HP578.HOURLY_RATE"
        cursor5.execute(query3)

        # Fetch all rows from the result
        rows_hw = cursor5.fetchall()
        # Insert data into the Treeview
        for row in rows_hw:
            tree_hw.insert("", "end", values=row)
        
        def on_treeview_select_hw(event):
    # Get the selected item
            selected_item_hw = tree_hw.selection()

            # Check if any item is selected
            if selected_item_hw:
                # Clear the entries
                self.view_hourly_id_entry.delete(0, 'end')
                self.view_hourly_rate_entry.delete(0, 'end')

                # Get values from the selected item and fill the entries
                values = tree_hw.item(selected_item_hw)['values']
                if values:
                    self.view_hourly_id_entry.insert(0, values[0])  # Assuming name is the first column
                    self.view_hourly_rate_entry.insert(0, values[1])
        tree_hw.bind('<ButtonRelease-1>', on_treeview_select_hw)

        #--------------------------------------------------- Adding sub-tabs under Tab Daily Zoo Activity -------------------------------------------

        self.sub_tab_control_daily = ttk.Notebook(self.daily_zoo_activity)
        self.sub_tab_daily_attractions = ttk.Frame(self.sub_tab_control_daily)
        self.sub_tab_daily_concessions = ttk.Frame(self.sub_tab_control_daily)
        self.sub_tab_daily_attendance = ttk.Frame(self.sub_tab_control_daily)


        self.sub_tab_control_daily.add(self.sub_tab_daily_attractions, text='Attractions')
        self.sub_tab_control_daily.add(self.sub_tab_daily_concessions, text='Concessions')
        self.sub_tab_control_daily.add(self.sub_tab_daily_attendance, text='Attendance')

        self.sub_tab_control_daily.pack(expand=1, fill='both')

        #--------------------------------------------------- Adding sub-tabs under Tab Daily Attractions -------------------------------------------

        self.date_attractions_label = tk.Label(self.sub_tab_daily_attractions, text='Enter Date in YYYY-MM-DD Formate : ')
        self.date_attractions_entry = tk.Entry(self.sub_tab_daily_attractions)
        self.date_attractions_label.grid(row=0, column=0, padx=5, pady=5)
        self.date_attractions_entry.grid(row=0, column=1, padx=5, pady=5)  

        self.selected_option_var1 = tk.StringVar()
        options1=["Conservation Admission", "Butterfly garden Admission", "Events and Shows"]
        self.name_attractions_label = tk.Label(self.sub_tab_daily_attractions, text='Select Type of Attraction : ')
        self.name_attractions_label.grid(row=1, column=0, padx=5, pady=5)
        self.dropdown1 = ttk.Combobox(self.sub_tab_daily_attractions, values=options1, textvariable=self.selected_option_var1)
        # self.dropdown1.set(options1[0])  # Set the default value
        self.dropdown1.grid(row=1, column=1, padx=10, pady=10)
        # self.dropdown1.bind("<<ComboboxSelected>>", on_dropdown_change1)
        
        self.selected_option_var2 = tk.StringVar()
        options=["Child", "Adult", "Senior"]
        self.type_attractions_label = tk.Label(self.sub_tab_daily_attractions, text='Select Type of Ticket : ')
        self.type_attractions_label.grid(row=2, column=0, padx=5, pady=5)
        self.dropdown2 = ttk.Combobox(self.sub_tab_daily_attractions, values=options, textvariable=self.selected_option_var2)
        # self.dropdown2.set(options[0])  # Set the default value
        self.dropdown2.grid(row=2, column=1, padx=10, pady=10)
        # self.dropdown2.bind("<<ComboboxSelected>>", on_dropdown_change2)

        self.get_attractions_button = tk.Button(self.sub_tab_daily_attractions, text='Get Tickets for Attractions', command=self.attraction_report)
        self.get_attractions_button.grid(row=3, column=0, columnspan=2, pady=10, sticky='w')

        columns_a = ("REVENUETYPES_ID", "REV_NAME", "tickets_sold", "date_time", "revenue")
        tree_a = ttk.Treeview(self.sub_tab_daily_attractions, columns=columns_a, show="headings")

        # Set column headings
        for col in columns_a:
            tree_a.heading(col, text=col)

        # Grid the Treeview
        tree_a.grid(row=4, column=0, columnspan=2,padx=10, pady=10)

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_a = ttk.Scrollbar(self.sub_tab_daily_attractions, orient="vertical", command=tree_a.yview)
        vsb_a.grid(row=4, column=2, pady=10, sticky="ns")
        tree_a.configure(yscrollcommand=vsb_a.set)

        hsb_a = ttk.Scrollbar(self.sub_tab_daily_attractions, orient="horizontal", command=tree_a.xview)
        hsb_a.grid(row=6, column=0, padx=10, sticky="ew")
        tree_a.configure(xscrollcommand=hsb_a.set)
        cursor_a = connection.cursor()
        query_a = '''
        SELECT
            re.REVENUETYPES_ID AS Attraction_ID,
            rt.REV_NAME AS Attraction_Location,
            re.tickets_sold AS Ticket_Sold,
            re.date_time AS Date_Of_Attraction,
            re.revenue
        FROM
            HP578.revenue_events re
            JOIN
            HP578.revenue_types rt ON re.REVENUETYPES_ID = rt.REVENUETYPES_ID
            WHERE
            re.REVENUETYPES_ID IN (SELECT DISTINCT REVENUETYPES_ID FROM animal_show)
        '''
        cursor_a.execute(query_a)

        # Fetch all rows from the result
        rows_a = cursor_a.fetchall()
        # Insert data into the Treeview
        for row in rows_a:
            tree_a.insert("", "end", values=row)
        
    #     def on_treeview_select_a(event):
    # # Get the selected item
    #         selected_item = tree_a.selection()

    #         # Check if any item is selected
    #         if selected_item:
    #             # Clear the entries
    #             self.date_attractions_entry.delete(0, 'end')
    #             # self.view_animal_status_entry.delete(0, 'end')
    #             # self.view_animal_birth_entry.delete(0, 'end')

    #             # Get values from the selected item and fill the entries
    #             values = tree_a.item(selected_item)['values']
    #             if values:
    #                 self.date_attractions_entry.insert(0, values[0])  # Assuming name is the first column
    #                 # self.view_animal_status_entry.insert(0, values[1])
    #                 # self.view_animal_birth_entry.insert(0, values[2]) 
    #     tree_a.bind('<ButtonRelease-1>', on_treeview_select_a)

        #--------------------------------------------------- Adding sub-tabs under Tab Daily Concessions -------------------------------------------

        self.date_concession_label = tk.Label(self.sub_tab_daily_concessions, text='Enter Date in YYYY-MM-DD Formate : ')
        self.date_concession_entry = tk.Entry(self.sub_tab_daily_concessions)
        self.date_concession_label.grid(row=0, column=0, padx=5, pady=5)
        self.date_concession_entry.grid(row=0, column=1, padx=5, pady=5)  

        self.selected_option_var_con = tk.StringVar()
        options_con=["Food Court", "Gift Shop"]
        self.name_concession_label = tk.Label(self.sub_tab_daily_concessions, text='Select Type of Attraction : ')
        self.name_concession_label.grid(row=1, column=0, padx=5, pady=5)
        self.dropdown_con = ttk.Combobox(self.sub_tab_daily_concessions, values=options_con, textvariable=self.selected_option_var_con)
        self.dropdown_con.grid(row=1, column=1, padx=10, pady=10)
        
        self.get_concession_button = tk.Button(self.sub_tab_daily_concessions, text='Get Concessions', command=self.concession_report)
        self.get_concession_button.grid(row=2, column=0, columnspan=2, pady=10, sticky='w')

        columns_con = ("Concessions_ID", "Product_Location", "Total_Item_Sold","Date_", "Revenue")
        tree_con = ttk.Treeview(self.sub_tab_daily_concessions, columns=columns_con, show="headings")

        # Set column headings
        for col in columns_con:
            tree_con.heading(col, text=col)

        # Grid the Treeview
        tree_con.grid(row=3, column=0, columnspan=2,padx=10, pady=10)

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_con = ttk.Scrollbar(self.sub_tab_daily_concessions, orient="vertical", command=tree_con.yview)
        vsb_con.grid(row=3, column=2, pady=10, sticky="ns")
        tree_con.configure(yscrollcommand=vsb_con.set)

        hsb_con = ttk.Scrollbar(self.sub_tab_daily_concessions, orient="horizontal", command=tree_con.xview)
        hsb_con.grid(row=5, column=0, padx=10, sticky="ew")
        tree_con.configure(xscrollcommand=hsb_con.set)
        cursor_con = connection.cursor()
        query_con = '''
        SELECT
            c.RevenueTypes_ID AS Concessions_ID,
            rt.rev_name AS Product_Location,
            re.tickets_sold AS Total_Item_Sold,
            re.date_time AS Date_,
            re.revenue AS Revenue
        FROM
            CONCESSION c
        JOIN
            revenue_events re on c.RevenueTypes_ID=re.RevenueTypes_ID
        JOIN
            revenue_types rt on rt.revenuetypes_id=re.revenuetypes_id
        '''
        cursor_con.execute(query_con)

        # Fetch all rows from the result
        rows_con = cursor_con.fetchall()
        # Insert data into the Treeview
        for row in rows_con:
            tree_con.insert("", "end", values=row)

        #--------------------------------------------------- Adding sub-tabs under Tab Daily Attendance -------------------------------------------

        self.date_attendance_label = tk.Label(self.sub_tab_daily_attendance, text='Enter Date in YYYY-MM-DD Formate : ')
        self.date_attendance_entry = tk.Entry(self.sub_tab_daily_attendance)
        self.date_attendance_label.grid(row=0, column=0, padx=5, pady=5)
        self.date_attendance_entry.grid(row=0, column=1, padx=5, pady=5)  

        self.selected_option_var_atd_1 = tk.StringVar()
        options_atd_1=["General Admission", "Bird House Admission", "Aquarium Admission", "Reptile House Admission", "Insectariums Admission", "Conservation Admission", "Penguin Admission", "Turtle habitat Admission", "Butterfly garden Admission"]
        self.name_attendance_label = tk.Label(self.sub_tab_daily_attendance, text='Select Type of Attraction : ')
        self.name_attendance_label.grid(row=1, column=0, padx=5, pady=5)
        self.dropdown_atd = ttk.Combobox(self.sub_tab_daily_attendance, values=options_atd_1, textvariable=self.selected_option_var_atd_1)
        self.dropdown_atd.grid(row=1, column=1, padx=10, pady=10)
        
        self.selected_option_var_atd_2 = tk.StringVar()
        options_atd_2=["Child", "Adult", "Senior"]
        self.type_attendance_label = tk.Label(self.sub_tab_daily_attendance, text='Select Type of Ticket : ')
        self.type_attendance_label.grid(row=2, column=0, padx=5, pady=5)
        self.dropdown_atd_2 = ttk.Combobox(self.sub_tab_daily_attendance, values=options_atd_2, textvariable=self.selected_option_var_atd_2)
        self.dropdown_atd_2.grid(row=2, column=1, padx=10, pady=10)
        
        self.get_attendance_button = tk.Button(self.sub_tab_daily_attendance, text='Get Tickets for Attendance', command=self.attendance_report)
        self.get_attendance_button.grid(row=3, column=0, columnspan=2, pady=10, sticky='w')

        columns_atd = ("REVENUETYPES_ID", "Attendance", "Date_", "Total_Revenue")
        tree_atd = ttk.Treeview(self.sub_tab_daily_attendance, columns=columns_atd, show="headings")

        # Set column headings
        for col in columns_atd:
            tree_atd.heading(col, text=col)

        # Grid the Treeview
        tree_atd.grid(row=4, column=0, columnspan=2,padx=10, pady=10)

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_atd = ttk.Scrollbar(self.sub_tab_daily_attendance, orient="vertical", command=tree_atd.yview)
        vsb_atd.grid(row=4, column=2, pady=10, sticky="ns")
        tree_atd.configure(yscrollcommand=vsb_atd.set)

        hsb_atd = ttk.Scrollbar(self.sub_tab_daily_attendance, orient="horizontal", command=tree_atd.xview)
        hsb_atd.grid(row=6, column=0, padx=10, sticky="ew")
        tree_atd.configure(xscrollcommand=hsb_atd.set)
        cursor_atd = connection.cursor()
        query_atd = '''
        SELECT
            re.RevenueTypes_ID AS Revenue_ID,
            re.tickets_sold AS Attendance,
            re.date_time AS Date_,
            re.revenue AS Total_Revenue
        FROM
            HP578.zoo_admission za
        JOIN
            HP578.revenue_events re ON za.RevenueTypes_ID = re.RevenueTypes_ID
        '''
        cursor_atd.execute(query_atd)

        # Fetch all rows from the result
        rows_atd = cursor_atd.fetchall()
        # Insert data into the Treeview
        for row in rows_atd:
            tree_atd.insert("", "end", values=row)

        #--------------------------------------------------- Adding sub-tabs under Tab Management -------------------------------------------
        
        # Adding sub-tabs under Tab Management
        self.sub_tab_control_manage = ttk.Notebook(self.management_reporting)
        self.sub_tab_total_rev = ttk.Frame(self.sub_tab_control_manage)
        self.sub_tab_animal_report = ttk.Frame(self.sub_tab_control_manage)
        self.sub_tab_revenue_by_time = ttk.Frame(self.sub_tab_control_manage)


        self.sub_tab_control_manage.add(self.sub_tab_total_rev, text='Total Revenue')
        self.sub_tab_control_manage.add(self.sub_tab_animal_report, text='Animal Report')
        self.sub_tab_control_manage.add(self.sub_tab_revenue_by_time, text='Revenue By Time Period')

        self.sub_tab_control_manage.pack(expand=1, fill='both')

        #--------------------------------------------------- Adding sub-tabs under Tab Total Revenue -------------------------------------------

        self.cal_total_revenue_label = tk.Label(self.sub_tab_total_rev, text='Enter Date in YYYY-MM-DD Formate : ')
        self.cal_total_revenue_entry = tk.Entry(self.sub_tab_total_rev)
        self.cal_total_revenue_label.grid(row=0, column=0, padx=5, pady=5)
        self.cal_total_revenue_entry.grid(row=0, column=1, padx=5, pady=5)

        self.get_total_revenue_button = tk.Button(self.sub_tab_total_rev, text='Get Total Report', command=self.total_rev)
        self.get_total_revenue_button.grid(row=2, column=0, columnspan=2, pady=10)

        #--------------------------------------------------- Adding sub-tabs under Tab Animal Report -------------------------------------------

        self.get_total_revenue_button = tk.Button(self.sub_tab_animal_report, text='Get Total Report', command=self.animal_roport)
        self.get_total_revenue_button.grid(row=0, column=0, columnspan=2, pady=10)

        #--------------------------------------------------- Adding sub-tabs under Tab Revenue By Time Period -------------------------------------------
        
        self.sub_tab_control_revenue_time = ttk.Notebook(self.sub_tab_revenue_by_time)
        self.sub_tab_revenue_time_top_3 = ttk.Frame(self.sub_tab_control_revenue_time)
        self.sub_tab_revenue_time_best_5 = ttk.Frame(self.sub_tab_control_revenue_time)
        self.sub_tab_revenue_time_avg = ttk.Frame(self.sub_tab_control_revenue_time)

        self.sub_tab_control_revenue_time.add(self.sub_tab_revenue_time_top_3, text='Top 3')
        self.sub_tab_control_revenue_time.add(self.sub_tab_revenue_time_best_5, text='Best 5 for Month')
        self.sub_tab_control_revenue_time.add(self.sub_tab_revenue_time_avg, text='Average')

        self.sub_tab_control_revenue_time.pack(expand=1, fill='both')
        
        #--------------------------------------------------- Adding sub-tabs under Tab Top-3 -----------------------------------------------------------
         
        self.top_3_report_sd_label = tk.Label(self.sub_tab_revenue_time_top_3, text='Enter Start Date in YYYY-MM-DD format ')
        self.top_3_report_sd_entry = tk.Entry(self.sub_tab_revenue_time_top_3)
        self.top_3_report_sd_label.grid(row=0, column=0, padx=5, pady=5)
        self.top_3_report_sd_entry.grid(row=0, column=1, padx=5, pady=5)

        self.top_3_report_ed_label = tk.Label(self.sub_tab_revenue_time_top_3, text='Enter End Date in YYYY-MM-DD format ')
        self.top_3_report_ed_entry = tk.Entry(self.sub_tab_revenue_time_top_3)
        self.top_3_report_ed_label.grid(row=1, column=0, padx=5, pady=5)
        self.top_3_report_ed_entry.grid(row=1, column=1, padx=5, pady=5)

        self.get_top_3_button = tk.Button(self.sub_tab_revenue_time_top_3, text='Get Report', command=self.top_3)
        self.get_top_3_button.grid(row=2, column=0, columnspan=2, pady=10)

        #--------------------------------------------------- Adding sub-tabs under Tab Best-5 ----------------------------------------------------------
        
        self.best_5_report_id_label = tk.Label(self.sub_tab_revenue_time_best_5, text='Enter month in MM format ')
        self.best_5_report_id_entry = tk.Entry(self.sub_tab_revenue_time_best_5)
        self.best_5_report_id_label.grid(row=0, column=0, padx=5, pady=5)
        self.best_5_report_id_entry.grid(row=0, column=1, padx=5, pady=5)


        self.get_best_5_button = tk.Button(self.sub_tab_revenue_time_best_5, text='Get Best 5 of the month', command=self.best_5)
        self.get_best_5_button.grid(row=2, column=0, columnspan=2, pady=10)

        #--------------------------------------------------- Adding sub-tabs under Tab Average ----------------------------------------------------------
        
        self.avg_report_sd_label = tk.Label(self.sub_tab_revenue_time_avg, text='Enter Start Date in YYYY-MM-DD format ')
        self.avg_report_sd_entry = tk.Entry(self.sub_tab_revenue_time_avg)
        self.avg_report_sd_label.grid(row=0, column=0, padx=5, pady=5)
        self.avg_report_sd_entry.grid(row=0, column=1, padx=5, pady=5)

        self.avg_report_ed_label = tk.Label(self.sub_tab_revenue_time_avg, text='Enter End Date in YYYY-MM-DD format ')
        self.avg_report_ed_entry = tk.Entry(self.sub_tab_revenue_time_avg)
        self.avg_report_ed_label.grid(row=1, column=0, padx=5, pady=5)
        self.avg_report_ed_entry.grid(row=1, column=1, padx=5, pady=5)

        self.get_avg_button = tk.Button(self.sub_tab_revenue_time_avg, text='Get Average', command=self.avg)
        self.get_avg_button.grid(row=2, column=0, columnspan=2, pady=10)

#-------------------------------------------------------- FUNCTIONS -------------------------------------------------------------------------------------------------------------------------------------------
    def add_animal(self):
        ani_id = self.view_animal_id_entry.get()
        print(ani_id)
        ani_status = self.view_animal_status_entry.get()
        print(ani_status)
        ani_birth = self.view_animal_birth_entry.get()
        print(ani_birth)
        ani_spc = self.view_animal_spc_id_entry.get()
        print(ani_spc)
        ani_enc = self.view_animal_enc_id_entry.get()
        print(ani_enc)
        ani_bid = self.view_animal_build_id_entry.get()
        print(ani_bid)
        cursor = connection.cursor()
        query = 'INSERT INTO HP578.ANIMAL (Ani_ID , Status, Birth_Year, Spc_ID, Enc_ID, Building_ID) VALUES(:1, :2, :3, :4, :5, :6)'
        cursor.execute(query , (ani_id, ani_status,ani_birth,ani_spc,ani_enc,ani_bid))
        connection.commit()
        cursor.close()
        # connection.close()
        # Clear input fields
        self.view_animal_id_entry.delete(0, 'end')
        self.view_animal_status_entry.delete(0, 'end')
        self.view_animal_birth_entry.delete(0, 'end')
        self.view_animal_spc_id_entry.delete(0, 'end')
        self.view_animal_enc_id_entry.delete(0, 'end')
        self.view_animal_build_id_entry.delete(0, 'end')

        # Display a message in the label
        message = "Animal added successfully!"
        self.message_label.config(text=message)

        columns = ("Animal_ID", "Status", "Birth Year", "Species Id", "Encloser Id", "Building ID")
        tree = ttk.Treeview(self.sub_tab_animal, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            tree.heading(col, text=col)

        # Grid the Treeview
        tree.grid(row=7, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb = ttk.Scrollbar(self.sub_tab_animal, orient="vertical", command=tree.yview)
        vsb.grid(row=7, column=2, pady=10, sticky="ns")
        tree.configure(yscrollcommand=vsb.set)

        hsb = ttk.Scrollbar(self.sub_tab_animal, orient="horizontal", command=tree.xview)
        hsb.grid(row=10, column=0, padx=10, sticky="ew")
        tree.configure(xscrollcommand=hsb.set)
        cursor2 = connection.cursor()
        query = "SELECT * FROM HP578.ANIMAL"
        cursor2.execute(query)

        # Fetch all rows from the result
        rows = cursor2.fetchall()
        # Insert data into the Treeview
        for row in rows:
            tree.insert("", "end", values=row)

        def on_treeview_select(event):
    # Get the selected item
            selected_item = tree.selection()

            # Check if any item is selected
            if selected_item:
                # Clear the entries
                self.view_animal_id_entry.delete(0, 'end')
                self.view_animal_status_entry.delete(0, 'end')
                self.view_animal_birth_entry.delete(0, 'end')
                self.view_animal_spc_id_entry.delete(0, 'end')
                self.view_animal_enc_id_entry.delete(0, 'end')
                self.view_animal_build_id_entry.delete(0, 'end')

                # Get values from the selected item and fill the entries
                values = tree.item(selected_item)['values']
                if values:
                    self.view_animal_id_entry.insert(0, values[0])  # Assuming name is the first column
                    self.view_animal_status_entry.insert(0, values[1])
                    self.view_animal_birth_entry.insert(0, values[2])
                    self.view_animal_spc_id_entry.insert(0, values[3])
                    self.view_animal_enc_id_entry.insert(0, values[4])
                    self.view_animal_build_id_entry.insert(0, values[5])  
        tree.bind('<ButtonRelease-1>', on_treeview_select)    
        # connection.close()

    def update_animal(self):
        ani_id = self.view_animal_id_entry.get()
        print(ani_id)
        ani_status = self.view_animal_status_entry.get()
        print(ani_status)
        ani_birth = self.view_animal_birth_entry.get()
        print(ani_birth)
        ani_spc = self.view_animal_spc_id_entry.get()
        print(ani_spc)
        ani_enc = self.view_animal_enc_id_entry.get()
        print(ani_enc)
        ani_bid = self.view_animal_build_id_entry.get()
        print(ani_bid)
        cursor = connection.cursor()
        query = 'UPDATE HP578.ANIMAL SET Status = :1, Birth_Year = :2, Spc_ID = :3, Enc_ID = :4, Building_ID = :5 WHERE Ani_ID = :6'
        cursor.execute(query, (ani_status, ani_birth, ani_spc, ani_enc, ani_bid, ani_id))
        connection.commit()
        cursor.close()
        #connection.close()
        # Clear input fields
        self.view_animal_id_entry.delete(0, 'end')
        self.view_animal_status_entry.delete(0, 'end')
        self.view_animal_birth_entry.delete(0, 'end')
        self.view_animal_spc_id_entry.delete(0, 'end')
        self.view_animal_enc_id_entry.delete(0, 'end')
        self.view_animal_build_id_entry.delete(0, 'end')

        # Display a message in the label
        message = "Animal data Updated successfully!"
        self.message_label.config(text=message)

        columns = ("Animal_ID", "Status", "Birth Year", "Species Id", "Encloser Id", "Building ID")
        tree = ttk.Treeview(self.sub_tab_animal, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            tree.heading(col, text=col)

        # Grid the Treeview
        tree.grid(row=7, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb = ttk.Scrollbar(self.sub_tab_animal, orient="vertical", command=tree.yview)
        vsb.grid(row=7, column=2, pady=10, sticky="ns")
        tree.configure(yscrollcommand=vsb.set)

        hsb = ttk.Scrollbar(self.sub_tab_animal, orient="horizontal", command=tree.xview)
        hsb.grid(row=10, column=0, padx=10, sticky="ew")
        tree.configure(xscrollcommand=hsb.set)
        cursor2 = connection.cursor()
        query = "SELECT * FROM HP578.ANIMAL"
        cursor2.execute(query)

        # Fetch all rows from the result
        rows = cursor2.fetchall()
        # Insert data into the Treeview
        for row in rows:
            tree.insert("", "end", values=row)
        
        def on_treeview_select(event):
    # Get the selected item
            selected_item = tree.selection()

            # Check if any item is selected
            if selected_item:
                # Clear the entries
                self.view_animal_id_entry.delete(0, 'end')
                self.view_animal_status_entry.delete(0, 'end')
                self.view_animal_birth_entry.delete(0, 'end')
                self.view_animal_spc_id_entry.delete(0, 'end')
                self.view_animal_enc_id_entry.delete(0, 'end')
                self.view_animal_build_id_entry.delete(0, 'end')

                # Get values from the selected item and fill the entries
                values = tree.item(selected_item)['values']
                if values:
                    self.view_animal_id_entry.insert(0, values[0])  # Assuming name is the first column
                    self.view_animal_status_entry.insert(0, values[1])
                    self.view_animal_birth_entry.insert(0, values[2])
                    self.view_animal_spc_id_entry.insert(0, values[3])
                    self.view_animal_enc_id_entry.insert(0, values[4])
                    self.view_animal_build_id_entry.insert(0, values[5])  
        tree.bind('<ButtonRelease-1>', on_treeview_select)    
        # connection.close()    

    def add_building(self):
        building_id = self.view_building_id_entry.get()
        print(building_id)
        building_name = self.view_building_name_entry.get()
        print(building_name)
        building_type = self.view_building_type_entry.get()
        print(building_type)
        cursor = connection.cursor()
        query = 'INSERT INTO HP578.BUILDING (Building_ID , Build_Name, Buid_Type) VALUES(:1, :2, :3)'
        cursor.execute(query , (building_id, building_name,building_type))
        connection.commit()
        cursor.close()
        # connection.close()

        self.view_building_id_entry.delete(0, 'end')
        self.view_building_name_entry.delete(0, 'end')
        self.view_building_type_entry.delete(0, 'end')

        # Display a message in the label
        message = "Building added successfully!"
        self.message_label.config(text=message)

        columns_build = ("Building_ID", "Building_Name", "Building_Type")
        tree_build = ttk.Treeview(self.sub_tab_building, columns=columns_build, show="headings")

        # Set column headings
        for col in columns_build:
            tree_build.heading(col, text=col)

        # Grid the Treeview
        tree_build.grid(row=4, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_build = ttk.Scrollbar(self.sub_tab_building, orient="vertical", command=tree_build.yview)
        vsb_build.grid(row=4, column=2, pady=10, sticky="ns")
        tree_build.configure(yscrollcommand=vsb_build.set)

        hsb_build = ttk.Scrollbar(self.sub_tab_building, orient="horizontal", command=tree_build.xview)
        hsb_build.grid(row=6, column=0, padx=10, sticky="ew")
        tree_build.configure(xscrollcommand=hsb_build.set)
        cursor3 = connection.cursor()
        query1 = "SELECT * FROM HP578.BUILDING"
        cursor3.execute(query1)

        # Fetch all rows from the result
        rows_build = cursor3.fetchall()
        # Insert data into the Treeview
        for row in rows_build:
            tree_build.insert("", "end", values=row)
        
        def on_treeview_select_b(event):
    # Get the selected item
            selected_item_build = tree_build.selection()

            # Check if any item is selected
            if selected_item_build:
                # Clear the entries
                self.view_building_id_entry.delete(0, 'end')
                self.view_building_name_entry.delete(0, 'end')
                self.view_building_type_entry.delete(0, 'end')

                # Get values from the selected item and fill the entries
                values = tree_build.item(selected_item_build)['values']
                if values:
                    self.view_building_id_entry.insert(0, values[0])  # Assuming name is the first column
                    self.view_building_name_entry.insert(0, values[1])
                    self.view_building_type_entry.insert(0, values[2]) 
        tree_build.bind('<ButtonRelease-1>', on_treeview_select_b)

    def upd_building(self):
        building_id = self.view_building_id_entry.get()
        print(building_id)
        building_name = self.view_building_name_entry.get()
        print(building_name)
        building_type = self.view_building_type_entry.get()
        print(building_type)
        cursor = connection.cursor()
        query = 'UPDATE HP578.BUILDING SET Build_Name = :1, Buid_Type = :2 WHERE Building_ID = :3'
        cursor.execute(query , (building_name,building_type, building_id))
        connection.commit()
        cursor.close()
        # connection.close()

        self.view_building_id_entry.delete(0, 'end')
        self.view_building_name_entry.delete(0, 'end')
        self.view_building_type_entry.delete(0, 'end')

        # Display a message in the label
        message = "Building Updated successfully!"
        self.message_label.config(text=message)

        columns_build = ("Building_ID", "Building_Name", "Building_Type")
        tree_build = ttk.Treeview(self.sub_tab_building, columns=columns_build, show="headings")

        # Set column headings
        for col in columns_build:
            tree_build.heading(col, text=col)

        # Grid the Treeview
        tree_build.grid(row=4, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_build = ttk.Scrollbar(self.sub_tab_building, orient="vertical", command=tree_build.yview)
        vsb_build.grid(row=4, column=2, pady=10, sticky="ns")
        tree_build.configure(yscrollcommand=vsb_build.set)

        hsb_build = ttk.Scrollbar(self.sub_tab_building, orient="horizontal", command=tree_build.xview)
        hsb_build.grid(row=6, column=0, padx=10, sticky="ew")
        tree_build.configure(xscrollcommand=hsb_build.set)
        cursor3 = connection.cursor()
        query1 = "SELECT * FROM HP578.BUILDING"
        cursor3.execute(query1)

        # Fetch all rows from the result
        rows_build = cursor3.fetchall()
        # Insert data into the Treeview
        for row in rows_build:
            tree_build.insert("", "end", values=row)
        
        def on_treeview_select_b(event):
    # Get the selected item
            selected_item_build = tree_build.selection()

            # Check if any item is selected
            if selected_item_build:
                # Clear the entries
                self.view_building_id_entry.delete(0, 'end')
                self.view_building_name_entry.delete(0, 'end')
                self.view_building_type_entry.delete(0, 'end')

                # Get values from the selected item and fill the entries
                values = tree_build.item(selected_item_build)['values']
                if values:
                    self.view_building_id_entry.insert(0, values[0])  # Assuming name is the first column
                    self.view_building_name_entry.insert(0, values[1])
                    self.view_building_type_entry.insert(0, values[2]) 
        tree_build.bind('<ButtonRelease-1>', on_treeview_select_b)

    def add_attraction(self):
        attraction_rev_id = self.view_attraction_rev_id_entry.get()
        print(attraction_rev_id)
        attraction_c_p = self.view_attraction_c_p_entry.get()
        print(attraction_c_p)
        attraction_s_p = self.view_attraction_s_p_entry.get()
        print(attraction_s_p)
        attraction_a_p = self.view_attraction_a_p_entry.get()
        print(attraction_a_p)
        attraction_per_day = self.view_attraction_per_day_entry.get()
        print(attraction_per_day)
        cursor = connection.cursor()
        query = 'INSERT INTO HP578.ANIMAL_SHOW (Child_Price , Adult_Price, Senior_Price, Shows_Per_Day, RevenueTypes_ID) VALUES(:1, :2, :3, :4, :5)'
        cursor.execute(query , (attraction_c_p, attraction_a_p, attraction_s_p, attraction_per_day, attraction_rev_id))
        connection.commit()
        cursor.close()
        # connection.close()

        self.view_attraction_rev_id_entry.delete(0, 'end')
        self.view_attraction_c_p_entry.delete(0, 'end')
        self.view_attraction_s_p_entry.delete(0, 'end')
        self.view_attraction_a_p_entry.delete(0, 'end')
        self.view_attraction_per_day_entry.delete(0, 'end')

        # Display a message in the label
        message = "Animal Attraction added successfully!"
        self.message_label.config(text=message)

        columns_att = ("Child Price", "Senior Price", "Adult Price", "Per Day", "Revenue Type ID")
        tree_att = ttk.Treeview(self.sub_tab_attraction, columns=columns_att, show="headings")

        # Set column headings
        for col in columns_att:
            tree_att.heading(col, text=col)

        # Grid the Treeview
        tree_att.grid(row=6, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_att = ttk.Scrollbar(self.sub_tab_attraction, orient="vertical", command=tree_att.yview)
        vsb_att.grid(row=6, column=2, pady=10, sticky="ns")
        tree_att.configure(yscrollcommand=vsb_att.set)

        hsb_att = ttk.Scrollbar(self.sub_tab_attraction, orient="horizontal", command=tree_att.xview)
        hsb_att.grid(row=8, column=0, padx=10, sticky="ew")
        tree_att.configure(xscrollcommand=hsb_att.set)
        cursor4 = connection.cursor()
        query2 = "SELECT * FROM HP578.ANIMAL_SHOW"
        cursor4.execute(query2)

        # Fetch all rows from the result
        rows_att = cursor4.fetchall()
        # Insert data into the Treeview
        for row in rows_att:
            tree_att.insert("", "end", values=row)
        
        def on_treeview_select_b(event):
    # Get the selected item
            selected_item_att = tree_att.selection()

            # Check if any item is selected
            if selected_item_att:
                # Clear the entries
                self.view_attraction_rev_id_entry.delete(0, 'end')
                self.view_attraction_c_p_entry.delete(0, 'end')
                self.view_attraction_s_p_entry.delete(0, 'end')
                self.view_attraction_a_p_entry.delete(0, 'end')
                self.view_attraction_per_day_entry.delete(0, 'end')

                # Get values from the selected item and fill the entries
                values = tree_att.item(selected_item_att)['values']
                if values:
                    self.view_attraction_rev_id_entry.insert(0, values[4])  # Assuming name is the first column
                    self.view_attraction_c_p_entry.insert(0, values[0])
                    self.view_attraction_s_p_entry.insert(0, values[1])
                    self.view_attraction_a_p_entry.insert(0, values[2])
                    self.view_attraction_per_day_entry.insert(0, values[3]) 
        tree_att.bind('<ButtonRelease-1>', on_treeview_select_b)

    def upd_attraction(self):
        attraction_rev_id = self.view_attraction_rev_id_entry.get()
        print(attraction_rev_id)
        attraction_c_p = self.view_attraction_c_p_entry.get()
        print(attraction_c_p)
        attraction_s_p = self.view_attraction_s_p_entry.get()
        print(attraction_s_p)
        attraction_a_p = self.view_attraction_a_p_entry.get()
        print(attraction_a_p)
        attraction_per_day = self.view_attraction_per_day_entry.get()
        print(attraction_per_day)
        cursor = connection.cursor()
        query = 'UPDATE HP578.ANIMAL_SHOW SET Child_Price = :1, Adult_Price = :2, Senior_Price = :3, Shows_Per_Day = :4 WHERE RevenueTypes_ID = :5'
        cursor.execute(query , (attraction_c_p, attraction_a_p, attraction_s_p, attraction_per_day, attraction_rev_id))
        connection.commit()
        cursor.close()
        # connection.close()

        self.view_attraction_rev_id_entry.delete(0, 'end')
        self.view_attraction_c_p_entry.delete(0, 'end')
        self.view_attraction_s_p_entry.delete(0, 'end')
        self.view_attraction_a_p_entry.delete(0, 'end')
        self.view_attraction_per_day_entry.delete(0, 'end')

        # Display a message in the label
        message = "Animal Attraction added successfully!"
        self.message_label.config(text=message)

        columns_att = ("Child Price", "Senior Price", "Adult Price", "Per Day", "Revenue Type ID")
        tree_att = ttk.Treeview(self.sub_tab_attraction, columns=columns_att, show="headings")

        # Set column headings
        for col in columns_att:
            tree_att.heading(col, text=col)

        # Grid the Treeview
        tree_att.grid(row=6, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_att = ttk.Scrollbar(self.sub_tab_attraction, orient="vertical", command=tree_att.yview)
        vsb_att.grid(row=6, column=2, pady=10, sticky="ns")
        tree_att.configure(yscrollcommand=vsb_att.set)

        hsb_att = ttk.Scrollbar(self.sub_tab_attraction, orient="horizontal", command=tree_att.xview)
        hsb_att.grid(row=8, column=0, padx=10, sticky="ew")
        tree_att.configure(xscrollcommand=hsb_att.set)
        cursor4 = connection.cursor()
        query2 = "SELECT * FROM HP578.ANIMAL_SHOW"
        cursor4.execute(query2)

        # Fetch all rows from the result
        rows_att = cursor4.fetchall()
        # Insert data into the Treeview
        for row in rows_att:
            tree_att.insert("", "end", values=row)
        
        def on_treeview_select_b(event):
    # Get the selected item
            selected_item_att = tree_att.selection()

            # Check if any item is selected
            if selected_item_att:
                # Clear the entries
                self.view_attraction_rev_id_entry.delete(0, 'end')
                self.view_attraction_c_p_entry.delete(0, 'end')
                self.view_attraction_s_p_entry.delete(0, 'end')
                self.view_attraction_a_p_entry.delete(0, 'end')
                self.view_attraction_per_day_entry.delete(0, 'end')

                # Get values from the selected item and fill the entries
                values = tree_att.item(selected_item_att)['values']
                if values:
                    self.view_attraction_rev_id_entry.insert(0, values[4])  # Assuming name is the first column
                    self.view_attraction_c_p_entry.insert(0, values[0])
                    self.view_attraction_s_p_entry.insert(0, values[1])
                    self.view_attraction_a_p_entry.insert(0, values[2])
                    self.view_attraction_per_day_entry.insert(0, values[3]) 
        tree_att.bind('<ButtonRelease-1>', on_treeview_select_b)

    def add_employee(self):
        emp_id = self.view_employee_id_entry.get()
        print(emp_id)
        sd_p = self.view_employee_start_entry.get()
        print(sd_p)
        jt = self.view_employee_job_entry.get()
        print(jt)
        fname = self.view_employee_f_entry.get()
        print(fname)
        minit = self.view_employee_m_entry.get()
        lname = self.view_employee_l_entry.get()
        print(lname)
        street = self.view_employee_st_entry.get()
        print(street)
        city = self.view_employee_city_entry.get()
        print(city)
        state = self.view_employee_state_entry.get()
        print(state)
        zip = self.view_employee_zip_entry.get()
        print(zip)
        hrid = self.view_employee_hr_id_entry.get()
        print(hrid)
        sup_id = self.view_employee_sup_id_entry.get()
        print(sup_id)
        rev_id = self.view_employee_rev_id_entry.get()
        print(rev_id)
        cursor = connection.cursor()
        # #INSERT INTO EMPLOYEE (Emp_ID, Start_Date, JobType, Fname, Minit, Lname, Street ,City, State_Name, PinCode, Hr_ID, Super_ID, RevenueTypes_ID) VALUES('563214789', TO_DATE('2022-01-01', 'YYYY-MM-DD'), 'Veterinarian', 'John', 'D', 'Doe', '123 Main St', 'New York', 'NY', '10001', 1, NULL, NULL);
        query = "INSERT INTO HP578.EMPLOYEE (Emp_ID, Start_Date, JobType, Fname, Minit, Lname, Street ,City, State_Name, PinCode, Hr_ID, Super_ID, RevenueTypes_ID) VALUES(:1, TO_DATE(:2, 'YYYY-MM-DD'), :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13)"
        cursor.execute(query , (emp_id,sd_p,jt,fname,minit,lname,street,city,state,zip,hrid,sup_id,rev_id))
        connection.commit()
        cursor.close()

        message = "Employee inserted successfully!"
        self.message_label.config(text=message)

        columns_em = ("Employee ID", "Start Date", "Job Type", "First","Middle initial", "Last", "Street","City","State","Zip","HR ID","Super ID","Revenue Type ID")
        tree_em = ttk.Treeview(self.sub_tab_employees, columns=columns_em, show="headings")

        # Set column headings
        for col in columns_em:
            tree_em.heading(col, text=col)

        # Grid the Treeview
        tree_em.grid(row=14, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_em = ttk.Scrollbar(self.sub_tab_employees, orient="vertical", command=tree_em.yview)
        vsb_em.grid(row=14, column=1, pady=10, sticky="ns")
        tree_em.configure(yscrollcommand=vsb_em.set)

        hsb_em = ttk.Scrollbar(self.sub_tab_employees, orient="horizontal", command=tree_em.xview)
        hsb_em.grid(row=16, column=0, padx=10, sticky="ew")
        tree_em.configure(xscrollcommand=hsb_em.set)
        cursor6 = connection.cursor()
        query4 = "SELECT * FROM HP578.EMPLOYEE"
        cursor6.execute(query4)

        # Fetch all rows from the result
        rows = cursor6.fetchall()
        # Insert data into the Treeview
        for row in rows:
            tree_em.insert("", "end", values=row)
        
        def on_treeview_select_em(event):
    # Get the selected item
            selected_item = tree_em.selection()

            # Check if any item is selected
            if selected_item:
                # Clear the entries
                self.view_employee_id_entry.delete(0, 'end')
                self.view_employee_start_entry.delete(0, 'end')
                self.view_employee_job_entry.delete(0, 'end')
                self.view_employee_f_entry.delete(0, 'end')
                self.view_employee_m_entry.delete(0, 'end')
                self.view_employee_l_entry.delete(0, 'end')
                self.view_employee_st_entry.delete(0, 'end')
                self.view_employee_city_entry.delete(0, 'end')
                self.view_employee_state_entry.delete(0, 'end')
                self.view_employee_zip_entry.delete(0, 'end')
                self.view_employee_hr_id_entry.delete(0, 'end')
                self.view_employee_sup_id_entry.delete(0, 'end')
                self.view_employee_rev_id_entry.delete(0, 'end')
                

                # Get values from the selected item and fill the entries
                values = tree_em.item(selected_item)['values']
                if values:
                    self.view_employee_id_entry.insert(0, values[0])
                    self.view_employee_start_entry.insert(0, values[1])
                    self.view_employee_job_entry.insert(0, values[2]) 
                    self.view_employee_f_entry.insert(0, values[3])  # Assuming name is the first column
                    self.view_employee_m_entry.insert(0, values[4])
                    self.view_employee_l_entry.insert(0, values[5])
                    self.view_employee_st_entry.insert(0, values[6])
                    self.view_employee_city_entry.insert(0, values[7])
                    self.view_employee_state_entry.insert(0, values[8])
                    self.view_employee_zip_entry.insert(0, values[9])  # Assuming name is the first column
                    self.view_employee_hr_id_entry.insert(0, values[10])
                    self.view_employee_sup_id_entry.insert(0, values[11])
                    self.view_employee_rev_id_entry.insert(0, values[12])
        tree_em.bind('<ButtonRelease-1>', on_treeview_select_em)

    def upd_employee(self):
        emp_id = self.view_employee_id_entry.get()
        print(emp_id)
        sd_p = self.view_employee_start_entry.get()
        sd_p=sd_p[0:10]
        print(sd_p)
        jt = self.view_employee_job_entry.get()
        print(jt)
        fname = self.view_employee_f_entry.get()
        print(fname)
        minit = self.view_employee_m_entry.get()
        lname = self.view_employee_l_entry.get()
        print(lname)
        street = self.view_employee_st_entry.get()
        print(street)
        city = self.view_employee_city_entry.get()
        print(city)
        state = self.view_employee_state_entry.get()
        print(state)
        zip = self.view_employee_zip_entry.get()
        print(zip)
        hrid = self.view_employee_hr_id_entry.get()
        print(hrid)
        sup_id = self.view_employee_sup_id_entry.get()
        if sup_id is None or sup_id=="None" :
            sup_id=None
        print(sup_id)
        rev_id = self.view_employee_rev_id_entry.get()
        if rev_id is None or rev_id=="None" :
            rev_id=None
        print(rev_id)
        cursor = connection.cursor()
        # #INSERT INTO EMPLOYEE (Emp_ID, Start_Date, JobType, Fname, Minit, Lname, Street ,City, State_Name, PinCode, Hr_ID, Super_ID, RevenueTypes_ID) VALUES('563214789', TO_DATE('2022-01-01', 'YYYY-MM-DD'), 'Veterinarian', 'John', 'D', 'Doe', '123 Main St', 'New York', 'NY', '10001', 1, NULL, NULL);
        query = "UPDATE HP578.EMPLOYEE SET Start_Date=TO_DATE(:1, 'YYYY-MM-DD') , JobType=:2, Fname=:3, Minit=:4, Lname=:5, Street=:6 ,City=:7, State_Name=:8, PinCode=:9, Hr_ID=:10, Super_ID=:11, RevenueTypes_ID=:12 WHERE Emp_ID =:13 "
        cursor.execute(query , (sd_p,jt,fname,minit,lname,street,city,state,zip,hrid,sup_id,rev_id,emp_id))
        connection.commit()
        # cursor.close()

        message = "Employee inserted successfully!"
        self.message_label.config(text=message)

        columns_em = ("Employee ID", "Start Date", "Job Type", "First","Middle initial", "Last", "Street","City","State","Zip","HR ID","Super ID","Revenue Type ID")
        tree_em = ttk.Treeview(self.sub_tab_employees, columns=columns_em, show="headings")

        # Set column headings
        for col in columns_em:
            tree_em.heading(col, text=col)

        def on_treeview_configure(event):
            # Update the scroll region to cover the entire treeview
            tree_em.update_idletasks()
            hsb_em.configure(command=tree_em.xview, scrollregion=tree_em.bbox("all"))    

        # Grid the Treeview
        tree_em.grid(row=14, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_em = ttk.Scrollbar(self.sub_tab_employees, orient="vertical", command=tree_em.yview)
        vsb_em.grid(row=14, column=2, pady=10, sticky="ns")
        tree_em.configure(yscrollcommand=vsb_em.set)

        hsb_em = ttk.Scrollbar(self.sub_tab_employees, orient="horizontal", command=tree_em.xview)
        tree_em.configure(xscrollcommand=hsb_em.set)
        hsb_em.grid(row=16, column=0, padx=10, sticky="ew")

        tree_em.bind("<Configure>", on_treeview_configure)
        cursor6 = connection.cursor()
        query4 = "SELECT * FROM HP578.EMPLOYEE"
        cursor6.execute(query4)

        # Fetch all rows from the result
        rows = cursor6.fetchall()
        # Insert data into the Treeview
        for row in rows:
            tree_em.insert("", "end", values=row)
        
        def on_treeview_select_em(event):
    # Get the selected item
            selected_item = tree_em.selection()

            # Check if any item is selected
            if selected_item:
                # Clear the entries
                self.view_employee_id_entry.delete(0, 'end')
                self.view_employee_start_entry.delete(0, 'end')
                self.view_employee_job_entry.delete(0, 'end')
                self.view_employee_f_entry.delete(0, 'end')
                self.view_employee_m_entry.delete(0, 'end')
                self.view_employee_l_entry.delete(0, 'end')
                self.view_employee_st_entry.delete(0, 'end')
                self.view_employee_city_entry.delete(0, 'end')
                self.view_employee_state_entry.delete(0, 'end')
                self.view_employee_zip_entry.delete(0, 'end')
                self.view_employee_hr_id_entry.delete(0, 'end')
                self.view_employee_sup_id_entry.delete(0, 'end')
                self.view_employee_rev_id_entry.delete(0, 'end')
                

                # Get values from the selected item and fill the entries
                values = tree_em.item(selected_item)['values']
                if values:
                    self.view_employee_id_entry.insert(0, values[0])
                    self.view_employee_start_entry.insert(0, values[1])
                    self.view_employee_job_entry.insert(0, values[2]) 
                    self.view_employee_f_entry.insert(0, values[3])  # Assuming name is the first column
                    self.view_employee_m_entry.insert(0, values[4])
                    self.view_employee_l_entry.insert(0, values[5])
                    self.view_employee_st_entry.insert(0, values[6])
                    self.view_employee_city_entry.insert(0, values[7])
                    self.view_employee_state_entry.insert(0, values[8])
                    self.view_employee_zip_entry.insert(0, values[9])  # Assuming name is the first column
                    self.view_employee_hr_id_entry.insert(0, values[10])
                    self.view_employee_sup_id_entry.insert(0, values[11])
                    self.view_employee_rev_id_entry.insert(0, values[12])
        tree_em.bind('<ButtonRelease-1>', on_treeview_select_em)

    def add_hourly(self):
        hr_id = self.view_hourly_id_entry.get()
        print(hr_id)
        hr_rate = self.view_hourly_rate_entry.get()
        print(hr_rate)
        cursor = connection.cursor()
        query = 'INSERT INTO HP578.HOURLY_RATE (Hr_ID , Rate) VALUES(:1, :2)'
        cursor.execute(query , (hr_id, hr_rate))
        connection.commit()
        cursor.close()
        # connection.close()

        self.view_hourly_id_entry.delete(0, 'end')
        self.view_hourly_rate_entry.delete(0, 'end')

        # Display a message in the label
        message = "Hourly Rate added successfully!"
        self.message_label.config(text=message)

        columns_hw = ("HR ID", "Rate")
        tree_hw = ttk.Treeview(self.sub_tab_hourly, columns=columns_hw, show="headings")

        # Set column headings
        for col in columns_hw:
            tree_hw.heading(col, text=col)

        # Grid the Treeview
        tree_hw.grid(row=3, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_hw = ttk.Scrollbar(self.sub_tab_hourly, orient="vertical", command=tree_hw.yview)
        vsb_hw.grid(row=3, column=2, pady=10, sticky="ns")
        tree_hw.configure(yscrollcommand=vsb_hw.set)

        hsb_hw = ttk.Scrollbar(self.sub_tab_hourly, orient="horizontal", command=tree_hw.xview)
        hsb_hw.grid(row=5, column=0, padx=10, sticky="ew")
        tree_hw.configure(xscrollcommand=hsb_hw.set)
        cursor4 = connection.cursor()
        query2 = "SELECT * FROM HP578.HOURLY_RATE"
        cursor4.execute(query2)

        # Fetch all rows from the result
        rows_hw = cursor4.fetchall()
        # Insert data into the Treeview
        for row in rows_hw:
            tree_hw.insert("", "end", values=row)
        
        def on_treeview_select_hw(event):
    # Get the selected item
            selected_item_hw = tree_hw.selection()

            # Check if any item is selected
            if selected_item_hw:
                # Clear the entries
                self.view_hourly_id_entry.delete(0, 'end')
                self.view_hourly_rate_entry.delete(0, 'end')

                # Get values from the selected item and fill the entries
                values = tree_hw.item(selected_item_hw)['values']
                if values:
                    self.view_hourly_id_entry.insert(0, values[0])  # Assuming name is the first column
                    self.view_hourly_rate_entry.insert(0, values[1])
        tree_hw.bind('<ButtonRelease-1>', on_treeview_select_hw)

    def upd_hourly(self):
        hr_id = self.view_hourly_id_entry.get()
        print(hr_id)
        hr_rate = self.view_hourly_rate_entry.get()
        print(hr_rate)
        cursor = connection.cursor()
        query = 'UPDATE HP578.HOURLY_RATE SET Rate=:1 WHERE Hr_Id=:2'
        cursor.execute(query , ( hr_rate,hr_id))
        connection.commit()
        cursor.close()
        # connection.close()

        self.view_hourly_id_entry.delete(0, 'end')
        self.view_hourly_rate_entry.delete(0, 'end')

        # Display a message in the label
        message = "Hourly Rate added successfully!"
        self.message_label.config(text=message)

        columns_hw = ("HR ID", "Rate")
        tree_hw = ttk.Treeview(self.sub_tab_hourly, columns=columns_hw, show="headings")

        # Set column headings
        for col in columns_hw:
            tree_hw.heading(col, text=col)

        # Grid the Treeview
        tree_hw.grid(row=3, column=0, pady=10, padx=10, sticky="nsew" , rowspan=2, columnspan=2, ipadx=10, ipady=10 )

        # Configure Treeview to allow vertical and horizontal scrollbar
        vsb_hw = ttk.Scrollbar(self.sub_tab_hourly, orient="vertical", command=tree_hw.yview)
        vsb_hw.grid(row=3, column=2, pady=10, sticky="ns")
        tree_hw.configure(yscrollcommand=vsb_hw.set)

        hsb_hw = ttk.Scrollbar(self.sub_tab_hourly, orient="horizontal", command=tree_hw.xview)
        hsb_hw.grid(row=5, column=0, padx=10, sticky="ew")
        tree_hw.configure(xscrollcommand=hsb_hw.set)
        cursor4 = connection.cursor()
        query2 = "SELECT * FROM HP578.HOURLY_RATE"
        cursor4.execute(query2)

        # Fetch all rows from the result
        rows_hw = cursor4.fetchall()
        # Insert data into the Treeview
        for row in rows_hw:
            tree_hw.insert("", "end", values=row)
        
        def on_treeview_select_hw(event):
    # Get the selected item
            selected_item_hw = tree_hw.selection()

            # Check if any item is selected
            if selected_item_hw:
                # Clear the entries
                self.view_hourly_id_entry.delete(0, 'end')
                self.view_hourly_rate_entry.delete(0, 'end')

                # Get values from the selected item and fill the entries
                values = tree_hw.item(selected_item_hw)['values']
                if values:
                    self.view_hourly_id_entry.insert(0, values[0])  # Assuming name is the first column
                    self.view_hourly_rate_entry.insert(0, values[1])
        tree_hw.bind('<ButtonRelease-1>', on_treeview_select_hw)
    
    def view_hourly(self):
        print("Hello")

    def best_5(self):
        month = self.best_5_report_id_entry.get()
        print(month)
        cursor = connection.cursor()
        query = '''
        WITH DailyRevenue AS (
        SELECT
            TO_CHAR(Date_Time, 'YYYY-MM-DD') AS RevenueDate,
            SUM(Revenue) AS TotalRevenue
        FROM
            HP578.REVENUE_EVENTS
            WHERE
            EXTRACT(MONTH FROM Date_Time) = :1 
        GROUP BY
            TO_CHAR(Date_Time, 'YYYY-MM-DD')
        )

        SELECT
            RevenueDate,
            TotalRevenue
        FROM (
            SELECT
                RevenueDate,
                TotalRevenue,
                RANK() OVER (ORDER BY TotalRevenue DESC) AS RevenueRank
            FROM
                DailyRevenue
        )
        WHERE
            RevenueRank <= 5
        ORDER BY
        TotalRevenue DESC
        '''
        cursor.execute(query, {'1': month})
        connection.commit()
        #cursor.close()
        # connection.close()

        self.best_5_report_id_entry.delete(0, 'end')

        # Display a message in the label
        message = "Report made successfully!"
        self.message_label.config(text=message)

        self.tree = ttk.Treeview(self.sub_tab_revenue_time_best_5)
        self.tree['show']='headings'
        self.tree["columns"] = ("RevenueDate", "TotalRevenue")
        self.tree.heading("RevenueDate", text="Revenue Date")
        self.tree.heading("TotalRevenue", text="Total Revenue")
        self.tree.grid(row=4, column=0, columnspan=2,padx=10, pady=10)
        
        
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)

    def top_3(self):
        st_d = self.top_3_report_sd_entry.get()
        print(st_d)
        ed_d = self.top_3_report_ed_entry.get()
        print(ed_d)
        cursor = connection.cursor()
        query = '''
        WITH AttractionRevenue AS (
            SELECT
                rt.Rev_Name AS Attraction,
                SUM(re.Revenue) AS TotalRevenue
            FROM
                HP578.REVENUE_EVENTS re
            JOIN REVENUE_TYPES rt ON re.RevenueTypes_ID = rt.RevenueTypes_ID
            WHERE
                re.Date_Time BETWEEN TO_DATE(:1, 'YYYY-MM-DD') AND TO_DATE(:2, 'YYYY-MM-DD')
            GROUP BY
                rt.Rev_Name
        )
        SELECT
            Attraction,
            TotalRevenue
        FROM
            (
                SELECT
                    Attraction,
                    TotalRevenue,
                    RANK() OVER (ORDER BY TotalRevenue DESC) AS rnk
                FROM
                    AttractionRevenue
            )
        WHERE
            rnk <= 4 and rnk>1
        '''
        cursor.execute(query, (st_d,ed_d))
        connection.commit()
        #cursor.close()
        # connection.close()

        self.top_3_report_sd_entry.delete(0, 'end')
        self.top_3_report_ed_entry.delete(0, 'end')

        # Display a message in the label
        message = "Report generated successfully!"
        self.message_label.config(text=message)

        self.tree = ttk.Treeview(self.sub_tab_revenue_time_top_3)
        self.tree['show']='headings'
        self.tree["columns"] = ("ATTRACTION", "TOTALREVENUE")
        self.tree.heading("ATTRACTION", text="ATTRACTION")
        self.tree.heading("TOTALREVENUE", text="TOTALREVENUE")
        self.tree.grid(row=4, column=0, columnspan=2,padx=10, pady=10)
        
        
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)

    def attraction_report(self):
        att_date = self.date_attractions_entry.get()
        print(att_date)
        att_name=self.dropdown1.get()
        print(att_name)
        att_type=self.dropdown2.get()
        print(att_type)
        att_type=att_type+'_Price'
        print(att_type)
        
        cursor = connection.cursor()
        if att_type=='Adult_Price':
            query = """
                UPDATE HP578.revenue_events
                SET REVENUE = REVENUE + (SELECT ADULT_PRICE FROM HP578.ANIMAL_SHOW WHERE revenuetypes_id = (SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)),
                    tickets_sold = tickets_sold + 1
                WHERE date_time = TO_DATE(:1, 'YYYY-MM-DD') AND revenuetypes_id = (SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)
                        """
        elif att_type=='Child_Price':
            query = """
                UPDATE HP578.revenue_events
                SET REVENUE = REVENUE + (SELECT CHILD_PRICE FROM HP578.ANIMAL_SHOW WHERE revenuetypes_id = (SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)),
                    tickets_sold = tickets_sold + 1
                WHERE date_time = TO_DATE(:1, 'YYYY-MM-DD') AND revenuetypes_id = (SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)
                        """
        elif att_type=='Senior_Price':
            query = """
                UPDATE HP578.revenue_events
                SET REVENUE = REVENUE + (SELECT SENIOR_PRICE FROM HP578.ANIMAL_SHOW WHERE revenuetypes_id = (SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)),
                    tickets_sold = tickets_sold + 1
                WHERE date_time = TO_DATE(:1, 'YYYY-MM-DD') AND revenuetypes_id = (SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)
                        """
        
#         query = """
#         UPDATE HP578.revenue_events
# SET REVENUE = REVENUE + (SELECT ADULT_PRICE FROM HP578.ANIMAL_SHOW WHERE revenuetypes_id = (SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)),
#     tickets_sold = tickets_sold + 1
# WHERE date_time = TO_DATE(:1, 'YYYY-MM-DD') AND revenuetypes_id = (SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)
#         """
        cursor.execute(query,{'1': att_date,'2':att_name})
        connection.commit()
        cursor.close()
        
        # Display a message in the label
        message = "Report generated successfully!"
        self.message_label.config(text=message)

        self.tree = ttk.Treeview(self.sub_tab_daily_attractions)
        self.tree['show']='headings'
        self.tree["columns"] = ("REVENUETYPES_ID", "REV_NAME", "tickets_sold", "date_time", "revenue")
        self.tree.heading("REVENUETYPES_ID", text="REVENUETYPES_ID")
        self.tree.heading("REV_NAME", text="REV_NAME")
        self.tree.heading("tickets_sold", text="tickets_sold")
        self.tree.heading("date_time", text="date_time")
        self.tree.heading("revenue", text="revenue")
        self.tree.grid(row=4, column=0, columnspan=2,padx=10, pady=10)
            
        cursor = connection.cursor()
        query = '''
        SELECT
            re.REVENUETYPES_ID AS Attraction_ID,
            rt.REV_NAME AS Attraction_Location,
            re.tickets_sold AS Ticket_Sold,
            re.date_time AS Date_Of_Attraction,
            re.revenue
        FROM
            HP578.revenue_events re
            JOIN
            HP578.revenue_types rt ON re.REVENUETYPES_ID = rt.REVENUETYPES_ID
            WHERE
            re.REVENUETYPES_ID IN (SELECT DISTINCT REVENUETYPES_ID FROM animal_show)
        '''
        cursor.execute(query)

        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)
            
        connection.commit()
        cursor.close()
        # connection.close()

    def attendance_report(self):
        atd_date = self.date_attendance_entry.get()
        print(atd_date)
        atd_name=self.dropdown_atd.get()
        print(atd_name)
        atd_type=self.dropdown_atd_2.get()
        print(atd_type)
        atd_type=atd_type+'_Price'
        print(atd_type)
        
        cursor = connection.cursor()
        
        if atd_type=='Adult_Price':
            query = """
                UPDATE HP578.revenue_events
SET revenue = revenue+ (SELECT ADULT_PRICE FROM HP578.zoo_admission WHERE revenuetypes_id=(SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)),
tickets_sold=tickets_sold + 1 WHERE date_time = TO_DATE(:1, 'YYYY-MM-DD') AND revenuetypes_id=(SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)
                        """
        elif atd_type=='Child_Price':
            query = """
                UPDATE HP578.revenue_events
SET revenue = revenue+ (SELECT CHILD_PRICE FROM HP578.zoo_admission WHERE revenuetypes_id=(SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)),
tickets_sold=tickets_sold + 1 WHERE date_time = TO_DATE(:1, 'YYYY-MM-DD') AND revenuetypes_id=(SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)
                        """
        elif atd_type=='Senior_Price':
            query = """
                UPDATE HP578.revenue_events
SET revenue = revenue+ (SELECT SENIOR_PRICE FROM HP578.zoo_admission WHERE revenuetypes_id=(SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)),
tickets_sold=tickets_sold + 1 WHERE date_time = TO_DATE(:1, 'YYYY-MM-DD') AND revenuetypes_id=(SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type=:2)
                        """
        
#         query = '''
#         UPDATE HP578.revenue_events
# SET revenue = revenue+ (SELECT adult_price FROM HP578.zoo_admission WHERE revenuetypes_id=(SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type='General Admission')),
# tickets_sold=tickets_sold + 1 WHERE date_time = TO_DATE('2023-01-01', 'YYYY-MM-DD') AND revenuetypes_id=(SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_type='General Admission')
#         '''
        # cursor.execute(query)
        cursor.execute(query,{'1': atd_date,'2':atd_name})
        connection.commit()
        cursor.close()
        # connection.close()
        
        # Display a message in the label
        message = "Report generated successfully!"
        self.message_label.config(text=message)


        self.tree = ttk.Treeview(self.sub_tab_daily_attendance)
        self.tree['show']='headings'
        self.tree["columns"] = ("Revenue_ID", "Attendance", "Date_", "Total_Revenue")
        self.tree.heading("Revenue_ID", text="Revenue_ID")
        self.tree.heading("Attendance", text="Attendance")
        self.tree.heading("Date_", text="Date_")
        self.tree.heading("Total_Revenue", text="Total_Revenue")
        self.tree.grid(row=4, column=0, columnspan=2,padx=10, pady=10)
        
        
        cursor = connection.cursor()
        query = '''
        SELECT
            re.RevenueTypes_ID AS Revenue_ID,
            re.tickets_sold AS Attendance,
            re.date_time AS Date_,
            re.revenue AS Total_Revenue
        FROM
            HP578.zoo_admission za
        JOIN
            HP578.revenue_events re ON za.RevenueTypes_ID = re.RevenueTypes_ID
        '''
        cursor.execute(query)

        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)
            
        connection.commit()
        cursor.close()

    def concession_report(self):
        con_date = self.date_concession_entry.get()
        print(con_date)
        con_name=self.dropdown_con.get()
        print(con_name)
        
        cursor = connection.cursor()
        query = '''
        UPDATE REVENUE_EVENTS
    SET revenue=revenue+(SELECT product from CONCESSION WHERE revenuetypes_id=(SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_name=:2)),
    tickets_sold=tickets_sold + 1
    WHERE date_time = TO_DATE(:1, 'YYYY-MM-DD') AND revenuetypes_id=(SELECT revenuetypes_id FROM HP578.revenue_types WHERE revenue_types.rev_name=:2)
        '''
        cursor.execute(query,{'1': con_date,'2':con_name})
        connection.commit()
        cursor.close()
        # connection.close()
        
        # Display a message in the label
        message = "Report generated successfully!"
        self.message_label.config(text=message)

        self.tree = ttk.Treeview(self.sub_tab_daily_concessions)
        self.tree['show']='headings'
        self.tree["columns"] = ("Concessions_ID", "Product_Location", "Total_Item_Sold","Date_", "Revenue")
        self.tree.heading("Concessions_ID", text="Concessions_ID")
        self.tree.heading("Product_Location", text="Product_Location")
        self.tree.heading("Total_Item_Sold", text="Total_Item_Sold")
        self.tree.heading("Date_", text="Date_")
        self.tree.heading("Revenue", text="Revenue")
        self.tree.grid(row=3, column=0, columnspan=2,padx=10, pady=10)
        
        
        cursor = connection.cursor()
        query = '''
        SELECT
            c.RevenueTypes_ID AS Concessions_ID,
            rt.rev_name AS Product_Location,
            re.tickets_sold AS Total_Item_Sold,
            re.date_time AS Date_,
            re.revenue AS Revenue
        FROM
            CONCESSION c
        JOIN
            revenue_events re on c.RevenueTypes_ID=re.RevenueTypes_ID
        JOIN
            revenue_types rt on rt.revenuetypes_id=re.revenuetypes_id
        '''
        cursor.execute(query)

        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)
            
        connection.commit()
        cursor.close()
    
    def total_rev(self):
        date_total = self.cal_total_revenue_entry.get()
        print(date_total)
        cursor = connection.cursor()
        query = '''
        SELECT
            re.date_time AS DATE_,
            rt.rev_name AS Revenue_Name,
            re.tickets_sold AS Ticket_Sold,
            re.revenue AS Revenue
        FROM
            HP578.revenue_events re
        JOIN
            HP578.revenue_types rt on re.revenuetypes_id=rt.revenuetypes_id and re.date_time=TO_DATE(:1, 'YYYY-MM-DD')
        '''
        cursor.execute(query,{'1': date_total})
        connection.commit()
        #cursor.close()
        # connection.close()

        # Display a message in the label
        message = "Report generated successfully!"
        self.message_label.config(text=message)

        self.tree = ttk.Treeview(self.sub_tab_total_rev)
        self.tree['show']='headings'
        self.tree["columns"] = ("DATE_", "Revenue_Name", "Ticket_Sold", "Revenue")
        self.tree.heading("DATE_", text="DATE_")
        self.tree.heading("Revenue_Name", text="Revenue_Name")
        self.tree.heading("Ticket_Sold", text="Ticket_Sold")
        self.tree.heading("Revenue", text="Revenue")
        self.tree.grid(row=3, column=0, columnspan=2,padx=10, pady=10)
        
        
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)

    def animal_roport(self):
        cursor = connection.cursor()
        query = '''
        SELECT
            S.Spc_ID,
            S.Spc_Name,
            COUNT(A.Ani_ID) AS Total_Animals,
            COUNT(CASE WHEN A.Status = 'Healthy' THEN 1 END) AS Healthy_Animals,
            COUNT(CASE WHEN A.Status = 'Ill' THEN 1 END) AS Sick_Animals,
            COUNT(CASE WHEN A.Status = 'Maternity' THEN 1 END) AS Animals_in_Maternity,
            SUM(S.Food_Cost) AS Total_Food_Cost,
            NVL((select rate FROM hourly_rate where Hr_ID=1) * 40 * COUNT(CASE WHEN A.Status = 'Ill' THEN 1 END),0) AS Total_Vet_Cost,
            NVL(((select rate FROM hourly_rate where Hr_ID=2) * 40 * COUNT(CASE WHEN A.Status = 'Maternity' THEN 1 END)),0) AS Total_Care_Specialist_Cost
        FROM
            SPECIES S
        JOIN
            ANIMAL A ON S.Spc_ID = A.Spc_ID
        LEFT JOIN
            CARES_FOR CF ON S.Spc_ID = CF.Spc_ID
        LEFT JOIN
            EMPLOYEE E ON CF.Emp_ID = E.Emp_ID
        LEFT JOIN
            HOURLY_RATE HR_Vet ON E.Hr_ID = HR_Vet.Hr_ID AND E.JobType = 'Veterinarian'
        LEFT JOIN
            HOURLY_RATE HR_Spec ON E.Hr_ID = HR_Spec.Hr_ID AND E.JobType = 'Animal Care'
        GROUP BY
            S.Spc_ID,S.Spc_Name
        '''
        cursor.execute(query)
        connection.commit()
        #cursor.close()
        # connection.close()

        # Display a message in the label
        message = "Report generated successfully!"
        self.message_label.config(text=message)

        self.tree = ttk.Treeview(self.sub_tab_animal_report)
        self.tree['show']='headings'
        self.tree["columns"] = ("Spc_ID", "Spc_Name", "Total_Animals", "Healthy_Animals", "Sick_Animals", "Animals_in_Maternity", "Total_Food_Cost", "Total_Vet_Cost", "Total_Care_Specialist_Cost")
        self.tree.heading("Spc_ID", text="Spc_ID")
        self.tree.heading("Spc_Name", text="Spc_Name")
        self.tree.heading("Total_Animals", text="Total_Animals")
        self.tree.heading("Healthy_Animals", text="Healthy_Animals")
        self.tree.heading("Sick_Animals", text="Sick_Animals")
        self.tree.heading("Animals_in_Maternity", text="Animals_in_Maternity")
        self.tree.heading("Total_Food_Cost", text="Total_Food_Cost")
        self.tree.heading("Total_Vet_Cost", text="Total_Vet_Cost")
        self.tree.heading("Total_Care_Specialist_Cost", text="Total_Care_Specialist_Cost")
        self.tree.grid(row=1, column=0, columnspan=2,padx=10, pady=10)

        def on_h(*args):
            self.tree.xview(*args)

        def on_v(*args):
            self.tree.yview(*args)    

        vsb_em = ttk.Scrollbar(self.sub_tab_animal_report, orient="vertical", command=on_v)
        vsb_em.grid(row=1, column=2, pady=10, sticky="ns")
        self.tree.configure(yscrollcommand=vsb_em.set)

        hsb_em = ttk.Scrollbar(self.sub_tab_animal_report, orient="horizontal", command=on_h)
        self.tree.configure(xscrollcommand=hsb_em.set)
        hsb_em.grid(row=2, column=0, padx=0, sticky="ew")

        self.sub_tab_animal_report.grid_rowconfigure(0, weight=1)
        self.sub_tab_animal_report.grid_columnconfigure(0, weight=1)
        
        
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)

    def avg(self):
        st_d = self.avg_report_sd_entry.get()
        print(st_d)
        ed_d = self.avg_report_ed_entry.get()
        print(ed_d)
        cursor = connection.cursor()
        query = '''
        SELECT
            rt.REV_NAME AS Revenue_Source,
            AVG(re.revenue) AS Average_Revenue
        FROM
            HP578.revenue_events re
        LEFT JOIN
            HP578.revenue_types rt ON re.revenuetypes_id = rt.revenuetypes_id
        WHERE
            re.date_time BETWEEN TO_DATE(:1, 'YYYY-MM-DD') AND TO_DATE(:2, 'YYYY-MM-DD')
        GROUP BY
            rt.rev_name
        ORDER BY
            AVG(re.revenue) DESC
        '''
        cursor.execute(query, (st_d,ed_d))
        connection.commit()
        #cursor.close()
        # connection.close()

        self.top_3_report_sd_entry.delete(0, 'end')
        self.top_3_report_ed_entry.delete(0, 'end')

        # Display a message in the label
        message = "Report generated successfully!"
        self.message_label.config(text=message)
        self.tree = ttk.Treeview(self.sub_tab_revenue_time_avg)
        self.tree['show']='headings'
        self.tree["columns"] = ("Revenue_Source", "Average_Revenue")
        self.tree.heading("Revenue_Source", text="Revenue_Source")
        self.tree.heading("Average_Revenue", text="Average_Revenue")
        self.tree.grid(row=4, column=0, columnspan=2,padx=10, pady=10)
        
        
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)



if __name__ == "__main__":
    root = tk.Tk()
    app = zoo(root)
    root.mainloop()
