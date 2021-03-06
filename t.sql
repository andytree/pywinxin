CREATE TABLE IF NOT EXISTS `mydb`.`phone` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `phone_nmu` VARCHAR(45) NULL,
  `short_num` VARCHAR(45) NULL,
  `tel_num` VARCHAR(45) NULL,
  `user_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_phone_user1_idx` (`user_id` ASC),
  CONSTRAINT `fk_phone_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8



ALTER TABLE `phone` ADD CONSTRAINT `fk_phone_user1` FOREIGN KEY(`user_id`) REFERENCES `user`(`id`)


CREATE TABLE IF NOT EXISTS `mydb`.`user_pos` (
  `user_id` INT NOT NULL,
  `pos_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `pos_id`),
  INDEX `fk_user_pos_position1_idx` (`pos_id` ASC),
  CONSTRAINT `fk_user_pos_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_pos_position1`
    FOREIGN KEY (`pos_id`)
    REFERENCES `mydb`.`position` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8


INSERT INTO user ( id, user_name ,depart_id )
                       VALUES
                       ( 1,"唐字符",1 );