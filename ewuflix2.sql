-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 12, 2024 at 07:05 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ewuflix2`
--

-- --------------------------------------------------------

--
-- Table structure for table `movies`
--

CREATE TABLE `movies` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `image_path` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movies`
--

INSERT INTO `movies` (`id`, `title`, `description`, `image_path`) VALUES
(1, 'Mujib: The Making of a Nation', '2023 ‧ Biography/Drama ‧ 2h 58m\r\n', 'static/images/MV5BMDFjNTk1OWEtMDgwYi00MDE1LWI1YTEtZjExN2Q3OTg4NWVkXkEyXkFqcGdeQXVyOTc5MjUzNjg@._V1_.jpg'),
(2, 'Monpura', 'A housemaid is killed by a local landlord\'s son. His servant takes the blame for the murder, to save the landlord\'s mentally ill son and is marooned in an island named Monpura. There the servant comes across a fisherman\'s daughter.\r\n\r\n', 'static/images/monpura.jpg'),
(3, 'Mohabbatein', 'Narayan is a strict principal of Gurukul who doesnot believe in love and forbids his studentsfrom following their hearts. However, things take a turn when a music teacher challenges his authority.', 'static/images/download.jpg'),
(4, 'Kal Ho Na Ho', 'Aman inserts positivitiy and liveliness into the life of Naina, a defeatist MBA student with familiar Problems. Naina, smittem with him, wishes to wed him, but is unware of his terminal illness.', 'static/images/download (3).jpg'),
(5, 'Jab Tak HA Jaan', 'In London, Samar falls for Meera but returns to india to work as a bumb disposal specialist after she leaves him. Arika, a journalism, falls in love with him but decides to untie the lovers', 'static/images/download (4).jpg'),
(6, 'Dilwale Dulhania Le Jayenge', 'Raj and Simran meet during a trip across Europe and the two fall in love. However, when Raj learns that Simran is already promised to another, he follows her to India to win her and her father over.', 'static/images/download (5).jpg'),
(7, 'Om Shanti Om', 'Om, a junior film artist, is smitten by Shantipriya, a renowned actress, but is killed while trying to save her from a fire accident. Thirty years later, he is reborn and sets out to avenge her death.', 'static/images/download (6).jpg'),
(8, '500 Days of Summer', 'After being dumped by the girl he believes to be his soulmate, hopeless romantic Tom Hansen reflects on their relationship to try and figure out where things went wrong and how he can win her back. Tom (Gordon-Levitt) is an aspiring architect who currently earns his living as a greeting card writer.', 'static/images/download (7).jpg'),
(9, 'Past Lives', 'Starring Greta Lee, Teo Yoo, and John Magaro, the film follows the relationship between two childhood friends over the course of 24 years, as they contemplate their relationship when they grow apart to have different lives. The plot is semi-autobiographical and inspired by real events from Song\'s life.', 'static/images/download (8).jpg'),
(10, 'Mission: Impossible', 'Mission: Impossible is a series of American action spy films, based on the 1966 TV series created by Bruce Geller. The series is mainly produced by and stars Tom Cruise, who plays Ethan Hunt, an agent of the Impossible Missions Force. Wikipedia', 'static/images/download (10).jpg'),
(11, 'Transformers', 'Based on the Hasbro toyline and it\'s resulting animated series/comics, the film follows high-schooler Sam Witwicky who discovers his Camaro is a shape-shifting alien robot; he is soon brought into the middle of a war between the Autobots and the Decepticons, warring factions of a race of sentient robots.', 'static/images/download (11).jpg'),
(12, 'WAR', 'Khalid (Tiger Shroff), an Indian Research and Analysis Wing (RAW) agent, is assigned to eliminate Kabir (Hrithik Roshan), a former soldier-turned-rogue, who mentored Khalid. Col Luthra (Ashutosh Rana) is on a mission to bring Kabir to justice, who seems to be eliminating RAW targets all over the world.', 'static/images/download (2).jpg'),
(13, 'RAEES', 'Raees (Shah Rukh Khan), from Fatehpur, Gujarat gets involved in illegal liquor trade at a very young age. Along with Sadiq (Mohammed Zeeshan Ayyub), Raees works for a notorious gangster Jairaj (Atul Kulkarni), smuggles alcohol illegally by bribing the police.', 'static/images/download (12).jpg'),
(14, 'KGF', 'Rocky, a high-ranking mercenary, working for a prominent gold mafia in Bombay, seeks power and wealth in order to fulfill his mother\'s promise. Due to his high fame, the leaders of the gold mafia where he works hire him to assassinate Garuda, the son of the founder of Kolar Gold Fields.', 'static/images/download (12).jpg'),
(15, 'Terminator', 'Disguised as a human, a cyborg assassin known as a Terminator (Arnold Schwarzenegger) travels from 2029 to 1984 to kill Sarah Connor (Linda Hamilton). Sent to protect Sarah is Kyle Reese (Michael Biehn), who divulges the coming of Skynet, an artificial intelligence system that will spark a nuclear holocaust.', 'static/images/download (27).jpg'),
(16, 'PARI', ' A kind hearted man tries to help Rukhsana, a chained women in a hut who is probably a victim of abuse.However, he soon realises that things are not as they appear to be', 'static/images/download (1).jpg'),
(17, '1920: Horrors of the Heart', 'Young Meghna tells her father, Dheeraj, of her love on her 21st birthday, and her worst nightmare comes alive when Dheeraj kills himself. Abandoned by her mother as a child, Meghna learns her mother is also responsible for her father\'s death. Unable to bear the betrayal, Meghna vows to destroy Radhika and her current family with a sinister plot using her father\'s spirit.', 'static/images/download (14).jpg'),
(18, 'CHHORII', 'Hemant and Sakshi, a married couple, are forced to move out of their home and seek refuge in a remote house. However, she soon experiences supernatural events which threaten her life.', 'static/images/download (15).jpg'),
(19, 'Stree', 'The people of Chanderi live under constant fear of Stree, the spirit of a woman who attacks men at night during festivals. Vicky, along with his friends, decides to unravel the mystery', 'static/images/download (16).jpg'),
(20, 'ANNABELLE', 'John and Mia Form are attacked by members of a satanic cult that uses their old doll as a conduit to make their life miserable. This unleashes a string of paranormal events in the Forms\' residence', 'static/images/download (17).jpg'),
(21, 'The NUN', 'A priest and a novice arrive in Romania to investigate the death of a young nun. However, things take an ugly turn after they encounter a supernatural force.', 'static/images/MV5BMjEzMjg1ZjItM2ViOS00ZTNmLWE5MTItYWE5ZGYyMmNhYjBkXkEyXkFqcGdeQXVyMTYzMDM0NTU@._V1_.jpg'),
(22, 'The Conjuring', 'Rod and Carolyn find their pet dog dead under mysterious circumstances and experience a spirit that harms their daughter Andrea. They finally call investigators who can help them get out of the mess.', 'static/images/download (18).jpg'),
(23, 'The theory of Everything', 'A look at the relationship between the famous physicist Stephen Hawking and his wife.', 'static/images/download (19).jpg'),
(24, 'American Buffalo', 'The American bison (Bison bison; pl: bison), also called the American buffalo or simply buffalo (not to be confused with true buffalo), is a species of bison native to North America.', 'static/images/download (20).jpg'),
(25, 'No one will save you', 'An exiled anxiety-ridden homebody must battle an alien who\'s found its way into her home.', 'static/images/download (21).jpg'),
(26, 'The Creator', 'Against the backdrop of a war between humans and robots with artificial intelligence, a former soldier finds the secret weapon, a robot in the form of a young child.', 'static/images/download (22).jpg'),
(27, 'Coherence', 'Theme is the underlying concept that a piece of literature or film conveys. It\'s the central idea, mood, and emotion of your work.', 'static/images/download (23).jpg'),
(28, 'Golmaaal', 'Golmaal is an Indian comedy film series directed by Rohit Shetty, with four installments to date, the first three produced by Dhilin Mehta, the fourth by Shetty and Sangeeta Ahir and the fifth which is a spin off is produced by Shetty with Bhushan Kumar.', 'static/images/download (24).jpg'),
(29, 'Doctor G', 'Doctor G is a  Indian Hindi-language comedy-drama film directed by Anubhuti Kashyap and produced by Junglee Pictures. It stars Ayushmann Khurrana, Rakul Preet Singh and Shefali Shah. The film follows the struggles of a medical student who is interested in orthopaedics but instead becomes a gynaecologist, and the ensuing chaos.', 'static/images/download (25).jpg'),
(30, 'Dream Girl-2', 'The film is about a man who cross-dresses and disguises as a woman, leading to a lot of chaos and confusion.', 'static/images/download (26).jpg');

