CREATE TABLE User_(
   id_user INT,
   name VARCHAR(50) NOT NULL,
   firstname VARCHAR(50) NOT NULL,
   email VARCHAR(50) NOT NULL,
   date_create DATE NOT NULL,
   is_active LOGICAL NOT NULL default= True,
   role VARCHAR(50) NOT NULL enum("apprenant", "formateur", "staff", "admin"),
   PRIMARY KEY(id_user),
   UNIQUE(email)
);

CREATE TABLE Learner(
   id_learner VARCHAR(50),
   birth_date DATE NOT NULL contrainte Pydantic >= 16,
   study_level VARCHAR(50) Optional[str],
   phone VARCHAR(50) Optional[str], validation regex,
   platform_registration_date DATE default: func.now(),
   id_user INT NOT NULL,
   PRIMARY KEY(id_learner),
   FOREIGN KEY(id_user) REFERENCES User_(id_user)
);

CREATE TABLE Trainer(
   Id_Trainer COUNTER,
   speciality VARCHAR(50) NOT NULL,
   date_hire DATE <today,
   hourly_rate DECIMAL(15,2) value >=0,
   bio VARCHAR(100),
   id_user INT NOT NULL,
   PRIMARY KEY(Id_Trainer),
   FOREIGN KEY(id_user) REFERENCES User_(id_user)
);

CREATE TABLE TeachingStaff(
   Id_TeachingStaff COUNTER,
   work VARCHAR(50) enum(),
   date_appointement DATE,
   responsabilities VARCHAR(50) dict(),
   id_user INT NOT NULL,
   PRIMARY KEY(Id_TeachingStaff),
   FOREIGN KEY(id_user) REFERENCES User_(id_user)
);

CREATE TABLE Admin(
   Id_Admin COUNTER,
   access_level VARCHAR(50) enum(),
   promotion_date DATE,
   id_user INT NOT NULL,
   PRIMARY KEY(Id_Admin),
   FOREIGN KEY(id_user) REFERENCES User_(id_user)
);

CREATE TABLE Room(
   id_room COUNTER,
   name VARCHAR(50) NOT NULL,
   capacity INT NOT NULL value >= 1,
   stuff VARCHAR(50) NOT NULL dict() or JSON,
   is_active LOGICAL default= True,
   localization VARCHAR(50) NOT NULL,
   PRIMARY KEY(id_room),
   UNIQUE(name)
);

CREATE TABLE Session(
   id_session COUNTER,
   title VARCHAR(100),
   description VARCHAR(50),
   start_date DATE NOT NULL,
   end_date DATE NOT NULL value > start_date,
   max_capacity INT value <= Salle.capacity,
   status VARCHAR(50) enum(OPEN, CLOSED, ARCHIVED),
   requirements VARCHAR(50) dict(),
   Id_Trainer INT NOT NULL,
   id_room INT NOT NULL,
   PRIMARY KEY(id_session),
   FOREIGN KEY(Id_Trainer) REFERENCES Trainer(Id_Trainer),
   FOREIGN KEY(id_room) REFERENCES Room(id_room)
);

CREATE TABLE Inscription(
   id_inscription COUNTER,
   inscription_date DATE default= funct.now(),
   inscription_status VARCHAR(50) enum(ENREGISTRE, DESINSCRIT, EN_ATTENTE),
   visit LOGICAL NOT NULL,
   id_session INT NOT NULL,
   id_learner VARCHAR(50) NOT NULL,
   PRIMARY KEY(id_inscription),
   FOREIGN KEY(id_session) REFERENCES Session(id_session),
   FOREIGN KEY(id_learner) REFERENCES Learner(id_learner)
);