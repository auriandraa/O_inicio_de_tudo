import time

import pywhatkit

#variaveis

mensagem_saudacao = (f"oi, tudo bom?")
mensagem_despedida = (f"Então ta... fui")

#contatos
auri = ("+5547984137785")

pywhatkit.sendwhatmsg_instantly(auri, mensagem_saudacao, 25, tab_close=False)
pywhatkit.sendwhatmsg_instantly(auri,mensagem_despedida,25, tab_close=True)
