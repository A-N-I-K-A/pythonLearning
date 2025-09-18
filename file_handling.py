with open("file1.txt","a+") as f:
    f.write("\nBye Bye")
    f.seek(0)
    for data in f:
        print(data)