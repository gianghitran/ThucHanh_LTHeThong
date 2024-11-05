# Gia tri tu v9 den v13
bien = [96, 43, 109, 116, 126]

# Doi dai user va pass
len = 9

# Tinh v6
def find_v6(username):
    v6 = [''] * len
    for i in range(len):
        if i <= 1:
            v6[i] = ord(username[i + 2])  # s[i + 2]
        elif 1 < i <= 3:
            v6[i] = ord(username[i + 5])  # s[i + 5]
        else:
            v6[i] = bien[i - 4]  
    return v6

# Tim pass dua tren username va v6
def find_pass(username):
    v6 = find_v6(username)
    password = [''] * len
    for i in range(len):
        v2 = ord(username[i])
        v6_value = v6[len - i - 1]
        password[i] = chr((v2 + v6_value) // 2)
    return ''.join(password)

# username: 792005802
username = "792005802"
password = find_pass(username)

print(f"name: {username}")
print(f"pass: {password}")
