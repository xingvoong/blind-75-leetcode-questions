'''
design an algorithm to encode and decode a list of string to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 does:

string encoded_string = encode(str)

and machine 2 does:
vector<string> strs2 = decode(encoded_string)

implement the encode and decode methods

you are not allowed to solve the problem using any serialize method (such as eval)

- the problem is to encode and decode strings, which includes creating a single string from a list of strings and then reverting it back to the original list of strings. this can be tricky since any string can contain any ASCII characters

- to accomplish this, we often use a delimiter, which is a character or sequence of characters that we insert between each string when we combine them into one. The key about a delimeter is that it must be a character or sequence of characters that doesn't occur in the strings we're encoding. this allow us to correctly separate the strings when we decode them.

Algorithm

'''

class Codec:
    def encode(self, strs):
        """encodes a list of strings to a single string"""
        print("❤️".join(strs))
        return "❤️".join(strs)

    def decode(self, s):
        """decode a single strings to a list of strings"""
        print(s.split("❤️"))
        return s.split("❤️")

str1 = ["Hello","World"]
codec = Codec()
print(codec.decode(codec.encode(str1)))

str2 = ["",""]
print(codec.decode(codec.encode(str2)))

'''
runtime:
n : the total number of characters across all strings in the input list
k: number of strings

space: O(k)

need extra space for delimiter (or seperator) between strings in a list

'''