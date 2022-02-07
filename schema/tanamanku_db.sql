-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 13, 2022 at 01:17 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tanamanku_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `blog`
--

CREATE TABLE `blog` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `slug` text NOT NULL,
  `tag` varchar(64) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blog`
--

INSERT INTO `blog` (`id`, `title`, `content`, `slug`, `tag`, `created_at`, `updated_at`) VALUES
(2, 'Test Blog', 'asd', 'Test-Blog-118387014011111747562133512653920935189', 'plantae, bougenvillae', '2022-01-13 02:40:45', '2022-01-13 02:46:37');

-- --------------------------------------------------------

--
-- Table structure for table `genus`
--

CREATE TABLE `genus` (
  `id` int(11) NOT NULL,
  `name` varchar(256) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `genus`
--

INSERT INTO `genus` (`id`, `name`, `description`) VALUES
(1, 'Bougainvillea', 'Bougainvillea (/ˌbuːɡənˈvɪli.ə/ BOO-gən-VIL-ee-ə, US also /ˌboʊ-/ BOH-) is a genus of thorny ornamental vines, bushes, and trees belonging to the four o\' clock family, Nyctaginaceae. It is native to eastern South America, found from Brazil, west to Peru, and south to southern Argentina. Different authors accept from 4 to 18 species in the genus. The inflorescence consists of large colourful sepal-like bracts which surround three simple waxy flowers.'),
(7, 'Unknown', 'Unknown');

-- --------------------------------------------------------

--
-- Table structure for table `plant`
--

CREATE TABLE `plant` (
  `id` int(11) NOT NULL,
  `slug` text NOT NULL,
  `picture_url` text NOT NULL,
  `name` varchar(256) NOT NULL,
  `description` text NOT NULL,
  `species` varchar(256) NOT NULL,
  `genus_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `plant`
--

INSERT INTO `plant` (`id`, `slug`, `picture_url`, `name`, `description`, `species`, `genus_id`, `created_at`, `updated_at`) VALUES
(3, 'Bougainvillea-Bonsai-Tree-204449438368570057906401929427666277570', 'Bougainvillea-Bonsai-Tree-204449438368570057906401929427666277570.jfif', 'Bougainvillea Bonsai Tree', 'Bougainvillea Bonsai is a genus of ornamental flowering plants that are native to South America — mainly Peru, Brazil, and Argentina. It is named after the French Navy Admiral, Louis Antoine de Bougainville. Bougainvillea was discovered in 1768 by Philibert Commerco, a French botanist, who accompanied Bougainville on a voyage to circumnavigate the globe.', 'Bonsai', 1, '2022-01-13 03:48:26', '2022-01-13 11:23:39');

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `name` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`id`, `name`) VALUES
(1, 'Admin'),
(2, 'User');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `avatar_url` text NOT NULL,
  `name` varchar(256) DEFAULT NULL,
  `username` varchar(256) NOT NULL,
  `email` varchar(256) NOT NULL,
  `password` text NOT NULL,
  `role_id` int(11) NOT NULL DEFAULT 2,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `avatar_url`, `name`, `username`, `email`, `password`, `role_id`, `created_at`, `updated_at`) VALUES
(1, 'https://avatars.dicebear.com/api/initials/admin.svg', 'Admin', 'admin', 'admin@mail.com', 'pbkdf2:sha256:260000$hrYSOqM1iV1wiylA$da2c2fecd43068595cb2a3c8ef7a1b586644e309f645b568b9be1420e35141c9', 1, '2022-01-03 11:42:28', '2022-01-13 12:00:08'),
(5, 'https://avatars.dicebear.com/api/initials/test.svg', 'asd', 'test', 'test@mail.com', 'pbkdf2:sha256:260000$buy5hOEEotTZr0y7$2c804ef591d04a94fa905a4185b64e2430ebfb61797677eaff53da79e8a03c36', 2, '2022-01-13 02:37:57', '2022-01-13 02:39:46'),
(7, 'https://avatars.dicebear.com/api/initials/user_test.svg', 'user', 'user_test', 'user@mail.com', 'pbkdf2:sha256:260000$Xqt693HhHPZW1dt6$295ef91cdf97965710b61474326f26f0b350b9362b849bcc1345f35be053e922', 2, '2022-01-13 09:38:51', '2022-01-13 09:38:51'),
(10, 'https://avatars.dicebear.com/api/initials/leonards03.svg', 'Edwin Leonard Salim', 'leonards03', 'edwin.leonards03@gmail.com', 'pbkdf2:sha256:260000$30LGclJrMq7hHmee$68495feecf5d1588b385ffd50efda9181e9d6f5a85f16a11e2a69adc2832785f', 2, '2022-01-13 11:10:40', '2022-01-13 11:10:40');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blog`
--
ALTER TABLE `blog`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `genus`
--
ALTER TABLE `genus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `plant`
--
ALTER TABLE `plant`
  ADD PRIMARY KEY (`id`),
  ADD KEY `genus_id` (`genus_id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blog`
--
ALTER TABLE `blog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `genus`
--
ALTER TABLE `genus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `plant`
--
ALTER TABLE `plant`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `plant`
--
ALTER TABLE `plant`
  ADD CONSTRAINT `plant_ibfk_1` FOREIGN KEY (`genus_id`) REFERENCES `genus` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
