USE project_info330_Shoes_2

/* Create a computed column that checks for the average shoe size
   for each model that has a color of 'red' and has a style of 'high top'
*/
GO
CREATE FUNCTION calc_avg_shoe_size(@PK_ID INT)
RETURNS numeric(4,2)
AS
BEGIN
	DECLARE @RET numeric(4,2) = (SELECT AVG(P.Size)
								 FROM tblModel M
									JOIN tblProduct P ON M.ModelID = P.ModelID
									JOIN tblPurpose PU ON M.PurposeID = PU.PurposeID
									JOIN tblStyle S ON PU.StyleID = S.StyleID
								 WHERE M.ModelID = @PK_ID AND
									   P.Color = 'red' AND
									   S.StyleName = 'high top'
								)
	RETURN @RET
END

GO
ALTER TABLE tblModel
ADD AverageShoeSize
AS (dbo.calc_avg_shoe_size(ModelID))

/* Create a computed column that has the total number of shoes
   that were ordered before 8/14/2016 and were manufactured
   by 'Adidas'
*/
GO
CREATE FUNCTION calc_tot_num_shoes(@PK_ID INT)
RETURNS INT
AS
BEGIN
	DECLARE @RET INT = (SELECT SUM(LI.Quantity)
						FROM tblOrder O
							JOIN tblLineItem LI ON O.OrderID = LI.OrderID
							JOIN tblProduct P ON LI.ProductID = P.ProductID
							JOIN tblModel MO ON P.ModelID = MO.ModelID
							JOIN tblManufacturer M ON MO.ManuID = M.ManuID
						WHERE O.OrderID = @PK_ID AND
							  O.OrderDate < '2016-08-14' AND
							  M.ManuName = 'Adidas'
					   )
	RETURN @RET
END

GO
ALTER TABLE tblOrder
ADD TotalNumShoes
AS (dbo.calc_tot_num_shoes(OrderID))