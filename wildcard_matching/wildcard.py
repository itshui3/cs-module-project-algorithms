s_input = 'acdcb'
p_input = 'a*c?b'

def phrase_matcher(s, p):

    s_pointer = 0
    p_pointer = 0
    while s_pointer < len(s) and p_pointer < len(s):

        if p[p_pointer] == '*':
            if p_pointer == len(p) - 1: return True

            if p[p_pointer + 1] == s[s_pointer]:
                p_pointer += 2
                s_pointer += 1

            elif p[p_pointer + 1] == '?':
                p_pointer += 2
                s_pointer += 1

            elif p[p_pointer + 1] == '*':
                p_pointer += 1

        elif p[p_pointer] == '?':
            p_pointer += 1
            s_pointer += 1

        else:
            if p[p_pointer] != s[s_pointer]: return False

            p_pointer += 1
            s_pointer += 1

    if s_pointer < len(s) or p_pointer < len(p):
        return False
    else:
        return True

print(phrase_matcher('acdcb', 'a*c?b'))