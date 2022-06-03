import numpy as np
import tabela_correcao_lista
from tkinter import *

tela=Tk()
tela.geometry('1000x600')
tela.title("Calculadora Balanço Hídrico")

# inserção de latitude e cad
texto_latitude = Label(tela, text = 'Latitude: ').grid(row=3, column=0)
valor_latitude = Entry(tela).grid(row=3, column=1)
texto_cad = Label(tela, text = 'CAD: ').grid(row=4, column=0)
valor_cad = Entry(tela).grid(row=4, column=1)


lista_latitudes = [2, 0 ,-2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -28, -30]
def closest(lista_latitudes, valor_latitude):
      
     lst = np.asarray(lista_latitudes)
     idx = (np.abs(lista_latitudes - valor_latitude)).argmin()
     return lista_latitudes[idx]     


# encontrar valor mais próximo
# def closest(lst, K):
      
#     return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
      
# # Driver code
# lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8]
# K = 9.1
# print(closest(lst, K))


# calculo temperatura e precipitação
def calcular():
    soma_temp = sum(lista_temperatura)
    media_temp = soma_temp/12
    soma_precipitacao = sum(lista_precipitacao)
    result_media_temp = Label(tela,text=' %.2f ' % media_temp).grid(row=23,column=1)
    result_soma_precip = Label(tela,text=' %.2f ' % soma_precipitacao).grid(row=23,column=5)
    
    indiceI = 12*(media_temp / 5)**1.514
    coefA = (6.75*(10**-7)*indiceI**3) - (7.71*(10**-5)*indiceI**2) + (1.792*(10**-2)*indiceI) + 0.49239
    ep_mes = []
    for temperatura in lista_temperatura:
        valor_ep_mes = 16*(10*temperatura / indiceI)**coefA
        ep_mes.append(valor_ep_mes)

    ep_jan = Label(tela,text=int(ep_mes[0])).grid(row=11,column=2)
    ep_fev = Label(tela,text=int(ep_mes[1])).grid(row=12,column=2)
    ep_mar = Label(tela,text=int(ep_mes[2])).grid(row=13,column=2)
    ep_abr = Label(tela,text=int(ep_mes[3])).grid(row=14,column=2)
    ep_mai = Label(tela,text=int(ep_mes[4])).grid(row=15,column=2)
    ep_jun = Label(tela,text=int(ep_mes[5])).grid(row=16,column=2)
    ep_jul = Label(tela,text=int(ep_mes[6])).grid(row=17,column=2)
    ep_ago = Label(tela,text=int(ep_mes[7])).grid(row=18,column=2)
    ep_set = Label(tela,text=int(ep_mes[8])).grid(row=19,column=2)
    ep_out = Label(tela,text=int(ep_mes[9])).grid(row=20,column=2)
    ep_nov = Label(tela,text=int(ep_mes[10])).grid(row=21,column=2)
    ep_dez = Label(tela,text=int(ep_mes[11])).grid(row=22,column=2)
    indice_i = Label(tela,text=' %.2f ' % indiceI).grid(row=11,column=8)
    coeficiente_a = Label(tela,text=' %.2f ' % coefA).grid(row=12,column=8)

    corr_q = tabela_correcao_lista.tabela_cor_q26s
    etp_mes = np.multiply(corr_q,ep_mes)
    
    # etp_jan = Label(tela,text=int(etp_mes[0]).grid(row=11,column=3))
    # etp_fev = Label(tela,text=int(etp_mes[1]).grid(row=12,column=3))
    # etp_mar = Label(tela,text=int(etp_mes[2]).grid(row=13,column=3))
    # etp_abr = Label(tela,text=int(etp_mes[3]).grid(row=14,column=3))
    # etp_mai = Label(tela,text=int(etp_mes[4]).grid(row=15,column=3))
    # etp_jun = Label(tela,text=int(etp_mes[5]).grid(row=16,column=3))
    # etp_jul = Label(tela,text=int(etp_mes[6]).grid(row=17,column=3))
    # etp_ago = Label(tela,text=int(etp_mes[7]).grid(row=18,column=3))
    # etp_set = Label(tela,text=int(etp_mes[8]).grid(row=19,column=3))
    # etp_out = Label(tela,text=int(etp_mes[9]).grid(row=20,column=3))
    # etp_nov = Label(tela,text=int(etp_mes[10]).grid(row=21,column=3))
    # etp_dez = Label(tela,text=int(etp_mes[11]).grid(row=22,column=3))
    corr1 = Label(tela,text=corr_q[0]).grid(row=11,column=3)
    corr2 = Label(tela,text=corr_q[1]).grid(row=12,column=3)
    corr3 = Label(tela,text=corr_q[2]).grid(row=13,column=3)
    corr4 = Label(tela,text=corr_q[3]).grid(row=14,column=3)
    corr5 = Label(tela,text=corr_q[4]).grid(row=15,column=3)
    corr6 = Label(tela,text=corr_q[5]).grid(row=16,column=3)
    corr7 = Label(tela,text=corr_q[6]).grid(row=17,column=3)
    corr8 = Label(tela,text=corr_q[7]).grid(row=18,column=3)
    corr9 = Label(tela,text=corr_q[8]).grid(row=19,column=3)
    corr10 = Label(tela,text=corr_q[9]).grid(row=20,column=3)
    corr11 = Label(tela,text=corr_q[10]).grid(row=21,column=3)
    corr12 = Label(tela,text=corr_q[11]).grid(row=22,column=3)
    etp_jan = Label(tela,text='%.2f' % etp_mes[0]).grid(row=11,column=4)
    etp_fev = Label(tela,text='%.2f' % etp_mes[1]).grid(row=12,column=4)
    etp_mar = Label(tela,text='%.2f' % etp_mes[2]).grid(row=13,column=4)
    etp_abr = Label(tela,text='%.2f' % etp_mes[3]).grid(row=14,column=4)
    etp_mai = Label(tela,text='%.2f' % etp_mes[4]).grid(row=15,column=4)
    etp_jun = Label(tela,text='%.2f' % etp_mes[5]).grid(row=16,column=4)
    etp_jul = Label(tela,text='%.2f' % etp_mes[6]).grid(row=17,column=4)
    etp_ago = Label(tela,text='%.2f' % etp_mes[7]).grid(row=18,column=4)
    etp_set = Label(tela,text='%.2f' % etp_mes[8]).grid(row=19,column=4)
    etp_out = Label(tela,text='%.2f' % etp_mes[9]).grid(row=20,column=4)
    etp_nov = Label(tela,text='%.2f' % etp_mes[10]).grid(row=21,column=4)
    etp_dez = Label(tela,text='%.2f' % etp_mes[11]).grid(row=22,column=4)


    return 

