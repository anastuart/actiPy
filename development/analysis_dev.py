import pathlib
import sys
import matplotlib.pyplot as plt
sys.path.insert(0, "/Users/angusfisk/Documents/01_PhD_files/"
                   "07_python_package/actigraphy_analysis")
import actigraphy_analysis.preprocessing as prep
import actigraphy_analysis.actogram_plot as act
import actigraphy_analysis.analysis as actan

# read the first file in from the input directory
# into a dataframe then apply split function to
# it then try and use actogram plotting
input_dir = pathlib.Path("/Users/angusfisk/Documents/01_PhD_files/"
                         "01_Projects/P2_Circ_Disruption_paper_chapt2"
                         "/03_data_files")
file_name = list(input_dir.glob("*.csv"))[0]
data = prep.read_file_to_df(file_name)
data_baseline = prep.separate_by_condition(data)[0]
data_clean = prep.remove_object_col(data_baseline)


