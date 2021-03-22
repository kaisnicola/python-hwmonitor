# SQL-Code ausführen, Parameter: Datenbank (die Verbindung), und der SQL-Befehl
def executeSQL(db, sql, dictionary=True):

        # Cursor setzen und Daten als Dictionary speichern, außer die Variabe wurde auf "FALSE" gesetzt
        if dictionary == True:
            cursor = db.cursor(dictionary=True)
        else:
            cursor = db.cursor()
        # SQL-Befehl ausführen
        cursor.execute(sql)
        # Daten abrufen
        data = cursor.fetchone()
        return data
