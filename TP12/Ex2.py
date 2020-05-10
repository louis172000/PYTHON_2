def reverse_string(s, i=0):
    """Reverses the string s recursively """
    if i == len(s):
        return ""
    return reverse_string(s, i+1) + s[i]


print("1-", reverse_string(""))  # ""
print("2-", reverse_string("bonjour"))  # ruojnob
print("3-", reverse_string("ressasser"))  # ressasser
