USE project_info330_Shoes_2

/* Business rule: No shoe of size 9 and color 'black' can be ordered
				  by a customer with first name 'Jerome'
*/
GO
CREATE FUNCTION no_shoe_jerome()
RETURNS INT
AS
BEGIN
	DECLARE @RET INT = 0
	IF EXISTS(SELECT *
			  FROM tblProduct P
				JOIN tblLineItem LI ON P.ProductID = LI.ProductID
				JOIN tblOrder O ON LI.OrderID = O.OrderID
				JOIN tblCustomer C ON O.CustID = C.CustID
			  WHERE P.Size = 9.0 AND
					P.Color = 'black' AND
					C.CustFName = 'Jerome'
			 )
	BEGIN
		SET @RET = 1
	END
	RETURN @RET
END

GO
ALTER TABLE tblOrder
ADD CONSTRAINT ck_no_shoe_jerome
CHECK (dbo.no_shoe_jerome() = 0)

/* Business rule: No employee with last name 'Orille' of employee type 'President'
				  can have an order of a shoe that has a style of 'running' before 9/26/2020
*/
GO
CREATE FUNCTION no_employee_orille()
RETURNS INT
AS
BEGIN
	DECLARE @RET INT = 0
	IF EXISTS(SELECT *
			  FROM tblEmployee E
				JOIN tblEmployeeType ET ON E.EmpTypeID = ET.EmpTypeID
				JOIN tblOrder O ON E.EmpID = O.EmpID
				JOIN tblLineItem LI ON O.OrderID = LI.OrderID
				JOIN tblProduct P ON LI.ProductID = P.ProductID
				JOIN tblModel M ON P.ModelID = M.ModelID
				JOIN tblPurpose PU ON M.PurposeID = PU.PurposeID
			  WHERE E.EmpLName = 'Orille' AND
					ET.EmpTypeName = 'President' AND
					PU.PurposeName = 'running' AND
					O.OrderDate < '2020-09-26'
			 )
	BEGIN
		SET @RET = 1
	END
	RETURN @RET
END

GO
ALTER TABLE tblOrder
ADD CONSTRAINT ck_no_employee_orille
CHECK (dbo.no_employee_orille() = 0)