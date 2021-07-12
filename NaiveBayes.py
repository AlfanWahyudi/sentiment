import numpy as np
from collections import Counter

def many_data(data):
    manyData = 0
    
    for value in data.values():
        data = len(value)
        manyData += data
    
    return manyData

def langkah_pertama(data, manyData):
    results = {}
    for labels, value in data.items():
        results[labels] = len(value) / manyData

    return results

def langkah_dua(data, uji):
    results = {}

    for labels, values in data.items():
        convertNP = np.array(values)
        counts = np.count_nonzero(convertNP == uji, axis=0)
        probabilitas = [count / len(values) for count in counts]
        results[labels] = np.prod(probabilitas)

    return results

def langkah_tiga(langkah_pertama, langkah_dua):
    temp1 = Counter(langkah_pertama)
    temp2 = Counter(langkah_dua)

    results = Counter({key : temp1[key] * temp2[key] for key in temp1})

    return results

def langkah_empat(langkah_tiga):
    return min(langkah_tiga, key=langkah_tiga.get)
    

data = {'T':[[0, 1, 1, 1], 
             [0, 1, 0, 1], 
             [0, 0, 1, 1], 
             [1, 1, 1, 1]],
        'Y':[[0, 0, 0, 0], 
             [1, 1, 0, 1], 
             [1, 0, 1, 1]]}

uji = [1,0,1,1]

manyData = many_data(data)
pertama = langkah_pertama(data, manyData)
kedua = langkah_dua(data, uji)
ketiga = langkah_tiga(pertama, kedua)
keempat = langkah_empat(ketiga)

print("Hasil langkah pertama: " + str(pertama))
print("Hasil langkah kedua: " + str(kedua))
print("Hasil langkah ketiga: " + str(dict(ketiga)))
print("Hasil langkah keempat: " + keempat)