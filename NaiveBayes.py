import numpy as np

data = {'T':[[0, 1, 1, 1], 
             [0, 1, 0, 1], 
             [0, 0, 1, 1], 
             [1, 1, 1, 1]],
        'Y':[[0, 0, 0, 0], 
             [1, 1, 0, 1], 
             [1, 0, 1, 1]]}

uji = [1,0,1,1]

# print(uji[0])
#langkah pertama
def many_data(data):
    manyData = 0
    
    for value in data.values():
        data = len(value)
        manyData += data
    
    return manyData

def langkah_pertama(data, manyData):
    probabilitas = []

    for value in data.values():
        probabilitas.append(len(value) / manyData)

    return probabilitas

def langkah_dua(data, uji):
    probabilitas = []
    results = {}

    for label, values in data.items():
        an_array = np.array(values)
        counts = np.count_nonzero(an_array == uji, axis=0)
        probabilitas = [count / len(values) for count in counts]
        results[label] = np.prod(probabilitas)

    return results

def langkah_tiga(langkah_pertama, langkah_dua):
    pass
    
manyData = many_data(data)
print(manyData)

print(langkah_pertama(data, manyData))

print(langkah_dua(data, uji))









