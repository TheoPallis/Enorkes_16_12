import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import os
import glob

def open_file():
    # Fetch the selected item from the combobox
    selected_category = combo.get()
    
    # Get the .lnk file path corresponding to the selected item
    file_path = mapping_ypodeigmaton.get(selected_category)
    
    if file_path:
        try:
            os.startfile(file_path)  # Open the .lnk file
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open {file_path}. Error: {str(e)}")
    else:
        messagebox.showwarning("Warning", f"No file found for the category: {selected_category}")

# Dictionary mapping categories to their respective .lnk files
katigories_enorkon= ('''(1) ΠΙΘΑΝΟΛΟΓΟΥΜΕΝΗ,(2) ΑΥΘΑΙΡΕΤΗ ΕΠΑΝΑΣΥΝΔΕΣΗ,(3) ΑΥΘΑΙΡΕΤΗ ΕΠΑΝΑΣΥΝΔΕΣΗ ΜΕ ΠΑΡΑΚΑΜΨΗ ΜΕΤΡΗΤΗ,(4) ΠΑΡΑΚΑΜΨΗ ΜΕΤΡΗΤΗ ΧΩΡΙΣ ΑΥΘΑΙΡΕΤΗ ΕΠΑΝΑΣΥΝΔΕΣΗ,(5) ΛΑΜΑΚΙΑ,(6) ΒΕΒΑΙΗ ΡΕΥΜΑΤΟΚΛΟΠΗ,
 '''.split(","))
word_files = glob.glob(os.path.join(os.getcwd(), "*.lnk*"))[:5]