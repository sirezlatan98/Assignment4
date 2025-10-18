#METHOD 1

"""x=1
try:
    with open("sample.txt","rt") as fh:
        data=fh.readline()
        while data!="":
            print(f"Line{x}: {data.strip('\n')}")
            x=x+1
            data=fh.readline()
except FileNotFoundError:
    print(f"Error: The File 'sample.txt' was not found.")
"""

#METHOD 2

try:
    with open("sample.txt","rt") as fh:
        data=fh.readlines()
        for i in range(len(data)):
            print(f"Line{i+1}: {data[i].strip('\n')}")
except FileNotFoundError:
    print(f"Error: The File 'sample.txt' was not found.")
