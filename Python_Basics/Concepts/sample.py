# File path for the sample file

file_path = 'C:\\Users\\Abhisekh\\Desktop\\Python_basics\\Python_concepts\\file.txt'

#function for reading files
def read_file(path) :
    file = open(path, 'r')
    sentence = file.readline()
    file.close()
    return sentence

sample_message = read_file(file_path)
print(sample_message)

# reading first 2 messages:
file_path_1 = 'C:\\Users\\Abhisekh\\Desktop\\Python_basics\\Python_concepts\\file_1.txt'
file_path_2 = 'C:\\Users\\Abhisekh\\Desktop\\Python_basics\\Python_concepts\\file_2.txt'

message_1 = read_file(file_path_1)
print(message_1)

message_2 = read_file(file_path_2)
print(message_2)



# Implementing integer(floor) division of message_b over message_a
def fuse_msg(message_a, message_b) :
    quotient = int(message_b) // int(message_a)
    return str(quotient)

secret_msg_1 = fuse_msg(message_1, message_2)
print(secret_msg_1)


# Decoding message 3:
file_path_3 = 'C:\\Users\\Abhisekh\\Desktop\\Python_basics\\Python_concepts\\file_3.txt'
message_3 = read_file(file_path_3)
print(message_3)

def substitute_msg(message_c) :
    if message_c == 'Abhishek':
        sub = 'Python developer'
    if message_3 == 'Hemant':
        sub = 'Data Scientist'
    if message_3 == 'Omkar':
        sub = 'Database Developer'
    return sub

secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)


# File path for message 4  and message 5
# Decoding message 4 & 5
file_path_4 = 'C:\\Users\\Abhisekh\\Desktop\\Python_basics\\Python_concepts\\file_4.txt'
file_path_5 = 'C:\\Users\\Abhisekh\\Desktop\\Python_basics\\Python_concepts\\file_5.txt'

message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4)
print(message_5)

#comparing and taking only unique words from message 4
def compare_msg(message_d, message_e) :
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [i for i in a_list if not i in b_list]
    print(c_list)
    final_msg = " ".join(c_list)
    return final_msg

secret_msg_3 = compare_msg(message_4, message_5)
print(secret_msg_3)



# another message 6
file_path_6 = 'C:\\Users\\Abhisekh\\Desktop\\Python_basics\\Python_concepts\\file_6.txt'
message_6 = read_file(file_path_6)
print(message_6)

def extract_msg(message_f):
    a_list = message_f.split()                       #splitting sentence to list of words
    even_word = lambda x : (len(x) % 2 == 0)         #condition to check even no. of letters in a word
    b_list = list(filter(even_word, a_list))         #filtering words divisible by 2 from list of words
    final_msg = ' '.join(b_list)                     #converting from list to sentence separated by space ' '
    return final_msg

secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)



#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

final_path= 'C:\\Users\\Abhisekh\\Desktop\\Python_basics\\Python_concepts\\secret_message.txt'

secret_msg = ' '.join(message_parts)

def write_file(secret_msg, path):
    f = open(path, 'a+')
    f.write(secret_msg)
    f.close()

write_file(secret_msg, final_path)
print(secret_msg)