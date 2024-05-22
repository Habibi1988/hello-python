# Define the preproinsulin sequence
preproinsulin_sequence = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Extract amino acids 1–24
amino_acids_1_to_24 = preproinsulin_sequence[:24]

# Print the extracted amino acids
print("Amino acids 1–24:")
print(amino_acids_1_to_24)

# Save to file
with open("insulin-seq-clean.txt", "w") as f:
    f.write(amino_acids_1_to_24)

# Verify file length
with open("insulin-seq-clean.txt", "r") as f:
    content = f.read()
    print("Length of the file:", len(content))

# Define the preproinsulin sequence
preproinsulin_sequence = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Extract amino acids 25–54
amino_acids_25_to_54 = preproinsulin_sequence[24:54]

# Print the extracted amino acids
print("Amino acids 25–54:")
print(amino_acids_25_to_54)

# Save to file
with open("insulin-seq-clean.txt", "w") as f:
    f.write(amino_acids_25_to_54)

# Verify file length
with open("insulin-seq-clean.txt", "r") as f:
    content = f.read()
    print("Length of the file:", len(content))
    
# Define the preproinsulin sequence
preproinsulin_sequence = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Extract amino acids 55–89
amino_acids_55_to_89 = preproinsulin_sequence[54:89]

# Print the extracted amino acids
print("Amino acids 55–89:")
print(amino_acids_55_to_89)

# Save to file
with open("cinsulin-seq-clean.txt", "w") as f:
    f.write(amino_acids_55_to_89)

# Verify file length
with open("cinsulin-seq-clean.txt", "r") as f:
    content = f.read()
    print("Length of the file:", len(content))
# Define the preproinsulin sequence
preproinsulin_sequence = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Extract amino acids 90–110
amino_acids_90_to_110 = preproinsulin_sequence[89:110]

# Print the extracted amino acids
print("Amino acids 90–110:")
print(amino_acids_90_to_110)

# Save to file
with open("ainsulin-seq-clean.txt", "w") as f:
    f.write(amino_acids_90_to_110)

# Verify file length
with open("ainsulin-seq-clean.txt", "r") as f:
    content = f.read()
    print("Length of the file:", len(content))

