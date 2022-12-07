import pandas as pd
df = pd.read_excel('C:/Users/HP/Downloads/Python_practice.xlsx')
x = df["Visit Number"]
print(x)
for i in x:
    visitid = i
    visit = "^" + str(visitid)
    print(visit)






# import openpyxl

# Define variable to load the dataframe
# dataframe = ("C:/Users/HP/Downloads/Patient Balance Report 10.31.2022.xlsx")

# Define variable to read sheet
# dataframe1 = dataframe.active

# # Iterate the loop to read the cell values
# for row in range(0, dataframe1.max_row):
#     for col in dataframe1.iter_cols(1, dataframe1.max_column):
#         print(col[row].value)