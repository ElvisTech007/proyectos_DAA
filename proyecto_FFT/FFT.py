import cmath
def fft(a):
    # a es el arreglo que contiene
    # los datos de la señal del sonido
    
    # Condiciṕn de paro
    if len(a): return a

    # Ahora tenemos que dividir en potencias pares
    # e impares haciendo un slicing

    # Pares, empezamos del 0 y vamos dando saltos de 2
    e = fft(a[0::2])
    # Impares emepzamos del 1, y vamos dandl saltos de 2
    d = fft(a[1::2])

    # Inicializamos nuestro arreglo de frecuencias
    Y = [0]*n
    for k in range(n//2):
        omega_k = cmath.exp(-2j * cmath.pi * k / n)
        Y[k] = e[k] + omega_k * d[k]
        Y[k + n // 2] = e[k] - omega_k * d[k]
    
    return Y

def ifft(a):
    # Misma cosa que lo anterior solo que 
    n = len(a)
    if n == 1:
        return a

    e = ifft(a[0::2])
    d = ifft(a[1::2])

    Y = [0] * n
    for k in range(n // 2):
        # Aquí cambia el signo por la matriz inversa de fourier
        omega_k = cmath.exp(-2j * cmath.pi * k / n)
        Y[k] = (e[k] + omega_k * d[k]) / n
        Y[k + n // 2] = (e[k] - omega_k * d[k]) / n
        
    return Y