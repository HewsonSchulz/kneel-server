--! RESET !--
DELETE FROM Styles;
DELETE FROM Sizes;
DELETE FROM Metals;
DELETE FROM Types;
DELETE FROM Orders;

DROP TABLE IF EXISTS Styles;
DROP TABLE IF EXISTS Sizes;
DROP TABLE IF EXISTS Metals;
DROP TABLE IF EXISTS Types;
DROP TABLE IF EXISTS Orders;


--* TABLE CREATION *--
CREATE TABLE `Styles` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Sizes` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(5,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Metals` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Types` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `type` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Orders` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `styleId` INTEGER NOT NULL,
    `sizeId` INTEGER NOT NULL,
    `metalId` INTEGER NOT NULL,
    `typeId` INTEGER NOT NULL,
    FOREIGN KEY (`styleId`) REFERENCES `Styles` (`id`),
    FOREIGN KEY (`sizeId`) REFERENCES `Sizes` (`id`),
    FOREIGN KEY (`metalId`) REFERENCES `Metals` (`id`),
    FOREIGN KEY (`typeId`) REFERENCES `Types` (`id`)
);

--* TABLE POPULATION *--
INSERT INTO `Styles`
    (`style`, `price`)
VALUES 
    ('Classic', 500),
    ('Modern', 710),
    ('Vintage', 965);

INSERT INTO `Sizes`
    (`carets`, `price`)
VALUES 
    (0.5, 405),
    (0.75, 782),
    (1, 1470),
    (1.5, 1997),
    (2, 3638);

INSERT INTO `Metals`
    (`metal`, `price`)
VALUES 
    ('Sterling Silver', 12.42),
    ('14K Gold', 736.4),
    ('24K Gold', 1258.9),
    ('Platinum', 795.45),
    ('Palladium', 1241);

INSERT INTO `Types`
    (`type`, `price`)
VALUES 
    ('Ring', 1),
    ('Earring', 2),
    ('Necklace', 4);

-- example orders
INSERT INTO `Orders`
    (`styleId`, `sizeId`, `metalId`, `typeId`)
VALUES 
    (1, 3, 2, 1),
    (2, 4, 3, 2),
    (3, 2, 4, 3),
    (1, 5, 1, 1),
    (2, 1, 5, 2);

--* DISPLAY ALL *--
SELECT * FROM Styles;
SELECT * FROM Sizes;
SELECT * FROM Metals;
SELECT * FROM Types;
SELECT * FROM Orders;
