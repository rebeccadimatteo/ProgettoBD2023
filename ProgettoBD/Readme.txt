TECNLOGIE UTILIZZATE
Questo progetto è stato sviluppato per l'esame di basi dati II utilizza le seguente tecnologie:
flask-2.1.3
pymongo-4.1.1

RACCOLTA REQUISITI
Sono state sviluppate delle query su un dataset denominato Applestore che contiene  
diverse caratteristiche sulle app apple.


CARATTERISTICHE APP:

id:281796108
track_name:"Evernote - stay organized"
size_bytes:158578688
currency:"USD"
price:"400"
rating_count_tot:161065
rating_count_ver:26
user_rating:4
user_rating_ver:3.5
ver:"8.2.2"
cont_rating:"4+"
prime_genre:"Productivity"
sup_devices:Object
ipadSc_urls:Object
lang Object vpp_lic :1


QUERY SVILUPPATE
Sono state sviluppate 7 query

1 inserimento di una nuova app nel database

2 proiezione delle app che hanno un prezzo scelto dall'utente

3 modifica del prezzo  di un app scelto dall'utente in base al nome, ed  il relativo prezzo

4 che rappresentano le app con un determinato prezzo e valutazione chiesto all'utente

5 chiede all'utente id dell'app che vuole cancallare

6 che rappresenta l'app che hanno genere, versione e valutazione scelta dall'utente

7 modifica nome, valutazione e prezzo di un app con un determinato id 