
# lines = ['I am a line', 'So am I', 'I am not a line, oh wait, yeah i am']

# with open('data/demo.txt', mode='w') as f:
#     #do stuff
#     f.write(str(lines[0]) + '\n')

#     for line in lines[1:]:
#         f.write(str(line)+ '\n')

# print('done writing to file' + '\n')


# with open('data/demo.txt', mode='r') as f:
#     lines = []

#     line = True
#     while line:
#         line = f.readline()
#         if line:
#             lines.append(line[:-1])

# print(lines)


# import csv

# results = []

# with open('data/Demographic_Statistics_By_Zip_Code.csv', mode='r') as f:
#     # print(type(f))

#     lines = csv.reader(f, delimiter=',')

#     # print(type(lines))

#     for line in lines:
#         results.append(line)

# # print(results[0][0], results[0][1])
# # print(results[1][0], results[1][1])
# # print(results[1])

# results_to_write = results[0:101]

# # trim to 4 cols
# for i,row in enumerate(results_to_write):
#     results_to_write[i] = row[0:5]

# print(results_to_write)

# with open('data/demo_out.csv', mode='w') as f:
#     writer = csv.writer(f)
#     writer.writerows(results_to_write)



import pandas as pd

df = pd.read_csv('data/Demographic_Statistics_By_Zip_Code.csv')

# print(type(df))

# print(df.head())
# print(df.columns)
# print(df.dtypes)
# cols = list(df.columns)
# print(df[cols[0]][0:100])

print(f"Participants in { df['JURISDICTION NAME'][0] }: { df['COUNT PARTICIPANTS'][0] }")