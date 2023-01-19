def mochila(n,w,v,peso):
    if n == 0 or peso == 0:
        return 0
    if peso[n-1] > w:
        return mochila(n-1,w,v,peso)
    else:
        return max(v[n-1] + mochila(n-1,w-peso[n-1],v,peso), mochila(n-1,w,v,peso))
def main():
    precio = [103,60,70,5,15]
    pesos = [12,23,11,15,7]
    pesomax = 100
    n = len(precio)
    valor_maximo = mochila(n,pesomax,precio,pesos)

if __name__ == '__main__':
    main()