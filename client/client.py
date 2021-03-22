# Module importieren
import csv
import psutil
import mysql.connector
import sys
import time

# GeräteID festlegen
deviceID = 1

# Intervall in dem die Daten übertragen werden (Sekunden)
interval = 2

# Datenbankverbindung - Zugangsdaten
datenbank = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hwmonitor"
)

print("Hintergrund-Monitoring der CPU- und RAM-Werte gestartet...")
print("Ctrl+C zum Beenden")

try:
    while True:            
        # Zeit und Auslastung ermitteln
        cpu = psutil.cpu_percent(1)
        ram = psutil.virtual_memory().percent

        # Cursor erstellen
        cursor = datenbank.cursor()

        # SQL-Befehl zum Einfügen in die Datenbank
        sql = "INSERT INTO monitor (deviceID, cpu, ram) VALUES (%s, %s, %s)"
        val = (deviceID, cpu, ram)

        # Ausführen
        cursor.execute(sql, val)
        datenbank.commit()
    
        # Intervall
        time.sleep(interval)
            
except KeyboardInterrupt: 
   # Skript beenden
   print("Monitoring beendet")
   sys.exit(0)
