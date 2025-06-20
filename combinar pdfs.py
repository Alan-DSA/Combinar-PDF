#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from PyPDF2 import PdfMerger

# Cria um objeto para fazer a junção
merger = PdfMerger()

# Lista dos arquivos PDF que você quer unir
# Coloque os arquivos na mesma pasta do script
arquivos_pdf = [
    'arquivo1.pdf',
    'arquivo2.pdf',
    'arquivo3.pdf'
]

# Adiciona cada arquivo ao merger
for pdf in arquivos_pdf:
    if os.path.exists(pdf):
        merger.append(pdf)
        print(f'Adicionado: {pdf}')
    else:
        print(f'Arquivo não encontrado: {pdf}')

# Salva o PDF unido
merger.write("pdf_unido.pdf")
merger.close()

print("PDFs unidos com sucesso em 'pdf_unido.pdf'")


# In[ ]:





# In[ ]:




