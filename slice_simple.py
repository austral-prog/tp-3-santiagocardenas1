def slice_simple():
    texto = "Awesome"
    texto = texto.lower()
    print(texto[0:3])
    print(texto[2:5])
    parte_1 = (texto[0:4])
    parte_2 = (texto[-3:])
    resultado = parte_1 + parte_2
    print(resultado)
