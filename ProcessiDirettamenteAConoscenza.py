import os #Il modulo fornisce funzionalità per interagire con il sistema operativo
from multiprocessing import Process,current_process,Pipe

def process_id():
    #stampa proprietà del processo
    print(f"Server PID: {os.getpid()}, Process Name: {current_process().name}, Process PID: {current_process().pid}")

def process_function(conn):
    process_id()
    print("Elabora il dato ricevuto ed invio il risultato")
    data_received=conn.recv() #riceve dati dalla conessione
    result=data_received*2
    conn.send(result) #invia i dati della conessione
    conn.close() #chiude la conessione

if __name__=="__main__":
    process_id()
    print("Creo una conessione e un processo figlio")
    parent_conn, child_conn = Pipe() #creazione di un pipe per la comunicazione
    data=5
    p=Process(target=process_function, args=(child_conn,)) #crea un nuovo processo
    p.start() #avvio del processo figlio
    parent_conn.send(data)  #invia il dato al processo figlio tramite la pipe
    result=parent_conn.recv() #riceve risultato del processo figlio
    p.join()
    process_id()
    print("Stampo il risultato ricevuto")
    print(result)