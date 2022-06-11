d=True
i=1
with open("sample.txt") as f:
    while(d):
        d=f.readline().lower()
        if "python" in d:
            print(d,end="")
            print(f"present on line number={i}")
        i+=1