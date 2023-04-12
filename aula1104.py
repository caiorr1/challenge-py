import os
import json
import requests
import glob as gl

# for i in range(10):
#     arquivo = open(fr'.\arquivos\arquivo_{i}.txt','x')
#     arquivo.write(f'Conteúdo do arquivo número {i}')
#     arquivo.close()

# gl.glob(r'.\arquivos\arquivo_*.txt')

dicionario = {
    'nome' : 'Caio Rodrigues',
    'idade' : 18,
    'peso' : 73.4,
    'altura' : 1.78,
    'usuario_python' : True,
    'lista' : [1, 2, 3, 4]
}
for i in range(10):
    arquivo = open(fr'.\arquivos\arquivo_{i}.json','x')
    arquivo.write(f'Conteúdo do arquivo número {i}')
    dicionario['id'] = i

    json.dump(dicionario,arquivo)
    arquivo.close()