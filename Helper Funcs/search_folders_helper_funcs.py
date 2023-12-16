
import re
PATTERN = r'\b\w\.\b'

def get_modified_folder_name(folder_name, pattern=PATTERN):
    """Modify the folder name based on the provided pattern."""
    return re.sub(pattern, '', folder_name)

def get_all_folders(path, list_ofeileton, df1, out_path):
    """Search for specific folders and files, and map them to the dataframe."""
    mapping_folders = {name: "-" for name in list_ofeileton} #Now that it returns one folder it is not needed
    mapping_files = {name: "-" for name in list_ofeileton}
    for root, _, files in os.walk(path):
        if "Υποθέσεις" in root and "ανάθεσης" in root:
            for name in list_ofeileton:
                first_word_folder = os.path.basename(root).split()[0]
                if mapping_anatheseis[name] in str(root):
                    if str(mapping_kodikoi[name]) in str(files):
                        mapping_folders[name] = root
                        nea_agogi_found = False  # Flag to track if ΝΕΑ ΑΓΩΓΗ is found

                        for file in files:
                            full_path = os.path.join(root, file)
                            if file.endswith(".docx"):
                                # Check for 'ΝΕΑ ΑΓΩΓΗ' in file name
                                if "ΝΕΑ ΑΓΩΓΗ" in file:
                                    nea_agogi_found = True
                                    mapping_files[name] = full_path
                                    shutil.copy(full_path, out_path)
                                    break

                                include_conditions = [first_word_folder in file, "ΣΧΕΔΙΟ ΑΓΩΓΗΣ ΔΕΔΔΗΕ" in file]
                                exclude_conditions = ["ηρεξούσιο", "Προτάσεις", "Σχετικών", "ΒΕΒΑΙΗ", "οτάσεις", "ενορκη", "ΛΑΜΑΚΙΑ"]

                                if any(include_conditions) and all(term not in file for term in exclude_conditions):
                                    if not nea_agogi_found:  # If 'ΝΕΑ ΑΓΩΓΗ' not already found
                                        mapping_files[name] = full_path
                                        shutil.copy(full_path, out_path)
                                        break
                                elif first_word_folder not in file:
                                    print(f"Not found : {first_word_folder} : {file}")


    df1['Φάκελος'] = df1['Αντίδικος'].map(mapping_folders)

    df1['Έλεγχος_κωδικού_ενέργειας'] = df1['Αντίδικος'].map(mapping_kodikos_check,'ignore')

    return mapping_files

def get_folder_or_filename(x, position=-1):
    parts = str(x).split("\\")
    if len(parts) > 1:  # check if there's at least one delimiter
        return parts[position]
    return ""  # return an empty string if not


def create_file_dict() :
    mapping_files = get_all_folders(path_to_search_enorkes, list_ofeileton, df1, out_path)
    file_list = [mapping_files.get(folder_name, "-") for folder_name in list_ofeileton]
    return file_list

def fill_path_enorkon_col() :
    df1['Φάκελος'] = (r"\\lawoffice\\Applications\\ScanDocs\\ΔΕΔΔΗΕ scandocs\\" 
                      + df1['Φάκελος'].apply(lambda x: get_folder_or_filename(x, -3)) # For subfolders (eg Θεσσαλονίκη)
                       + "\\" 
                      + df1['Φάκελος'].apply(lambda x: get_folder_or_filename(x, -2)) 
                      + "\\" 
                      + df1['Φάκελος'].apply(lambda x: get_folder_or_filename(x, -1)))

    df1['Φάκελος'] = df1['Φάκελος'].astype(str) 
    df1['Φάκελος'] =df1['Φάκελος'].apply(lambda x : x.replace("ΦΑΚΕΛΟΙ ΕΝΟΡΚΩΝ",""))
    return df1['Φάκελος']


def bundle_funcs(pattern = PATTERN) :
    list_ofeileton = list(anathesi_df['Επωνυμία Αποδέκτη'])
    list_ofeileton = [re.sub(pattern, '', x) for x in list_ofeileton]
    half_list_ofeileton = [x.split(" ")[0] for x in list_ofeileton]
    out_path = r"C:\Users\pallist\Desktop\ΤΡΕΧΟΝΤΑ\Testing Folder\ΦΑΚΕΛΟΙ ΕΝΟΡΚΩΝ\Results" 
    path_to_search_enorkes = r"C:\Users\pallist\Desktop\ΤΡΕΧΟΝΤΑ\Testing Folder\ΦΑΚΕΛΟΙ ΕΝΟΡΚΩΝ"
    anathesi_list = list(anathesi_df['Ανάθεση'].apply(lambda x : str(x).split()[0].replace("η","").replace("ης","")))
    kodikos_list = list(anathesi_df['Κωδικός Ενέργειας'])
    mapping_anatheseis = dict(zip(list_ofeileton,anathesi_list))
    mapping_kodikoi = dict(zip(list_ofeileton,kodikos_list))
    mapping_kodikos_check = dict(zip(list_ofeileton,"-"))
    empty_doc = Document()
    empty_doc.save(os.path.join(out_path,'empty.docx'))
    empty = os.path.join(out_path,'empty.docx')
    create_file_dict()
    fill_path_enorkon_col()
