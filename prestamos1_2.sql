-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-08-2023 a las 13:31:07
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `prestamos1_2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_usuario` int(10) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `ape_pat` varchar(25) NOT NULL,
  `ape_mat` varchar(25) NOT NULL,
  `id_genero` tinyint(4) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `id_nivelEdu` tinyint(4) NOT NULL,
  `id_ocupacion` tinyint(4) NOT NULL,
  `ingresos_mensuales` float DEFAULT NULL,
  `curp` varchar(18) NOT NULL,
  `tel_cel` varchar(10) NOT NULL,
  `tel_casa` varchar(12) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_usuario`, `nombre`, `ape_pat`, `ape_mat`, `id_genero`, `fecha_nacimiento`, `id_nivelEdu`, `id_ocupacion`, `ingresos_mensuales`, `curp`, `tel_cel`, `tel_casa`, `email`, `password`) VALUES
(4, 'Angel', 'Perez', 'Rodriguez', 1, '2001-01-01', 1, 1, 2000, 'PERA030717HTLRDN03', '2471014138', '2453511112', 'ared2@gmail.com', 'pbkdf2:sha256:600000$D2WUy1AbjsJjmjio$3b2fe1e277797bd56cf55d6ca1f5f24309654fd7ed92f311fc8ff6804d25cac1'),
(5, 'omar', 'Rodriguez', 'Lopez', 1, '2012-12-12', 1, 1, 6000, 'PERA030717HTLRDNA4', '2471014136', '2453511112', 'omar@gmail.com', 'pbkdf2:sha256:600000$w1OzpYDOSC52HjW4$a1cf26383edeac15cc612fef7793a20f4e1b51e27058b66a54c5910f1aa38d6c'),
(6, 'omar', 'Perez', 'Lopez', 1, '2012-12-12', 1, 1, 6000, 'PERA030717HTLRDNA7', '2471014138', '2453511111', 'omar1@gmail.com', 'pbkdf2:sha256:600000$g2YGf0mWVtFjvJP1$306bd4107dd13f85a2b4674e8adcfa65b3a0ed4ae584262b55d9ad6ac2a32afa'),
(7, 'Alon', 'Perez', 'Rodriguez', 1, '2023-08-06', 4, 1, 200, 'PERA030717HTLRDNA4', '2471014131', '2453511112', 'ared88@gmail.com', 'pbkdf2:sha256:600000$l2lucyEzvogHlboL$90ce415830ea14b1438842e7dae998d0e1cbaceed7539416841d573276137c16'),
(8, 'omar', 'Perez', 'Bonilla', 1, '2023-08-04', 1, 1, 2000, 'PERA000718HTLRDNA3', '2471014136', '2453511112', 'omarr@gmail.com', 'pbkdf2:sha256:600000$KsJfD2sWUuO8cius$aa155e8b24b8a2abf8f7b112d3cd7b178d0daf9422dbf3017e51f35c79eeff1a'),
(9, 'Aldo', 'Hernández', 'Bonilla', 1, '2023-08-07', 1, 1, 2000, 'PERA000718HTLRDNA3', '2411342422', '2453511112', 'prueba@gmail.com', 'pbkdf2:sha256:600000$bL7Eqbme82jL5xFb$64331c0df24451aeb89fedb8572cd784de8bc21c5d1177661e4bf2bfaacaf488');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `domicilio`
--

CREATE TABLE `domicilio` (
  `id_domicilio` int(10) NOT NULL,
  `id_estado` tinyint(4) UNSIGNED NOT NULL,
  `municipio` varchar(50) NOT NULL,
  `cp` mediumint(5) NOT NULL,
  `tipo_asen` tinyint(4) NOT NULL,
  `asentamiento` varchar(60) NOT NULL,
  `calle` varchar(50) NOT NULL,
  `num_ext` smallint(5) UNSIGNED DEFAULT NULL,
  `num_int` smallint(5) UNSIGNED DEFAULT NULL,
  `id_cliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `domicilio`
--

