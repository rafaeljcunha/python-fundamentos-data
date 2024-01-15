CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY NOT NULL,
    CustomerName NVARCHAR(255) NOT NULL,
    Cpf NVARCHAR(11) NOT NULL
);

CREATE TABLE Product (
    ProductID INT PRIMARY KEY NOT NULL,
    ProductName NVARCHAR(255) NOT NULL,
    PackageName NVARCHAR(255) NOT NULL,
    IsDiscontinued BIT NOT NULL
);

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY NOT NULL,
    EmployeeName NVARCHAR(255) NOT NULL,
    EmployeeNumber INT NOT NULL,
);

CREATE TABLE Store (
    StoreID INT PRIMARY KEY NOT NULL,
    StoreNumber INT NOT NULL,
    StoreRegion NVARCHAR(255) NOT NULL
);

CREATE TABLE [Date] (
    DateID INT PRIMARY KEY NOT NULL,
    DateHour TIME NOT NULL,
    DateDay INT NOT NULL,
    DateMonth INT NOT NULL,
    DateYear INT NOT NULL,
    DateTrimester INT NOT NULL
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY NOT NULL,
    ProductID INT NOT NULL,
    CustomerID INT NOT NULL,
    EmployeeID INT NOT NULL,
    StoreID INT NOT NULL,
    DateID INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Quantity INT NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID),
    FOREIGN KEY (DateID) REFERENCES [Date](DateID)
);

CREATE INDEX INDEX_Orders_ProductID ON Orders (ProductID);
CREATE INDEX INDEX_Orders_CustomerID ON Orders (CustomerID);
CREATE INDEX INDEX_Orders_EmployeeID ON Orders (EmployeeID);
CREATE INDEX INDEX_Orders_StoreID ON Orders (StoreID);
CREATE INDEX INDEX_Orders_DateID ON Orders (DateID);