--IF OBJECT_ID('xtr.Doc_Pre') IS NOT NULL
--	   DROP TABLE xtr.Doc_Pre;

--CREATE TABLE xtr.Doc_Pre
--(
--	Doc_Pre_ID int,
--	Doc_ID int,
--	Version varchar(10),
--	Field_Name varchar(50),
--	Search_String varchar(max),
--	Page_Num int not null,
--	Minpoint_X float not null,
--	Minpoint_Y float not null,
--	Maxpoint_X float not null,
--	Maxpoint_Y float not null,
--	Is_From_Table bit,
--	Is_Horizontal bit,
--	Is_Organized_In_Row bit,
--	Result_Type varchar(10) not null,
--	CONSTRAINT Doc_Pre_ID PRIMARY KEY(Doc_Pre_ID)


--);

--ALTER TABLE Guest_Writer.xtr.Doc_Pre
--ADD Max_Column int, Max_Row int;
--SELECT * FROM Guest_Writer.xtr.Doc_Pre;


--INSERT INTO xtr.Doc_PDF 
--(Import_Date_Time, Agency_Name, PDF_File_Name, Extracted_File_Name)
--VALUES (GETDATE(), 'GinnieMae', 'GinnieMae _2016May23-011O_2016_05_26.pdf', 'GinnieMae _2016May23-011O_2016_05_26.csv');


--SELECT *
--FROM xtr.Doc_Pre INNER JOIN xtr.Doc_PDF on xtr.Doc_Pre.[Doc_ID] = xtr.Doc_PDF.[Doc_ID];


--ALTER TABLE Guest_Writer.xtr.Doc_PDF
--ADD Doc_Type_ID int;
--SELECT * FROM Guest_Writer.xtr.Doc_Pre;


--IF OBJECT_ID('xtr.Doc_Type') IS NOT NULL
--	   DROP TABLE xtr.Doc_Type;

--CREATE TABLE xtr.Doc_Type
--(
--	Doc_Type_ID int not null,
--	Doc_Type_Name varchar(20)
--	CONSTRAINT Doc_Type_ID PRIMARY KEY(Doc_Type_ID)
--);

--ALTER TABLE [Guest_Writer].[xtr].[Doc_Page_Pic]
--ADD [Is_Vertical] BIT ;

--ALTER TABLE Guest_Writer.xtr.Doc_Pre
--DROP COLUMN [Minpoint_X],[Minpoint_Y],[Maxpoint_X],[Maxpoint_Y]; 

--ALTER TABLE Guest_Writer.xtr.Doc_Field_Value
--ADD [Calcrt_ID] nchar(50); 

--DELETE FROM xtr.Doc_PDF WHERE Doc_ID = 236 or Doc_ID = 239 or Doc_ID = 240;
--SELECT * FROM xtr.Doc_Pre INNER JOIN xtr.Doc_PDF on xtr.Doc_Pre.[Doc_ID] = xtr.Doc_PDF.[Doc_ID];


 
--SELECT * 

--FROM ([xtr].[Doc_Field_Name] dfn INNER JOIN [xtr].[Doc_Field_Value] dfv ON dfn.Field_Name_ID = dfv.Field_Name_ID)
--		INNER JOIN [xtr].[Doc_Tranche] dt ON dfn.[Tranche_ID] = dt.[Tranche_ID]
--WHERE dt.Cusip = '38376RWH5';

--SELECT * 

--FROM ([xtr].[Doc_Field_Name] dfn INNER JOIN [xtr].[Doc_Field_Value] dfv ON dfn.Field_Name_ID = dfv.Field_Name_ID)
--		INNER JOIN [xtr].[Doc_Tranche] dt ON dfn.[Tranche_ID] = dt.[Tranche_ID]
--WHERE dt.Cusip = '38379XS84';

