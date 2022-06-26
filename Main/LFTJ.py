import os
import gzip

import numpy as np

import Trie

# define constant
END = -1
# Variable_Order = ['x1', 'x2', 'x3', 'x1']
# Tries=[]


def report(context, output_path):
    with open(output_path, mode="a") as f:
        str_context = [str(i) for i in context]
        line = ','.join(str_context) + "\n"
        f.write(line)
        f.close()
        print(line)

def LFTJ_triangle_count(data,output_path,file_name):
    Variable_Order = ['x1', 'x2', 'x3']
    context = []

    data.dtype.names = ['X1', 'X2']
    R = Trie.Trie(data)
    data.dtype.names = ['X2', 'X3']
    S = Trie.Trie(data)
    data.dtype.names = ['X1', 'X3']
    T = Trie.Trie(data)

    Tries = [R,S,T]

    global count
    count=0

    LFTJ_count(context,Variable_Order,Tries,output_path)
    print(count)
    report([count],output_path + '\\' + file_name )
    return count


def LFTJ_count(context,Variable_Order,Tries,output_path):
    global count
    vo_i = len(context) - 1  # starting from -1
    if len(context) == len(Variable_Order):  # base case
        count += 1
        return END

    tries = position(Tries, context,Variable_Order)

    A = Variable_Order[vo_i + 1]
    tries_with_variable_A = [trie for trie in tries if A in trie.col_names]
    for tri in tries_with_variable_A:
        tri.open(A)

    while True:
        a = LF_next(tries_with_variable_A)
        if a != END:
            while True:
                r = LFTJ_count(context.append(a),Variable_Order,Tries,output_path)
                if r == END:
                    break
        else:
            break
    return END


def LFTJ_triangle_full(data,output_path,file_name):
    Variable_Order = ['X1', 'X2', 'X3']
    context = []

    data.dtype.names = ['X1', 'X2']
    R = Trie.Trie(data)

    data.dtype.names = ['X2', 'X3']
    S = Trie.Trie(data)

    data.dtype.names = ['X1', 'X3']
    T = Trie.Trie(data)

    Tries = [R, S, T]

    LFTJ_full(context, Variable_Order, Tries, output_path,file_name)



def LFTJ_full(context,Variable_Order,Tries,output_path,file_name):


    vo_i = len(context) - 1  # starting from -1

    if len(context) == len(Variable_Order):  # base case
        report(context,output_path+ '\\' + file_name )
        return END

    tries = position(Tries, context,Variable_Order)

    A = Variable_Order[vo_i + 1]
    print("run on variable "+A)

    tries_with_variable_A = [trie for trie in tries if A in trie.col_names]


    for tri in tries_with_variable_A:
        tri.open(A)


    while True:
        a = LF_next(tries_with_variable_A)

        if a != END:
            while True:
                new_context = context + [a]
                r = LFTJ_full(new_context,Variable_Order,Tries,output_path,file_name)
                if r == END:
                    break
        else:
            LF_up(tries_with_variable_A, context, Variable_Order, A)
            break
    return END



def LF_up(tries_with_variable_A,context,Variable_Order,val_name):
    for tri in tries_with_variable_A:
        tri.up(context,Variable_Order,val_name)

def position(all_Tries,context,Variable_Order):
    tries_iterable = [t for t in all_Tries if t.positioning_by_sequence(context,Variable_Order)]
    return tries_iterable









# def LFTJ_path_1_count(data,output_path):
#
# def LFTJ_path_1_full(data,output_path):
#
#
# def LFTJ_path_2_count(data,output_path):
#
# def LFTJ_path_2_full(data,output_path):
#




def key_equal(keys):
    return all(x == keys[0] for x in keys)


def LF_next(tries_leapfrog):
    keys = [trie.next2() for trie in tries_leapfrog]
    while not key_equal(keys): # will end when [-1,-1,-1]
        for i in range(len(keys)):
            if keys[i]!=(max(keys)): # and keys[i]!=END:
                keys[i]=tries_leapfrog[i].seek2(max(keys))
                if keys[i] == END:
                    return END
                if key_equal(keys):
                    if keys[0] == END: # will end when [-1,-1,-1]
                        return END;
                    return keys[0]
    return keys[0];

#
# def LFTJ(context,Variable_Order): # context is a list of values of variables such as [a1,b2,c3], starting with []
#     vo_i = len(context)-1 # starting from -1
#     if len(context)==len(Variable_Order): #base case
#         # return ([],1)
#         # return []
#     tries = position(all_Tries,context)
#
#     A = Variable_Order[vo_i +1]
#     tries_leapfrog = [trie for trie in tries if A in trie.col_name]
#
#     for tri in tries_leapfrog:
#         tri.open(A)
#
#     sum_payload = 0
#     while True:
#         a = LF_next(A, tries_leapfrog)
#         if a!=END:
#             while True:
#                 child_tuple, child_payload = LFTJ(context.append(a))
#                 if child_tuple
#                 sum_payload += child_payload
#                 # if child_tuple != END:
#                 #     if len(child_tuple) + len(context)+1 == len(Variable_Order):
#                 #         return child_tuple.insert(0,a)
#                 # else:
#                 #     break
#         else:
#             break
#     return END





