
from flask import Flask, render_template, request, jsonify
from query_manager import query1
from query_manager import query2
from query_manager import query3
from query_manager import query4
from query_manager import query5
from query_manager import query6
from query_manager import query7


app = Flask(__name__)



@app.route('/')
def hello():
    return render_template('/index.html', test="uueueueue")



@app.route('/query1', methods=['POST'])
def handle_query1():
    nuovo_oggetto = {}

    nuovo_oggetto["id"] = int(request.form.get('id'))
    nuovo_oggetto["track_name"] = request.form.get('track_name')
    nuovo_oggetto["size_bytes"] = int(request.form.get('size_bytes'))
    nuovo_oggetto["currency"] = request.form.get('currency')
    nuovo_oggetto["price"] = float(request.form.get('price'))
    nuovo_oggetto["rating_count_tot"] = int(request.form.get('rating_count_tot'))
    nuovo_oggetto["rating_count_ver"] = int(request.form.get('rating_count_ver'))
    nuovo_oggetto["user_rating"] = float(request.form.get('user_rating'))
    nuovo_oggetto["user_rating_ver"] = float(request.form.get('user_rating_ver'))
    nuovo_oggetto["ver"] = request.form.get('ver')
    nuovo_oggetto["cont_rating"] = request.form.get('cont_rating')
    nuovo_oggetto["prime_genre"] = request.form.get('prime_genre')
    nuovo_oggetto["sup_devices"] = {"num": int(request.form.get('sup_devices'))}
    nuovo_oggetto["ipadSc_urls"] = {"num": int(request.form.get('ipadSc_urls'))}
    nuovo_oggetto["lang"] = {"num": int(request.form.get('lang'))}
    nuovo_oggetto["vpp_lic"] = int(request.form.get('vpp_lic'))

    # Chiamata alla funzione query1 con i valori del form
    risultato=query1(nuovo_oggetto)

    return render_template('query1_result.html', oggetto=risultato)

@app.route('/query2', methods=['POST'])
def handle_query2():
    nuovo_prezzo = {
        "price": float(request.form.get('price'))
    }

    risultati = query2(nuovo_prezzo)

    return render_template('query_result.html', prezzo=nuovo_prezzo["price"], risultati=risultati)


@app.route('/query3', methods=['POST'])
def handle_query3():
    nome_oggetto = request.form['nome_oggetto']
    nuovo_prezzo = request.form['nuovo_prezzo']
    
    risultato=query3(nome_oggetto,nuovo_prezzo)

    return render_template('query3_result.html', oggetto=risultato)


@app.route('/query4', methods=['GET', 'POST'])
def handle_query4():
    if request.method == 'POST':
        prezzo = request.form['prezzo']
        valutazione = request.form['valutazione']
        
        risultati = query4(prezzo, valutazione)

        return render_template('query4_result.html', oggetto=risultati)




@app.route('/query5', methods=['GET', 'POST'])
def handle_query5():
    if request.method == 'POST':
        id_oggetto = request.form['id_oggetto']
        
        query5(id_oggetto)

    return render_template('form.html')



@app.route('/query6', methods=['GET', 'POST'])
def handle_query6():
    if request.method == 'POST':
        genere = request.form['genere']
        versione = request.form['versione']
        valutazione = request.form['valutazione']
        
        risultati = query6(genere, versione, valutazione)

        return render_template('query6_result.html', oggetto=risultati)
    


@app.route('/query7', methods=['GET', 'POST'])
def query7_form():
    if request.method == 'POST':
        id_oggetto = request.form['id_oggetto']
        nuovo_nome = request.form['nuovo_nome']
        nuovo_prezzo = request.form['nuovo_prezzo']
        nuova_valutazione = request.form['nuova_valutazione']
        
        oggetti_modificati = query7(id_oggetto, nuovo_nome, nuovo_prezzo, nuova_valutazione)
        
        return render_template('risultati_query7.html', oggetto=oggetti_modificati)
    
   

    

app.run(port=5005)




