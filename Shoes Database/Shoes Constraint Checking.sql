USE project_info330_Shoes_2

-- Checking no_shoe_jerome()
EXECUTE populateProduct
@MName = 'Ultra Boost Clima',
@MDescr = 'Comes in black',
@Color = 'black',
@Size = 9.0

EXECUTE populateCustType
@CustTypeName = 'person'

EXECUTE populateCustomer
@CustTName = 'person',
@CustFName = 'Jerome',
@CustLname = 'Orville',
@CustAddress = '123 Sunset Ave',
@CustCity = 'Renton',
@CustState = 'WA'

EXECUTE populateEmpType
@EmpTypeName = 'retail'

EXECUTE populateEmployee
@EmpTName = 'retail',
@EmpFName = 'Officer',
@EmpLname = 'Jenny',
@EmpNum = 420,
@BeginDate = '08/14/1978',
@Salary = 11.50,
@EndDate = null

EXECUTE populateOrder
@CustFName = 'Jerome',
@CustLName = 'Orville',
@CustAddress = '123 Sunset Ave',
@EmpNum = 420,
@OrderDate = '03/10/2020'

EXECUTE populateLineItem
@OrderDate = '03/10/2020',
@Color = 'black',
@Size = 9.0,
@Quantity = 4,
@Price = 192.00

-- Checking no_employee_orille()
EXECUTE populateEmpType
@EmpTypeName = 'President'

EXECUTE populateEmployee
@EmpTName = 'President',
@EmpFName = 'Donovan',
@EmpLname = 'Orille',
@EmpNum = 133,
@BeginDate = '04/20/1923',
@Salary = 60.50,
@EndDate = null

EXECUTE populateOrder
@CustFName = 'Jerome',
@CustLName = 'Orville',
@CustAddress = '123 Sunset Ave',
@EmpNum = 133,
@OrderDate = '09/25/2020'

SELECT * from tblOrder
SELECT * from tblCustomer
SELECT * from tblProduct