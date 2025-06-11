# Primero voy a tratar de abrir un audio 
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import seaborn as sns

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
    # np.iinfo(audio_data.dtype).max
    audio_data = audio_data.astype(np.float32) / np.iinfo(audio_data.dtype).max
    # Esto nomas es pa verlo
    #sns.lineplot(audio_data)
    #plt.show()
except FileNotFoundError:
    print(f"No existe el archivo xd")
