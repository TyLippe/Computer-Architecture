"""CPU functionality."""

import sys

OP1 = 0b00000001    # HLT
OP2 = 0b10000010    # LDI
OP3 = 0b01000111    # PRN
OP4 = 0b10100010    # MUL

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.branchtable = {}
        self.branchtable[OP1] = self.handle_op1
        self.branchtable[OP2] = self.handle_op2
        self.branchtable[OP3] = self.handle_op3
        self.branchtable[OP4] = self.handle_op4
    
    def handle_op1(self, a):
        print("op 1: " + a)

    def handle_op2(self, a):
        print("op 2: " + a)
    
    def handle_op3(self, a):
        print("op 3: " + a)
    
    def handle_op4(self, a):
        print("op 4: " + a)

    def ram_read(self, mar):
        mdr = self.ram[mar]
        return mdr

    def ram_write(self, mdr, mar):
        self.ram[mar] = mdr

    def load(self, filename):
        print(filename)
        """Load a program into memory."""
        try:
            address = 0
            # Open the file
            with open(filename) as f:
                # Read all the lines
                for line in f:
                    # Parse out comments
                    comment_split = line.strip().split("#")
                    # Cast the numbers from strings to ints
                    value = comment_split[0].strip()
                    # Ignore blank lines
                    if value == "":
                        continue

                    num = int(value, 2)
                    self.ram[address] = num
                    address += 1

        except FileNotFoundError:
            print("File not found")
            sys.exit(2)

    if len(sys.argv) != 2:
        print("ERROR: Must have file name")
        sys.exit(1)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while True:
            opcode = self.ram[self.pc]
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            if opcode == LDI:
                print('LDI')
                self.reg[operand_a] = operand_b
                self.pc += 3
            elif opcode == PRN:
                print('PRN')
                print(self.reg[operand_a])
                self.pc += 2
            elif opcode == MUL:
                print('MUL')
                product = self.reg[operand_a] * self.reg[operand_b]
                print(product)
                self.pc += 3
            elif opcode == HLT:
                print('HTL')
                sys.exit(0)
            else:
                print(f'I did not understand that command: {opcode}')
                sys.exit(1)


