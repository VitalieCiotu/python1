import os #Il modulo fornisce funzionalità per interagire con il sistema operativo
from multiprocessing import ProcessError, Queue, Process, current_process


def process_id():
    #stampa proprietà del processo
    print(f"Server PID: {os.getpid()}, Process Name: { current_process().name}, Process PID: {current_process().pid}")

def process_function(data, result_queue):
    process_id()
    print("Elabora: ",data)
    result=data*2
    result_queue.put(result) #viene messo il risultato in coda
    
if __name__=="__main__":
    data_list=[1,2,3,4]
    result_queue=Queue() #creazione coda
    processes=[]

    for data in data_list:
        p=Process(target=process_function, args=(data, result_queue)) #creazione processo
        processes.append(p)
        p.start()

    for z in processes:
        z.join()

    print("Il main stampa i risultati")
    while not result_queue.empty(): #controllo sulla coda
        result=result_queue.get()
        print(result) 