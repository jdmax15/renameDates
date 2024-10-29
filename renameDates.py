#! python3
# renameDates.py - Renames filenames with Maerican MM-DD-YYYY date format to European DD-MM-YYYY format.

import shutil, os, re
# Create a regex that matches files iwth the American date format.

datePattern = re.compile(r"""^(.*?)             # All text before the date
                         ((0|1?\d)-)            # One or two digits for the month
                         ((0|1|2|3)?\d)-        # One or two digits for the day
                         ((19|20)\d\d)          # Four digits for the year
                         (.*?)$                 # All text after the date
                         """, re.VERBOSE)

# Loop over the files in the working directory.

# Skip files without a date.

# Get the different parts of the filename.

# Form the European-style filename.

# Get the full, absolute file paths.

# Rename the files.