--SELECT * FROM ([xtr].[Doc_Field_Name] dfn INNER JOIN [xtr].[Doc_Field_Value] dfv ON dfn.Field_Name_ID = dfv.Field_Name_ID) INNER JOIN [xtr].[Doc_Tranche] dt ON dfn.[Tranche_ID] = dt.[Tranche_ID] WHERE dt.Cusip = '38379XT91';


--SELECT dfn.[Field_Name_ID],
--	   dfn.[Tranche_ID],
--	   [Tranche_Name],
--	   [Cusip],
--	   dfn.[Calcrt_ID],
--	   [Field_Name],
--	   [Field_Value]
--FROM ([xtr].[Doc_Field_Name] dfn INNER JOIN [xtr].[Doc_Field_Value] dfv ON dfn.Field_Name_ID = dfv.Field_Name_ID)
--		INNER JOIN [xtr].[Doc_Tranche] dt ON dfn.[Tranche_ID] = dt.[Tranche_ID];



--SELECT * 

--FROM ([xtr].[Doc_Field_Name] dfn INNER JOIN [xtr].[Doc_Field_Value] dfv ON dfn.Field_Name_ID = dfv.Field_Name_ID)
--		INNER JOIN [xtr].[Doc_Tranche] dt ON dfn.[Tranche_ID] = dt.[Tranche_ID]
--WHERE dfv.[Field_Value] = 'IX';



--SELECT * 

--FROM ([xtr].[Doc_Field_Name] dfn INNER JOIN [xtr].[Doc_Field_Value] dfv ON dfn.Field_Name_ID = dfv.Field_Name_ID)
--		INNER JOIN [xtr].[Doc_Tranche] dt ON dfn.[Tranche_ID] = dt.[Tranche_ID]
--WHERE dt.[Tranche_ID] = 16914;

--SELECT *

--FROM ([xtr].[Doc_Field_Name] dfn INNER JOIN [xtr].[Doc_Field_Value] dfv ON dfn.Field_Name_ID = dfv.Field_Name_ID)
--		INNER JOIN [xtr].[Doc_Tranche] dt ON dfn.[Tranche_ID] = dt.[Tranche_ID]
--WHERE dfn.[Field_Name] = 'Class Coupon' and [Field_Value_Is_Numeric]=0;



--UPDATE [xtr].[Doc_Field_Value] SET [Field_Value] = '38376RWV4 ' ,[Calcrt_ID] = 'ID032
--           ',[Field_Value_Is_Numeric] = ISNUMERIC( '38376RWV4 ')  WHERE [Field_Name_ID] = 61232 IF @@ROWCOUNT=0 INSERT
--INTO [xtr].[Doc_Field_Value] (Field_Name_ID, Field_Value, Calcrt_ID, Field_Value_Is_Numeric) VALUES (61232, '38376RWV4 '
--, 'ID032                                             ', ISNUMERIC('38376RWV4 '));






--create table [Guest_Writer].[xtr].[Doc_Special_Pic] 
--(	
--	Doc_Special_Pic_ID int not null IDENTITY(1,1)  Primary key,
--	Doc_Special_Pic_Bin varbinary(MAX),
--	Field_Value_ID int FOREIGN KEY REFERENCES [xtr].[Doc_Field_Value]([Field_Value_ID])
--);

--CREATE TABLE [Guest_Writer].[xtr].[Doc_Field_Pic_Info]
--(
--	Doc_Field_Pic_Info_ID int not null IDENTITY(1,1)  Primary key,
--	Doc_Page_Pic_ID int FOREIGN KEY REFERENCES [xtr].[Doc_Page_Pic](Doc_Page_Pic_ID),
--	Doc_Field_Value_ID int FOREIGN KEY REFERENCES [xtr].[Doc_Field_Value](Field_Value_ID),
--	Doc_Pic_Rotation_Degree int,
--	Pos_Minpoint_X float,
--	Pos_Minpoint_Y float,
--	Pos_Maxpoint_X float,
--	Pos_Maxpoint_Y float
--);

