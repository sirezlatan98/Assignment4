try:
    with open("output.txt","a+") as fh:
        data=input("Enter text to write to the file:")
        fh.write(data)
        print("Data successfully written to 'output.txt'")
        data=input("Enter additional text to append:")
        fh.write(data)
        print("final content of 'output.txt'")
        fh.seek(0)
        data=fh.readlines()
        for i in range(len(data)):
            print(f"Line{i+1}: {data[i].strip('\n')}")
except:
    print("Some error occurred")