# Primero voy a tratar de abrir un audio 
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import seaborn as sns
from FFT import fft, ifft

# El requisito es que el archivo de audio tenga una
# cantidad de puntos que sea una potencia de 2
# para lograr la recursividad:
def audio_potencia(a):
    # Cuantas veces cabe el dos, ahora solo debemos redondear hacia abajo
    # Potencia de dos más cercana:
    nearest_power = int(2**np.ceil(np.log2(len(a))))
    if len(a) == nearest_power: return a
    # Lafunción np.pad es para agregar numeros
    # a la izquierda o deracha deu un array
    # (0, nearest_power - len(a)) esto quiere decir que no se agrega
    # a la izquierda, pero si a la derecha
    # constant por default es 0
    return np.pad(a, (0, nearest_power - len(a)), 'constant')
# Primero vamos a leer el archivo
path = "audio_prueba.wav"
try:
    # Tratamos de leer el archiv wav  
    rate, data = wavfile.read(path)
    # debemso ver si tiene dos o un canal:
    if len(data.shape) > 1:
        audio_data = data[:, 0]
    else:
        # Si ya es monoide xd
        audio_data = data

    #Debemos convertir a flotante para tener la maxima precisión
    # El tipo de dato maximo que soporta el tipo de dato actual que es el audio
    # np.iinfo(audio_data.dtyp_audie).max
    OG_DATATYPE = audio_data.dtype
    MAX_INT = np.iinfo(audio_data.dtype).max
    audio_data = audio_data.astype(np.float32) / MAX_INT
    # Esto nomas es pa verlo
    #sns.lineplot(audio_data)
    #plt.show()
    audio_data = audio_potencia(audio_data)

    # El algoritmo funciona con listas de python
    # entonces casteamos:
    print("Señal original:", audio_data[5:11])
    audio_fft = fft(audio_data.tolist())
    print("Señal transformada:", audio_fft[5:11])
    ifft_result = ifft(audio_fft)
    print("Señal reconstruida:", ifft_result[5:11])
    print(len(audio_data), len(audio_fft), len(ifft_result))
    #wavfile.write("XD.wav", 44100 ,np.array(ifft_result))

    # AHORA como sabemos que justamente quedan residuos de 
    # numeros complejos solamente tomamos la parte REAL
    # que es la que da el audio:
    audio_reconstruido = np.array(ifft_result).real
    # Ahora debemos regresar a las aplitudes originales
    # COmo antes dividimos ahora multiplicamos para recuperer
    # el volumen por así decirlo
    audio_reconstruido *= MAX_INT
    # AHora debo guardar el tipo de dato correcto en el
    # formato que tiene WAV que es int16
    audio_reconstruido = audio_reconstruido.astype(OG_DATATYPE)
    wavfile.write("./AUDIO_RECONSTRUIDO.wav", rate, audio_reconstruido)
except FileNotFoundError:
    print(f"No existe el archivo xd")
