# Insert Custom table records
set_data = [
    {
        "emp_name": "Test Data",
        "emp_id": 1001
    },{
        "emp_name": "Test Data 1",
        "emp_id": 1002
    }
]

get_ct_tbl = SqlHelper.GetTable("CT_Employee")

for data in set_data:
    get_ct_tbl.AddRow(data)

SqlHelper.Upsert(get_ct_tbl)

# Update custom table records
employee_records = [
    {
        "emp_name": "Test data",
        "CpqTableEntryId": 1
    },{
        "emp_name": "Test data 1",
        "CpqTableEntryId": 2
    },{
        "emp_name": "Test data 2",
        "CpqTableEntryId": 3
    }
]

get_table_update = SqlHelper.GetTable('CT_Employee')

for data in employee_records:
    get_table_update.AddRow(data)

SqlHelper.Upsert(get_table_update)

#Delete cstome table records
fetch_data = SqlHelper.GetList("select CpqTableEntryId from CT_Employee")

get_table_del = SqlHelper.GetTable("CT_Employee")

for data in fetch_data:
    get_table_del.AddRow(data)

SqlHelper.Delete(get_table_del)


