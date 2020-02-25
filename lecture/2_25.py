import sys

print(sys.argv)

if len(sys.argv) != 2:
    print('ERR: Must have a file name')
    sys.exit()

memory = [0] * 256

mem_pointer = 0

try: 
    # Open files
    with open(sys.argv[1]) as f:

        # Read lines
        for line in f:

            # Parse out comments
            comment_split = line.strip().split('#')


            # Cast the numbers from strings to ints
            value = comment_split[0].strip
            
            # Ignore blank linkes
            if value == '':
                continue
            
            num = int(value, 2)
            memory[mem_pointer] = num
            mem_point += 1

            print(f'{num:08b}: {num}')

except FileNotFoundError:
    print('File not found')
    sys.exit(2)
