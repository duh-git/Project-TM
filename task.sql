-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Мар 21 2024 г., 19:01
-- Версия сервера: 8.0.30
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `Project TM`
--

-- --------------------------------------------------------

--
-- Структура таблицы `task`
--

CREATE TABLE `task` (
  `id` int NOT NULL,
  `name` text NOT NULL,
  `worker` text NOT NULL,
  `speciality` text NOT NULL,
  `deadline` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `task`
--

INSERT INTO `task` (`id`, `name`, `worker`, `speciality`, `deadline`) VALUES
(1, 'A', 'Dima', 'Backend', '2024-11-10'),
(2, 'B', 'Vladimir', 'Frontend', '2024-12-20'),
(3, 'C', 'Petr', 'Frontend', '2024-03-30'),
(4, 'D', 'Vladislav', 'Backend', '2024-06-17'),
(5, 'E', 'Egor', 'Frontend', '2024-05-31'),
(6, 'F', 'Alexandr', 'Frontend', '2024-06-22'),
(7, 'I', 'Rinat', 'Team Leader', '2024-11-10'),
(8, 'G', 'Andrew', 'Designer', '2024-12-20'),
(9, 'K', 'Nikolay', 'Designer', '2024-03-30'),
(10, 'L', 'Igor', 'Designer', '2024-06-17');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `task`
--
ALTER TABLE `task`
  ADD KEY `TID` (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `task`
--
ALTER TABLE `task`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
