SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `articles` (
  `article_id` int(11) NOT NULL,
  `article_title` varchar(500) NOT NULL,
  `article_author_id` int(11) NOT NULL,
  `article_content` mediumtext NOT NULL,
  `article_published_date` datetime NOT NULL,
  `article_category_id` int(11) NOT NULL,
  `article_thumbnail_url` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `user_name` varchar(32) NOT NULL,
  `user_full_name` varchar(250) NOT NULL,
  `user_email` varchar(150) NOT NULL,
  `user_role` set('admin','author','editor') NOT NULL,
  `user_password_hash` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


ALTER TABLE `articles`
  ADD PRIMARY KEY (`article_id`),
  ADD KEY `author_id` (`article_author_id`),
  ADD KEY `article_category_id` (`article_category_id`);

ALTER TABLE `categories`
  ADD PRIMARY KEY (`category_id`);


ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `user_name` (`user_name`);


ALTER TABLE `articles`
  MODIFY `article_id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `categories`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `articles`
  ADD CONSTRAINT `articles_ibfk_1` FOREIGN KEY (`article_author_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `articles_ibfk_2` FOREIGN KEY (`article_category_id`) REFERENCES `categories` (`category_id`);
COMMIT;