# calculo ep * q




# calculo evapotranspiração

# def calculo_EP():
#     media_temp = sum(lista_temperatura) / 12
#     indiceI = 12*(media_temp / 5)**1.514
#     coefA = (6.75*(10**-7)*indiceI**3) - (7.71*(10**-5)*indiceI**2) + (1.792*(10**-2)*indiceI) + 0.49239
#     ep_mes = []
#     for temperatura in lista_temperatura:
#         valor_ep_mes = 16*(10*temperatura / indiceI)**coefA
#         ep_mes.append(valor_ep_mes)

#     ep_jan = Label(tela,text=int(ep_mes[0])).grid(row=11,column=2)
#     ep_fev = Label(tela,text=int(ep_mes[1])).grid(row=12,column=2)
#     ep_mar = Label(tela,text=int(ep_mes[2])).grid(row=13,column=2)
#     ep_abr = Label(tela,text=int(ep_mes[3])).grid(row=14,column=2)
#     ep_mai = Label(tela,text=int(ep_mes[4])).grid(row=15,column=2)
#     ep_jun = Label(tela,text=int(ep_mes[5])).grid(row=16,column=2)
#     ep_jul = Label(tela,text=int(ep_mes[6])).grid(row=17,column=2)
#     ep_ago = Label(tela,text=int(ep_mes[7])).grid(row=18,column=2)
#     ep_set = Label(tela,text=int(ep_mes[8])).grid(row=19,column=2)
#     ep_out = Label(tela,text=int(ep_mes[9])).grid(row=20,column=2)
#     ep_nov = Label(tela,text=int(ep_mes[10])).grid(row=21,column=2)
#     ep_dez = Label(tela,text=int(ep_mes[11])).grid(row=22,column=2)
#     indice_i = Label(tela,text=' %.2f ' % indiceI).grid(row=11,column=3)
#     coeficiente_a = Label(tela,text=' %.2f ' % coefA).grid(row=12,column=3)

#     return


