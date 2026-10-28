def rotate_right_no_carry(bin_str, positions):
    """Performs Rotate Right without carry (ROR) on an 8-bit binary string."""
    if len(bin_str) != 8:
        raise ValueError("Binary string must be exactly 8 bits.")
    
    positions = positions % 8  # Normalize positions if >= 8
    print(f"\n--- ROR Operation on {bin_str} by {positions} positions ---")
    print(f"Original Binary: {bin_str}")
    
    current = bin_str
    for i in range(1, positions + 1):
        rightmost = current[-1]  # Get the LSB (wraparound bit)
        current = rightmost + current[:-1]  # Prepend LSB, shift rest right
        print(f"Step {i}: {current} (Wraparound bit: {rightmost})")
        
    print(f"Final ROR Result: {current}")
    return current


def rotate_right_with_carry(bin_str, carry_in, positions):
    """Performs Rotate Right with carry (RCR) on an 8-bit binary string and a carry bit."""
    if len(bin_str) != 8:
        raise ValueError("Binary string must be exactly 8 bits.")
    if carry_in not in (0, 1):
        raise ValueError("Carry flag must be 0 or 1.")
        
    positions = positions % 9  # RCR involves 9 bits total (8 data bits + 1 carry)
    print(f"\n--- RCR Operation on {bin_str} with Initial Carry C={carry_in} by {positions} positions ---")
    print(f"Original Binary: {bin_str} | Initial Carry (C): {carry_in}")
    
    current_byte = bin_str
    current_carry = carry_in
    
    for i in range(1, positions + 1):
        old_lsb = int(current_byte[-1])  # Save old LSB before shift
        # Shift byte right, placing the current carry into the MSB position
        current_byte = str(current_carry) + current_byte[:-1]
        # The old LSB becomes the new carry flag
        current_carry = old_lsb
        print(f"Step {i}: Byte = {current_byte} | New Carry (C) = {current_carry} (Old LSB moved to C: {old_lsb})")
        
    print(f"Final RCR Result: {current_byte} | Final Carry (C): {current_carry}")
    return current_byte, current_carry


if __name__ == "__main__":
    # a) Rotate right without carry (ROR) on 11010101 by 2 positions
    rotate_right_no_carry("11010101", 2)

    # b) Rotate right with carry (RCR) on 11010101 by 2 positions (assuming initial Carry C = 0)
    rotate_right_with_carry("11010101", 0, 2)
