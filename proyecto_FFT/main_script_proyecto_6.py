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
    # print(len(audio_data))
    # quit()
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
    audio_reconstruido = (np.array(ifft_result)/len(audio_data)).real
    # Ahora debemos regresar a las aplitudes originales
    # COmo antes dividimos ahora multiplicamos para recuperer
    # el volumen por así decirlo
    audio_reconstruido *= MAX_INT
    # AHora debo guardar el tipo de dato correcto en el
    # formato que tiene WAV que es int16
    audio_reconstruido = audio_reconstruido.astype(OG_DATATYPE)
    wavfile.write("./AUDIO_RECONSTRUIDO.wav", rate, audio_reconstruido)

    # Ahora vamos a generar la grafica:
    # vamos a hacer la comparativa de antes, transofrmado y despues
    fig, axes = plt.subplots(3,1,figsize=(12, 10))
    # Para la grafica de la señal original
    tiempo = np.arange(len(audio_data))/rate
    axes[0].set_title("Audio original")
    axes[0].set_xlabel("Tiempo (s)")
    axes[0].set_xlabel("Amplitud (s)")
    axes[0].grid(True) 
    sns.lineplot(x=tiempo, y =audio_data*MAX_INT, ax=axes[0])

    # Para la grafica de las frecuencias
    # Aquí hay que hacer algunas cositas
    # primero debemos calcular que frecuencias tiene nuestra señal
    frecuencias = np.fft.fftfreq(len(audio_fft), 1/rate)
    # Misma señal original
    frecuencias_positivas = frecuencias[:len(audio_fft)//2]
    # Arreglo de las magnitudes, al sacarle valor asboluto 
    # a un complejo sacas su modulo:
    # cabe destacar que cuando aplicamos fft se ordenan 
    # en que el primer elemento es 0 hz y así
    magnitudes = np.abs(np.array(audio_fft[:len(audio_fft)//2]))

    sns.lineplot(x=frecuencias_positivas, y=magnitudes, ax=axes[1])

    axes[1].set_title('Espectro de amplitud de la FFT') # Cambia el título
    axes[1].set_xlabel('Frecuencia (Hz)')
    axes[1].set_ylabel('Potencia') # O 'Magnitud Cuadrada'
    axes[1].set_xlim(0, rate / 2)
    axes[1].grid(True)

    sns.lineplot(x=tiempo, y=audio_reconstruido, ax=axes[2])
    axes[2].set_title("Audio reconstruido")
    axes[2].set_xlabel("Tiempo (s)")
    axes[2].set_xlabel("Amplitud (s)")
    axes[2].grid(True)
    plt.subplots_adjust(hspace=0.5)
    plt.show()

    # Ahora vamos a modificar la señal
    frecuencia_corte = 2000
    # Mascara binaria de 1 y 0,
    filtro = (np.abs(frecuencias) <= 1000) & (500 <= np.abs(frecuencias)) 
    audio_fft_filtrado = audio_fft * filtro
    # Ahora realizamos la inversa:
    audio_filtrado = ifft(audio_fft_filtrado)
    # Ahora pasamos las frecuencias a audio de nuevo:
    audio_filtrado_reconstruido = (np.array(audio_filtrado)/len(audio_data)).real
    audio_filtrado_reconstruido *= MAX_INT
    audio_filtrado_reconstruido = audio_filtrado_reconstruido.astype(OG_DATATYPE)
    wavfile.write("./AUDIO_FILTRDO_RECONSTRUIDO.wav", rate, audio_filtrado_reconstruido)

        # Ahora vamos a generar la grafica:
    # vamos a hacer la comparativa de antes, transofrmado y despues
    fig, axes = plt.subplots(3,1,figsize=(12, 10))
    # Para la grafica de la señal original
    tiempo = np.arange(len(audio_data))/rate
    axes[0].set_title("Audio original")
    axes[0].set_xlabel("Tiempo (s)")
    axes[0].set_xlabel("Amplitud (s)")
    axes[0].grid(True) 
    sns.lineplot(x=tiempo, y =audio_data*MAX_INT, ax=axes[0])

    # Misma señal original
    frecuencias_positivas_filtradas = frecuencias[:len(audio_fft_filtrado)//2]
    # Arreglo de las magnitudes, al sacarle valor asboluto 
    # a un complejo sacas su modulo:
    magnitudes_filtradas = np.abs(np.array(audio_fft_filtrado[:len(audio_fft_filtrado)//2]))

    sns.lineplot(x=frecuencias_positivas_filtradas, y=magnitudes_filtradas, ax=axes[1])

    axes[1].set_title('Espectro de amplitud de la FFT filtrada') # Cambia el título
    axes[1].set_xlabel('Frecuencia (Hz)')
    axes[1].set_ylabel('Potencia') # O 'Magnitud Cuadrada'
    axes[1].set_xlim(0, rate / 2)
    axes[1].grid(True)

    sns.lineplot(x=tiempo, y=audio_filtrado_reconstruido, ax=axes[2])
    axes[2].set_title("Audio filtrado reconstruido")
    axes[2].set_xlabel("Tiempo (s)")
    axes[2].set_xlabel("Amplitud (s)")
    axes[2].grid(True)
    plt.subplots_adjust(hspace=0.5)
    plt.show()

except FileNotFoundError:
    print(f"No existe el archivo xd")
