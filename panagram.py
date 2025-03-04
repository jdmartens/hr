def pangrams(s):
    # Write your code here
    s = s.lower()
    abet = "abcdefghijklmnopqrstuvwxyz"
    
    for a in abet:
        try:
            found = s.index(a)
        except ValueError:
            return "not pangram"
    return "pangram"