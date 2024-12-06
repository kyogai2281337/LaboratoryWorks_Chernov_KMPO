CREATE DATABASE IF NOT EXISTS `book_shop` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `book_shop`;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

-- ! Initialization TX
START TRANSACTION;
SET time_zone = "+03:00";

CREATE TABLE `account` (
  `login` varchar(255) NOT NULL,
  `passwd` varchar(255) NOT NULL,
  `surname` varchar(255) DEFAULT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `birthdate` date DEFAULT NULL,
  `phonenum` varchar(20) DEFAULT NULL,
  `address` text,
  `accesscode` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `account` (`login`, `passwd`, `surname`, `firstname`, `lastname`, `birthdate`, `phonenum`, `address`, `accesscode`) VALUES
('admin', 'adminpass', 'Сидоров', 'Сергей', 'Сергеевич', '1980-12-01', '+71234567892', 'Екатеринбург, ул. Мира, д.5', 1),
('user1', 'passwd1', 'Иванов', 'Иван', 'Иванович', '1985-05-10', '+71234567890', 'Москва, ул. Ленина, д.10', 3),
('user2', 'passwd2', 'Петров', 'Петр', 'Петрович', '1990-08-15', '+71234567891', 'Санкт-Петербург, пр. Невский, д.25', 2);

CREATE TABLE `good_category` (
  `code` int NOT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `good_category` (`code`, `name`) VALUES
(1, 'Электроника'),
(2, 'Еда'),
(3, 'Одежда');

CREATE TABLE `cart` (
  `code` int NOT NULL,
  `length` int DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `login` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `cart` (`code`, `length`, `price`, `login`) VALUES
(1, 1, '19999.99', 'user1'),
(2, 2, '1999.98', 'user2'),
(3, 3, '1499.97', 'admin');

CREATE TABLE `access_rights` (
  `code` int NOT NULL PRIMARY KEY,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `access_rights` (`code`, `name`) VALUES
(1, 'Администратор'),
(2, 'Менеджер'),
(3, 'Пользователь');

CREATE TABLE `storage` (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `length` int DEFAULT NULL,
  `desc` TINYINT(1) not null,
  `good_id` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `storage` (`id`, `length`, `desc`, `good_id`) VALUES
(1, 50, 1, 'A001'),
(2, 100, 1, 'A002'),
(3, 200, 1, 'A003');

CREATE TABLE `containment_request` ( -- ! ZayaVka
  `id` int NOT NULL, -- * PrimKey
  `request_id` int DEFAULT NULL, -- * ID?
  `length` int DEFAULT NULL, -- ? len of 
  `good_id` varchar(255) DEFAULT NULL,
  `storage_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `containment_request` (`id`, `request_id`, `length`, `good_id`, `storage_id`) VALUES
(1, 101, 1, 'A001', 1),
(2, 102, 2, 'A002', 2),
(3, 103, 3, 'A003', 3);

-- CREATE TEMPORARY TABLE `good_size` (
--     w int -- * 10
--     l int -- * 50
--     h int -- * 250
--     size_type string -- * milli
-- )

CREATE TABLE `good` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `size` varchar(255) DEFAULT NULL, -- ! {10x50x250mm}???
  `price` decimal(10,2) DEFAULT NULL,
  `color` varchar(50) DEFAULT NULL,
  `photo` blob, -- ! typename > size, metadata (syscall > get(photo(route)))
  `category_code` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `good` (`id`, `name`, `size`, `price`, `color`, `photo`, `category_code`) VALUES
('A001', 'Смартфон', '15см', '19999.99', 'Черный', NULL, 1),
('A002', 'Футболка', 'M', '999.99', 'Белый', NULL, 2),
('A003', 'Шоколад', '15см', '499.99', 'Синий', NULL, 3);

CREATE TABLE `request` (
  `id` int NOT NULL,
  `creation_date` date DEFAULT NULL,
  `done` tinyint(1) DEFAULT NULL,
  `done_date` date DEFAULT NULL,
  `login` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `request` (`id`, `creation_date`, `done`, `done_date`, `login`) VALUES
(101, '2024-10-10', 1, '2024-10-12', 'user1'),
(102, '2024-10-11', 0, NULL, 'user2'),
(103, '2024-10-12', 1, '2024-10-13', 'admin');

ALTER TABLE `account`
  ADD PRIMARY KEY (`login`),
  ADD KEY `accesscode` (`accesscode`);

ALTER TABLE `good_category`
  ADD PRIMARY KEY (`code`);

ALTER TABLE `cart`
  ADD PRIMARY KEY (`code`),
  ADD KEY `account_login` (`login`);

ALTER TABLE `storage`
  ADD KEY `good_id` (`good_id`);

ALTER TABLE `containment_request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `request_id` (`request_id`),
  ADD KEY `good_id` (`good_id`),
  ADD KEY `storage_id` (`storage_id`);

ALTER TABLE `good`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_code` (`category_code`);

ALTER TABLE `request`
  ADD PRIMARY KEY (`id`),
  ADD KEY `login` (`login`);

ALTER TABLE `account`
  ADD CONSTRAINT `accaunt_ibfk_1` FOREIGN KEY (`accesscode`) REFERENCES `access_rights` (`code`);

ALTER TABLE `cart`
  ADD CONSTRAINT `korz_ibfk_1` FOREIGN KEY (`login`) REFERENCES `account` (`login`);

ALTER TABLE `storage`
  ADD CONSTRAINT `sklad_ibfk_1` FOREIGN KEY (`good_id`) REFERENCES `good` (`id`);

ALTER TABLE `containment_request`
  ADD CONSTRAINT `sostav_zayavki_ibfk_1` FOREIGN KEY (`request_id`) REFERENCES `request` (`id`),
  ADD CONSTRAINT `sostav_zayavki_ibfk_2` FOREIGN KEY (`good_id`) REFERENCES `good` (`id`),
  ADD CONSTRAINT `sostav_zayavki_ibfk_3` FOREIGN KEY (`storage_id`) REFERENCES `storage` (`id`);

ALTER TABLE `good`
  ADD CONSTRAINT `tovar_ibfk_1` FOREIGN KEY (`category_code`) REFERENCES `good_category` (`code`);

ALTER TABLE `request`
  ADD CONSTRAINT `zayavka_ibfk_1` FOREIGN KEY (`login`) REFERENCES `account` (`login`);
ALTER table `request`
  ADD COLUMN `total_price` decimal(10,2) DEFAULT NULL;
COMMIT;


-- ! TX on Procs;
START TRANSACTION;
DELIMITER //

CREATE PROCEDURE add_account(
  IN login VARCHAR(255),
  IN passwd VARCHAR(255),
  IN surname VARCHAR(255),
  IN firstname VARCHAR(255),
  IN lastname VARCHAR(255),
  IN birthdate DATE,
  IN phonenum VARCHAR(20),
  IN address TEXT,
  IN accesscode INT
)
BEGIN
  INSERT INTO account (login, passwd, surname, firstname, lastname, birthdate, phonenum, address, accesscode)
  VALUES (login, passwd, surname, firstname, lastname, birthdate, phonenum, address, accesscode);
END//

DELIMITER ;

DELIMITER //

CREATE PROCEDURE get_account_info()
BEGIN
  SELECT a.login, a.surname, a.firstname, a.lastname, ar.name AS access_rights
  FROM account a
  JOIN access_rights ar ON a.accesscode = ar.code;
END//

DELIMITER ;

CALL add_account('new_login', 'new_passwd', 'New', 'Surname', 'Firstname', '1990-01-01', '+71234567890', 'New Address', 1);

CALL get_account_info();

COMMIT;

-- ! TX on Triggers to save last updates on accounts
START TRANSACTION;
-- ? creating table workspace_history
CREATE TABLE `workspace_history` (
  `acc_login` VARCHAR(255),
  `last_task_time` DATETIME
);

-- ? trigger to save last change time
CREATE TRIGGER `save_to_history`
AFTER UPDATE ON `account`
FOR EACH ROW
BEGIN
  INSERT INTO `workspace_history` (`acc_login`, `last_task_time`)
  VALUES (NEW.login, NOW());
END;

-- ? trigger to delete last change time with the deletion of user
CREATE TRIGGER `delete_from_history`
AFTER DELETE ON `account`
FOR EACH ROW
BEGIN
  DELETE FROM `workspace_history`
  WHERE `acc_login` = OLD.login;
END;

-- ? trigger to create price for the cart
CREATE TRIGGER `update_price_cart`
AFTER INSERT ON `containment_request`
FOR EACH ROW
BEGIN
  UPDATE `request`
  SET total_price = total_price + (SELECT price FROM `good` WHERE id = NEW.good_id) * NEW.`length`
  WHERE `id` = NEW.request_id; -- Unknown column 'code' in 'where clause' fixed by using `id`
END;

create trigger `update_price_cart_delete`
after delete on `containment_request`
for each row
begin
  update `request`
  set total_price = total_price - (SELECT price FROM `good` WHERE id = OLD.good_id) * OLD.`length`
  where code = OLD.request_id;
end;

COMMIT;