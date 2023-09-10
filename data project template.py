######################################################################################################################################################
################################################################    Control Panel    #################################################################
project_name = 'project name'
file_name = f'{project_name}'
file_save_path = f'\Desktop\{project_name}'

######    Functions   ######
# Full dataset
save_dataset_to_csv = True
save_dataset_to_json = False

# Error log
save_error_log = True

################################################################    Control Panel    #################################################################
######################################################################################################################################################

import os
import time
import pandas as pd


###################################################################    Metadata    ###################################################################53
print()
# Times calculated to have control log of the script
script_start_time = time.time() 
script_start_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("="*12,f"Project {project_name} | Script started {script_start_timestamp}","="*12,"\n")

# Checks the file directory and creates it dosnt exist
file_save_path = os.path.expanduser(f"~{file_save_path}")
os.makedirs(file_save_path, exist_ok=True)

sample_dataset = pd.DataFrame()
error_log = []

####################################################################    Functions    ###################################################################
def df_size(dataframe_name):
    """Calculates and formats the size of a dataframe (rows, columns)."""
    rows = dataframe_name.shape[0]
    columns = dataframe_name.shape[1]
    return f'{rows} rows, {columns} columns.'


# <==============   code   ===================>


#legend print for loops with error handeling.
#print(f'<loop> extraction finished    |    {len(set(extracted_list))} successful extractions.    |    {len(set(failed_list))} failed extractions.    |    dataset size: {df_size(sample_dataset)}')


########################################################    Output the data to CSV files    ##########################################################
file_save_path = f'{file_save_path}\{file_name}'

if save_dataset_to_csv:
    #  Output the full dataset into a csv file
    sample_dataset.to_csv(f'{file_save_path}.csv', header=True, index=False)
    
if save_dataset_to_csv:
    print(f"CSV file saved to {file_save_path}")
    if save_error_log: 
        error_log.to_csv(f'{file_save_path} - error log.csv', header=True, index=False)


########################################################    Output the data to JSON files    ######################################################## 
if save_dataset_to_json:
    #  Output the full dataset into a csv file
    sample_dataset.to_json(f'{file_save_path}.json', orient='records', lines=True)
    
if save_dataset_to_json:
    print(f"JSON file saved to {file_save_path}")
    if save_error_log: 
        error_log.to_json(f'{file_save_path} - error log.json', orient='records', lines=True)
        
        

###################################################################    Metadata    ###################################################################
# Record the end time to calculate and format the elapsed time
script_end_time = time.time()
script_end_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
script_elapsed_time = time.strftime("%H:%M:%S", time.gmtime(script_end_time - script_start_time))

# Checks if the project folder exists, is a folder, and if it is still in use, if not, deletes it.
if os.path.exists(file_save_path) and os.path.isdir(file_save_path) and not os.listdir(file_save_path):
    os.rmdir(file_save_path)
    
# Time check
print("="*10,f"{sample_dataset.shape[0]} rows, {sample_dataset.shape[1]} columns in {script_elapsed_time} | Script ended on {script_end_timestamp}","="*10,"\n")