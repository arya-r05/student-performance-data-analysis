-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: attendance_system
-- ------------------------------------------------------
-- Server version	8.0.44

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
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL,
  `year` int DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=153 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (101,'Akhil Nair','BCA',1),(102,'Anjali Menon','BCA',1),(103,'Rahul Raj','BCA',1),(104,'Meera Krishnan','BCA',1),(105,'Vishnu Prasad','BCA',1),(106,'Arun Suresh','BCA',1),(107,'Nithya Mohan','BCA',1),(108,'Sreeram N','BCA',1),(109,'Keerthana R','BCA',1),(110,'Aditya Varma','BCA',1),(111,'Devika Pillai','BCA',1),(112,'Karthik B','BCA',1),(113,'Lakshmi Nair','BCA',1),(114,'Gokul Krishna','BCA',1),(115,'Sneha S','BCA',1),(116,'Abhinav P','BCA',1),(117,'Gayathri R','BCA',1),(118,'Anoop Kumar','BCA',2),(119,'Diya Thomas','BCA',2),(120,'Rohit S','BCA',2),(121,'Athira Nair','BCA',2),(122,'Manoj K','BCA',2),(123,'Harsha V','BCA',2),(124,'Neha Suresh','BCA',2),(125,'Vivek Raj','BCA',2),(126,'Ananya P','BCA',2),(127,'Sanjay Menon','BCA',2),(128,'Reshma R','BCA',2),(129,'Nikhil Das','BCA',2),(130,'Aiswarya K','BCA',2),(131,'Pranav S','BCA',2),(132,'Anu Maria','BCA',2),(133,'Rahul Krishna','BCA',2),(134,'Divya Mohan','BCA',2),(135,'Abhishek Nair','BCA',3),(136,'Megha S','BCA',3),(137,'Sidharth R','BCA',3),(138,'Keerthi P','BCA',3),(139,'Ramesh Kumar','BCA',3),(140,'Aparna L','BCA',3),(141,'Vishal K','BCA',3),(142,'Anita S','BCA',3),(143,'Sreenath P','BCA',3),(144,'Deepa R','BCA',3),(145,'Harikrishnan V','BCA',3),(146,'Aswathy N','BCA',3),(147,'Naveen Raj','BCA',3),(148,'Bhavana M','BCA',3),(149,'Ajith K','BCA',3),(150,'Tejaswini S','BCA',3),(151,'kavya','BCA',3),(152,'Vasanth','BCA',3);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-04 20:16:10
