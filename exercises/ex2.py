"""Sort and display numeric values from a mixed list."""


def main(data):
    temp = []
    for item in data:
        if isinstance(item, int) or isinstance(item, float):
            temp.append(item)
        else:
            print(f"Skipping: {item}")
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i] > temp[j]:
                temp[i], temp[j] = temp[j], temp[i]
    for val in temp:
        print(val)

    return temp
