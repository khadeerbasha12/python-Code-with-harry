with open("sample.txt") as f:
    d=f.read().lower()

if "python" in d:
    print("present")
else:
    print("not present")