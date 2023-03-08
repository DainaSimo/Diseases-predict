-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: derma_predict
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `id_patient` int NOT NULL,
  `érythème` int DEFAULT NULL,
  `desquamation` int DEFAULT NULL,
  `limites_définies` int DEFAULT NULL,
  `démangeaisons` int DEFAULT NULL,
  `phénomène_de_Koebner` int DEFAULT NULL,
  `papules_polygonales` int DEFAULT NULL,
  `papules_folliculaires` int DEFAULT NULL,
  `atteinte_des_muqueuses_buccales` int DEFAULT NULL,
  `atteinte_des_genoux_et_des_coudes` int DEFAULT NULL,
  `atteinte_du_cuir_chevelu` int DEFAULT NULL,
  `antécédents_familiaux` int DEFAULT NULL,
  `incontinence_de_mélanine` int DEFAULT NULL,
  `éosinophiles_dans_infiltrat` int DEFAULT NULL,
  `infiltrat_de_la_PNL` int DEFAULT NULL,
  `fibrose_du_derme_papillaire` int DEFAULT NULL,
  `exocytose` int DEFAULT NULL,
  `acanthose` int DEFAULT NULL,
  `hyperkératose` int DEFAULT NULL,
  `parakératose` int DEFAULT NULL,
  `hernie_des_crêtes_de_rete` int DEFAULT NULL,
  `allongement_des_crêtes_de_rete` int DEFAULT NULL,
  `amincissement_de_épiderme_suprapapillaire` int DEFAULT NULL,
  `pustule_spongiforme` int DEFAULT NULL,
  `Micro_abcès_de_Munro` int DEFAULT NULL,
  `hypergranulie_focale` int DEFAULT NULL,
  `disparition_de_la_couche_granuleuse` int DEFAULT NULL,
  `vacuolisation_et_atteinte_de_la_couche_basale` int DEFAULT NULL,
  `spongiose` int DEFAULT NULL,
  `aspect_en_dents_de_scie_des_rets` int DEFAULT NULL,
  `bouchon_de_corne_folliculaire` int DEFAULT NULL,
  `parakératose_périfolliculaire` int DEFAULT NULL,
  `infiltrat_monolucléaire_inflammatoire` int DEFAULT NULL,
  `infiltrat_en_forme_de_bande` int DEFAULT NULL,
  `Âge` int DEFAULT NULL,
  PRIMARY KEY (`id_patient`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (1,2,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,2,0,25),(2,3,2,1,0,1,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,1,0,1,0,0,0,2,0,36);
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-12 14:36:54
