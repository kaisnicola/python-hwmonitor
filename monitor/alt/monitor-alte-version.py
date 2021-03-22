# Module importieren
import csv
import psutil
import mysql.connector
import sys
import os
import time

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
        
        cursor0 = datenbank.cursor(dictionary=True)
        sql0 = "SELECT * FROM monitor WHERE deviceid = " + deviceID + " ORDER by timestamp DESC LIMIT 1"
        cursor0.execute(sql0)
        current = cursor0.fetchone()

        cursor1 = datenbank.cursor()
        sql1 = "SELECT MAX(cpu) FROM monitor WHERE deviceid = " + deviceID
        cursor1.execute(sql1)
        maxcpu = cursor1.fetchone()
        
        cursor2 = datenbank.cursor()
        sql2 = "SELECT MAX(ram) FROM monitor WHERE deviceid = " + deviceID
        cursor2.execute(sql2)
        maxram = cursor2.fetchone()

        cursor3 = datenbank.cursor()
        sql3 = "SELECT MIN(cpu) FROM monitor WHERE deviceid = " + deviceID
        cursor3.execute(sql3)
        mincpu = cursor3.fetchone()

        cursor4 = datenbank.cursor()
        sql4 = "SELECT MIN(ram) FROM monitor WHERE deviceid = " + deviceID
        cursor4.execute(sql4)
        minram = cursor4.fetchone()

        
        

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
