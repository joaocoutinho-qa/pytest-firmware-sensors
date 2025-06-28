#código principal, para aquisição de dados do sensor e tomado de decisão
from sensor import pulse_sensor, temp_sensor, pressure_sensor
import pandas as pd
import time

iniciar = input('Iniciar sistema? 1-Sim 2-Não: ')
dados_pulso = {}
dados_temperatura = {}
dados_pressao = {}
tabela_pulso = []
tabela_temperatura = []
tabela_pressao = []
tabela_sensores = []

if(iniciar == 'Sim'):
    print('Sistema ligado')
    for i in range (30):
        read_pulse = pulse_sensor()
        read_pulse = round(read_pulse,2)
        dados_pulso = {"Sensor":"Pulso","Valor":read_pulse}
        tabela_pulso.append(dados_pulso)
        print(f'Pulse: {read_pulse}')
        time.sleep(0.1)

    for i in range (30):
        read_temperature = temp_sensor()
        read_temperature = round(read_temperature,2)
        dados_temperatura = {"Sensor":"Temperatura","Valor":read_temperature}
        tabela_temperatura.append(dados_temperatura)
        print(f'Temp: {read_temperature:.2f} ºC')
        time.sleep(0.1)
      
    for i in range (30):
        read_pressure = pressure_sensor()
        read_pressure = round(read_pressure,2)
        dados_pressao = {"Sensor":"Pressão","Valor":read_pressure}
        tabela_pressao.append(dados_pressao)
        print(f'Pressure: {read_pressure:.2f} bar')
        time.sleep(0.1)
    tabela_sensores = tabela_pulso + tabela_temperatura + tabela_pressao
    df = pd.DataFrame(tabela_sensores)
    df.to_csv('dados_sensores.csv',sep=';', index=False)

else:
    print('Sistema desligado')
