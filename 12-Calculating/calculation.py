# Python3.6
# Coding: utf-8

# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

# Create a dictionary of pKa values:
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# Count the numbers of each amino acid:
seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}

# Initialize pH:
pH = 0.0

# While loop to calculate the net charge from pH 0 to pH 14:
while pH <= 14:
    netCharge = (
        +(sum({x: ((seqCount[x] * (10 ** pKR[x])) / ((10 ** pH) + (10 ** pKR[x]))) \
        for x in ['k', 'h', 'r']}.values()))
        -(sum({x: ((seqCount[x] * (10 ** pH)) / ((10 ** pH) + (10 ** pKR[x]))) \
        for x in ['y', 'c', 'd', 'e']}.values()))
    )
    
    # Print the pH and corresponding net charge:
    print('{0:.2f}'.format(pH), netCharge)
    
    # Increment pH by 0.1:
    pH += 0.1
