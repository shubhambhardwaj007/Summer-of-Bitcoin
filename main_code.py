import pandas as pd
    mempool = pd.read_csv("mempool.csv")
    max_fee= 0
    combined_weight= 0
    block_array= []
    allowed_weight=4000000
    index=0
    while combined_weight < allowed_weight:
        i=0
        max_fee=0
        for i in range(mempool.shape[0] - 1):
            if mempool["fee"][i] > max_fee:
                max_fee = mempool["fee"][i]
                max_fee_position=i
                tx_id=mempool["tx_id"][i]
                weight=mempool["weight"][i]
                parent=mempool["parents "][i]
            else:
                pass
        if str(parent) == 'nan':
            combined_weight=combined_weight + weight
            block_array.append(str(tx_id))
            mempool.drop(index=max_fee_position,inplace=True)
            mempool.reset_index(inplace=True)
            mempool.drop(labels=['index'],axis=1,inplace=True)
        elif str(parent) != 'nan':
            for j in range(mempool.shape[0] - 1):
                if str(parent) == str(mempool["parents "][j]):
                    combined_weight = combined_weight + mempool["weight"][j]
                    block_array.append(str(mempool["tx_id"][j]))
                    mempool.drop(index=j,inplace=True)
                    mempool.reset_index(inplace=True)
                    mempool.drop(labels=['index'],axis=1,inplace=True)
                else:
                    pass
            combined_weight=combined_weight + weight
            block_array.append(str(tx_id))
            mempool.drop(index=max_fee_position,inplace=True)
            mempool.reset_index(inplace=True)
            mempool.drop(labels=['index'],axis=1,inplace=True)
        else:
            pass
    with open('block_test.txt', "a+") as file_object:
        appendEOL = False
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            appendEOL = True
        for line in block_array:
            if appendEOL == True:
                file_object.write("\n")
            else:
                appendEOL = True
            file_object.write(line)
    
