import random

#função para simular um sensor de temperatura em ºC
def temp_sensor():
    return random.uniform(0,60)

#função para simular um sensor de pressão em bar
def pressure_sensor():
    return random.uniform(0,20)

#função para simular um sensor de pulso 0 ou 1
def pulse_sensor():
    return random.choice([0,1])
