from pymongo import MongoClient

# Configura la connessione a MongoDB
client = MongoClient('mongodb://localhost:27017')  # Sostituisci con l'indirizzo del tuo database

# Seleziona il database e la collezione
database = client['Bd2Store']  # Sostituisci con il nome del tuo database
collection= database['AppleStore']  # Sostituisci con il nome della tua collezione

# Recupera tutti i documenti nella collezione
documenti = collection.find()

# Stampa i documenti
for documento in documenti:
    print(documento)

# Chiudi la connessione a MongoDB
client.close()
