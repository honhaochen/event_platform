CREATE TABLE IF NOT EXISTS `event_db`.`auth_tab` (
	`id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(20) NOT NULL,
    `email` VARCHAR(20) NOT NULL UNIQUE,
	`password` VARCHAR(128) NOT NULL,
    `is_admin` TINYINT UNSIGNED NOT NULL DEFAULT 0,
	PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `event_db`.`event_tab` (
	`id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(20) NOT NULL,
    `description` VARCHAR(128) NOT NULL,
	`start_time` DATETIME NOT NULL,
	`end_time` DATETIME NOT NULL,
    `category` VARCHAR(20) NOT NULL,
    `location` VARCHAR(20) NOT NULL,
	PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE INDEX `idx_time` ON `event_db`.`event_tab` (`start_time`, `end_time`);
CREATE INDEX `idx_category_location_time` ON `event_db`.`event_tab` (`category`, `location`, `start_time`, `end_time`);
CREATE INDEX `idx_location_category_time` ON `event_db`.`event_tab` (`location`, `category`, `start_time`, `end_time`);

CREATE TABLE IF NOT EXISTS `event_db`.`event_comment_tab` (
	`id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `event_id` BIGINT UNSIGNED NOT NULL,
	`name` VARCHAR(20) NOT NULL,
    `comment` VARCHAR(128) NOT NULL,
	PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE INDEX `idx_event_id` ON `event_db`.`event_comment_tab` (`event_id`);

CREATE TABLE IF NOT EXISTS `event_db`.`event_participant_tab` (
	`id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `event_id` BIGINT UNSIGNED NOT NULL,
	`name` VARCHAR(20) NOT NULL,
	PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE INDEX `idx_event_id` ON `event_db`.`event_participant_tab` (`event_id`);

CREATE TABLE IF NOT EXISTS `event_db`.`event_likes_tab` (
	`id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `event_id` BIGINT UNSIGNED NOT NULL,
	`name` VARCHAR(20) NOT NULL,
	PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE INDEX `idx_event_id` ON `event_db`.`event_likes_tab` (`event_id`);

CREATE TABLE IF NOT EXISTS `event_db`.`event_images_tab` (
	`id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `event_id` BIGINT UNSIGNED NOT NULL,
	`image` VARCHAR(128) NOT NULL,
	PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE INDEX `idx_event_id` ON `event_db`.`event_images_tab` (`event_id`);
