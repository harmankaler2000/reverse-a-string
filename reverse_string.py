print("Reverse a string")
str = input("Enter a string to reverse: ")
print("Using for loop")
str_for_reverse = ""
for i in str:
    str_for_reverse = i + str_for_reverse
print("Reversed using for loop: "+str_for_reverse)

print("Using recursion for reversal: ")

def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]

print("Reversed using recursion: " + reverse_recursion(str))

print("Using reversed keyword: ")
str_reversed = "".join(reversed(str))
print("Reversed using reversed keyword: "+str_reversed)

print("Using string slice syntax: ")
str_string_slice = str[::-1]
print("Reversed using string slice syntax: " + str_string_slice)