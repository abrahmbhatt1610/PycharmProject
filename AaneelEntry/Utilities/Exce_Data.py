import pandas as pd

df = pd.read_excel('C:/Users/HP/Downloads/Aaneel status Entry.xlsx')

df["Appointment"] = pd.to_datetime(df['Appointment'], format='%Y%m%d')

for row in range(df.shape[0]):

    patient_last_name = df.at[row, "Patient last name"]
    patient_first_name = df.at[row, "PatientFirstname"]
    appoint_date = df.at[row, "Appointment"].strftime('%m/%d/%Y')

    print(patient_first_name, patient_last_name, appoint_date)


# import openpyxl
#
# wrkbk = openpyxl.load_workbook("C:/Users/HP/Downloads/Aaneel status Entry.xlsx")
#
# sh = wrkbk.active

# for i in range(1, sh.max_row + 1):
#     print("\n")
#     print("Row", i, "data:")
#     for j in range(1, sh.max_column + 1):
#         cell_obj = sh.cell(row=i, column=j)
#         print(cell_obj.value, end=" ")

# for row in sh.iter_rows(min_row=2, min_col=1, max_row=12, max_col=10):
#     for cell in row:
#         print(cell.value, end=" ")
#         print("Coming")
#         print("good")
#     # print("Dear")
