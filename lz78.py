### lz78 algorithm
### using dictionary
import json

comp_dict = []
decomp_dict = []

''' Compress_LZ78
	==> input : input string
	==> output : dictionary & bit of this dictionary
	==> e.g: [[0, 'w'], [0, 'a'], [0, 'b'], [3, 'a'], [0, '_'], [1, 'a'], [3, 'b'], [2, '']]
'''
def Compress_LZ78(input):
    compress_dict = ['']	### init a dict with empty string
    word = ''				### empty char
    i = 0					### index
    for key in input:		### iterate input
        i += 1			
        word += key			### append a string
        if not word in compress_dict:	## word is not in dict
        	compress_dict.append(word)	## append compress_dict
        	comp_dict.append([compress_dict.index(word[:-1]), word[-1]])
        	word = ''
        elif i == len(input):	## if yes
        	comp_dict.append([compress_dict.index(word), ''])
        	word = ''
        else:
        	pass
    return comp_dict, bitMapping(comp_dict)

''' Decompress_LZ78
	==> input: input string as compressed string (obtained from Compress_LZ78)
	==> output : 2 params ==> dictionary & original string
	==> e.g : ... & wabba_wabba_wabba_woo_woo
'''
def Decompress_LZ78(compressedInput):
    p = ""
    outString = ""
    for (i, j) in compressedInput:	### compressedInput is a dict <key, value>
        if i is not 0:				### if dict is exisr -> recursive the decompression
        	p = decomp_dict [i-1]
        else:					### empty dict
        	p = ""
        decomp_dict.append(p + j)
    for s in decomp_dict :			### concat string to have original string
        outString += s
    return dictMapping(bitMapping(decomp_dict)), outString	### return a dict and original string

''' bitMapping  ==> convert a dict to bit (0,1)'''
def bitMapping(inputDict):
    str = json.dumps(inputDict)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)
    return binary

''' dictMapping ==> convert bit to dict'''
def dictMapping(inputBin):
     jsn = ''.join(chr(int(x, 2)) for x in inputBin.split())
     d = json.loads(jsn)  
     return d

# #### simple test ==> please uncomment to test 

# ## Uncomment to test
# data = 'wabba_ wabba_ wabba_ wabba_ wabba_ wabba_ wabba_woo_woo_woo_woo'
# print("original_string_is : ", data)
# print("************************************************************************************************************************************************************************************")

# # # # compress data	==> return a dict
# compress_data,bin_comp_data = Compress_LZ78(data)
# print("compressed_dict : ", compress_data)
# print("compressed_data_by_binary : ",  bin_comp_data)

# # # # decompress data ==> return a dict and original string
# print("************************************************************************************************************************************************************************************")
# decompress_data,original_string = Decompress_LZ78(compress_data)
# print("decompressed_dict : ", decompress_data)
# print("original_string : ",  original_string)

# # # #### compress ratio = original_size / compress_size
# print("compress_ratio : ", (len(compress_data)/len(data) * 100), "%")

# with open("testcase1", "w") as f:
# 	f.write("original_string_is : \r\n" + data)
# 	f.write("************************************************************************************************************************************************************************************")

# 	f.write("compressed_dict : \r\n"+ str(compress_data))
# 	f.write("compressed_data_by_binary : \r\n"+  str(bin_comp_data))

# 	f.write("************************************************************************************************************************************************************************************")

# 	f.write("decompressed_dict : \r\n" + str(decompress_data))
# 	f.write("original_string : \r\n" +  str(original_string))

# 	f.write("compress_ratio : " + str((len(compress_data)/len(data) * 100)) + "%")





# ### complex test with text file
file = "dameCamelia.txt"
compress_data = []

with open(file, "r") as file:
	data = file.read()
	data_size = len(data)
	_,bin_comp_data = Compress_LZ78(data)

	with open("lz78_coded_dame.txt","w") as f:
		compress_data,_ = Compress_LZ78(data)
		f.write(str(compress_data))

	with open("lz78_decoded_dame.txt", "w") as f:
		_,decompress_data = Decompress_LZ78(compress_data)
		f.write(str(decompress_data))

	with open("testcase6.txt", "w") as f:
		ratio = len(compress_data) / data_size
		f.write("ratio is : " + str(ratio*100) + "%")
