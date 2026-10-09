def read_file(filename):
    file = open(filename , "r")
    text = file.read()
    file.close()
#     return text 
# or with open(filename , "r") as file :
#     text = file.read()
#     return text

