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
def manyData(data):
    manyData = 0
    for value in data.values():
        data = len(value)
        manyData += data
    
    return manyData

def perhitunganPertama(data, manyData):
    p = []
    for value in data.values():
        probabilitas = len(value) / manyData
        p.append(probabilitas)
    return p

def langkahdua(data, uji):
    results = []
    labels = {}

    for label, values in data.items():
        kolom = 0
        manyData = len(values)
        # print(manyData)
        for value in values:
            if value[kolom] != uji[kolom]:
                print("   tidak sama")
            else:
                print("   sama")
            print(uji[kolom])
            # print(value[1])
            # print(value[kolom])
            # print(kolom)
        kolom += 1
            # probabilitas = values[value][kolom] / manyData
        print("")
        # print(data[values][1])
        # tambahSatu = 0
        # baris = 0
        # manyData = 0
        # panjang_data = len(data[values])
        # print(panjang_data)
        # print(data[values][baris][tambahSatu])
        # for value in uji:
        #     print(uji[value])
        #     if data[values][tambahSatu] == uji[value]:
        #         manyData += 1
        #         tambahSatu += 1
        #         print("    dalam if")
        #     print("  for2")
        # print("for 1")
        # print(values[0][1])
        # result = manyData / panjang_data
        # results.append(result)

    return results
    
# manyData = manyData(data)
# print(manyData)

# print(perhitunganPertama(data, manyData))

print(langkahdua(data, uji))







