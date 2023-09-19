# my program
big_string = "ahbdngjgisabbbagdfyvnskfoeybnxmfpyuwkfbs"
searched_string = "ab"
length_big = len(big_string)
length_search = len(searched_string)
print("Given string is: "+ big_string)
print("Searching for \""+ searched_string +"\"")
a = int()
substring = str()
for a in range(0, length_big-length_search):
	substring = big_string[a:a+length_search:1]
	if searched_string == substring:
		print(" - substring found at index: "+ str(a))