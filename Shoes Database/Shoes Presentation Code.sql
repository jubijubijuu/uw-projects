USE project_info330_Shoes_2

-- before executing
SELECT * FROM tblOrder WHERE OrderDate = '1999-09-26'

EXECUTE populateOrder
@CustFName = 'Lebron',
@CustLName = 'James',
@CustAddress = '236Miami Drive N',
@EmpNum = 8,
@OrderDate = '1999-09-26'

-- after executing
SELECT * FROM tblOrder WHERE OrderDate = '1999-09-26'


/* Write the code to find employees who handled at
   least 2 orders made by customer with first name
   'Jerome' and the shoes ordered had a purpose of
   'Running'
*/
SELECT E.EmpID, E.EmpFName, E.EmpLName, COUNT(O.OrderID) AS TotRunningOrders
FROM tblEmployee E
	JOIN tblOrder O ON E.EmpID = O.EmpID
	JOIN tblCustomer C ON O.CustID = C.CustID
	JOIN tblLineItem LI ON O.OrderID = LI.OrderID
	JOIN tblProduct P ON LI.ProductID = P.ProductID
	JOIN tblModel M ON P.ModelID = M.ModelID
	JOIN tblPurpose PU ON M.PurposeID = PU.PurposeID
WHERE C.CustFName = 'Jerome' AND
	  PU.PurposeName = 'Running'
GROUP BY E.EmpID, E.EmpFName, E.EmpLName
HAVING COUNT(O.OrderID) >= 2

/* Write the code to find average shoe sizes of
   at least 5.0 with the purpose of 'Running' that
   were manufactured by 'Adidas'  that also were
   handled with employees that processed more than
   3 orders
*/
SELECT M.ModelID, M.ModelName, subq.EmpOrderTotal, AVG(P.Size) AS AvgAtLeast5
FROM tblModel M
	JOIN tblProduct P ON M.ModelID = P.ModelID
	JOIN tblManufacturer MA ON M.ManuID = MA.ManuID
	JOIN tblPurpose PU ON M.PurposeID = PU.PurposeID
	JOIN (SELECT M.ModelID, COUNT(O.OrderID) AS EmpOrderTotal
		  FROM tblEmployee E
			JOIN tblOrder O ON E.EmpID = O.EmpID
			JOIN tblLineItem LI ON O.OrderID = LI.OrderID
			JOIN tblProduct P ON LI.ProductID = P.ProductID
			JOIN tblModel M ON P.ModelID = M.ModelID
		  GROUP BY M.ModelID
		  HAVING COUNT(O.OrderID) > 3
         ) AS subq ON M.ModelID = subq.ModelID
WHERE PU.PurposeName = 'Running' AND
	  MA.ManuName = 'Adidas'
GROUP BY M.ModelID, M.ModelName, subq.EmpOrderTotal
HAVING AVG(P.Size) >= 5
