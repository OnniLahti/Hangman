
def csv_to_list(csv):
    csv_list_2d = []    # defining a new list for the 2d list version
    csv_list = csv.split("/n")    # splitting the list from the new line

    for i in range(len(csv_list)):    # iterating for the list length
        csv_split = csv_list[i].split(",")    # splitting the list from ','
        csv_list_2d.append(csv_split)    # adding the split to 2d list
    print(csv_list_2d)

csv_to_list("1,Jussi,Virtanen/n2,Pekka,Keinänen")