--DELETE [xtr].[Doc_Img_Pic];
--UPDATE [xtr].[Doc_Field_Pic] SET [Doc_Field_Pic_Bin] = convert(varbinary,'123') WHERE [Field_Value_ID] = 129144 IF @@ROWCOUNT = 0 INSERT INTO [xtr].[Doc_Field_Pic] ( [Field_Value_ID], [Doc_Field_Pic_Bin] ) VALUES ( 129144, convert(varbinary,'123'));


--DELETE FROM [xtr].[Doc_Field_Name];
--DELETE FROM [xtr].[Doc_Field_Value];
--DELETE FROM [xtr].[Doc_Tranche];
--DELETE FROM [xtr].[Doc_PDF];
--DELETE FROM [xtr].[Doc_Deal];
--DELETE FROM [xtr].[Doc_Page_Pic];
--DELETE FROM [xtr].[Doc_Field_Pic];
--DELETE FROM [xtr].[Doc_Field_Pic_Info];
--DELETE FROM [xtr].[Doc_Special_Pic];

--Insert into [xtr].[Doc_Type] ([Doc_Type_ID],[Doc_Type_Name]) Output Inserted.[Doc_Type_ID]
-- Values (2,'Fraddie Mac');

--UPDATE [xtr].[Doc_Type] SET [Doc_Type_Name] = 'HEIHEI'  Output Inserted.[Doc_Type_ID] WHERE [Doc_Type_ID] = 3

--DECLARE @output_id int
--UPDATE [xtr].[Doc_Field_Value] SET [Field_Value] = '38379XQ37' ,[Calcrt_ID] = 'ID032',
--[Field_Value_Is_Numeric] = ISNUMERIC( '38379XQ37') WHERE [Field_Name_ID] = 132312 
--IF @@ROWCOUNT=0 INSERT INTO [xtr].[Doc_Field_Value] (Field_Name_ID, Field_Value, Calcrt_ID, Field_Value_Is_Numeric) 
--OUTPUT Inserted.[Field_Value_ID] VALUES (132312, '38379XQ37', 'ID032', ISNUMERIC('38379XQ37'))
--ELSE SELECT [Field_Value_ID] FROM [xtr].[Doc_Field_Value] WHERE [Field_Name_ID] = 132312;





--UPDATE [xtr].[Doc_Field_Value] SET [Field_Value] = '38379XQ37' ,[Calcrt_ID] = 'ID032',
--[Field_Value_Is_Numeric] = ISNUMERIC( '38379XQ37') WHERE [Field_Name_ID] = 136184 
--IF @@ROWCOUNT=0 INSERT INTO [xtr].[Doc_Field_Value] (Field_Name_ID, Field_Value, Calcrt_ID, Field_Value_Is_Numeric) 
--OUTPUT Inserted.[Field_Value_ID] VALUES (136184, '38379XQ37', 'ID032', ISNUMERIC('38379XQ37')) 
--ELSE SELECT [Field_Value_ID] FROM [xtr].[Doc_Field_Value] WHERE [Field_Name_ID] = 136184 ;


 SELECT * FROM 
	(
	SELECT * FROM [xtr].[Doc_Field_Value] 
	WHERE [Field_Name_ID] in 
	 (SELECT [Field_Name_ID] FROM [xtr].[Doc_Field_Name] 
		WHERE [Tranche_ID] in 
		( SELECT [Tranche_ID] FROM [xtr].[Doc_Tranche] 
			WHERE [Deal_ID] = (SELECT [Deal_ID] FROM [xtr].[Doc_Deal] WHERE [Doc_ID]=738)) 
		)) as fvt INNER JOIN [xtr].[Doc_Field_Pic_Info] fpit ON fvt.Field_Value_ID = fpit.Doc_Field_Value_ID  ORDER BY fvt.[Field_Value_ID] ASC ;

--SELECT * FROM [xtr].[Doc_Page_Pic] WHERE [Doc_ID] = 738;