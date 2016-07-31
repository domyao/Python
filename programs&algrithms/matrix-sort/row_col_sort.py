



def row_col_sort(filename):

    with open(filename) as nf:
        data = [[int(x) for x in line.split()] for line in nf]    # from http://stackoverflow.com/questions/6583573/how-to-read-numbers-from-file-in-python

    row_sum_idx_dict = sum_of_row_idx_dictionary(data)
    col_sum_idx_dict = sum_of_col_idx_dictionary(data)

    print("\nRow Sums:", sums_in_string(row_sum_idx_dict), sep= " ")
    print("\nColumn Sums:", sums_in_string(col_sum_idx_dict), sep= " " )
    print

    row_sum_sort = sorted(row_sum_idx_dict.items(), key = lambda item: item[1] )
    col_sum_sort = sorted( col_sum_idx_dict.items(), key = lambda item: item[1] )

    print("\n")
    print_rows_sorted(data, row_sum_sort)
    print("\n")
    print_cols_sorted(data, col_sum_sort)


#creat a dictionary with keys being the idx of the rows, values being the sums of each row.

def sum_of_row_idx_dictionary(data):
    row_sum_idx_dict = {}

    for col_idx, row in enumerate(data):
        row_sum_idx_dict[col_idx] = sum(row)

    return row_sum_idx_dict


#creat a dictionary with keys being the idx of the cols, values being the sums of each col.

def sum_of_col_idx_dictionary(data):
    col_sum_idx_dict = {}

    row_idx = 0

    while row_idx < len(data[0]):
        col_sum_idx_dict[row_idx] = 0
        col_idx = 0

        while col_idx < len(data):
            col_sum_idx_dict[row_idx] += data[col_idx][row_idx]
            col_idx += 1

        row_idx += 1

    return col_sum_idx_dict





def sums_in_string(sum_idx_dict ):


    idx = 0
    sums = []

    while idx < len(sum_idx_dict):
        sums.append(sum_idx_dict[idx])
        idx += 1

    return to_string(sums)     #use to_stirng func to convert a list of numbers into a stirng









# Fuctions for printing

def print_rows_sorted(data, row_sum_sort):
    idx = 0
    while idx < len(row_sum_sort):
        print( to_string( data[ row_sum_sort[idx][0] ] ) )
        idx += 1




def print_cols_sorted(data, col_sum_sort):

    row_idx = 0

    while row_idx < len(data):
        new_row = []
        idx = 0

        while idx < len(col_sum_sort):
            new_row.append( data[row_idx] [ col_sum_sort[idx][0] ] )
            idx += 1

        row_idx += 1

        print(to_string(new_row))




def to_string(num_list):
    return "  ".join(str(x) for x in num_list )



# ['10 5 4 20', '9 33 27 16', '11 6 55 3']
# [['10', '5', '4', '20'], ['9', '33', '27', '16'], ['11', '6', '55', '3']]
