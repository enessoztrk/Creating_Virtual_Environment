    # Creating a Virtual Environment #

###############################################
# Create a virtual environment with your own name and do the following.
###############################################

###############################################
# Task 1: Create a virtual environment under your own name, install Python 3 during creation.
###############################################

# conda create -n Enes python=3

###############################################
# Task 2: Activate the environment you created.
###############################################

# conda activate Enes

###############################################
# Task 3: List the installed packages.
###############################################

# conda list

###############################################
# Task 4: Download the current version of Numpy and version 1.2.1 of Pandas into Environment at the same time.
###############################################

# conda install numpy pandas=1.2.1

###############################################
# Task 5: What is the version of the downloaded Numpy?
###############################################

# conda list

###############################################
# Task 6: Upgrade Pandas. What is the new version?
###############################################

# conda upgrade pandas
# conda list

###############################################
# Task 7: Delete Numpy from environment.
###############################################

# conda remove numpy

###############################################
# Task 8: Download the Seaborn library and the Matplotlib library with their current versions at the same time.
###############################################

# conda install seaborn matplotlib

###############################################
# Task 9: Export the libraries in the virtual environment with the version information and examine the yaml file.
###############################################

# conda env export > environment.yaml

###############################################
# Task 10: The environment you created is deleted.
###############################################
# Deactivate environment first.

# conda deactivate
# conda env remove -n Enes