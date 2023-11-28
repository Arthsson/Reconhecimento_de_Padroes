def achar_padrao(texto, padrao):
    inidices_encontrados = []
    for i in range(len(texto)-len(padrao)+1):
        j=0
        while j < len(padrao) and texto[i+j] == padrao[j]:
            j+=1
        
        if j == len(padrao):
            inidices_encontrados.append(i)

    return inidices_encontrados

texto = "BRUNO ARTHSSON SILVA"
padrao = "SON"
resultados = achar_padrao(texto , padrao )

if resultados:
    print(f'O padrão "{padrao}" foi encontrado nos a partir dos índices: "{resultados}"')
else:
    print(f'O padrão "{padrao}" nao foi encontrado')