print("Count to 10!")
for x in range (0, 11):
    print(x)

# Provided preproinsulin sequence
preproinsulin = (
    "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaed"
    "lqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
)

# Extract amino acids 25–54 (B-chain) and 90–110 (A-chain)
b_chain = preproinsulin[24:54]  # Amino acids 25 to 54 (0-based index starts at 24)
a_chain = preproinsulin[89:110]  # Amino acids 90 to 110 (0-based index starts at 89)

# Combine B-chain and A-chain to get the insulin sequence
insulin = b_chain + a_chain
insulin
print("Insulin sequence:", insulin)