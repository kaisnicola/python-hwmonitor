# Maik Günes - BS-FISI-01 - LF5

# Python-Monitor
# Zeigt die aktuellen Werte des RAMs, der CPU und die minimal- und maximalwerte an.

# Module importieren
import csv
import psutil
import mysql.connector
import sys
import os
import time
from monitorfunctions import executeSQL

# Befehlszeile leeren (Windows)
os.system('cls')

# Datenbankverbindung - Zugangsdaten
datenbank = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hwmonitor"
)

# Update-Intervall (Sekunden)
interval = 2

# Geräte-ID, die abgerufen werden soll
deviceID = input("Geräte-ID eingeben: ")

# Befehlszeile leeren (Windows)
os.system('cls')

try:
    while True:

        current = executeSQL(datenbank, "SELECT * FROM monitor WHERE deviceid = " + deviceID + " ORDER by timestamp DESC LIMIT 1")
        maxcpu = executeSQL(datenbank, "SELECT MAX(cpu) FROM monitor WHERE deviceid = " + deviceID, False)
        maxram = executeSQL(datenbank, "SELECT MAX(ram) FROM monitor WHERE deviceid = " + deviceID, False)
        mincpu = executeSQL(datenbank, "SELECT MIN(cpu) FROM monitor WHERE deviceid = " + deviceID, False)
        minram = executeSQL(datenbank, "SELECT MIN(ram) FROM monitor WHERE deviceid = " + deviceID, False)

        print("")
        print("")
        print("Aktuell: \n CPU: " + str(current['cpu']) + " \n RAM: " + str(current['ram']))
        print("Maximalwert: \n CPU: " + str(maxcpu[0]) + " \n RAM: " + str(maxram[0]))
        print("Minimalwert: \n CPU: " + str(mincpu[0]) + " \n RAM: " + str(minram[0]))
        print("")
        print("")
        
        # Intervall
        time.sleep(interval)
        os.system('cls')
            
except KeyboardInterrupt: 
   # Skript beenden
   print("Überwachung beendet")
   sys.exit(0)
