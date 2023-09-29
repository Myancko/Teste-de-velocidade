import time
import random

def Generate_vector_10000():

    vector = []
    
    while True:

        r = random.randint(1, 100000)

        if r not in vector:

            vector.append(r)
        
        if len(vector) >= 10001:
            #print('.', len(vector))
            break

    return vector

if __name__ == "__main__":
    
    start_time = time.time()
    x = Generate_vector_10000()
    print(x)
    print("O vetor de 10000 elementos foi gerado em %s segundos" % (time.time() - start_time))