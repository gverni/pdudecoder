def extract_value(input_ar, decode_ar, start_index):
    value = "" + str(input_ar[start_index])
    for a_i in range(start_index+1, min(len(decode_ar), len(input_ar))):
        if decode_ar[a_i] <> decode_ar[start_index]:
            break
        else:
            value += str(input_ar[a_i])

    if a_i == len(decode_ar)- 1: #Input array bigger than decoder array. We should not decode further
        return (int(value,2), a_i)
    elif a_i == len(input_ar) -1: #Input array is smaller than decoder array. Return error
        return value, -1
    else: #Detected a different decoder function. Hence we go back one position and return
        return (int(value,2), a_i-1)

def decode(input_ar, decode_ar, decode_hash):
    a_i = 0
    while a_i <= len(input_ar)-1:
        if (a_i > (len(decode_ar) - 1)) or decode_ar[a_i] == 0: #If decode function is not specified (either 0, or array too short)
            print "[" + str(a_i) + "]: " + str(input_ar[a_i])
        else:
            value, new_pos = extract_value(input_ar, decode_ar, a_i)
            if new_pos == -1:
                print "Remaining bits: " + value
                break
            print decode_hash[decode_ar[a_i]] + ": " + str(value)
            a_i = new_pos
        a_i += 1

test_decode_ar = [1, 1, 1, 2, 3, 3, 3, 3]
test_decode_hash = {1: "first field", 2: "second field", 3: "third field"}

#Test input vector long as decoder
decode([0, 0, 1, 1, 0, 0, 1, 1], test_decode_ar, test_decode_hash)

#Test input vector longer than decoder
decode([0, 0, 1, 1, 0, 0, 1, 1, 1], test_decode_ar, test_decode_hash)

#Test input smaller than decoder
decode([0, 0, 1, 1, 0, 1], test_decode_ar, test_decode_hash)

