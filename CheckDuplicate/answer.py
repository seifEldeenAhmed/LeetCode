



def checkDuplicate(lst: list) -> bool:
    # Check if there are any duplicate values in the list

    return True if len(set(lst)) != len(lst) else False

print(checkDuplicate([1,2,3,4,5,6]))