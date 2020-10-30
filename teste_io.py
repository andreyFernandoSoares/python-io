with open('dados/contatos-escrita.csv', encoding='UTF-8', mode='w') as arquivo:
    #conteudo = arquivo.buffer.read()
    contato = bytes('15,Veronica,veronica@veronica.com.br', 'utf-8')
    arquivo.buffer.write(contato)