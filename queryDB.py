import queryFileSize
import os
try:
    queryFileSize.view(os.getenv("muneeb"))
except:
    print("That file is not in the database")