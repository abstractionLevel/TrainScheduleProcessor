FLUSSO

1 - lettura csv (current,planned)
2 - prendere la destinazione dei treni
3 - Calcolo ritardo
    2a - current >  planned  = ritardo  (n)
    2b - current <  planned  = ritardo  (-n)
4 - sort list con il campo delay descrescente
5 - prendo i primi 5
6 - Scrittura csv (output) con colonna ritardo espresso in secondi


PROBLEMA: lettura csv
SOLUZIONE: (metodo:getListFromCsv)- per la lettura dei csv, ho usato la funzione open() che restituisce un oggetto di tipo file per passarla al metodo
reader del modulo csv che mi restituisce oggetto iterabile di tipo csv, il quale mi ha permesso di iterare attraverso le righe del file csv
==============
PROBLEMA: prendere la destinazione dei treni
SOLUZIONE: (metodo:getDestinationOfTrains) - sapendo che la destinazione di ogni treno si trova in ultima posizione in ordine cronologico, dalla lista originale mi sono preso per ogni
treno l' ultimo elemeneto
==============
PROBLEMA:Calcolo ritardo 
SOLUZIONE:(metodo:calculateDelay) - Per ciascuna riga nei due file (actual, planned), ho confrontato le stazioni e i numeri dei treni come criteri di corrispondenza poi
successivamente, ho convertito le date con gli orari in oggetti datetime utilizzando il metodo fromisoformat.
Ho eseguito un confronto tra gli orari effettivi (current) e quelli pianificati (planned), ho consculo che se ce un ritardo
significa che actual e' maggiore di planned quindi ho sottratto ad actual l' orario di planned (actual-planned) per prendere la differenza, se invece
e' in anticipo signifca che planned e' maggiore di actual quindi a planned ho sottratto l' orario di actual (planned-actual) per prendere la differenza ed aggiungere un - davanti.
===============
PROBLEMA:Visualizzare 5 treni che hanno un ritardo maggiore 
SOLUZIONE:(metodo:getTopNTrainsWithHighestDelays) - per ordinare la lista in ordine descrescente per il campo ritardo ho usato la funzione sorted() per poi prendere solo i primi 5 risulati.
===============
PROBLEMA:Scrittura csv 
SOLUZIONE:(metodo:writeCsv) - per la lettura dei csv, ho usato la funzione open() con il parametro 'w' (scrittura) e grazie al metodo writer del modulo csv gli ho passato la lista manipolata.
===================================================================

PYTHON: versione 3.12.1
ESECUZIONE SCRIPT: aprire il temrminale e posizionarsi nella cartella del test e digitare: python o python3 trainScheduleProcessor.py
ESECUZIONE TEST: aprire il temrminale e posizionarsi nella cartella del test e digitare: python o python3 test_trainScheduleProcessor.py