# # calculo ep * q
# def calculo_etp():
#     valor_latitude = int(latitude_digitada.get(Value))
#     if int(valor_latitude.get()) == 2:
#         latitude_calculo = tabela_correcao.tabela_cor_q2s
#     elif int(valor_latitude.get()) == 4:
#                 latitude_calculo = tabela_correcao.tabela_cor_q4s
#     elif int(valor_latitude.get()) == 6:
#                 latitude_calculo = tabela_correcao.tabela_cor_q6s
#     elif int(valor_latitude.get()) == 8:
#                 latitude_calculo = tabela_correcao.tabela_cor_q8s
#     elif int(valor_latitude.get()) == 10:
#                 latitude_calculo = tabela_correcao.tabela_cor_q10s
#     elif int(valor_latitude.get()) == 12:
#                 latitude_calculo = tabela_correcao.tabela_cor_q12s
#     elif int(valor_latitude.get()) == 14:
#                 latitude_calculo = tabela_correcao.tabela_cor_q14s
#     elif int(valor_latitude.get()) == 16:
#                 latitude_calculo = tabela_correcao.tabela_cor_q16s
#     elif int(valor_latitude.get()) == 18:
#                 latitude_calculo = tabela_correcao.tabela_cor_q18s
#     elif int(valor_latitude.get()) == 20:
#                 latitude_calculo = tabela_correcao.tabela_cor_q20s
#     elif int(valor_latitude.get()) == 22:
#                 latitude_calculo = tabela_correcao.tabela_cor_q22s
#     elif int(valor_latitude.get()) == 24:
#                 latitude_calculo = tabela_correcao.tabela_cor_q24s
#     elif int(valor_latitude.get()) == 26:
#                 latitude_calculo = tabela_correcao.tabela_cor_q26s
#     elif int(valor_latitude.get()) == 28:
#                 latitude_calculo = tabela_correcao.tabela_cor_q28s
#     elif int(valor_latitude.get()) == 30:
#                 latitude_calculo = tabela_correcao.tabela_cor_q30s 
#     latitude_mostrada = Label(text=latitude_calculo).grid(ro2=50,column=0)
#     etp_jan = latitude_calculo('jan')*
#     return
# valor_latitude = 1
# latitude_digitada = Entry(tela).grid(row=40,column=0)


# #Create a button
# botao = Button(tela, text="Calcular latitude", command=calculo_etp).grid(row=5,column=2)
# # .grid(ro2=4, column=0)
# # botao.pack()
# #Create a label
# latitude_mostrada = Label(tela)
# # .grid(row=5, column=0)

# cad_mostrado = Label(tela)
# # .grid(row=6, column=0)



# informações da tabela
col_mes = Label(tela, text = 'Mês').grid(row=10, column=0)
col_temperatura = Label(tela, text = 'T °C ').grid(row=10, column=1)
col_evapotranspiracao = Label(tela, text = 'EP (mm)').grid(row=10, column=2)
col_correcao = Label(tela, text = 'Corr (q)').grid(row=10, column=3)
col_evapo_potencial = Label(tela, text = 'ETP (mm)').grid(row=10, column=4)
col_precipitacao = Label(tela, text = 'P (mm)').grid(row=10, column=5)
col_precip_evapo = Label(tela, text = 'P - ETP (mm)').grid(row=10, column=6)
col_negativo = Label(tela, text = 'Neg (mm)').grid(row=10, column=7)
col_arm = Label(tela, text = 'ARM (mm)').grid(row=10, column=8)
col_alt = Label(tela, text = 'ALT (mm)').grid(row=10, column=9)
col_etr = Label(tela, text = 'ETR (mm)').grid(row=10, column=10)
col_def = Label(tela, text = 'DEF (mm)').grid(row=10, column=11)
col_exc = Label(tela, text = 'EXC (mm').grid(row=10, column=12)

mes_jan = Label(tela, text = 'Jan').grid(row=11, column=0)
mes_fev = Label(tela, text = 'Fev').grid(row=12, column=0)
mes_mar = Label(tela, text = 'Mar').grid(row=13, column=0)
mes_abr = Label(tela, text = 'Abr').grid(row=14, column=0)
mes_mai = Label(tela, text = 'Mai').grid(row=15, column=0)
mes_jun = Label(tela, text = 'Jun').grid(row=16, column=0)
mes_jul = Label(tela, text = 'Jul').grid(row=17, column=0)
mes_ago = Label(tela, text = 'Ago').grid(row=18, column=0)
mes_set = Label(tela, text = 'Set').grid(row=19, column=0)
mes_out = Label(tela, text = 'Out').grid(row=20, column=0)
mes_nov = Label(tela, text = 'Nov').grid(row=21, column=0)
mes_dez = Label(tela, text = 'Dez').grid(row=22, column=0)
media_soma = Label(tela, text = 'Média/Soma').grid(row=23, column=0)

