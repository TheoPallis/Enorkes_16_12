import pandas as pd
from tstamp import generate_timestamp_filename

def create_dataframe(anathesi_df, df_type):
    """
    Creates a DataFrame based on the type specified ('df1' or 'df2').

    Parameters:
    anathesi_df (pd.DataFrame): The source DataFrame.
    df_type (str): Type of DataFrame to create ('df1' or 'df2').

    Returns:
    pd.DataFrame: The created DataFrame.
    """
    common_columns = {
        'A/A': [x for x in range(1, len(anathesi_df['Επωνυμία Αποδέκτη']) + 1)],
        'Αντίδικος': nathesi_df['Επωνυμία Αποδέκτη']
    }
    match df_type:
        
    
        case('df1') 
        specific_columns = {
                'Ανάθεση': anathesi_df['Ανάθεση'].apply(lambda x: str(x)[:str(x).index('Ανάθεση')] + 'Ανάθεση'),
                'ΔΙΚΑΣΤΙΚΟ ΙΔΡΥΜΑ': "",
                'Διαδκασία': "",
                'Μάρτυρας': anathesi_df['Μάρτυρας'],
                'Φάκελος': ""
            }
        break

        case('df2')
        specific_columns = {
                'Διαδικασία': anathesi_df['Διαδικασία'],
                'Δικαστικό Ίδρυμα': anathesi_df['Δικαστικό Ίδρυμα'],
                'Ημερομηνία Κατάθεσης': anathesi_df['Date_Katathesi'],
                'Ημερομηνία Κατάθεσης2': "",
                'ΓΑΚ': anathesi_df['ΓΑΚ'].apply(lambda x: str(x).replace(".0", "")).replace("nan", ""),
                'ΕΑΚ': anathesi_df['ΕΑΚ'].apply(lambda x: str(x).replace(".0", "")).replace("nan", "")
            }
        break


        case('df3[')
        specific_columns = {
            'Αντίδικος_1': antidikos_1,
            'Αντίδικος_2': antidikos_2,
            'Αντίδικος_3':antidikos_3,
            'Ημερομηνία_Αγωγής':  last_date,
            'Ημερομηνία_Ένορκης' : pd.to_datetime(anathesi_df['Ημερομηνία Προγραμματισμού  Ένορκης'], errors='coerce').dt.strftime('%d/%m/%Y'),
            'Ώρα ένορκης': hours_col,
            'Δικηγόρος' : anathesi_df['ΔΙΚΗΓΟΡΟΣ_full'] ,
            'Ημερομηνία Κλήσης' : '-',
            'Αίθουσα' : AITHOUSA
        } 
        break
    
        case('df4') 
        specific_columns = {
            'Αντίδικος 1' : "ΚΕΝΟ"
            'Μορφ.αντίδικος 1' : df3['Αντίδικος_1'] + " "
            'Αντίδικος 2' : "ΚΕΝΟ"
            'Μορφ.αντίδικος 2' : df3['Αντίδικος_2'] + " "
            'Αντίδικος 3' : "ΚΕΝΟ"
            'Μορφ.αντίδικος 3' : df3['Αντίδικος_3'] + " "
            'Αντίδικος ένορκης' : df3['Αντίδικος_1'].apply(lambda x : x.replace('Του ','του ').replace('Της ','της ') )
            'Μορφ.αντίδικος ένορκης 1' : "ΚΕΝΟ"
            'Μορφ.αντίδικος ένορκης 2' : "ΚΕΝΟ"
            'ΣΥΝΟΠΤΙΚΗ ΗΜΕΡΟΜΗΝΙΑ ΕΝΟΡΚΗΣ' : df3['Ημερομηνία_Ένορκης'].fillna("01/01/1900")
            'ΗΜΕΡΑ ΕΝΟΡΚΗΣ' : 'ΣΥΝΟΠΤΙΚΗ ΗΜΕΡΟΜΗΝΙΑ ΕΝΟΡΚΗΣ'.apply(get_day_name)
            'ΗΜΕΡΑ ΕΝΟΡΚΗΣ' : 'ΗΜΕΡΑ ΕΝΟΡΚΗΣ'.map(day_dict)
            'ΩΡΑ' : hours_col
            'ΗΜΕΡΑ ΕΝΟΡΚΗΣ ΑΡΙΘΜΟΣ'  = 'ΣΥΝΟΠΤΙΚΗ ΗΜΕΡΟΜΗΝΙΑ ΕΝΟΡΚΗΣ'.apply(lambda x : str(x).split("/")[0])
            'ΜΗΝΑΣ ΕΝΟΡΚΗΣ' : 'ΣΥΝΟΠΤΙΚΗ ΗΜΕΡΟΜΗΝΙΑ ΕΝΟΡΚΗΣ'.apply(lambda x : str(x).split("/")[1]).map(month_dict)
            'ΕΤΟΣ ΕΝΟΡΚΗΣ'  = 'ΣΥΝΟΠΤΙΚΗ ΗΜΕΡΟΜΗΝΙΑ ΕΝΟΡΚΗΣ'.apply(lambda x : str(x).split("/")[2])
            'ΔΙΚΗΓΟΡΟΣ 1' : anathesi_df'ΔΙΚΗΓΟΡΟΣ_full'.map(mapping_dikigoron) 
            'ΔΙΚΗΓΟΡΟΣ 2' : anathesi_df'ΔΙΚΗΓΟΡΟΣ_full'
            'ΓΕΝΟΣ ΔΙΚΗΓΟΡΟΥ 1' : np.where('ΔΙΚΗΓΟΡΟΣ 1'.apply(lambda x : str(x)[:3])== 'του','Ο','Η')
            'ΓΕΝΟΣ ΔΙΚΗΓΟΡΟΥ 2' : np.where('ΔΙΚΗΓΟΡΟΣ 1'.apply(lambda x : str(x)[:3])== 'του',' Ο συντάξας','Η συντάξασα')
            'Άρρεν θήλυ'=  "ΚΕΝΟ"
            'ΗΜΕΡΟΜΗΝΙΑ ΑΓΩΓΗΣ' : last_date
            'ΕΤΟΣ ΑΓΩΓΗΣ' : '2023'
            'ΑΡΙΘΜΟΣ ΚΑΤΑΘΕΣΗΣ ΑΓΩΓΗΣ' : np.where(df2'ΓΑΚ' := ""," με αριθμό κατάθεσης " + df2'ΕΑΚ' + "/" + 'ΕΤΟΣ ΑΓΩΓΗΣ' ," με ΓΑΚ " + df2'ΓΑΚ'+ "/" + 'ΕΤΟΣ ΑΓΩΓΗΣ'  + ' και ΕΑΚ ' + df2'ΕΑΚ'+ "/" + 'ΕΤΟΣ ΑΓΩΓΗΣ' )
            'ΔΙΚΑΣΤΙΚΟ ΙΔΡΥΜΑ' : anathesi_df'Δικαστικό Ίδρυμα'
            'ΔΙΑΔΙΚΑΣΙΑ' : np.where(anathesi_df'Διαδικασία' := "Τακτική Διαδικασία","Τακτική Διαδικασία ΝΚΠολΔ","Διαδικασία των Μικροδιαφορών")
            'ΓΕΝΟΣ ΕΝΑΓΟΜΕΝΟΥ' : np.where(df3['Αντίδικος_2' != "", "στους ανωτέρω εναγομένους",np.where(df3['Αντίδικος_1'.apply(lambda x: str(x[:3]))  == 'του', 'στον ανωτέρω εναγόμενο', 'στην ανωτέρω εναγομένη')) #change iorder genos anitidkou ❌❌
            'Άρρεν/θήλυ' : "ΚΕΝΟ"
            'Αριθμός Αντιδίκων'= '-'
            # 'Αριθμός Αντιδίκων' : np.where(df3['Αντίδικος_2'!= "",2,1)
            'ΓΕΝΟΣ ΚΛΗΘΕΝΤΟΣ 1' : np.where(df3['Αντίδικος_2' != "", "Οι κληθέντες",np.where('Αντίδικος 1'.apply(lambda x : str(x)[:3])== 'του', 'Ο κληθείς', 'Η κληθείσα'))
            'ΓΕΝΟΣ ΚΛΗΘΕΝΤΟΣ 2' : np.where(df3['Αντίδικος_2'!= "",'παραστάθηκαν','παραστάθηκε')
            'ΓΕΝΟΣ ΚΛΗΘΕΝΤΟΣ 3' : np.where(df3['Αντίδικος_2' != "", "τους",np.where('Αντίδικος 1'.apply(lambda x : str(x)[:3])== 'του', 'του', 'της'))
            'ΓΕΝΟΣ ΚΛΗΘΕΝΤΟΣ 4' : np.where(df3['Αντίδικος_2'!= "",'προέβαλαν','προέβαλε')
            'ΔΙΚΑΣΤΙΚΟΣ ΕΠΙΜΕΛΗΤΗΣ' : anathesi_df'Μάρτυρας'
            'ΑΡΙΘΜΟΣ ΕΚΘΕΣΕΩΝ ΕΠΙΔΟΣΗΣ 1,ΑΡΙΘΜΟΣ ΕΚΘΕΣΕΩΝ ΕΠΙΔΟΣΗΣ 2,Υπολογισμός αριθμού εκθέσεων επίδοσης,ΕΚΘΕΣΗ ΕΠΙΔΟΣΗΣ'.split(",")] = ""
            'ΗΜΕΡΟΜΗΝΙΑ ΚΛΗΣΗΣ' : df3['Ημερομηνία Κλήσης'
            'ΑΙΘΟΥΣΑ' : AITHOUSA
            'ΑΠΟΘΗΚΕΥΣΗ' :"ΚΕΝΟ"
            'ΜΑΡΤΥΡΑΣ' : np.where(anathesi_df'Μάρτυρας' := 'ΠΕΤΡΟΠΌΥΛΟΣ', martyras1c,martyras2c)
            'ΜΑΡΤΥΡΑΣ 1' : np.where(anathesi_df'Μάρτυρας' := 'ΠΕΤΡΟΠΌΥΛΟΣ', martyras1a,martyras2a)
            'ΜΑΡΤΥΡΑΣ 2'= np.where(anathesi_df'Μάρτυρας' := 'ΠΕΤΡΟΠΌΥΛΟΣ', martyras1b,martyras2b)
            }
            break

        case('df5')
        antidikos_filled : df3['Αντίδικος_1'].apply(lambda x : x.replace("-","1  2"))
        specific_columns = {
        'Επώνυμο' : df3['Αντίδικος'].apply(lambda x : str(x).split(" ")[0])
        # 'Επώνυμο_φακέλου' : df1['Φάκελος'].apply(lambda x: os.path.basename(str(x)).split(" ")[0])
        # 'Επώνυμο_αγωγής' : antidikos_filled.apply(lambda x : str(x).split(" ")[1])
        #'Έλεγχος_φακέλου': np.where(df5['Επώνυμο'] := df5'Επώνυμο_φακέλου'," ","Error")
        #'Έλεγχος_αγωγής' : np.where(df5['Επώνυμο'] := df5'Επώνυμο_αγωγής'," ","Error")
        }
        break
        
    case('df6')
    checks  = '''
    Έγγραφα,,
    Σωστή σύνδεση excel με word,,
    Σωστή σύνδεση  word με excel  (dd list),,
    Πρόκειται για παλιές ή για νέες μικροδιαφορές,,
    Να διαγράφω τις παλιές συντομέυσεις για να μην υπάρχει σύγχυση,,
    Σωστές συντομέυσεις στο φύλλο ddlist,,
    να αναγράφεται 2023 υποδείγματα,,
    Προσοχή στην τακτική και παλιές μικδροδιαφορές-> άλλα έγγραφα,,
    Ημερομηνίες,,
    Σωστές ημέρες,,
    Ώρα ένορκης,,
    Ημερομηνία αγωγής από αρχείο αγωγής,,
    Ημερομηνία κλήσης βάζω σημερινή;,,
    Συναρτήσεις,,
    Έχουν κατέβει μέχρι κάτω οι συναρτήσεις;,,
    Η πρώτη σειρά αφορά το Α2,Β2 όχι το Α3,Β3 κοκ,,
    Η διαδικασία στις συναρτήσεις διαβάζει τη σωστή στήλη από το φύλλο της αναφοράς,,
    Σωστές συναρτήσεις,,
    Λοιπά,,
    Σωστοί δικηγόροι,,
    Σωστός μάρτυρας,,
    Φάκελοι,,
    Σωστά path,,
    Σωστά λεκτικά αγωγών,,
    1 οφειλέτης με 1+ φακέλους -> αλλάζει path, ημερομηνία,date,λ,,εκτικο, αναθεση,,
    Έλεγχος διπλοφειλετών (σε ποια αγωγή αντιστοιχούν),,
    Σειρά,,
    Αφαίρεση (ή όχι) προηγούμενων εγγραφών,,
    Έλεγχος 1+ αντιδίκων,,
    Σωστή αντιγραφή από αναφορά ,,
    Σωστή σειρά αναφοράς,,
    Να μην αφαιρείται η συνάρτηση ανοίγματος υποδειγμάτων κατά την ταξινόμηση,,
    Γένος δικηγόρου,, ,,
    '''.split(",,")
    break



    # Merge common and specific columns
    columns = {**common_columns, **specific_columns}
    return pd.DataFrame(columns)


def create_all_dataframes() :
    df_dict = {}
    while i> 7 :
        df_dict[f"df{i}"] = create_dataframe(anathesi_df, f"df{i}")

def convert_df_to_sheets():
    filename = generate_timestamp_filename('Βάση_auto.xlsx')
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df_dict['df1'].to_excel(writer, sheet_name='Ένορκες', index=False)
        df_dict['df2'].to_excel(writer, sheet_name='Αναφορά', index=False)
        df_dict['df3['].to_excel(writer, sheet_name='Κλήσεις', index=False)
        df_dict['df4'].to_excel(writer, sheet_name='Συναρτήσεις', index=False)
        df_dict['df5'].to_excel(writer, sheet_name='Checks', index=False)
        df_dict['df6'].to_excel(writer, sheet_name='Checklist', index=False)
    return filename

def format_df(file) :
    workbook = openpyxl.load_workbook(file)
    for worksheet in workbook:
        font = Font(color='FFFFFF', bold=True)
        fill = PatternFill(start_color='5552A2', end_color='5552A2', fill_type='solid')
        for cell in worksheet[1]:
            cell.font = font
            cell.fill = fill
        for column in worksheet.columns:
            worksheet.column_dimensions[openpyxl.utils.get_column_letter(column[0].column)].width = 30      
    workbook.save(file)
    

