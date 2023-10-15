def encode(data):
    if not data:
        return []

    def encode_helper(data, current, count, result):
        if not data:
            if count == 1:
                result.append(current)
            else:
                result.extend([current, count])
            return result

        if current is None:
            return encode_helper(data[1:], data[0], 1, result)

        if data[0] == current:
            return encode_helper(data[1:], current, count + 1, result)

        if count == 1:
            result.append(current)
        else:
            result.extend([current, count])

        return encode_helper(data[1:], data[0], 1, result)

    return encode_helper(data[1:], data[0], 1, [])

# Приклад використання:
decoded_list = ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']
encoded_list = encode(decoded_list)
print(encoded_list)