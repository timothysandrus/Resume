-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: cards
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `idadmins` int NOT NULL,
  `admin_fn` varchar(45) NOT NULL DEFAULT 'test',
  `admin_ln` varchar(45) NOT NULL DEFAULT 'test',
  `cardnum` int NOT NULL,
  PRIMARY KEY (`idadmins`),
  UNIQUE KEY `cardnum_UNIQUE` (`cardnum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'Test','Admin',1234);
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `card_numbers`
--

DROP TABLE IF EXISTS `card_numbers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `card_numbers` (
  `usernumber` int NOT NULL AUTO_INCREMENT,
  `cardnum` int NOT NULL,
  `first_name` varchar(45) DEFAULT 'null',
  `last_name` varchar(45) DEFAULT 'null',
  `special` int DEFAULT '1' COMMENT '1 = students\n2 = TA\n3 = teacher\n4 = Admin',
  PRIMARY KEY (`usernumber`),
  UNIQUE KEY `usernumber_UNIQUE` (`usernumber`),
  UNIQUE KEY `cardnum_UNIQUE` (`cardnum`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `card_numbers`
--

LOCK TABLES `card_numbers` WRITE;
/*!40000 ALTER TABLE `card_numbers` DISABLE KEYS */;
INSERT INTO `card_numbers` VALUES (6,32710,'null','null',1),(7,15419,'null','null',1),(8,11775,'null','null',1),(9,1193,'null','null',1),(10,1111,'null','null',1),(11,5667,'null','null',1),(12,1112,'qrqwoer','ofmiemf',2),(13,1113,'121331','121313',2),(14,111,'null','null',1),(15,11111111,'null','null',1),(16,11111,'null','null',1),(17,6666,'null','null',1),(18,11131113,'null','null',1),(19,1234,'null','null',4);
/*!40000 ALTER TABLE `card_numbers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classes`
--

DROP TABLE IF EXISTS `classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classes` (
  `idClasses` int NOT NULL,
  `className` varchar(45) DEFAULT 'null',
  `classHour` varchar(45) DEFAULT 'null',
  PRIMARY KEY (`idClasses`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes`
--

LOCK TABLES `classes` WRITE;
/*!40000 ALTER TABLE `classes` DISABLE KEYS */;
INSERT INTO `classes` VALUES (1,'Math 1','2:00'),(2,'Math 2','3:00'),(3,'Math 3','12:00'),(4,'Math 4','10:00');
/*!40000 ALTER TABLE `classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `signed_in`
--

DROP TABLE IF EXISTS `signed_in`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `signed_in` (
  `idsigned_in` int NOT NULL,
  `teacher_num` int DEFAULT '0',
  `class_id` int DEFAULT '0',
  PRIMARY KEY (`idsigned_in`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `signed_in`
--

LOCK TABLES `signed_in` WRITE;
/*!40000 ALTER TABLE `signed_in` DISABLE KEYS */;
INSERT INTO `signed_in` VALUES (12,0,0),(13,0,0),(18,0,0);
/*!40000 ALTER TABLE `signed_in` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tas`
--

DROP TABLE IF EXISTS `tas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tas` (
  `idTAs` int NOT NULL,
  `here` tinyint DEFAULT '0',
  PRIMARY KEY (`idTAs`),
  UNIQUE KEY `idTAs_UNIQUE` (`idTAs`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tas`
--

LOCK TABLES `tas` WRITE;
/*!40000 ALTER TABLE `tas` DISABLE KEYS */;
INSERT INTO `tas` VALUES (12,1),(13,1);
/*!40000 ALTER TABLE `tas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `idTeachers` int NOT NULL,
  `TeacherfirstName` varchar(45) NOT NULL,
  `TeacherlastName` varchar(45) NOT NULL,
  PRIMARY KEY (`idTeachers`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (1,'Mr','Sine'),(2,'Mrs','Cosine'),(3,'Mr','Tangent');
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-23 10:56:19