# temperatura a serem inserida

valor_jan = Entry(tela).grid(row=11, column=1)
valor_fev = Entry(tela).grid(row=12, column=1)
valor_mar = Entry(tela).grid(row=13, column=1)
valor_abr = Entry(tela).grid(row=14, column=1)
valor_mai = Entry(tela).grid(row=15, column=1)
valor_jun = Entry(tela).grid(row=16, column=1)
valor_jul = Entry(tela).grid(row=17, column=1)
valor_ago = Entry(tela).grid(row=18, column=1)
valor_set = Entry(tela).grid(row=19, column=1)
valor_out = Entry(tela).grid(row=20, column=1)
valor_nov = Entry(tela).grid(row=21, column=1)
valor_dez = Entry(tela).grid(row=22, column=1)

lista_temperatura = [valor_jan, valor_fev, valor_mar, valor_abr, valor_mai, valor_jun, valor_jul, valor_ago, valor_set, valor_out, valor_nov, valor_dez]

# precipitação a ser inserida

precip_jan = Entry(tela).grid(row=11, column=5)
precip_fev = Entry(tela).grid(row=12, column=5)
precip_mar = Entry(tela).grid(row=13, column=5)
precip_abr = Entry(tela).grid(row=14, column=5)
precip_mai = Entry(tela).grid(row=15, column=5)
precip_jun = Entry(tela).grid(row=16, column=5)
precip_jul = Entry(tela).grid(row=17, column=5)
precip_ago = Entry(tela).grid(row=18, column=5)
precip_set = Entry(tela).grid(row=19, column=5)
precip_out = Entry(tela).grid(row=20, column=5)
precip_nov = Entry(tela).grid(row=21, column=5)
precip_dez = Entry(tela).grid(row=22, column=5)

lista_precipitacao = [precip_jan, precip_fev, precip_mar, precip_abr, precip_mai, precip_jun, precip_jul, precip_ago, precip_set, precip_out, precip_nov, precip_dez]

# valores teste
valor_jan = 19.6
valor_fev = 19.9
valor_mar = 19.0
valor_abr = 16.7
valor_mai = 14.6
valor_jun = 12.2
valor_jul = 12.8
valor_ago = 14.0
valor_set = 15.0
valor_out = 16.5
valor_nov = 18.2
valor_dez = 19.3
precip_jan = 165
precip_fev = 142
precip_mar = 127
precip_abr = 90
precip_mai = 99
precip_jun = 98
precip_jul = 89
precip_ago = 75
precip_set = 115
precip_out = 134
precip_nov = 124
precip_dez = 150
lista_temperatura = [valor_jan, valor_fev, valor_mar, valor_abr, valor_mai, valor_jun, valor_jul, valor_ago, valor_set, valor_out, valor_nov, valor_dez]
lista_precipitacao = [precip_jan, precip_fev, precip_mar, precip_abr, precip_mai, precip_jun, precip_jul, precip_ago, precip_set, precip_out, precip_nov, precip_dez]



# prod=StringVar()
# qtde=StringVar()
# preco=StringVar()

# label1=Label(tela,text="Fernando Ibrahim",fg="black").grid(row=0,column=0,pady=2)
# label5=Label(tela,text="").grid(row=1,column=0)
# label2=Label(tela,text="Produto").grid(row=2,column=0)
# label3=Label(tela,text="Quantidade").grid(row=3,column=0)
# label4=Label(tela,text="Preco").grid(row=4,column=0)

# prodvar=Entry(tela,textvariable=prod).grid(row=2,column=2)
# qtdevar=Entry(tela,textvariable=qtde).grid(row=3,column=2)
# precovar=Entry(tela,textvariable=preco).grid(row=4,column=2)
#Create a input box for pressure


button1=Button(tela,text="Calcular", command=calcular).grid(row=5,column=0)
# button2=Button(tela,text="EP", command=calculo_EP).grid(row=5,column=1)
tela.mainloop()

valor = float(tabela_correcao.tabela_cor_q0.get('jan'))
x = 2*valor
print(x)




