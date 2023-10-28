
## Writing into an files
with open("just.txt", "w" ,encoding='utf-8') as file:
    file.write("import pandas as np\n")
    
    
    ## reading the file
with open("just.txt", "r" ,encoding='utf-8') as file:

    content = file.read()


    print(content)