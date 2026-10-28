
def to_signed_8bit_bin(n):
  """Converts a decimal integer to its 8-bit 2's complement binary string."""
  if not (-128 <= n <= 127):
    raise ValueError(f"Value {n} is out of the 8-bit signed range [-128, 127].")
  if n < 0:
    n = (1 << 8) + n  # Equivalent to 256 + n
  return format(n, "08b")


def from_signed_8bit_bin(b_str):
  """Converts an 8-bit 2's complement binary string back to a signed decimal integer."""
  if len(b_str) != 8:
    raise ValueError("Binary string must be exactly 8 bits.")
  val = int(b_str, 2)
  if b_str[0] == "1":  # If the sign bit is 1, it's negative
    val -= 1 << 8
  return val


def add_8bit_binary(bin1, bin2):
  """Performs 8-bit binary addition and detects signed overflow."""
  val1 = from_signed_8bit_bin(bin1)
  val2 = from_signed_8bit_bin(bin2)

  # Bit-by-bit addition with carry propagation
  carry = 0
  res_bits = []
  for i in range(7, -1, -1):
    bit1 = int(bin1[i])
    bit2 = int(bin2[i])
    total = bit1 + bit2 + carry
    res_bits.insert(0, str(total % 2))
    carry = total // 2

  res_bin = "".join(res_bits)
  res_val = from_signed_8bit_bin(res_bin)

  # Signed overflow occurs if two operands of the same sign yield a result of the opposite sign
  overflow = (val1 > 0 and val2 > 0 and res_val < 0) or (
      val1 < 0 and val2 < 0 and res_val > 0
  )

  return res_bin, res_val, overflow


def perform_operation(op1, op2, operation_type="+"):
  """Performs addition or subtraction using 8-bit 2's complement arithmetic."""
  print(f"\n--- Expression: ({op1} {operation_type} ({op2})) ---")

  # For subtraction, convert to addition of the 2's complement (negation of op2)
  if operation_type == "-":
    actual_op2 = -op2
    op2_bin = to_signed_8bit_bin(actual_op2)
    print(
        f"Operation converted to addition: {op1} + ({op2} negated to {actual_op2})"
    )
  else:
    actual_op2 = op2
    op2_bin = to_signed_8bit_bin(actual_op2)

  op1_bin = to_signed_8bit_bin(op1)

  print(f"Operand 1 ({op1}): {op1_bin} (Binary)")
  print(f"Operand 2 ({actual_op2}): {op2_bin} (Binary)")

  res_bin, res_val, overflow = add_8bit_binary(op1_bin, op2_bin)

  print(f"Result Binary : {res_bin}")
  print(f"Result Decimal: {res_val}")
  print(
      f"Overflow Detected: {'YES (Arithmetic Overflow!)' if overflow else 'NO'}"
  )


if __name__ == "__main__":
  # Verify Expression a: (34 + (+27))
  perform_operation(34, 27, "+")

  # Verify Expression b: ((-34) - (-27)) -> (-34) + (+27)
  perform_operation(-34, -27, "-")
