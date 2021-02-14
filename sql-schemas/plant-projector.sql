CREATE TABLE `plant_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `day_temp_upper` int DEFAULT NULL,
  `day_temp_lower` int DEFAULT NULL,
  `night_temp_upper` int DEFAULT NULL,
  `night_temp_lower` int DEFAULT NULL,
  `absolute_min_temp` int DEFAULT NULL,
  `absolute_max_temp` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
