piplineOuts = [0.92, 0.42, 0.17, 0.65, 0.49, 0.50, 0.70]

outsFiltered = list(map(lambda x: 'Healthy' if x >= 0.50 else 'Damaged', piplineOuts))
print(outsFiltered)

damagedIDs = []
healthyIDs = []

for out in range(len(outsFiltered)):
    if outsFiltered[out] == 'Damaged':
        damagedIDs.append(out)
    else:
        healthyIDs.append(out)

#damagedIDs = list(filter(lambda x : x == 'Damaged', outsFiltered))
#healthyIDs = list(filter(lambda x : x == 'Healthy', outsFiltered))
        
print("Damaged IDs =", str(damagedIDs))
print("Healthy IDs =", str(healthyIDs))