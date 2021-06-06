import time
from database import insertData

def selectionsort (jsonArray, columnIdx, orientation):
    start_time = time.time()
    keys = list(jsonArray[0].keys())
    key = keys[columnIdx]
    for i in range (len(jsonArray)):
        min_idx = i
        for j in range (i+1, len(jsonArray)):
            if(orientation == "asc"):
                try:
                    if (float(jsonArray[min_idx][key]) > float(jsonArray[j][key])):
                        min_idx = j
                except ValueError:
                    if (jsonArray[min_idx][key] > jsonArray[j][key]):
                        min_idx = j
            elif (orientation == 'desc'):
                try:
                    if (float(jsonArray[min_idx][key]) < float(jsonArray[j][key])):
                        min_idx = j
                except ValueError:
                    if (jsonArray[min_idx][key] < jsonArray[j][key]):
                        min_idx = j
                
        # Swap the found minimum element with
        # the first element       
        jsonArray[i], jsonArray[min_idx] = jsonArray[min_idx], jsonArray[i]
    end_time = time.time()
    exectime = end_time - start_time # in seconds
    # insertData(conn, str(jsonArray), 'selection', exectime)
    return jsonArray, exectime