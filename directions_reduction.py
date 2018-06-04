def dirReduc(arr):

    patterns = [["NORTH", "SOUTH"], ["SOUTH", "NORTH"], ["EAST", "WEST"], ["WEST", "EAST"]]

    for i in range(0, len(arr)):
        for combo in patterns:
            if combo == arr[i:i+2]:
                del arr[i:i+2]
                dirReduc(arr)

    return arr


if __name__ == '__main__':
    # input_data = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    input_data = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]
    print(dirReduc(input_data))
