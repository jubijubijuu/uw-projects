USE project_info330_Shoes_2

EXECUTE populateCustomer
@CustTName = 'Individual',
@CustFName = 'Jerome',
@CustLname = 'Oreo',
@CustAddress = '123 Sunset Ave',
@CustCity = 'Renton',
@CustState = 'WA'

EXECUTE populateOrder
@CustFName = 'Jerome',
@CustLName = 'Oreo',
@CustAddress = '123 Sunset Ave',
@EmpNum = 420,
@OrderDate = '03/17/2016'

EXECUTE populateModel
@MaName = 'Adidas',
@MaDescr = 'Thanks Kanye West',
@PName = 'Running',
@PDescr = 'Used for everyday use and track people',
@MoName = 'NMD Triple Black',
@MoDescr = null

EXECUTE populateProduct
@MName = 'NMD Triple Black',
@MDescr = null,
@Color = 'black',
@Size = 8.0

EXECUTE populateLineItem
@OrderDate = '03/17/2016',
@Color = 'black',
@Size = 8.0,
@Quantity = 7,
@Price = 169.00

SELECT * FROM tblProduct