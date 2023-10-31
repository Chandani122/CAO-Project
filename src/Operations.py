import pandas as pd
import streamlit as st

def right_shift(acc, q, q0):
    acc = list(acc)
    q = list(q)
    q0 = list(q0)
    temp1 = acc[len(acc) - 1]
    q0 = q[len(q) - 1]

    for i in range(len(acc) - 1, 0, -1):
        acc[i] = acc[i - 1]

    for i in range(len(q) - 1, 0, -1):
        q[i] = q[i - 1]
        
    q[0] = temp1
    acc = "".join(acc)
    q = "".join(q)
    q0 = "".join(q0)
    
    return acc, q, q0

def twoscomplement(m):
    m = list(m)
    for i in range(len(m)-1, -1, -1):
        if m[i] == "0":
            m[i] = "1"
        elif m[i] == "1":
            m[i] = "0"
            
    m = "".join(m)
    ans = add(m, "1")
    ans = "".join(ans)
    
    return ans
            
def fadd(x, y, cin):
    a = int(x, 2)
    b = int(y, 2)
    cin = int(cin, 2)
    sum_out = a ^ b ^ cin
    carry_out = (a & b) | ((a ^ b) & cin)
    
    return bin(sum_out)[2:], bin(carry_out)[2]

def add(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    carry = "0"
    result = ""
    for i in range(max_len - 1, -1, -1):
        sum_out, carry = fadd(a[i], b[i], carry)
        result = sum_out + result

    result = list(result)
    carry = list(carry)
    for i in range(len(result)):
        carry.append(result[i])

    temp = []
    for i in range(len(result)+1):
        if i == 0:
            pass
        else:
            temp.append(carry[i])
    temp = "".join(temp)
    
    return temp

def restore(acc, q, m):
    comp = twoscomplement(m)
    temp = add(acc, comp)
    q = list(q)
    if temp[0] == "0":
        q[len(q)-1] = "1"
        acc = temp
    elif temp[0] == "1":
        q[len(q)-1] = "0"
        
    q = "".join(q)
    
    return acc, q

def shift_left(acc, q) :
    acc = list(acc)
    q = list(q)
    temp = q[0]
    for i in range(len (acc) -1) :
        acc[i] = acc[i+1]
    acc[len(acc)-1] = temp
    
    for i in range(len (q) - 1) :
        q[i] = q[i+1]
    q[len(q) - 1] = "_"
    
    acc = "".join(acc)
    q = "".join(q)
    
    return acc, q

def binaryaddition(x, y):
    result_str = f"Binary Addition of {x} and {y}\n\n"
    x_bin = bin(int(x))[2:]
    y_bin = bin(int(y))[2:]
    n = max(len(x_bin), len(y_bin)) + 1
    x_bin = x_bin.zfill(n)
    y_bin = y_bin.zfill(n)
    result_str += f"\t{x_bin}\n"
    result_str += f"\t{y_bin}\n"
    result = add(x_bin, y_bin)
    result_str += f"\t{'-' * n}\n"
    result_str += f"\t{result}\n"
    result_str += f"\t{'-' * n}\n"
    result = int(result, 2)
    result_str += f"\nResult: {result}"
    st.write(result_str)
    
    return result

def binarysubtraction(x, y):
    result_str = f"Binary Subtraction of {x} and {y}\n\n"
    x_bin = bin(int(x))[2:]
    y_bin = bin(int(y))[2:]
    n = max(len(x_bin), len(y_bin)) + 1
    x_bin = x_bin.zfill(n)
    y_bin = y_bin.zfill(n)
    result_str += f"\t{x_bin}\n"
    result_str += f"\t{y_bin}\n"
    comp = twoscomplement(y_bin)
    result = add(x_bin, comp)
    result_str += f"\t{'-' * n}\n"
    result_str += f"\t{result}\n"
    result_str += f"\t{'-' * n}\n"
    result = int(result, 2)
    result_str += f"\nResult: {result}"
    st.write(result_str)
    
    return result

def boothmultiplication(x, y):
    x_bin = bin(int(x))[2:]
    y_bin = bin(int(y))[2:]
    n = max(len(x_bin), len(y_bin)) + 1
    x_bin = x_bin.zfill(n)
    y_bin = y_bin.zfill(n)
    a = 0
    acc = f"{a:0{n}b}"
    q = y_bin
    q0 = "0"
    
    steps = []
    
    for i in range(n, 0, -1):
        lsb = int(q) & 1
        comp = str(lsb) + q0
        if (comp == "00" or comp == "11"):
            acc, q, q0 = right_shift(acc, q, q0)
            steps.append((i, acc, q, q0, "Arithmetic Right Shift"))
        elif (comp == "01"):
            acc = add(acc, x_bin)
            acc, q, q0 = right_shift(acc, q, q0)
            steps.append((i, acc, q, q0, "A<-A+M and Arithmetic Right Shift"))
        elif (comp == "10"):
            xcomp = twoscomplement(x_bin)
            acc = add(acc, xcomp)
            acc, q, q0 = right_shift(acc, q, q0)
            steps.append((i, acc, q, q0, "A<-A-M and Arithmetic Right Shift"))
    
    result = acc + q
    result = int(result, 2)
    
    st.write(f"Booth Multiplication of {x} and {y}")
    st.write(pd.DataFrame(steps, columns=["Count", "A", "Q", "Q0", "Operation"]))
    st.write(f"Product: {result}")
    
    return result

def restoringdivision(y, x):
    x_bin = bin(int(x))[2:]
    y_bin = bin(int(y))[2:]
    n = max(len(x_bin), len(y_bin)) + 1
    x_bin = x_bin.zfill(n)
    y_bin = y_bin.zfill(n)
    a = 0
    acc = f"{a:0{n}b}"
    q = y_bin
    steps = []

    for i in range(n, 0, -1):
        acc, q = shift_left(acc, q)
        steps.append((i, acc, q, "Shift Left"))

        temp = acc
        acc, q = restore(acc, q, x_bin)
        if acc == temp:
            steps.append((i, acc, q, "A<-A-M, Q[0] = 0 & Restore A"))
        else:
            steps.append((i, acc, q, "A<-A-M & Q[0] = 1"))

    st.write(f"Restoring division of {y} by {x}")
    st.write(pd.DataFrame(steps, columns=["Count", "A", "Q", "Operation"]))
    st.write(f"Quotient: {int(q,2)}\nRemainder: {int(acc,2)}")
    
    return int(acc,2), int(q,2)

def nonrestoringdivision(y, x):
    x_bin = bin(int(x))[2:]
    y_bin = bin(int(y))[2:]
    n = max(len(x_bin), len(y_bin)) + 1
    x_bin = x_bin.zfill(n)
    y_bin = y_bin.zfill(n)
    a = 0
    acc = f"{a:0{n}b}"
    q = y_bin
    
    steps = []

    for i in range(n, 0, -1):
        if acc[0] == "0":
            acc, q = shift_left(acc, q)
            steps.append((i, acc, q, "Shift Left"))
            temp = twoscomplement(x_bin)
            acc = add(acc, temp)
            steps.append((i, acc, q, "A<-A-M"))
        elif acc[0] == "1":
            acc, q = shift_left(acc, q)
            steps.append((i, acc, q, "Shift Left"))
            acc = add(acc, x_bin)
            steps.append((i, acc, q, "A<-A+M"))

        q = list(q)
        if acc[0] == "0":
            q[len(q) - 1] = "1"
            q = "".join(q)
            steps.append((i, acc, q, "Q[0] = 1"))
        elif acc[0] == "1":
            q[len(q) - 1] = "0"
            q = "".join(q)
            steps.append((i, acc, q, "Q[0] = 0"))

    if acc[0] == "1":
        acc = add(acc, x_bin)
        steps.append((1, acc, q, "A<-A+M"))
    
    st.write(f"Non-restoring division of {y} by {x}")
    st.write(pd.DataFrame(steps, columns=["Count", "A", "Q", "Operation"]))
    st.write(f"Quotient: {int(q,2)}\nRemainder: {int(acc,2)}")
    
    return int(acc,2), int(q,2)