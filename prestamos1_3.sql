-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: prestamos1_2
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `ape_pat` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `ape_mat` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `id_genero` tinyint NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `id_nivelEdu` tinyint NOT NULL,
  `id_ocupacion` tinyint NOT NULL,
  `ingresos_mensuales` float unsigned NOT NULL,
  `curp` varchar(18) COLLATE utf8mb4_general_ci NOT NULL,
  `tel_cel` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `tel_casa` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `rol` varchar(7) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'cliente',
  `is_approved` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id_usuario`),
  KEY `fk_ocupacion` (`id_ocupacion`),
  KEY `fk_nivelEducativo` (`id_nivelEdu`),
  KEY `fk_genero` (`id_genero`),
  CONSTRAINT `fk_genero` FOREIGN KEY (`id_genero`) REFERENCES `genero` (`id_genero`),
  CONSTRAINT `fk_nivelEducativo` FOREIGN KEY (`id_nivelEdu`) REFERENCES `nivel_educativo` (`id_nivelEdu`),
  CONSTRAINT `fk_ocupacion` FOREIGN KEY (`id_ocupacion`) REFERENCES `ocupacion` (`id_ocupacion`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Angel','Perez','Rodriguez',1,'2003-07-17',3,1,2000,'PERA030717HTLRDNA4','255','0','ared230000@gmail.com','pbkdf2:sha256:600000$AyQuHTTQHSbzYSMd$e2fb291a4889891ba1344e8a99513c53e523f2d06af522614f63767cc06b68cc','admin',1),(2,'Adriana','Medina','Montiel',2,'2004-05-02',3,2,5000,'MEMD030723MTLRDPR4','2551342422','','adri@gmail.com','pbkdf2:sha256:600000$471yPAnI0TjdFiU7$475e17fa87a1b105b7b4b615b3cee9945c9c87c9d7b9613d05de14fe78185c98','cliente',1),(8,'Angelica','Hernández','Lopez',2,'1975-12-12',4,2,7000,'PERA030717HTLR1234','2551342422','','angy@gmail.com','pbkdf2:sha256:600000$kWTPIM13$b9f5fa426958410b4b1f2cc83c6701ccb64145c68db4d18c89a2576e182512ac','cliente',2),(11,'Brayan','Perez','Montiel',1,'2001-11-11',2,2,7000,'PERA030717HTLRDN22','2551342422','','prueba2@gmail.com','pbkdf2:sha256:600000$cVlGjsId$906bd9406dd2b611bc5ba1b9f3d97fe3a3e5410c92d29274fc16168eafed9918','cliente',0),(13,'Diana','Hernández','Rodriguez',2,'2001-12-12',1,1,2500,'PERA030717HTLRDNA7','2471014132','2713455540','prueba3@gmail.com','pbkdf2:sha256:600000$rYvmGAgK$0f2b6f0b6629ba885c567407d3ec5b0fe3c14d24febb921411fbb0916872a016','cliente',0),(14,'Angelica','Perez','Rodriguez',1,'2005-04-18',3,3,2000,'PERA030717HTLRDNA7','2551342422','','prueba4@gmail.com','pbkdf2:sha256:600000$Enmh8Q17$4b8f46865a838c0593a6449ff1c4c94ae6ea177cceb000cfe90c9fe1e64e4575','cliente',1),(19,'Joaquin','Perez','Rodriguez',1,'2000-01-01',1,3,7500,'PERA030718HTLRDNJ4','2411553132','','prueba5@gmail.com','pbkdf2:sha256:1000000$12p65cgC$1e07c12b5008cce4727fb16dfcbbe7f30291683aa0c5a7cb4bd665d2b9f6a020','cliente',0),(20,'Joaquin','Perez','Rodriguez',1,'2000-01-01',1,3,7500,'PERA030718HTLRDNJ4','2411553132','','prueba6@gmail.com','pbkdf2:sha256:1000000$JZxyAMXT$64133dd2dcc75a8f59e5be3bf7cc2998772223344c3aba135eec98fbe1e91ad8','cliente',0),(25,'Joaquin','Perez','Rodriguez',1,'2000-01-01',1,3,7500,'PERA030718HTLRDNJ4','2411553132','','prueba10@gmail.com','pbkdf2:sha256:1000000$2D6NRkdi$424417a29ff56c441856a1a4953eb99a97b15eb4a25a63b6c6511a3faea315b9','cliente',1),(26,'Joaquin','Perez','Rodriguez',1,'2000-01-01',1,3,7500,'PERA030718HTLRDNJ4','2411553132','','prueba11@gmail.com','pbkdf2:sha256:1000000$ZcxWEE90$67942a186541fc24ebaf6be44ee1f3a03b6341f29da525e794e73355274a6394','cliente',1);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `domicilio`
--

DROP TABLE IF EXISTS `domicilio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `domicilio` (
  `id_domicilio` int NOT NULL AUTO_INCREMENT,
  `id_estado` tinyint unsigned NOT NULL,
  `municipio` varchar(50) NOT NULL,
  `cp` mediumint NOT NULL,
  `tipo_asen` tinyint NOT NULL,
  `asentamiento` varchar(60) NOT NULL,
  `calle` varchar(50) NOT NULL,
  `num_ext` smallint unsigned DEFAULT NULL,
  `num_int` smallint unsigned DEFAULT NULL,
  `id_cliente` int NOT NULL,
  PRIMARY KEY (`id_domicilio`),
  KEY `cp` (`cp`),
  KEY `municipios_idx` (`municipio`),
  KEY `fk_domicilio_estados_idx` (`id_estado`),
  KEY `fk_domicilio_clientes` (`id_cliente`),
  KEY `fk_domicilio_tipoAsentamiento` (`tipo_asen`),
  CONSTRAINT `fk_domicilio_clientes` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_usuario`),
  CONSTRAINT `fk_domicilio_estados` FOREIGN KEY (`id_estado`) REFERENCES `estados` (`id_estado`),
  CONSTRAINT `fk_domicilio_tipoAsentamiento` FOREIGN KEY (`tipo_asen`) REFERENCES `tipos_asen` (`id_tipo_asen`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `domicilio`
--

LOCK TABLES `domicilio` WRITE;
/*!40000 ALTER TABLE `domicilio` DISABLE KEYS */;
INSERT INTO `domicilio` VALUES (1,29,'Huamantla',90506,30,'Ignacio Zaragoza','Andador Los Reyes',60,NULL,1),(2,29,'Tetla ',90501,29,'La Colina','Las Flores',12,4,2),(3,1,'Huamantla',2000,1,'La Colina','Río Coatzacoatcos ',1,NULL,2),(4,1,'Huamantla',30000,1,'Ignacio Zaragoza','Las Flores',60,NULL,2),(5,29,'Huamantla',90506,5,'Nuevos Horizontes','Las Flores',60,NULL,8),(6,29,'Ixtenco',90501,26,'Ignacio Zaragoza','Río Coatzacoatcos ',NULL,23,11),(7,1,'Huamantla',12345,27,'La Colina','Las Flores',NULL,NULL,2),(8,2,'Ixtenco',90506,14,'La Colina','Las Flores',2,NULL,2),(9,4,'Ixtenco',90506,12,'La Colina','Las Flores',12,NULL,2),(10,4,'Ixtenco',90506,12,'La Colina','Las Flores',12,NULL,2),(11,8,'Chihuahua',80500,6,'Estrella Roja','Duraznos',23,12,25),(12,5,'Tetla de la Solidaridad',50500,15,'manzana','rio coatzacoatcos',14,NULL,26),(13,7,'Tetla de la Solidaridad',90500,16,'diamante','los reyes',11,NULL,26);
/*!40000 ALTER TABLE `domicilio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estados`
--

DROP TABLE IF EXISTS `estados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estados` (
  `id_estado` tinyint unsigned NOT NULL,
  `estado` varchar(35) NOT NULL,
  PRIMARY KEY (`id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estados`
--

LOCK TABLES `estados` WRITE;
/*!40000 ALTER TABLE `estados` DISABLE KEYS */;
INSERT INTO `estados` VALUES (1,'Aguascalientes'),(2,'Baja California'),(3,'Baja California Sur'),(4,'Campeche'),(5,'Coahuila'),(6,'Colima'),(7,'Chiapas'),(8,'Chihuahua'),(9,'Ciudad de México'),(10,'Durango'),(11,'Estado de México'),(12,'Guanajuato'),(13,'Guerrero'),(14,'Hidalgo'),(15,'Jalisco'),(16,'Michoacán'),(17,'Morelos'),(18,'Nayarit'),(19,'Nuevo León'),(20,'Oaxaca'),(21,'Puebla'),(22,'Querétaro'),(23,'Quintana Roo'),(24,'San Luis Potosí'),(25,'Sinaloa'),(26,'Sonora'),(27,'Tabasco'),(28,'Tamaulipas'),(29,'Tlaxcala'),(30,'Veracruz'),(31,'Yucatán'),(32,'Zacatecas');
/*!40000 ALTER TABLE `estados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genero`
--

DROP TABLE IF EXISTS `genero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genero` (
  `id_genero` tinyint NOT NULL AUTO_INCREMENT,
  `genero` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_genero`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genero`
--

LOCK TABLES `genero` WRITE;
/*!40000 ALTER TABLE `genero` DISABLE KEYS */;
INSERT INTO `genero` VALUES (1,'Masculino'),(2,'Femenino');
/*!40000 ALTER TABLE `genero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nivel_educativo`
--

DROP TABLE IF EXISTS `nivel_educativo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nivel_educativo` (
  `id_nivelEdu` tinyint NOT NULL AUTO_INCREMENT,
  `nivelEdu` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_nivelEdu`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nivel_educativo`
--

LOCK TABLES `nivel_educativo` WRITE;
/*!40000 ALTER TABLE `nivel_educativo` DISABLE KEYS */;
INSERT INTO `nivel_educativo` VALUES (1,'Sin estudios'),(2,'Educación básica'),(3,'Preparatoria'),(4,'Licenciatura '),(5,'Ingeniería'),(6,'Maestría o Superior');
/*!40000 ALTER TABLE `nivel_educativo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ocupacion`
--

DROP TABLE IF EXISTS `ocupacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ocupacion` (
  `id_ocupacion` tinyint NOT NULL AUTO_INCREMENT,
  `ocupacion` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_ocupacion`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ocupacion`
--

LOCK TABLES `ocupacion` WRITE;
/*!40000 ALTER TABLE `ocupacion` DISABLE KEYS */;
INSERT INTO `ocupacion` VALUES (1,'Empleado del sector privado'),(2,'Empleado del sector público'),(3,'Desempleado');
/*!40000 ALTER TABLE `ocupacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestamos`
--

DROP TABLE IF EXISTS `prestamos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prestamos` (
  `id_prestamo` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `monto` decimal(10,2) NOT NULL,
  `interes` decimal(5,2) NOT NULL,
  `monto_total` decimal(10,2) NOT NULL,
  `plazo` int NOT NULL,
  `estado` enum('Pendiente','Activo','Pagado','Cancelado') DEFAULT 'Pendiente',
  `fecha_inicio` date DEFAULT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  PRIMARY KEY (`id_prestamo`),
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `prestamos_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestamos`
--

LOCK TABLES `prestamos` WRITE;
/*!40000 ALTER TABLE `prestamos` DISABLE KEYS */;
INSERT INTO `prestamos` VALUES (1,25,10000.00,0.15,11500.00,12,'Pendiente',NULL,NULL),(2,26,10000.00,0.15,11500.00,12,'Pendiente',NULL,NULL);
/*!40000 ALTER TABLE `prestamos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos_asen`
--

DROP TABLE IF EXISTS `tipos_asen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos_asen` (
  `id_tipo_asen` tinyint NOT NULL AUTO_INCREMENT,
  `tipoAsen` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_tipo_asen`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_asen`
--

LOCK TABLES `tipos_asen` WRITE;
/*!40000 ALTER TABLE `tipos_asen` DISABLE KEYS */;
INSERT INTO `tipos_asen` VALUES (1,'Ampliación'),(2,'Barrio'),(3,'Ciudad'),(4,'Ciudad Industrial'),(5,'Colonia'),(6,'Condominio'),(7,'Conjunto Habitacional'),(8,'Corredor Industrial'),(9,'Ejido'),(10,'Exhacienda'),(11,'Fracción'),(12,'Fraccionamiento'),(13,'Granja'),(14,'Hacienda'),(15,'Manzana'),(16,'Paraje'),(17,'Privada'),(18,'Prolongación'),(19,'Pueblo'),(20,'Puerto'),(21,'Ranchería'),(22,'Rancho'),(23,'Región'),(24,'Residencial'),(25,'Rinconada'),(26,'Sección'),(27,'Sector'),(28,'Supermanzana'),(29,'Unidad'),(30,'Unidad Habitacional'),(31,'Villa'),(32,'Zona Federal'),(33,'Zona Industrial'),(34,'Zona Militar');
/*!40000 ALTER TABLE `tipos_asen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vista_domicilioxcliente`
--

DROP TABLE IF EXISTS `vista_domicilioxcliente`;
/*!50001 DROP VIEW IF EXISTS `vista_domicilioxcliente`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vista_domicilioxcliente` AS SELECT 
 1 AS `id_domicilio`,
 1 AS `estado`,
 1 AS `municipio`,
 1 AS `codigo_postal`,
 1 AS `tipoAsen`,
 1 AS `nombre_asentamiento`,
 1 AS `calle`,
 1 AS `num_ext`,
 1 AS `num_int`,
 1 AS `id_cliente`,
 1 AS `domicilio_de`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vista_prestamos`
--

DROP TABLE IF EXISTS `vista_prestamos`;
/*!50001 DROP VIEW IF EXISTS `vista_prestamos`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vista_prestamos` AS SELECT 
 1 AS `id_prestamo`,
 1 AS `nombre`,
 1 AS `ape_pat`,
 1 AS `ape_mat`,
 1 AS `email`,
 1 AS `monto`,
 1 AS `interes`,
 1 AS `monto_total`,
 1 AS `plazo`,
 1 AS `estado`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vistaclientes`
--

DROP TABLE IF EXISTS `vistaclientes`;
/*!50001 DROP VIEW IF EXISTS `vistaclientes`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vistaclientes` AS SELECT 
 1 AS `id_usuario`,
 1 AS `nombre`,
 1 AS `ape_pat`,
 1 AS `ape_mat`,
 1 AS `genero`,
 1 AS `fecha_nacimiento`,
 1 AS `nivelEdu`,
 1 AS `ocupacion`,
 1 AS `ingresos_mensuales`,
 1 AS `curp`,
 1 AS `tel_cel`,
 1 AS `tel_casa`,
 1 AS `email`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vistausuarios`
--

DROP TABLE IF EXISTS `vistausuarios`;
/*!50001 DROP VIEW IF EXISTS `vistausuarios`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vistausuarios` AS SELECT 
 1 AS `id_usuario`,
 1 AS `nombre`,
 1 AS `ape_pat`,
 1 AS `ape_mat`,
 1 AS `genero`,
 1 AS `fecha_nacimiento`,
 1 AS `nivelEdu`,
 1 AS `ocupacion`,
 1 AS `ingresos_mensuales`,
 1 AS `curp`,
 1 AS `tel_cel`,
 1 AS `tel_casa`,
 1 AS `email`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vista_domicilioxcliente`
--

/*!50001 DROP VIEW IF EXISTS `vista_domicilioxcliente`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vista_domicilioxcliente` AS select `domicilio`.`id_domicilio` AS `id_domicilio`,`estados`.`estado` AS `estado`,`domicilio`.`municipio` AS `municipio`,`domicilio`.`cp` AS `codigo_postal`,`tipos_asen`.`tipoAsen` AS `tipoAsen`,`domicilio`.`asentamiento` AS `nombre_asentamiento`,`domicilio`.`calle` AS `calle`,`domicilio`.`num_ext` AS `num_ext`,`domicilio`.`num_int` AS `num_int`,`domicilio`.`id_cliente` AS `id_cliente`,`clientes`.`nombre` AS `domicilio_de` from (((`domicilio` join `estados` on((`domicilio`.`id_estado` = `estados`.`id_estado`))) join `tipos_asen` on((`domicilio`.`tipo_asen` = `tipos_asen`.`id_tipo_asen`))) join `clientes` on((`domicilio`.`id_cliente` = `clientes`.`id_usuario`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vista_prestamos`
--

/*!50001 DROP VIEW IF EXISTS `vista_prestamos`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`usuario`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vista_prestamos` AS select `p`.`id_prestamo` AS `id_prestamo`,`c`.`nombre` AS `nombre`,`c`.`ape_pat` AS `ape_pat`,`c`.`ape_mat` AS `ape_mat`,`c`.`email` AS `email`,`p`.`monto` AS `monto`,`p`.`interes` AS `interes`,`p`.`monto_total` AS `monto_total`,`p`.`plazo` AS `plazo`,`p`.`estado` AS `estado` from (`prestamos` `p` join `clientes` `c` on((`p`.`id_cliente` = `c`.`id_usuario`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vistaclientes`
--

/*!50001 DROP VIEW IF EXISTS `vistaclientes`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vistaclientes` AS select `clientes`.`id_usuario` AS `id_usuario`,`clientes`.`nombre` AS `nombre`,`clientes`.`ape_pat` AS `ape_pat`,`clientes`.`ape_mat` AS `ape_mat`,`genero`.`genero` AS `genero`,`clientes`.`fecha_nacimiento` AS `fecha_nacimiento`,`nivel_educativo`.`nivelEdu` AS `nivelEdu`,`ocupacion`.`ocupacion` AS `ocupacion`,`clientes`.`ingresos_mensuales` AS `ingresos_mensuales`,`clientes`.`curp` AS `curp`,`clientes`.`tel_cel` AS `tel_cel`,`clientes`.`tel_casa` AS `tel_casa`,`clientes`.`email` AS `email` from (((`clientes` join `genero` on((`clientes`.`id_genero` = `genero`.`id_genero`))) join `nivel_educativo` on((`clientes`.`id_nivelEdu` = `nivel_educativo`.`id_nivelEdu`))) join `ocupacion` on((`clientes`.`id_ocupacion` = `ocupacion`.`id_ocupacion`))) where ((`clientes`.`rol` = 'cliente') and (`clientes`.`is_approved` = 1)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vistausuarios`
--

/*!50001 DROP VIEW IF EXISTS `vistausuarios`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vistausuarios` AS select `clientes`.`id_usuario` AS `id_usuario`,`clientes`.`nombre` AS `nombre`,`clientes`.`ape_pat` AS `ape_pat`,`clientes`.`ape_mat` AS `ape_mat`,`genero`.`genero` AS `genero`,`clientes`.`fecha_nacimiento` AS `fecha_nacimiento`,`nivel_educativo`.`nivelEdu` AS `nivelEdu`,`ocupacion`.`ocupacion` AS `ocupacion`,`clientes`.`ingresos_mensuales` AS `ingresos_mensuales`,`clientes`.`curp` AS `curp`,`clientes`.`tel_cel` AS `tel_cel`,`clientes`.`tel_casa` AS `tel_casa`,`clientes`.`email` AS `email` from (((`clientes` join `genero` on((`clientes`.`id_genero` = `genero`.`id_genero`))) join `nivel_educativo` on((`clientes`.`id_nivelEdu` = `nivel_educativo`.`id_nivelEdu`))) join `ocupacion` on((`clientes`.`id_ocupacion` = `ocupacion`.`id_ocupacion`))) where ((`clientes`.`rol` = 'cliente') and (`clientes`.`is_approved` = 0)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-02 11:58:59
