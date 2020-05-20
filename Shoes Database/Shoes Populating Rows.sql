USE project_info330_Shoes_2

-- Populating ManuType (done)
EXECUTE populateManuType
@MName = 'Company',
@MDescr = 'Group of people'

-- Populating Manu (done)
EXECUTE populateManu
@MTName = 'Company',
@MTDescr = 'Group of people',
@MName = 'Adidas',
@MDescr = 'Thanks Kanye West'

EXECUTE populateManu
@MTName = 'Company',
@MTDescr = 'Group of people',
@MName = 'Nike',
@MDescr = 'Just do it!'

-- Populating Style (done)
EXECUTE populateStyle
@SName = 'low top',
@SDescr = 'Shorter shoe'

EXECUTE populateStyle
@SName = 'high top',
@SDescr = 'Taller shoe'

-- Populating Purpose (done)
EXECUTE populatePurpose
@SName = 'low top',
@SDescr = 'Shorter shoe',
@PName = 'Running',
@PDescr = 'Used for everyday use and track people'

EXECUTE populatePurpose
@SName = 'high top',
@SDescr = 'Taller shoe',
@PName = 'Basketball',
@PDescr = 'Used for everyday use and hoopin'

-- Populating Model (not done)
EXECUTE populateModel
@MaName = 'Adidas',
@MaDescr = 'Thanks Kanye West',
@PName = 'Running',
@PDescr = 'Used for everyday use and track people',
@MoName = 'Ultra Boost Clima',
@MoDescr = 'Comes in black, red and green'

EXECUTE populateModel
@MaName = 'Nike',
@MaDescr = 'Just do it!',
@PName = 'Basketball',
@PDescr = 'Used for everyday use and hoopin',
@MoName = 'Air Force 1',
@MoDescr = 'First Nike basketball shoes'

SELECT * FROM tblManufacturer
SELECT * FROM tblManufacturerType
SELECT * FROM tblStyle
SELECT * FROM tblPurpose
SELECT * FROM tblModel