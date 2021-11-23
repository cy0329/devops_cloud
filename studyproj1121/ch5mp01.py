import string

string.whitespace
" \t\n\r\x0b\x0c"
string.punctuation
blurt = "what the...!!?"
print(blurt.strip(string.punctuation))

prospector = "What in tarnation ...??!!"
print(prospector.strip(string.whitespace + string.punctuation))
