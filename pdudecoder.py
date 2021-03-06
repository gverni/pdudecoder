import re

def decode(input_ar, decode_ar, decode_hash):
    print "Length of input vector: " + str(len(input_ar))
    print "Length of decode vector: " + str(len(decode_ar))
    if len(input_ar) > len(decode_ar):
        print "Warning: decoding array shorter than input vector. Leftmost bits of input array will not be decoded"
        decode_ar = [0] * (len(input_ar) - len(decode_ar)) + decode_ar
    elif len(input_ar) < len(decode_ar):
        print "Warning: input vector shorter than decoding array. Padding the leftmost bits to 0"
        input_ar = [0] * (len(decode_ar) - len(input_ar)) + input_ar

    a_i = 0
    value = ""
    num_bit = 0
    while a_i < len(input_ar):
        decode_func = decode_ar[a_i]
        while a_i < len(input_ar) and decode_ar[a_i] == decode_func:
            value += str(input_ar[a_i])
            num_bit += 1
            a_i += 1
        print decode_hash[decode_func] + " [" + str(num_bit) + "]: " + value + "b = " + str(int(value, 2))
        value = ""
        num_bit = 0


def create_decode(input_file):  # Return decode_ar and decode_hash
    finput = open(input_file, 'r')
    decode_ar = []
    decode_hash = {0: "Undecoded bit(s)"}

    for line in finput:
        # We are looking for [XX:XX]
        line_decoded = re.search(r"\[([0-9]+)\:([0-9]+)\] (.+)", line)
        start_bit = int(line_decoded.group(1))
        stop_bit = int(line_decoded.group(2))
        decode_string = line_decoded.group(3)
        decode_string_pos = len(
            decode_hash)  # Use +1 because we want to avoid using the index 0, which means no function defined
        decode_hash[decode_string_pos] = decode_string
        if max(start_bit, stop_bit) > len(
                decode_ar) - 1:  # We use max function because user can give input bits in whichever order
            decode_ar = decode_ar + [0] * ((max(start_bit, stop_bit) + 1) - len(decode_ar))
        for a_i in range(min(start_bit, stop_bit), max(start_bit,
                                                       stop_bit) + 1):  # We use max function because user can give input bits in whichever order. We also add +1 to the right argument because range generate numbers until right argument -1
            decode_ar[a_i] = decode_string_pos

    return decode_ar, decode_hash


def test():
    test_decode_ar = [1, 1, 1, 2, 3, 3, 3, 3]
    test_decode_hash = {1: "first field", 2: "second field", 3: "third field"}

    #Test input vector long as decoder
    decode([0, 0, 1, 1, 0, 0, 1, 1], test_decode_ar, test_decode_hash)

    #Test input vector longer than decoder
    decode([0, 0, 1, 1, 0, 0, 1, 1, 1], test_decode_ar, test_decode_hash)

    #Test input smaller than decoder
    decode([0, 0, 1, 1, 0, 1], test_decode_ar, test_decode_hash)

    test_decode_ar, test_decode_hash = create_decode("pdude.txt")
    print test_decode_ar
    print test_decode_hash

in_decode_ar, in_decode_hash = create_decode("pdude.txt")
in_decode_ar.reverse() #Usually the decode array is given from higher to lowe bit
input_vector = map(int, list(raw_input())) #map(int, list(raw_input())).reverse()
#print input_vector
#print in_decode_ar
#print in_decode_hash
decode(input_vector, in_decode_ar, in_decode_hash)

