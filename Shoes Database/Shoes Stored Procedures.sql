USE project_info330_Shoes_2

/* Create a new stored procedure to populate tblModel
*/

GO
CREATE PROCEDURE populateModel
@MaName varchar(25),
@MaDescr varchar(50),
@PName varchar(25),
@PDescr varchar(50),
@MoName varchar(25),
@MoDescr varchar(50)
AS

DECLARE @M_ID INT, @P_ID INT

SET @M_ID = (SELECT ManuID
			 FROM tblManufacturer
			 WHERE ManuName = @MaName)

SET @P_ID = (SELECT PurposeID
			 FROM tblPurpose
			 WHERE PurposeName = @PName)

BEGIN TRAN Model1
INSERT INTO tblModel(ManuID, PurposeID, ModelName, ModelDescr)
VALUES(@M_ID, @P_ID, @MoName, @MoDescr)
COMMIT TRAN Model1

/* Create a new stored procedure to populate tblManufacturer
*/

GO
CREATE PROCEDURE populateManu
@MTName varchar(25),
@MTDescr varchar(50),
@MName varchar(25),
@MDescr varchar(50)
AS

DECLARE @M_ID INT

SET @M_ID = (SELECT ManuTypeID
			 FROM tblManufacturerType
			 WHERE ManuTypeName = @MTName)

BEGIN TRAN Manu1
INSERT INTO tblManufacturer(ManuTypeID, ManuName, ManuDescr)
VALUES(@M_ID, @MName, @MDescr)
COMMIT TRAN Manu1

/* Create a new stored procedure to populate tblManufacturerType
*/

GO
CREATE PROCEDURE populateManuType
@MName varchar(25),
@MDescr varchar(50)
AS

BEGIN TRAN ManuT1
INSERT INTO tblManufacturerType(ManuTypeName, ManuTypeDescr)
VALUES(@MName, @MDescr)
COMMIT TRAN ManuT1

/* Create a new stored procedure to populate tblProduct
*/

GO
CREATE PROCEDURE populateProduct
@MName varchar(25),
@MDescr varchar(50),
@Color varchar(20),
@Size numeric(3,1)
AS

DECLARE @M_ID INT

SET @M_ID = (SELECT ModelID
			 FROM tblModel
			 WHERE ModelName = @MName)

BEGIN TRAN Product1
INSERT INTO tblProduct(ModelID, Color, size)
VALUES(@M_ID, @MName, @MDescr)
COMMIT TRAN Product1

/* Create a new stored procedure to populate tblPurpose
*/

GO
CREATE PROCEDURE populatePurpose
@SName varchar(25),
@SDescr varchar(50),
@PName varchar(25),
@PDescr varchar(25)
AS

DECLARE @S_ID INT

SET @S_ID = (SELECT StyleID
			 FROM tblStyle
			 WHERE StyleName = @SName)

BEGIN TRAN Purpose1
INSERT INTO tblPurpose(StyleID, PurposeName, PurposeDescr)
VALUES(@S_ID, @PName, @PDescr)
COMMIT TRAN Purpose1

/* Create a new stored procedure to populate tblStyle
*/

GO
CREATE PROCEDURE populateStyle
@SName varchar(25),
@SDescr varchar(50)
AS

BEGIN TRAN Style1
INSERT INTO tblStyle(StyleName, StyleDescr)
VALUES(@SName, @SDescr)
COMMIT TRAN Style1

/* Create a new stored procedure to populate tblLine_Item
*/
GO
CREATE PROCEDURE populateLineItem
@OrderDate Date,
@Color varchar(25),
@Size numeric(3,1),
@Quantity INT,
@Price numeric(6,2)
AS

DECLARE @O_ID INT, @P_ID INT

SET @O_ID = (SELECT OrderID
			 FROM tblOrder
			 WHERE OrderDate = @OrderDate)

SET @P_ID = (SELECT ProductID
			 FROM tblProduct
			 WHERE Color = @Color AND
				   Size = @Size)

BEGIN TRAN LineItem1
INSERT INTO tblLineItem(OrderID, ProductID, Quantity, Price)
VALUES(@O_ID, @P_ID, @Quantity, @Price)
COMMIT TRAN LineItem1

GO
CREATE PROCEDURE populateStyle
@SName varchar(25),
@SDescr varchar(50)
AS

BEGIN TRAN Style1
INSERT INTO tblStyle(StyleName, StyleDescr)
VALUES(@SName, @SDescr)
COMMIT TRAN Style1