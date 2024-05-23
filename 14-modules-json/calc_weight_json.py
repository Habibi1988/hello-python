import jsonFileHandler

# Retrieve the JSON data and store it in a data variable.
data = jsonFileHandler.readJsonFile('files/insulin.json')

# Check if the returned data is not empty and obtain the insulin data.
if data != "":
    try:
        bInsulin = data['molecules']['bInsulin']
        aInsulin = data['molecules']['aInsulin']
        insulin = bInsulin + aInsulin
        molecularWeightInsulinActual = data['molecularWeightInsulinActual']
        
        print('bInsulin: ' + bInsulin)
        print('aInsulin: ' + aInsulin)
        print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))

        # Calculating the molecular weight of insulin
        # Getting a list of the amino acid (AA) weights
        aaWeights = data['weights']
        
        # Count the number of each amino acid
        aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeights.keys()}
        
        # Multiply the count by the weights
        molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaWeights.keys())
        
        print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
        print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))
        
    except KeyError as e:
        print(f"Key error: {e}. The JSON structure is not as expected.")
    except TypeError as e:
        print(f"Type error: {e}. The JSON data might be malformed.")
else:
    print("Error. Exiting program")
