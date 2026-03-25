import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there my name is Sunny Thapa"

tokens = enc.encode(text)

print("Encoded Tokens", tokens)


decoded = enc.decode([25216, 1354, 922, 1308, 382, 66035, 748, 7063])
print("Decoded TOkens", decoded)

