#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
from PyPDF2 import PdfMerger

# Cria o objeto merger
merger = PdfMerger()

# Pasta onde estão os PDFs
pasta = '.'

# Lista todos os arquivos PDF na pasta
arquivos_pdf = [f for f in os.listdir(pasta) if f.endswith('.pdf')]
arquivos_pdf.sort()  # Ordena pelo nome dos arquivos

# Adiciona os PDFs
for pdf in arquivos_pdf:
    merger.append(os.path.join(pasta, pdf))
    print(f'Adicionado: {pdf}')

# Salva o PDF final
merger.write("pdf_unido.pdf")
merger.close()

print("PDFs unidos com sucesso em 'pdf_unido.pdf'")


# In[ ]:




