def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


   #write from project description

	with open(file2, 'r') as b:
    data_b = b.read()

     #write from project description


    with open(file2, 'w') as b:
    b.write(data_a)

swapFileData()
