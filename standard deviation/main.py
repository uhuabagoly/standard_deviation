import math

data = open("number.txt", "r")
data_list = []
data_szoras = []

for i in data:
    i = i.strip()
    i = int(i)
    
    data_list.append(i)

print(f"Data: {data_list}")
alt = sum(data_list) / len(data_list)

data.close()

for i in data_list:
    egy_cela = (i - alt) ** 2
    data_szoras.append(egy_cela)

eredmeny = math.sqrt(sum(data_szoras) / len(data_szoras))

print(f"standard deviation: {eredmeny}")