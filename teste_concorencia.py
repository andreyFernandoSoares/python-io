contato_carol = '11,Carol,carol@carol.com.br\n'
contato_ana = '12,Ana,ana@ana.com.br\n'

with open('dados/contatos-escrita.csv', mode='w', encoding="utf-8") as arquivo1:
    arquivo1.write(contato_carol)

with open('dados/contatos-escrita.csv', mode='a', encoding="utf-8") as arquivo2:
    arquivo2.write(contato_ana)