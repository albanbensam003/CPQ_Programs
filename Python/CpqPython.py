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


#Insert Container Data

get_cont_data = Product.GetContainerByName('Container_Name')

custom_table_records = {}

for data in custom_table_records:
    row_insert = get_cont_data.AddNewRow(True)
    row_insert['Emp_Name'] = data['Emp_Name']
    row_insert.Calculate()
get_cont_data.ApplyProductChanges()

# Get Container Records
get_cont_data = Product.GetContainerByName('COntain_Name').Rows

#Set Dropdown Values
Product.Attr('DropDown_Attr_Name').SelectValues('HardWare')

#Get Attribute Values
Product.Attr('AttriBute_Name').GetValue()

#Assign Text box Field Value
Product.Attr("Attribute_Name").AssignValue()

#Get Custom Field Value
context.Quote.GetCustomField('CustomField').Value

#Get Quote AutoComplete Value
context.Quote.GetCustomField('AutoCompleteValue').AttributeValue

#Set CustomField Value
context.Quote.GetCustomField('CF_Account_Country').Value = 'Test'

#Assign AutoComplete Value
Product.Attr('AutoCompleteValue').SelectDisplayValue("Values")
Product.Attr('AutoCompleteValue').AssignValue('Values')

#Show and Hide Attr Values in DropDown
Product.SelectAttrValues('SFDC_Sub_Solution_CAT_Family', list())
Product.DisallowAttrValues('SFDC_Sub_Solution_CAT_Family',tuple())
Product.AllowAttrValues('SFDC_Sub_Solution_CAT_Family',tuple())

#Count Of SAP CPQ Tables
data_insert = context.Quote.QuoteTables['Quote_Details']
data_insert.AddNewRow()
Trace.Write(data_insert.Rows.Count)

#Get All sys_table in SAP CPQ
show_all_table = SqlHelper.GetList("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES where table_name like '%sys_%'")

for data in show_all_table:
    Trace.Write(data.TABLE_NAME)


#Get Overall table count
get_show_tables = SqlHelper.GetFirst("SELECT count(table_name) as tbl_name from information_schema.tables")
Trace.Write(get_show_tables.tbl_name)

#Fetch 1000 to 2000 inbetween records
get_show_tables = SqlHelper.GetList("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES ORDER BY TABLE_NAME OFFSET 999 rows FETCH NEXT 1000 ROWS ONLY")
Trace.Write(get_show_tables)


#Get quote details
quote = QuoteHelper.Get("1234") # Quote ID
get_quote_tbl = quote.QuoteTable['Quote_Details']

#Get Current Quote ID
get_quote_id = context.Quote.Id