-- --------------------------------------------------------

--
-- Table structure for table `movie_ratings`
--

CREATE TABLE `movie_ratings` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `rating1` int(11) DEFAULT NULL,
  `rating2` int(11) DEFAULT NULL,
  `rating3` int(11) DEFAULT NULL,
  `rating4` int(11) DEFAULT NULL,
  `overall_rating` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movie_ratings`
--

INSERT INTO `movie_ratings` (`id`, `user_id`, `movie_id`, `rating1`, `rating2`, `rating3`, `rating4`, `overall_rating`) VALUES
(1, 1, 1, 3, 2, 3, 1, '3.57'),
(2, 1, 2, 5, 4, 5, 3, '4.25'),
(3, 1, 2, 5, 5, 5, 3, '4.50'),
(4, 1, 2, 3, 3, 3, 3, '3.00'),
(5, 3, 1, 4, 5, 3, 2, '3.50'),
(6, 4, 1, 5, 5, 5, 5, '5.00'),
(7, 6, 3, 4, 5, 5, 5, '4.75'),
(8, 6, 4, 5, 4, 3, 3, '3.75'),
(9, 6, 5, 5, 5, 5, 5, '5.00'),
(10, 6, 6, 4, 5, 4, 3, '4.00'),
(11, 6, 7, 5, 5, 5, 5, '5.00'),
(12, 6, 8, 3, 3, 3, 4, '3.25'),
(13, 6, 9, 5, 4, 4, 4, '4.25'),
(14, 6, 9, 4, 3, 3, 4, '3.50'),
(15, 6, 10, 5, 4, 3, 4, '4.00'),
(16, 6, 11, 3, 4, 3, 4, '3.50'),
(17, 6, 12, 4, 4, 4, 4, '4.00'),
(18, 6, 13, 4, 4, 4, 4, '4.00'),
(19, 6, 14, 5, 5, 5, 5, '5.00'),
(20, 6, 15, 4, 4, 4, 4, '4.00'),
(21, 6, 16, 3, 3, 3, 3, '3.00'),
(22, 6, 17, 5, 3, 3, 4, '3.75'),
(23, 6, 18, 2, 3, 4, 3, '3.00'),
(24, 6, 19, 4, 4, 4, 4, '4.00'),
(25, 6, 20, 4, 4, 4, 4, '4.00'),
(26, 6, 21, 4, 3, 4, 4, '3.75'),
(27, 6, 22, 4, 4, 4, 4, '4.00'),
(28, 6, 23, 3, 3, 3, 3, '3.00'),
(29, 6, 24, 3, 3, 3, 3, '3.00'),
(30, 6, 25, 4, 3, 4, 5, '4.00'),
(31, 6, 26, 4, 4, 2, 3, '3.25'),
(32, 6, 27, 4, 3, 5, 3, '3.75'),
(33, 6, 28, 4, 4, 4, 3, '3.75'),
(34, 6, 29, 3, 3, 2, 3, '2.75'),
(35, 6, 30, 3, 4, 4, 4, '3.75'),
(36, 7, 3, 5, 4, 5, 4, '4.50'),
(37, 7, 4, 5, 4, 5, 4, '4.50'),
(38, 7, 5, 4, 5, 5, 5, '4.75'),
(39, 7, 6, 5, 5, 4, 5, '4.75'),
(40, 7, 7, 4, 4, 5, 5, '4.50'),
(41, 7, 8, 5, 4, 4, 4, '4.25'),
(42, 7, 9, 5, 4, 5, 4, '4.50'),
(43, 7, 10, 3, 3, 3, 3, '3.00'),
(44, 7, 11, 5, 3, 4, 3, '3.75'),
(45, 7, 12, 4, 3, 3, 3, '3.25'),
(46, 7, 13, 4, 3, 3, 4, '3.50'),
(47, 7, 14, 5, 4, 5, 5, '4.75'),
(48, 7, 15, 4, 5, 4, 3, '4.00'),
(49, 7, 16, 4, 4, 5, 3, '4.00'),
(50, 7, 17, 5, 4, 4, 4, '4.25'),
(51, 7, 18, 3, 3, 4, 5, '3.75'),
(52, 7, 19, 5, 5, 4, 5, '4.75'),
(53, 7, 20, 4, 3, 3, 4, '3.50'),
(54, 7, 21, 4, 5, 5, 4, '4.50'),
(55, 7, 22, 4, 5, 4, 5, '4.50'),
(56, 7, 23, 4, 5, 4, 4, '4.25'),
(57, 7, 25, 4, 5, 3, 3, '3.75'),
(58, 7, 26, 2, 3, 4, 5, '3.50'),
(59, 7, 27, 3, 3, 5, 5, '4.00'),
(60, 7, 28, 3, 4, 5, 5, '4.25'),
(61, 7, 29, 4, 3, 4, 3, '3.50'),
(62, 7, 30, 2, 3, 3, 3, '2.75'),
(63, 8, 3, 3, 4, 4, 3, '3.50'),
(64, 8, 4, 5, 4, 4, 3, '4.00'),
(65, 8, 5, 5, 5, 4, 4, '4.50'),
(66, 8, 6, 5, 4, 4, 3, '4.00'),
(67, 8, 7, 5, 5, 5, 5, '5.00'),
(68, 8, 8, 2, 3, 4, 3, '3.00'),
(69, 8, 9, 2, 4, 5, 3, '3.50'),
(70, 8, 10, 4, 5, 4, 3, '4.00'),
(71, 8, 11, 4, 5, 3, 4, '4.00'),
(72, 8, 12, 4, 3, 4, 3, '3.50'),
(73, 8, 13, 3, 4, 5, 4, '4.00'),
(74, 8, 14, 3, 4, 5, 5, '4.25'),
(75, 8, 15, 4, 4, 5, 4, '4.25'),
(76, 8, 16, 4, 5, 3, 4, '4.00'),
(77, 8, 17, 2, 3, 5, 5, '3.75'),
(78, 8, 17, 4, 3, 3, 4, '3.50'),
(79, 8, 18, 4, 5, 3, 3, '3.75'),
(80, 8, 19, 4, 5, 4, 5, '4.50'),
(81, 8, 20, 2, 4, 5, 5, '4.00'),
(82, 8, 21, 4, 5, 4, 4, '4.25'),
(83, 8, 22, 3, 4, 4, 4, '3.75'),
(84, 8, 23, 5, 5, 3, 3, '4.00'),
(85, 8, 24, 3, 3, 3, 3, '3.00'),
(86, 8, 25, 3, 3, 3, 3, '3.00'),
(87, 8, 26, 4, 4, 4, 4, '4.00'),
(88, 8, 27, 5, 4, 4, 4, '4.25'),
(89, 8, 28, 4, 3, 3, 4, '3.50'),
(90, 8, 29, 3, 3, 3, 3, '3.00'),
(91, 8, 30, 3, 3, 3, 3, '3.00'),
(92, 9, 3, 3, 5, 4, 4, '4.00'),
(93, 9, 4, 4, 3, 3, 3, '3.25'),
(94, 9, 5, 3, 3, 3, 3, '3.00'),
(95, 9, 6, 5, 4, 4, 4, '4.25'),
(96, 9, 7, 5, 4, 4, 3, '4.00'),
(97, 9, 8, 5, 4, 4, 3, '4.00'),
(98, 9, 9, 4, 4, 4, 4, '4.00'),
(99, 9, 10, 3, 3, 3, 3, '3.00'),
(100, 9, 11, 4, 5, 3, 3, '3.75'),
(101, 9, 12, 4, 4, 4, 4, '4.00'),
(102, 9, 13, 4, 5, 4, 4, '4.25'),
(103, 9, 14, 5, 5, 4, 3, '4.25'),
(104, 9, 15, 4, 3, 3, 3, '3.25'),
(105, 9, 16, 4, 3, 3, 3, '3.25'),
(106, 9, 17, 4, 4, 4, 4, '4.00'),
(107, 9, 18, 4, 3, 3, 3, '3.25'),
(108, 9, 19, 4, 3, 3, 3, '3.25'),
(109, 9, 20, 4, 3, 3, 3, '3.25'),
(110, 9, 21, 4, 5, 4, 3, '4.00'),
(111, 9, 22, 4, 3, 3, 3, '3.25'),
(112, 9, 23, 5, 3, 2, 2, '3.00'),
(113, 9, 24, 4, 4, 4, 4, '4.00'),
(114, 9, 25, 4, 4, 3, 3, '3.50'),
(115, 9, 26, 4, 4, 4, 4, '4.00'),
(116, 9, 27, 5, 5, 3, 4, '4.25'),
(117, 9, 28, 3, 3, 3, 3, '3.00'),
(118, 9, 29, 4, 5, 4, 4, '4.25'),
(119, 9, 30, 4, 3, 3, 4, '3.50'),
(120, 2, 14, 2, 3, 5, 2, '3.00'),
(121, 2, 1, 5, 5, 5, 5, '5.00'),
(122, 1, 2, 5, 5, 2, 5, '4.25'),
(123, 1, 2, 5, 5, 5, 5, '5.00'),
(124, 1, 1, 4, 5, 2, 1, '3.00');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`) VALUES
(1, 'haider', 'h@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$dmPihyVwLAiu7qLqHlo2Xu$9W36C5OOEcZ6oBPPoylJoRUZiDhvgvW'),
(2, 'hello', 'hello@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$vSPfNwiJGbNCMy/a.64fRu$b/R/5vwSG1rIQYtjqSEx8/CNhnXrQwe'),
(3, 'suma', 'suma@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$D/FPMeFuQ6gHOB8rxlxrSu$HeBqbxa65lW42PE8mllwzrQaQBrlcSm'),
(4, 'nidhi', 'n@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$Ff.BrwUQGPWo4SHmIYRg0e$gdas/GMRvBCrurA3DmbYnbL0w0bp.vO'),
(5, 'milu', 'milu@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$1seY9sNxXMU4V0SzwV1Ewe$ynlO2Py/EDKQn1NHQGqwWmbedUOisB6'),
(6, 'sumy', 'aaresha.suma@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$wCC0mZed0Vk.AjBz28UWUe$b3hhxaZfi9p2WweAJU0xOxQngkmXNo.'),
(7, 'babu', 'a@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$z6cSFLFKihMZw7R9lSG7fe$MkzgGR/8gJZwqiSSuVZb1GtNRcizLnW'),
(8, 'sajib', 'ar@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$7pb6NOaj3CtzrCaLiFmRee$GcnuIrnWLhyQ7EBl/RyxzCl7zUlr1kO'),
(9, 'aaresh', 'are@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$4idCOJmU7h.ZDl5jCDLwE.$43RZ7Sb3YLqt2fhDj3iWENOCp/vuM4i'),
(10, 'aaresha', 'ares@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$XjT71Bo/Phyty5ExmdFEee$kM/HQxraYeSNfiESPlJKoWjI0fOn7wK'),
(11, 'maya', 'm@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$oiBVikBRtGBeVozb0NlQfe$awp.Dx/nXbxLJHvuMUkKVXlVa8qPQT2'),
(12, 'kaya', 'k@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$SOOSBJg97/q.zruP09Nc.u$q3HjYX7k9ji17JhTKbZSZATuScnN6qi'),
(13, 'chaya', 'ka@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$beTAA/gBu3htVBc968AuwO$sWfFO4a6soR9ZAeQXPrRaJORRKf9DYW'),
(14, 'keya', 'kay@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$X5cIDsyJ0766VpBHuefEM.$lGUcm7oSfGUAZe9ytIYquX1Dc4bfUee'),
(15, 'titu', 'may@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$UsgR66LkAxxlMZzYVL64lu$Oimwe8mmLaK.BhJRB9MvGzk3cI.FaJm'),
(16, 'toufiq', 'my@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$5jvWLbTfPnfB1Loo1QEHYu$81xc8VwyXC6VZxMOiydHDge9pvdzqLq'),
(17, 'anabil', 'my1@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$FcQRjRsGtlKYUzUZkFZNWO$Jdgp6Xk79l1nsb/tZRldkVR3P5vf9dC'),
(18, 'mayetri', 'my12@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$xP8qUuLbkZOH.oaxMI3ame$xoY1kAYr2hceMSLZh5SDDvwZjlWtfbq'),
(19, 'prito', 'p@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$sZ9shBAfwrdK7cbuxJ.v0.$75DF/HCPSWyZRU1TXU7JCCnTELbKMle'),
(20, 'fahim', 'p1@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$tlFqERvCcyXwlubVdcByKu$90g8Dlr4T7JcCLbD5UTnGw8rEzyNd0C'),
(21, 'rohan', 'p12@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$6swPmNociAbSiTVckzuz7u$RSqmepFXgM93tF6eLMlCmzkS2ikddNq'),
(22, 'farhan', 'p112@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$JzOWxi3zUILz7wFLhzfGKu$bC5s8M0kSUg4oJP/OEOFuPGuio9l7.a'),
(23, 'sourov', 'r112@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$YmCVhRm9QCWKRh1y33QUI.$IItGq0rVBiEROpvd55V31s/2mdeaDMW'),
(24, 'bappy', 'r12@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$jXvg92oWFLiT3dVsJAn/Oe$0jOy6c9m.bFvZ/7YCKtCzbfPiwMzp6S'),
(25, 'dipto', 'r@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$LtnagWQczbrE/I./kzD7Fu$kAwXvaJSqrlEeLRhOLgwuNSba7sphb.'),
(26, 'khokon', 're@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$RIGpsUjKNWHF0askUNst2O$IJhdsWY/mB0Jp6YKQKnT8pN9ZSeERF.'),
(27, 'mahatir', 'res@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$7xfMbiY5yjr0CZnq7M.WT.$OY02Bwi0AoY3iOgL.eqHuPLjtxb7n8.'),
(28, 'haider31', 'ha@gmail.com', '$bcrypt-sha256$v=2,t=2b,r=12$S6AoOxkbLoOTTikYODNYK.$2OAcbqeMuiY90x9jMgqWXgEeP.GvX/i');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `movie_ratings`
--
ALTER TABLE `movie_ratings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `movie_id` (`movie_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `movies`
--
ALTER TABLE `movies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `movie_ratings`
--
ALTER TABLE `movie_ratings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=125;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `movie_ratings`
--
ALTER TABLE `movie_ratings`
  ADD CONSTRAINT `movie_ratings_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `movie_ratings_ibfk_2` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
