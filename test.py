def decodeString(s: str) -> str:
    def decode_from(i):
        current_string = ""
        repeat_count = 0

        while i < len(s):
            char = s[i]

            if char.isdigit():
                # Build the full repeat count (can be more than 1 digit)
                repeat_count = repeat_count * 10 + int(char)

            elif char == '[':
                # Start decoding the substring inside brackets
                i, decoded_substring = decode_from(i + 1)

                # Append the repeated substring
                current_string += repeat_count * decoded_substring

                # Reset repeat count for future numbers
                repeat_count = 0

            elif char == ']':
                # End of current decoding segment, return control
                return i, current_string

            else:
                # Normal characters, add to current segment
                current_string += char

            i += 1

        return current_string  # top-level return

    # Kick off the decoding from index 0
    result = decode_from(0)

    # If it's a tuple (due to return from inside recursion), unwrap it
    return result if isinstance(result, str) else result[1]

s = "2[a]"
print(decodeString(s))


# alternative

for x in zip(range(10),range(5)):
    print(x)