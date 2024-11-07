from pathlib import Path

### Current script and project directories
script_dir = Path( __file__ ).parent.absolute().as_posix()
project_dir = (Path(script_dir).parent.absolute()).as_posix()

### Data directories
base_data_dir = (Path(project_dir).parents[1].absolute()).as_posix() + '/ABS/Geography'
raw_data_dir = base_data_dir + '/raw/'
processed_data_dir = base_data_dir + '/processed/'

raw_data_file_CA = raw_data_dir + 'CA_POSTCODE_2018_LGA_2018.xlsx'
raw_data_file_lprw = raw_data_dir + 'POA_LGA_Rented_2016.xlsx'
geography_transforms = {'LGA': {'2016-2021': raw_data_dir + 'CG_LGA_2016_LGA_2021.csv'},
    'POA': {'2016-2021': raw_data_dir + 'CG_POA_2016_POA_2021.csv'}}

read_options_CA = {'sheet_name': "Table 3", 'skiprows': [0, 1, 2, 3, 4, 6], 'skipfooter': 6, 'usecols': 'A,C:E'}
read_options_lprw = {'index_col': 1, 'skipfooter': 7, 'skiprows': [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]}

new_col_names = {'POSTCODE_2018': 'Postcode', 'LGA_CODE_2018': 'LGA Code', 'LGA_NAME_2018': 'LGA', 'RATIO': 'Ratio'}

### New file formats

raw_data_file_lga = raw_data_dir + 'POA2021_LGA2022_Rented.csv'
raw_data_file_sed = raw_data_dir + 'POA2021_SED2022_Rented.csv'

raw_lga_2021_2022 = raw_data_dir + 'CG_LGA_2021_LGA_2022.csv'
raw_lga_2016_2021 = raw_data_dir + 'CG_LGA_2016_LGA_2021.csv'

raw_sed_2021_2022 = raw_data_dir + 'CG_SED_2021_SED_2022.csv'
raw_sed_2016_2021 = raw_data_dir + 'CG_SED_2016_SED_2021.csv'