CREATE TABLE `web-project-g20`.`users` (
  `email` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `web-project-g20`.`tours` (
  `tour_dt` datetime NOT NULL,
  `tour_name` varchar(255) NOT NULL,
  `ticket_price` double NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `max_participants` int NOT NULL,
  `places_left` int NOT NULL,
  PRIMARY KEY (`tour_dt`));


CREATE TABLE `web-project-g20`.`users_tours` (
  `email` varchar(255) NOT NULL,
  `tour_dt` datetime NOT NULL,
  `num_of_tickets` int NOT NULL,
  PRIMARY KEY (`email`,`tour_dt`),
  KEY `tour_td_idx` (`tour_dt`),
  CONSTRAINT `email` FOREIGN KEY (`email`) REFERENCES `users` (`email`),
  CONSTRAINT `tour_td` FOREIGN KEY (`tour_dt`) REFERENCES `tours` (`tour_dt`));
    
    
CREATE TABLE `web-project-g20`.`comments` (
  `comment_dt` datetime NOT NULL,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `text` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`comment_dt`,`email`)) ;

    

   CREATE TABLE `web-project-g20`.`orders` (
  `order_id` INT NOT NULL,
  `order_DT` datetime NOT NULL,
  `is_delivery` tinyint NOT NULL,
  `email` varchar(255) NOT NULL,
  `order_cost`  DOUBLE NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `email_order_idx` (`email`),
  CONSTRAINT `email_order` FOREIGN KEY (`email`) REFERENCES `users` (`email`)); 
    
    
    CREATE TABLE `web-project-g20`.`products` (
  `product_id` VARCHAR(255) NOT NULL,
  `product_name` VARCHAR(255) NOT NULL,
  `product_price` DOUBLE NOT NULL,
  `product_picture` VARCHAR(255) NULL,
  PRIMARY KEY (`product_id`));
  
  
  CREATE TABLE `web-project-g20`.`order_products` (
  `order_id` INT NOT NULL,
  `product_id` VARCHAR(255) NOT NULL,
  `quantity` DOUBLE NOT NULL,
  PRIMARY KEY (`order_id`, `product_id`),
  INDEX `product_id_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `order_id`
    FOREIGN KEY (`order_id`)
    REFERENCES `web-project-g20`.`orders` (`order_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `product_id`
    FOREIGN KEY (`product_id`)
    REFERENCES `web-project-g20`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
  
 CREATE TABLE  `web-project-g20`.`recipes` (
  `recipe_id` VARCHAR(255) NOT NULL,
  `recipe_name` varchar(255) NOT NULL,
  `description` varchar(500) NOT NULL,
  `picture` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`recipe_id`));
  
  
