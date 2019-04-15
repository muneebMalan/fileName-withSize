import queryFileSizeTest
import os
try:
    queryFileSizeTest.view(os.getenv("muneeb"))
except:
    print("That file is not in the database")