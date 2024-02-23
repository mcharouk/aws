import os

import pandas

# get the current working directory
current_working_directory = os.getcwd()
# print output to the console
print("current directory : " + current_working_directory)

if current_working_directory.endswith("Demos"):
    new_wd = "Module_4/DynamoDB"
    print("changing working directory to " + current_working_directory + "/" + new_wd)
    os.chdir(new_wd)

# read file in Raw-file/all-in-one.csv
# split it in as many files as lines
# write files in Sample-data folder


def split_file(file_path, sample_data_path):
    df = pandas.read_csv(file_path, header=0)
    file_index = 0

    # get first line as dataframe

    for index, row in df.iterrows():
        file_name = "file-{0}.csv".format(file_index)
        file_path = os.path.join(sample_data_path, file_name)
        # get first row as dataframe

        split_df = df.iloc[[file_index]]

        print(split_df)
        with open(file_path, "w") as f:
            # data frame to csv, don't write index
            split_df.to_csv(f, index=False, lineterminator="\n")

        file_index += 1


# split_file("Raw-file/all-in-one.csv", "Sample-data")
