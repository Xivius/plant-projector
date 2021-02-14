CREATE TABLE `plant_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `temp_upper` int DEFAULT NULL,
  `temp_lower` int DEFAULT NULL,
  `abs_temp_upper` int DEFAULT NULL,
  `abs_temp_lower` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
