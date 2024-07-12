def print_hex_pattern(rows, cols):
    hex_top = "  ___ "
    hex_mid_top = " /   \\"
    hex_mid_bottom = " \\___/"
    hex_mid_spacing = "___"  # middle    space between hexagons in the same row
    hex_spacing="   "
    for r in range(rows):
        # Print top part of hexagons
        for c in range(cols):
            print(hex_top, end=hex_spacing)
        print()

        # Print upper middle part of hexagons
        for c in range(cols):
            print(hex_mid_top, end=hex_mid_spacing)
        print()

        # Print lower middle part of hexagons
        for c in range(cols):
            print(hex_mid_bottom, end=hex_spacing)
        print()

# Input rows and column
rows=int(input("Enter no of rows: "))
cols=int(input("Enter no of cols: "))
print_hex_pattern(rows, cols)