INSERT INTO `domicilio` (`id_domicilio`, `id_estado`, `municipio`, `cp`, `tipo_asen`, `asentamiento`, `calle`, `num_ext`, `num_int`, `id_cliente`) VALUES
(1, 1, 'Huamantla', 22222, 14, 'La Colina', 'Andador Los Reyes', NULL, NULL, 9);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estados`
--

CREATE TABLE `estados` (
  `id_estado` tinyint(4) UNSIGNED NOT NULL,
  `estado` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `estados`
--

INSERT INTO `estados` (`id_estado`, `estado`) VALUES
(1, 'Aguascalientes'),
(2, 'Baja California'),
(3, 'Baja California Sur'),
(4, 'Campeche'),
(5, 'Coahuila'),
(6, 'Colima'),
(7, 'Chiapas'),
(8, 'Chihuahua'),
(9, 'Ciudad de México'),
(10, 'Durango'),
(11, 'Estado de México'),
(12, 'Guanajuato'),
(13, 'Guerrero'),
(14, 'Hidalgo'),
(15, 'Jalisco'),
(16, 'Michoacán'),
(17, 'Morelos'),
(18, 'Nayarit'),
(19, 'Nuevo León'),
(20, 'Oaxaca'),
(21, 'Puebla'),
(22, 'Querétaro'),
(23, 'Quintana Roo'),
(24, 'San Luis Potosí'),
(25, 'Sinaloa'),
(26, 'Sonora'),
(27, 'Tabasco'),
(28, 'Tamaulipas'),
(29, 'Tlaxcala'),
(30, 'Veracruz'),
(31, 'Yucatán'),
(32, 'Zacatecas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `id_genero` tinyint(4) NOT NULL,
  `genero` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `genero`
--

INSERT INTO `genero` (`id_genero`, `genero`) VALUES
(1, 'Masculino'),
(2, 'Femenino');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modalidades_pago`
--

