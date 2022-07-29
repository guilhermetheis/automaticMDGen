
"""
This code is meant to create markdown files for future automation of github pages specifically

Author: Guilherme Theis
"""

import os    # standard library
import sys

from mdutils.mdutils import MdUtils # remember that this is how to import it properly

from datetime import datetime #to get name of the file based on YYYY-MM-DD

date = datetime.today().strftime('%Y-%m-%d')
fileExtension = '-TitlePlaceHolder'
myFileName = date + fileExtension

mdFile = MdUtils(file_name=myFileName, title='Markdown File Example')
mdFile.create_md_file()