CREATE TABLE `web-project-g20`.`recipe_products` (
  `product_id` VARCHAR(255) NOT NULL,
  `recipe_id` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`product_id`, `recipe_id`),
  INDEX `recipe_id_idx` (`recipe_id` ASC) VISIBLE,
  CONSTRAINT `product_id_recipe`
    FOREIGN KEY (`product_id`)
    REFERENCES `web-project-g20`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `recipe_id`
    FOREIGN KEY (`recipe_id`)
    REFERENCES `web-project-g20`.`recipes` (`recipe_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


INSERT INTO `web-project-g20`.`users` (email, first_name, last_name, password, phone_number, address) VALUES ('barshv@gmail.com', 'bar', 'shvarzman', '555555', '0542376609', 'netaim');
INSERT INTO `web-project-g20`.`users` (email, first_name, last_name, password, phone_number, address) VALUES ('naamah@gmail.com', 'naama', 'haaroni', '123123', '0545675576', 'beer sheva');
INSERT INTO `web-project-g20`.`users` (email, first_name, last_name, password, phone_number, address) VALUES ('omri55@gmail.com', 'omri', 'garenda', '123456', '0546758897', 'beer sheva');
INSERT INTO `web-project-g20`.`users` (email, first_name, last_name, password, phone_number, address) VALUES ('shaked95@gmail.com', 'shaked', 'haimi', '111111', '0523454433', 'beer sheva');

INSERT INTO `web-project-g20`.`tours` (`tour_dt`, `tour_name`, `ticket_price`, `description`, `picture`, `max_participants`, `places_left`) VALUES ('2020-03-01 10:00:00', 'סיור תותים', '30.5', 'נלמד על עקרונות גידול התותים וכמובן שנקטוף ונאכל', '/static/media/img/tour1.jpeg', '40', '40');
INSERT INTO `web-project-g20`.`tours` (`tour_dt`, `tour_name`, `ticket_price`, `description`, `picture`, `max_participants`, `places_left`) VALUES ('2020-03-01 14:00:00', 'סיור משפחות', '20', 'סיור שמתאים למשפחות עם ילדים קטנים, קליל וכיף', '/static/media/img/picking.jpeg', '50', '50');
INSERT INTO `web-project-g20`.`tours` (`tour_dt`, `tour_name`, `ticket_price`, `description`, `picture`, `max_participants`, `places_left`) VALUES ('2020-03-12 11:00:00', 'סיור משפחות', '20', 'סיור שמתאים למשפחות עם ילדים קטנים, קליל וכיף', '/static/media/img/picking.jpeg', '50', '50');
INSERT INTO `web-project-g20`.`tours` (`tour_dt`, `tour_name`, `ticket_price`, `description`, `picture`, `max_participants`, `places_left`) VALUES ('2020-03-13 13:00:00', 'סיור תותים', '30.5', 'נלמד על עקרונות גידול התותים וכמובן שנקטוף ונאכל', '/static/media/img/tour1.jpeg', '40', '40');
INSERT INTO `web-project-g20`.`tours` (`tour_dt`, `tour_name`, `ticket_price`, `description`, `picture`, `max_participants`, `places_left`) VALUES ('2020-03-17 10:00:00', 'סיור מתקדם', '50', 'סיור לאנשים שמבינים בתחום ומעוניינים להעשיר את הידע', '/static/media/img/vip.jpeg', '15', '15');
INSERT INTO `web-project-g20`.`tours` (`tour_dt`, `tour_name`, `ticket_price`, `description`, `picture`, `max_participants`, `places_left`) VALUES ('2020-04-20 10:00:00', 'סיור מתקדם', '50', 'סיור לאנשים שמבינים בתחום ומעוניינים להעשיר את הידע', '/static/media/img/vip.jpeg', '15', '15');


INSERT INTO `web-project-g20`.`comments` (`comment_dt`, `email`, `first_name`, `last_name`, `phone_number`, `text`) VALUES ('2020-01-01 10:00:00', 'omri55@gmail.com', 'עומרי', 'גרנדה', '0542223307', 'אשמח לברר לגבי משלוח');
INSERT INTO `web-project-g20`.`comments` (`comment_dt`, `email`, `first_name`, `last_name`, `phone_number`, `text`) VALUES ('2020-01-02 10:00:00', 'shaked95@gmail.com', 'שקד', 'חיימי', '0542223305', 'איך מתנהלים הסיורים?');
INSERT INTO `web-project-g20`.`comments` (`comment_dt`, `email`, `first_name`, `last_name`, `phone_number`, `text`) VALUES ('2020-01-03 10:00:00', 'barshv@gmail.com', 'בר', 'שוורצמן', '0542223303', 'אשמח לברר לגבי אישור אורגני');
INSERT INTO `web-project-g20`.`comments` (`comment_dt`, `email`, `first_name`, `last_name`, `phone_number`, `text`) VALUES ('2020-01-03 12:00:00', 'barshv@gmail.com', 'בר', 'שוורצמן', '0542223301', 'מהי עלות סיור');
INSERT INTO `web-project-g20`.`comments` (`comment_dt`, `email`, `first_name`, `last_name`, `phone_number`, `text`) VALUES ('2020-01-03 13:00:00', 'shaked95@gmail.com', 'שקד', 'חיימי', '0542223309', 'האם אפשר להזמין ולבוא לקחת');


INSERT INTO `web-project-g20`.`products` (product_id, product_name, product_price, product_picture) VALUES ('5', 'גינג''ר', 39, "../static/media/img/product5.jfif");
INSERT INTO `web-project-g20`.`products` (product_id, product_name, product_price, product_picture) VALUES ('6', 'עגבניה', 12, "../static/media/img/product6.jfif");
INSERT INTO `web-project-g20`.`products` (product_id, product_name, product_price, product_picture) VALUES ('4', 'בצל יבש', 12, "../static/media/img/product4.jfif");
INSERT INTO `web-project-g20`.`products` (product_id, product_name, product_price, product_picture) VALUES ('3', 'אבוקדו', 13, "../static/media/img/product3.jfif");
INSERT INTO `web-project-g20`.`products` (product_id, product_name, product_price, product_picture) VALUES ('2', 'גזר', 12, "../static/media/img/product2.jfif");
INSERT INTO `web-project-g20`.`products` (product_id, product_name, product_price, product_picture) VALUES ('1', 'אספרגוס', 29, "../static/media/img/product1.jfif");
INSERT INTO `web-project-g20`.`products` (product_id, product_name, product_price, product_picture) VALUES ('10', 'תפוח אדמה', 11, "../static/media/img/product10.jfif");
INSERT INTO `web-project-g20`.`products` (product_id, product_name, product_price, product_picture) VALUES ('9', 'פלפל', 12, "../static/media/img/product9.jfif");
INSERT INTO `web-project-g20`.`products` (product_id, product_name, product_price, product_picture) VALUES ('8', 'דלעת', 12, "../static/media/img/product8.jfif");
INSERT INTO `web-project-g20`.`products` (product_id, product_name, product_price, product_picture) VALUES ('7', 'תפוח עץ', 25, "../static/media/img/product7.jfif");

INSERT INTO `web-project-g20`.`recipes` (recipe_id, recipe_name, description, picture) VALUES ('4', 'חומוס עדשים כתומות', '/', "../static/media/img/recipe4.png");
INSERT INTO `web-project-g20`.`recipes` (recipe_id, recipe_name, description, picture) VALUES ('3', 'סלט נבטים', '/', "../static/media/img/recipe3.png");
INSERT INTO `web-project-g20`.`recipes` (recipe_id, recipe_name, description, picture) VALUES ('2', 'קרפציו תאנים', 'מרכיבים:

תאנים
אגוזי מלך קלויים
עלי נענע
מעט פלפל חריף
גבינה בולגרית/גבינה כחולה

לתיבול:
שמן זית
מיץ לימון
חומץ בלסמי מצומצם
מעט מלח

אופן הכנה:
להניח על מגש תאנים קלופות ופרוסות.
לפזר מעל את אגוזי המלך, נענע, פלפל חריץ קצוץ דק, גבינה ולבסוף את הרוטב.
בתאבון!', "../static/media/img/recipe2.png");
INSERT INTO `web-project-g20`.`recipes` (recipe_id, recipe_name, description, picture) VALUES ('1', 'סלט חסה חגיגי', '/', "../static/media/img/recipe1.png");
INSERT INTO `web-project-g20`.`recipes` (recipe_id, recipe_name, description, picture) VALUES ('8', 'סלט שורשים', '/', "../static/media/img/recipe8.png");
INSERT INTO `web-project-g20`.`recipes` (recipe_id, recipe_name, description, picture) VALUES ('7', 'סלט תלתלי גזר', '/', "../static/media/img/recipe7.png");
INSERT INTO `web-project-g20`.`recipes` (recipe_id, recipe_name, description, picture) VALUES ('6', 'סלט תירס מקסיקני', '/', "../static/media/img/recipe6.png");
INSERT INTO `web-project-g20`.`recipes` (recipe_id, recipe_name, description, picture) VALUES ('5', 'גוואקמולי', '/', "../static/media/img/recipe5.png");

INSERT INTO `web-project-g20`.`recipe_products` (product_id, recipe_id) VALUES ('1', '1');
INSERT INTO `web-project-g20`.`recipe_products` (product_id, recipe_id) VALUES ('2', '1');
INSERT INTO `web-project-g20`.`recipe_products` (product_id, recipe_id) VALUES ('3', '1');
INSERT INTO `web-project-g20`.`recipe_products` (product_id, recipe_id) VALUES ('4', '1');
INSERT INTO `web-project-g20`.`recipe_products` (product_id, recipe_id) VALUES ('5', '1');
INSERT INTO `web-project-g20`.`recipe_products` (product_id, recipe_id) VALUES ('6', '1');
INSERT INTO `web-project-g20`.`recipe_products` (product_id, recipe_id) VALUES ('5', '2');
INSERT INTO `web-project-g20`.`recipe_products` (product_id, recipe_id) VALUES ('6', '2');
INSERT INTO `web-project-g20`.`recipe_products` (product_id, recipe_id) VALUES ('7', '3');
INSERT INTO `web-project-g20`.`recipe_products` (product_id, recipe_id) VALUES ('8', '3');
INSERT INTO `web-project-g20`.`recipe_products` (product_id, recipe_id) VALUES ('9', '3');
