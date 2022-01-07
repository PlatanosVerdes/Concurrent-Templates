import threading            # Generar threads
import random               # Generar valores aleatorios
from random import randint  
from time import sleep      # Sleep/Delay

# Constantes 
NUM_THREADS = 5


class Process(threading.Thread):

    thread_id = 0
    
    def __init__(self, num_thread):
        super().__init__()
        self.thread_id = num_thread

    def run(self):
        print(f"Soy el Thread-{self.thread_id}")


def main():
    threads = []

    # Cargamos todos los threads en un array
    for i in range(NUM_THREADS):
        threads.append(Process(i))

    random.shuffle(threads) # Asi evitamos un posible orden en caso que nuestros threads tengan caracteristicas diferentes

    # Ejecutamos todos los threads
    for thread in threads:
        thread.start()

    # Esperamos que acaben todos los threads
    for threads in threads:
        thread.join()

print("End")


if __name__ == "__main__":
    main()