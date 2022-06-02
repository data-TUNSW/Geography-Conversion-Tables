from pathlib import Path

### Current script and project directories
script_dir = Path( __file__ ).parent.absolute().as_posix()
project_dir = (Path(script_dir).parent.absolute()).as_posix()

### Data directories
base_data_dir = (Path(project_dir).parents[1].absolute()).as_posix() + '/ABS/Geography'
raw_data_dir = base_data_dir + '/raw/'
processed_data_dir = base_data_dir + '/processed/'

geo_codes = ['POA', 'LGA', 'SA4', 'SED', 'CED', 'GCCSA', 'RA']
geo_names = {'POA': 'Postcode', 'LGA': 'LGA', 'SA4': 'SA4', 'RA': 'Remoteness Area',
    'SED': 'State Electorate', 'CED': 'Commonwealth Electorate', 'GCCSA': 'GCCSA'}

raw_data_file_CA = raw_data_dir + 'CA_POSTCODE_2018_LGA_2018.xlsx'
raw_data_file_lprw = raw_data_dir + 'POA_LGA_Rented_2016.xlsx'
geography_weightings = {'POA': {'LGA': raw_data_dir + 'POA_LGA_Rented_2016.xlsx',
    'SA4': raw_data_dir + 'POA_SA4_Rented_2016.xlsx',
    'CED': raw_data_dir + 'POA_CED_Rented_2016.xlsx',
    'SED': raw_data_dir + 'POA_SED_Rented_2016.xlsx',
    'GCCSA': raw_data_dir + 'POA_GCCSA_Rented_2016.xlsx',
    'RA': raw_data_dir + 'POA_RA_Rented_2016.xlsx'}
    }

geography_updates = {'LGA': {'2016-2021': raw_data_dir + 'CG_LGA_2016_LGA_2021.csv'},
    'POA': {'2016-2021': raw_data_dir + 'CG_POA_2016_POA_2021.csv'},
    'SA4': {'2016-2021': raw_data_dir + 'CG_SA4_2016_SA4_2021.csv'},
    'CED': {'2016-2021': raw_data_dir + 'CG_CED_2016_CED_2021.csv'},
    'SED': {'2016-2021': raw_data_dir + 'CG_SED_2016_SED_2021.csv'},
    'GCCSA': {'2016-2021': raw_data_dir + 'CG_GCCSA_2016_GCCSA_2021.csv'}
    }

read_options_CA = {'sheet_name': "Table 3", 'skiprows': [0, 1, 2, 3, 4, 6], 'skipfooter': 6, 'usecols': 'A,C:E'}
read_options_lprw = {'index_col': 1, 'skipfooter': 7, 'skiprows': [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]}

new_col_names = {'POSTCODE_2018': 'Postcode', 'LGA_CODE_2018': 'LGA Code', 'LGA_NAME_2018': 'LGA', 'RATIO': 'Ratio'}