print("Write a long string below")
big_string = input() # ahbdngjgisabbbagdfyvnskfoeybnxmfpyuwkfbs
print("Write a substring that the program will search for:")
searched_string = input() # ab
length_big = len(big_string)
length_search = len(searched_string)
if length_search > length_big:
	print("ERROR: substring is too old")
elif length_search == length_big:
	print("Given string is: "+ big_string)
	if searched_string == big_string:
		print("String and substring are identical")
	else:
		print("String and substring aren't the same")
else:
    print("Given string is: "+ big_string)
    print("Searching for \""+ searched_string +"\"")
    a = int()
    substring = str()
    result = 0
    for a in range(0, length_big-length_search):
        substring = big_string[a:a+length_search:1]
        if searched_string == substring:
            result = 1
            print(" - substring found at index: "+ str(a))
    if result == 0:
        print("Nothing was found")