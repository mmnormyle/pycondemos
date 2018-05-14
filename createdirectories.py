import os
from shutil import copy2
import os
import glob

basename = 'user'

with open("/home/revoscaler/Source/pycondemos/BeginHere_TextClassificationPython.ipynb", "r") as f:
    textdemo = f.read()

with open("/home/revoscaler/Source/pycondemos/Hospital_Length_Of_Stay_Notebook.ipynb", "r") as f:
    hlosdemo = f.read()
    

server_list = ["copyconvm1zyi56it3tx4xo.eastus.cloudapp.azure.com", "copyconvm2zyi56it3tx4xo.eastus.cloudapp.azure.com", "copyconvm3zyi56it3tx4xo.eastus.cloudapp.azure.com", "copyconvm6zyi56it3tx4xo.eastus.cloudapp.azure.com"]


for i in range(100):
    name = basename + str(i)
    dirname = os.path.join("/home", name)

    files = glob.glob(dirname + "/*")
    for f in files:
        if not os.path.isdir(f):
            os.remove(f)

    server = server_list[i % len(server_list)]
    uid = "MySqlUser"
    pwd = "MyInsecureSqlPassword"
    db = "TextClassification_Py"
    txtconnection = "Driver=ODBC Driver 17 for SQL Server;Server={};Database={};Uid={};Pwd={};".format(server, db, uid, pwd)
    db = "Hospital_Py"
    hlosconnection = "Driver=ODBC Driver 17 for SQL Server;Server={};Database={};Uid={};Pwd={};".format(server, db, uid, pwd)

    textmodeltable = "TextModel_" + name
    intermediate = "PredictionsIntermediate_" + name
    predictions = "Predictions_" + name
    modtextdemo = textdemo.replace("USER_MODEL_TABLE", textmodeltable).replace("USER_PREDICTIONS_IMMEDIATE_TABLE", intermediate).replace("USER_PREDICTIONS_TABLE", predictions)

    models_table = "Models_" + name
    modhlosdemo = hlosdemo.replace("USER_MODELS_TABLE", models_table)

    with open(os.path.join(dirname, "BeginHere_TextClassificationPython.ipynb"), "w") as f:
        f.write(modtextdemo)

    with open(os.path.join(dirname, "Hospital_Length_Of_Stay_Notebook.ipynb"), "w") as f:
        f.write(modhlosdemo)

    with open(os.path.join(dirname, "text_database_connection.txt"), "w") as f:
        f.write(txtconnection)

    with open(os.path.join(dirname, "hospital_database_connection.txt"), "w") as f:
        f.write(hlosconnection)
