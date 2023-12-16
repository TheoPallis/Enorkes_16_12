import pandas as pd
import numpy as np
from tkinter import filedialog as fd
import datetime
planned_date = 'Ημερομηνία Προγραμματισμού  Ένορκης'
dikigoros_col = 'Υπογράφων Δικηγόρος Ένορκης'
date_katathesi_options= ["Κατάθεση μικροδ ΝΚΠολ Δ",'Ημ νια Κατάθεσης Αγωγής ΝΚπολ Δ']

# Function to load excel file with error handling
def load_excel_file():
    # File dialog with file type filtering for Excel files
    # file_path = fd.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    file_path = r"C:\Users\Θοδωρής\Code\Python\Main-Scripts\Enorkes\Helper Funcs\Ένορκες_Δεκεμβρίου.xlsx"
    # Check if a file was selected
    if file_path:
        try:
            anathesi_df = pd.read_excel(file_path, dtype=str)
            return anathesi_df
        except Exception as e:
            print(f"Error loading file: {e}")   
            return None
    else:
        print("No file selected.")
        return None

def get_date_column(df, date_katathesi_options):
    
   # Checks which date column from the date_katathesi_options list exists in the df
    date_column = date_katathesi_options[0] if date_katathesi_options[0] in df.columns else date_katathesi_options[1]
    return(date_column)






def filter_dataframe_by_date(anathesi_df, date_column, input_date):
    """
    Filters the DataFrame based on a given date, regardless of the date format.

    Parameters:
    anathesi_df (pd.DataFrame): The DataFrame to filter.
    date_column (str): The name of the date column in the DataFrame.
    input_date (str): The date to filter by.

    Returns:
    pd.DataFrame: Filtered DataFrame.
    """
    # Normalize the dates in the DataFrame
    anathesi_df[date_column] = anathesi_df[date_column].apply(normalize_date)
    # Normalize the input date
    normalized_input_date = normalize_date(input_date)
    # Filter the DataFrame
    return anathesi_df[anathesi_df[date_column] == normalize_date]


def load_filtered_df(mode):
    # Load the unfiltered dataframe
    unfiltered_anathesi_df = load_excel_file()
    # Get and normalize the date column
    date_column = get_date_column(unfiltered_anathesi_df, date_katathesi_options)
    unfiltered_anathesi_df[date_column] = unfiltered_anathesi_df[date_column].apply(normalize_date)
    
    # print(f" The date column is : {date_column}")
    # print(unfiltered_anathesi_df[date_column])
    
    # Filter the dataframe if mode == 'filtered'
    if mode == 'filtered':
        current_date = input("Enter the date (DD/MM/YYYY): ")
        anathesi_df = filter_dataframe_by_date(unfiltered_anathesi_df, date_column, current_date)
    elif mode == 'unfiltered' :  
        anathesi_df = unfiltered_anathesi_df

    return anathesi_df

def normalize_date(date_string):
    """
    Converts the input date string to a standardized format (YYYY-MM-DD).
    Parameters:
    date_string (str): The date string to normalize.

    Returns:
    str: Normalized date string.s
    """
    try:
        return pd.to_datetime(date_string, errors='coerce').strftime('%d/%m/%y')

    except ValueError:
            # You can add more date formats here if needed
            return None

def get_day_name(date_string, date_format='%d/%m/%Y'):
    date_object = datetime.datetime.strptime(date_string, date_format)
    return date_object.strftime('%A')

def create_dicts_from_df(df, key_col_index, value_col_index):
    '''
    Creates a dict from two columns with the first col as the keys and the second column as the values
    '''
    keys = df.iloc[:, key_col_index]
    values = df.iloc[:, value_col_index]
    return dict(zip(keys, values))

def create_lawyer_dicts(df) :
    mapping_dikigoron = create_dicts_from_df(df, 0, 1)
    mapping_dikigoron_full_names = create_dicts_from_df(df, 2, 0)
    return (mapping_dikigoron_full_names,mapping_dikigoron)
 
def fill_lawyer_full_names(df) :
    mapping_dikigoron_full_names = create_lawyer_dicts(df)[0]
    df['ΔΙΚΗΓΟΡΟΣ_full'] = df[dikigoros_col].map(mapping_dikigoron_full_names)
    return df




def assign_hours_to_lawyers(df, hours, lawyer_column='ΔΙΚΗΓΟΡΟΣ_full'):
    if 'Hours' not in df.columns:
        df['Hours'] = pd.Series(np.nan, index=df.index)

    # Replace NaN with 'Unknown' in lawyer column
    df[lawyer_column].fillna('Unknown', inplace=True)

    hour_index = 0
    for i in range(len(df)):
        if hour_index >= len(hours):
            print("Warning: Ran out of hours!")
            break

        if i == 0 or df[lawyer_column].iloc[i] != df[lawyer_column].iloc[i-1]:
            df.at[i, 'Hours'] = hours[hour_index]
            hour_index += 1
        else:
            df.at[i, 'Hours'] = df['Hours'].iloc[i-1]

    return df

def write_hyperlink(link):
    # Using the openpyxl syntax to specify a hyperlink
    return f'=HYPERLINK("{link}", "{link}")'