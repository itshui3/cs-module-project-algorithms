Given two strings, s and p, determine if they match given 2 rules
s is only normal characters
p has 2 special characters that have special matching properties '*' and '?'

1] '?' Matches any single character in s
2] '*' Matches any sequence of characters(including a 0 length sequence)

acdcb
a*c?b
not a match

'a' and 'a'
'cd' and '*'
'c' and 'c'
'b' and '?'
'nothing left' doesn't match leftover 'b' in p

