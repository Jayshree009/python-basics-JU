# read -"r"
# write - "w"
#f = open("demo.txt","r")
# content = f.read()
# print(content)

# append -a

f = open("demo.txt","a")
add_text = f.write("\nThis is in append mode")
print(add_text)
f.close()

# Len function
f = open("demo.txt","r")
data = f.read()
total_cnt = len(data)
print(total_cnt)
f.close()
