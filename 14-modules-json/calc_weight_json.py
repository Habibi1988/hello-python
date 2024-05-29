import jsonFileHandler

# Retrieve JSON data
data = jsonFileHandler.readJsonFile('files/insulin.json')

if data != "":
    # Extract data from JSON
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    
    # Print extracted data
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    
    # Calculate the molecular weight of insulin
    aaWeights = data['weights']
    aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeights.keys()}
    molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaWeights.keys())
    
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))
else:
    print("Error. Exiting program")
