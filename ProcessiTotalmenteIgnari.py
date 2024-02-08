from multiprocessing import Process #Importo del processo dalla libreria per la creazione

def process_function(data):
    result = data * 2
    print(result)

if __name__ == "__main__": #Controlliamo di essere nel main
    data_list=[1 ,2 ,3 ,4]
    processes = []

    for data in data_list:
        p = Process(target=process_function, args=(data,)) #p crea processo con dati dalla lista
        processes.append(p)
        p.start() #Avvia l'esecuzione del processo separato

    for z in processes:
        z.join() #Blocca il processo proncipale fino a quando il processo separato non termina