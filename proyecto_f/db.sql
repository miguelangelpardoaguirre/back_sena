DROP DATABASE IF EXISTS mi_proyecto_f;
CREATE DATABASE mi_proyecto_f CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE mi_proyecto_f;

CREATE TABLE rol(
    id_rol SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre_rol VARCHAR(20)
);

CREATE TABLE estado_de_normas (
    cod_programa MEDIUMINT PRIMARY KEY AUTO_INCREMENT,
    cod_version VARCHAR(50) NOT NULL,
    fecha_elaboracion DATE NOT NULL,
    anio SMALLINT NOT NULL,
    red_conocimiento VARCHAR(150) NOT NULL,
    nombre_ncl VARCHAR(150) NOT NULL,
    cod_ncl INT NOT NULL,
    ncl_version SMALLINT NOT NULL,
    norma_corte_noviembre VARCHAR(100) NOT NULL,
    version INT NOT NULL,
    norma_version VARCHAR(100) NOT NULL,
    mesa_sectorial VARCHAR(150) NOT NULL,
    tipo_norma VARCHAR(80) NOT NULL,
    tipo_competencia VARCHAR(80) NOT NULL,
    observacion VARCHAR(255),
    fecha_revision DATE,
    vigencia VARCHAR(50),
    fecha_indice VARCHAR(50)
);


INSERT INTO rol (nombre_rol) VALUES 
('Administrador'),
('Editor'),
('Usuario');


