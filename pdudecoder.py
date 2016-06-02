def extract_value(input_ar, decode_ar, start_index):
    value = "" + str(input_ar[start_index])
    for a_i in range(start_index+1, len(input_ar)):
        if decode_ar[a_i] <> decode_ar[start_index]:
            break
        else:
            value += str(input_ar[a_i])
    return (int(value,2), a_i-1)

def decode(input_ar, decode_ar, decode_hash):
    for a_i in range(len(input_ar)):
        if decode_ar[a_i] <> 0:
            value, new_pos = extract_value(input_ar, a_i)
            print decode_hash[decode_ar] + ": " + str(value)
            a_i = new_pos






