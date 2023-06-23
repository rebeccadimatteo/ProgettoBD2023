from bson import ObjectId
from pymongo import MongoClient
import pymongo


# Configura la connessione a MongoDB
client = MongoClient('mongodb://localhost:27017')  # Sostituisci con l'indirizzo del tuo database
database = client['Bd2Store']  # Sostituisci con il nome del tuo database
collection= database['AppleStore']  # Sostituisci con il nome della tua collezione



# query 1: inserimento di una nuova app nel database
def query1(nuovo_oggetto):
    collection.insert_one(nuovo_oggetto)
    oggetto_inserito = collection.find_one({"id": nuovo_oggetto["id"]})

    return oggetto_inserito



# query 2: proiezione delle app che hanno un prezzo scelto dall'utente
def query2(nuovo_prezzo):
    risultati = collection.find(
        {"price": {"$lte": nuovo_prezzo["price"]}},
        {'track_name': 1, 'size_bytes': 1, 'currency': 1, 'price': 1}
    ).sort('price', -1).limit(3)

   # Crea una lista per i risultati
    risultati_lista = []

    # Aggiungi i risultati alla lista
    for risultato in risultati:
        risultati_lista.append(risultato)

    return risultati_lista

 



#query 3 modifica del prezzo  di un app scelta dall'utente in base al nome, ed  il relativo prezzo
def query3(nome_oggetto,nuovo_prezzo):
    # Chiedi all'utente il nome dell'oggetto e il nuovo prezzo
    # Esegui la query di aggiornamento
    risultati = collection.update_many(
        {'track_name': nome_oggetto},
        {'$set': {'price': nuovo_prezzo}}
    )
     # Verifica se ci sono documenti modificati
    documenti_modificati = risultati.modified_count

    if documenti_modificati > 0:
        # Recupera gli oggetti modificati dalla collezione
        oggetti_modificati = collection.find({'track_name': nome_oggetto})

        # Restituisci la lista degli oggetti modificati
        return list(oggetti_modificati)
    else:
        return []
    
    
    




        
 # query4 che rappresenta un app con un determinato prezzo e valutazione chiesto all'utente
def query4(prezzo,valutazione):
    # Crea la query per filtrare gli oggetti
    query = {
        "price": prezzo,
        "user_rating": valutazione
    }

    # Esegui la query sul database MongoDB
    risultati = collection.find(query)

    # Restituisci i risultati come lista di oggetti
    return list(risultati)




#query5 chiede all'utente id dell'app che vuole cancallare
def query5(id_oggetto):

    # Crea la query per la cancellazione dell'oggetto
    query = {
        "_id": ObjectId(id_oggetto)
    }

    # Esegui la query di cancellazione sul database MongoDB
    risultato = collection.delete_one(query)

   





#query6 che rappresenta le app che hanno genere, versione e valutazione scelta dall'utente
def query6(genere,versione,valutazione):
   
    # Crea la query per filtrare gli oggetti
    query = {
        "prime_genre": genere,
        "ver": versione,
        "user_rating": valutazione
    }

    # Esegui la query sul database MongoDB
    risultati = collection.find(query)

    # Restituisci i risultati come lista di oggetti
    return list(risultati)





#query7 modifica nome, valutazione e prezzo dell'app con un determinato id 

def query7(id_oggetto,nuovo_nome,nuovo_prezzo,nuova_valutazione):
        # Crea la query di aggiornamento
        query = {"_id": ObjectId(id_oggetto)}
        update = {"$set": {"track_name": nuovo_nome, "price": nuovo_prezzo, "user_rating": nuova_valutazione}}

        # Esegui la query di aggiornamento nel database MongoDB
        risultato = collection.update_one(query, update)
     
        oggetti_modificati = collection.find(query)
        
        # Restituisci la lista degli oggetti modificati
        return list(oggetti_modificati)
        

        