CREATE TABLE `modalidades_pago` (
  `id_modalidad` tinyint(4) NOT NULL,
  `modalidad_pago` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `modalidades_pago`
--

INSERT INTO `modalidades_pago` (`id_modalidad`, `modalidad_pago`) VALUES
(1, 'Quincenal'),
(2, 'Mensual');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nivel_educativo`
--

CREATE TABLE `nivel_educativo` (
  `id_nivelEdu` tinyint(4) NOT NULL,
  `nivelEdu` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `nivel_educativo`
--

INSERT INTO `nivel_educativo` (`id_nivelEdu`, `nivelEdu`) VALUES
(1, 'Sin estudios'),
(2, 'Educación básica'),
(3, 'Preparatoria'),
(4, 'Licenciatura '),
(5, 'Ingeniería'),
(6, 'Maestría o Superior');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ocupacion`
--

CREATE TABLE `ocupacion` (
  `id_ocupacion` tinyint(4) NOT NULL,
  `ocupacion` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ocupacion`
--

INSERT INTO `ocupacion` (`id_ocupacion`, `ocupacion`) VALUES
(1, 'Empleado del sector privado'),
(2, 'Empleado del sector público');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamos`
--

CREATE TABLE `prestamos` (
  `id_prestamo` int(11) NOT NULL,
  `id_cliente` int(10) NOT NULL,
  `monto` float UNSIGNED NOT NULL,
  `periodo` tinyint(3) UNSIGNED NOT NULL,
  `modalidad_pago` tinyint(4) NOT NULL,
  `fecha_in` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `prestamos`
--

INSERT INTO `prestamos` (`id_prestamo`, `id_cliente`, `monto`, `periodo`, `modalidad_pago`, `fecha_in`) VALUES
(1, 9, 1200, 4, 2, '2023-08-15 12:31:14'),
(2, 9, 5000, 8, 1, '2023-08-15 23:54:44'),
(3, 9, 4000, 12, 1, '2023-08-16 01:26:35'),
(4, 9, 3550, 6, 1, '2023-08-16 02:06:03'),
(5, 8, 4200, 2, 2, '2023-08-16 04:13:18'),
(6, 8, 5000, 6, 1, '2023-08-16 04:17:21'),
(7, 8, 1200, 4, 1, '2023-08-16 04:20:28'),
(8, 8, 1800, 8, 1, '2023-08-16 04:28:16'),
(9, 8, 6000, 2, 1, '2023-08-16 04:31:20'),
(10, 8, 550, 4, 2, '2023-08-16 10:28:52'),
(11, 8, 550, 4, 2, '2023-08-16 10:33:07');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos_asen`
--

CREATE TABLE `tipos_asen` (
  `id_tipo_asen` tinyint(4) NOT NULL,
  `tipoAsen` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipos_asen`
--

INSERT INTO `tipos_asen` (`id_tipo_asen`, `tipoAsen`) VALUES
(1, 'Ampliación'),
(2, 'Barrio'),
(3, 'Ciudad'),
(4, 'Ciudad Industrial'),
(5, 'Colonia'),
(6, 'Condominio'),
(7, 'Conjunto Habitacional'),
(8, 'Corredor Industrial'),
(9, 'Ejido'),
(10, 'Exhacienda'),
(11, 'Fracción'),
(12, 'Fraccionamiento'),
(13, 'Granja'),
(14, 'Hacienda'),
(15, 'Manzana'),
(16, 'Paraje'),
(17, 'Privada'),
(18, 'Prolongación'),
(19, 'Pueblo'),
(20, 'Puerto'),
(21, 'Ranchería'),
(22, 'Rancho'),
(23, 'Región'),
(24, 'Residencial'),
(25, 'Rinconada'),
(26, 'Sección'),
(27, 'Sector'),
(28, 'Supermanzana'),
(29, 'Unidad'),
(30, 'Unidad Habitacional'),
(31, 'Villa'),
(32, 'Zona Federal'),
(33, 'Zona Industrial'),
(34, 'Zona Militar');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `fk_ocupacion` (`id_ocupacion`),
  ADD KEY `fk_nivelEducativo` (`id_nivelEdu`),
  ADD KEY `fk_genero` (`id_genero`);

--
-- Indices de la tabla `domicilio`
--
ALTER TABLE `domicilio`
  ADD PRIMARY KEY (`id_domicilio`),
  ADD KEY `cp` (`cp`),
  ADD KEY `municipios_idx` (`municipio`),
  ADD KEY `fk_domicilio_estados_idx` (`id_estado`),
  ADD KEY `fk_domicilio_clientes` (`id_cliente`),
  ADD KEY `fk_domicilio_tipoAsentamiento` (`tipo_asen`);

--
-- Indices de la tabla `estados`
--
ALTER TABLE `estados`
  ADD PRIMARY KEY (`id_estado`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id_genero`);

--
-- Indices de la tabla `modalidades_pago`
--
ALTER TABLE `modalidades_pago`
  ADD PRIMARY KEY (`id_modalidad`);

--
-- Indices de la tabla `nivel_educativo`
--
ALTER TABLE `nivel_educativo`
  ADD PRIMARY KEY (`id_nivelEdu`);

--
-- Indices de la tabla `ocupacion`
--
ALTER TABLE `ocupacion`
  ADD PRIMARY KEY (`id_ocupacion`);

--
-- Indices de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD PRIMARY KEY (`id_prestamo`),
  ADD KEY `fk_prestamo_cliente` (`id_cliente`),
  ADD KEY `fk_prestamo_modalidad` (`modalidad_pago`);

--
-- Indices de la tabla `tipos_asen`
--
ALTER TABLE `tipos_asen`
  ADD PRIMARY KEY (`id_tipo_asen`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_usuario` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `domicilio`
--
ALTER TABLE `domicilio`
  MODIFY `id_domicilio` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `id_genero` tinyint(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `modalidades_pago`
--
ALTER TABLE `modalidades_pago`
  MODIFY `id_modalidad` tinyint(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `nivel_educativo`
--
ALTER TABLE `nivel_educativo`
  MODIFY `id_nivelEdu` tinyint(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `ocupacion`
--
ALTER TABLE `ocupacion`
  MODIFY `id_ocupacion` tinyint(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  MODIFY `id_prestamo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `tipos_asen`
--
ALTER TABLE `tipos_asen`
  MODIFY `id_tipo_asen` tinyint(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `fk_genero` FOREIGN KEY (`id_genero`) REFERENCES `genero` (`id_genero`),
  ADD CONSTRAINT `fk_nivelEducativo` FOREIGN KEY (`id_nivelEdu`) REFERENCES `nivel_educativo` (`id_nivelEdu`),
  ADD CONSTRAINT `fk_ocupacion` FOREIGN KEY (`id_ocupacion`) REFERENCES `ocupacion` (`id_ocupacion`);

--
-- Filtros para la tabla `domicilio`
--
ALTER TABLE `domicilio`
  ADD CONSTRAINT `fk_domicilio_clientes` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_usuario`),
  ADD CONSTRAINT `fk_domicilio_estados` FOREIGN KEY (`id_estado`) REFERENCES `estados` (`id_estado`),
  ADD CONSTRAINT `fk_domicilio_tipoAsentamiento` FOREIGN KEY (`tipo_asen`) REFERENCES `tipos_asen` (`id_tipo_asen`);

--
-- Filtros para la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD CONSTRAINT `fk_prestamo_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_usuario`),
  ADD CONSTRAINT `fk_prestamo_modalidad` FOREIGN KEY (`modalidad_pago`) REFERENCES `modalidades_pago` (`id_modalidad`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
