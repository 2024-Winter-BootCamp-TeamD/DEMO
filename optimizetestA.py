def find_duplicates(data_list):
    duplicates = []
    for i in range(len(data_list)):
        for j in range(i+1, len(data_list)):
            if data_list[i] == data_list[j] and data_list[i] not in duplicates:
                duplicates.append(data_list[i])
    return duplicates

sample_data = [3, 5, 3, 2, 7, 2, 5, 10]
print("Duplicates:", find_duplicates(sample_data))