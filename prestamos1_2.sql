-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-11-2024 a las 18:57:24
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

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
  `ingresos_mensuales` float UNSIGNED NOT NULL,
  `curp` varchar(18) NOT NULL,
  `tel_cel` varchar(10) NOT NULL,
  `tel_casa` varchar(10) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(255) NOT NULL,
  `rol` varchar(7) NOT NULL DEFAULT 'cliente',
  `is_approved` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_usuario`, `nombre`, `ape_pat`, `ape_mat`, `id_genero`, `fecha_nacimiento`, `id_nivelEdu`, `id_ocupacion`, `ingresos_mensuales`, `curp`, `tel_cel`, `tel_casa`, `email`, `password`, `rol`, `is_approved`) VALUES
(1, 'Angel', 'Perez', 'Rodriguez', 1, '2003-07-17', 3, 1, 2000, 'PERA030717HTLRDNA4', '255', '0', 'ared230000@gmail.com', 'pbkdf2:sha256:600000$AyQuHTTQHSbzYSMd$e2fb291a4889891ba1344e8a99513c53e523f2d06af522614f63767cc06b68cc', 'admin', 1),
(2, 'Adriana', 'Medina', 'Montiel', 2, '2004-05-02', 3, 2, 5000, 'MEMD030723MTLRDPR4', '2551342422', '', 'adri@gmail.com', 'pbkdf2:sha256:600000$471yPAnI0TjdFiU7$475e17fa87a1b105b7b4b615b3cee9945c9c87c9d7b9613d05de14fe78185c98', 'cliente', 1),
(8, 'Angelica', 'Hernández', 'Lopez', 2, '1975-12-12', 4, 2, 7000, 'PERA030717HTLR1234', '2551342422', '', 'angy@gmail.com', 'pbkdf2:sha256:600000$kWTPIM13$b9f5fa426958410b4b1f2cc83c6701ccb64145c68db4d18c89a2576e182512ac', 'cliente', 2),
(11, 'Brayan', 'Perez', 'Montiel', 1, '2001-11-11', 2, 2, 7000, 'PERA030717HTLRDN22', '2551342422', '', 'prueba2@gmail.com', 'pbkdf2:sha256:600000$cVlGjsId$906bd9406dd2b611bc5ba1b9f3d97fe3a3e5410c92d29274fc16168eafed9918', 'cliente', 0),
(13, 'Diana', 'Hernández', 'Rodriguez', 2, '2001-12-12', 1, 1, 2500, 'PERA030717HTLRDNA7', '2471014132', '2713455540', 'prueba3@gmail.com', 'pbkdf2:sha256:600000$rYvmGAgK$0f2b6f0b6629ba885c567407d3ec5b0fe3c14d24febb921411fbb0916872a016', 'cliente', 0),
(14, 'Angelica', 'Perez', 'Rodriguez', 1, '2005-04-18', 3, 3, 2000, 'PERA030717HTLRDNA7', '2551342422', '', 'prueba4@gmail.com', 'pbkdf2:sha256:600000$Enmh8Q17$4b8f46865a838c0593a6449ff1c4c94ae6ea177cceb000cfe90c9fe1e64e4575', 'cliente', 1);

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
(1, 29, 'Huamantla', 90506, 30, 'Ignacio Zaragoza', 'Andador Los Reyes', 60, NULL, 1),
(2, 29, 'Tetla ', 90501, 29, 'La Colina', 'Las Flores', 12, 4, 2),
(3, 1, 'Huamantla', 2000, 1, 'La Colina', 'Río Coatzacoatcos ', 1, NULL, 2),
(4, 1, 'Huamantla', 30000, 1, 'Ignacio Zaragoza', 'Las Flores', 60, NULL, 2),
(5, 29, 'Huamantla', 90506, 5, 'Nuevos Horizontes', 'Las Flores', 60, NULL, 8),
(6, 29, 'Ixtenco', 90501, 26, 'Ignacio Zaragoza', 'Río Coatzacoatcos ', NULL, 23, 11),
(7, 1, 'Huamantla', 12345, 27, 'La Colina', 'Las Flores', NULL, NULL, 2),
(8, 2, 'Ixtenco', 90506, 14, 'La Colina', 'Las Flores', 2, NULL, 2),
(9, 4, 'Ixtenco', 90506, 12, 'La Colina', 'Las Flores', 12, NULL, 2),
(10, 4, 'Ixtenco', 90506, 12, 'La Colina', 'Las Flores', 12, NULL, 2);

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
(2, 'Empleado del sector público'),
(3, 'Desempleado');

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
(1, 2, 1000, 2, 1, '2023-09-05 04:54:32'),
(2, 2, 1000, 2, 1, '2023-09-05 04:56:03'),
(3, 2, 1000, 2, 2, '2023-09-05 04:56:24'),
(4, 8, 5000, 6, 1, '2024-11-15 12:14:38');

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

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vistaclientes`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vistaclientes` (
`id_usuario` int(10)
,`nombre` varchar(25)
,`ape_pat` varchar(25)
,`ape_mat` varchar(25)
,`genero` varchar(10)
,`fecha_nacimiento` date
,`nivelEdu` varchar(30)
,`ocupacion` varchar(30)
,`ingresos_mensuales` float unsigned
,`curp` varchar(18)
,`tel_cel` varchar(10)
,`tel_casa` varchar(10)
,`email` varchar(254)
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vistausuarios`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vistausuarios` (
`id_usuario` int(10)
,`nombre` varchar(25)
,`ape_pat` varchar(25)
,`ape_mat` varchar(25)
,`genero` varchar(10)
,`fecha_nacimiento` date
,`nivelEdu` varchar(30)
,`ocupacion` varchar(30)
,`ingresos_mensuales` float unsigned
,`curp` varchar(18)
,`tel_cel` varchar(10)
,`tel_casa` varchar(10)
,`email` varchar(254)
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_domicilioxcliente`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_domicilioxcliente` (
`id_domicilio` int(10)
,`estado` varchar(35)
,`municipio` varchar(50)
,`codigo_postal` mediumint(5)
,`tipoAsen` varchar(25)
,`nombre_asentamiento` varchar(60)
,`calle` varchar(50)
,`num_ext` smallint(5) unsigned
,`num_int` smallint(5) unsigned
,`id_cliente` int(11)
,`domicilio_de` varchar(25)
);

-- --------------------------------------------------------

--
-- Estructura para la vista `vistaclientes`
--
DROP TABLE IF EXISTS `vistaclientes`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vistaclientes`  AS SELECT `clientes`.`id_usuario` AS `id_usuario`, `clientes`.`nombre` AS `nombre`, `clientes`.`ape_pat` AS `ape_pat`, `clientes`.`ape_mat` AS `ape_mat`, `genero`.`genero` AS `genero`, `clientes`.`fecha_nacimiento` AS `fecha_nacimiento`, `nivel_educativo`.`nivelEdu` AS `nivelEdu`, `ocupacion`.`ocupacion` AS `ocupacion`, `clientes`.`ingresos_mensuales` AS `ingresos_mensuales`, `clientes`.`curp` AS `curp`, `clientes`.`tel_cel` AS `tel_cel`, `clientes`.`tel_casa` AS `tel_casa`, `clientes`.`email` AS `email` FROM (((`clientes` join `genero` on(`clientes`.`id_genero` = `genero`.`id_genero`)) join `nivel_educativo` on(`clientes`.`id_nivelEdu` = `nivel_educativo`.`id_nivelEdu`)) join `ocupacion` on(`clientes`.`id_ocupacion` = `ocupacion`.`id_ocupacion`)) WHERE `clientes`.`rol` = 'cliente' AND `clientes`.`is_approved` = 1 ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vistausuarios`
--
DROP TABLE IF EXISTS `vistausuarios`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vistausuarios`  AS SELECT `clientes`.`id_usuario` AS `id_usuario`, `clientes`.`nombre` AS `nombre`, `clientes`.`ape_pat` AS `ape_pat`, `clientes`.`ape_mat` AS `ape_mat`, `genero`.`genero` AS `genero`, `clientes`.`fecha_nacimiento` AS `fecha_nacimiento`, `nivel_educativo`.`nivelEdu` AS `nivelEdu`, `ocupacion`.`ocupacion` AS `ocupacion`, `clientes`.`ingresos_mensuales` AS `ingresos_mensuales`, `clientes`.`curp` AS `curp`, `clientes`.`tel_cel` AS `tel_cel`, `clientes`.`tel_casa` AS `tel_casa`, `clientes`.`email` AS `email` FROM (((`clientes` join `genero` on(`clientes`.`id_genero` = `genero`.`id_genero`)) join `nivel_educativo` on(`clientes`.`id_nivelEdu` = `nivel_educativo`.`id_nivelEdu`)) join `ocupacion` on(`clientes`.`id_ocupacion` = `ocupacion`.`id_ocupacion`)) WHERE `clientes`.`rol` = 'cliente' AND `clientes`.`is_approved` = 0 ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_domicilioxcliente`
--
DROP TABLE IF EXISTS `vista_domicilioxcliente`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_domicilioxcliente`  AS SELECT `domicilio`.`id_domicilio` AS `id_domicilio`, `estados`.`estado` AS `estado`, `domicilio`.`municipio` AS `municipio`, `domicilio`.`cp` AS `codigo_postal`, `tipos_asen`.`tipoAsen` AS `tipoAsen`, `domicilio`.`asentamiento` AS `nombre_asentamiento`, `domicilio`.`calle` AS `calle`, `domicilio`.`num_ext` AS `num_ext`, `domicilio`.`num_int` AS `num_int`, `domicilio`.`id_cliente` AS `id_cliente`, `clientes`.`nombre` AS `domicilio_de` FROM (((`domicilio` join `estados` on(`domicilio`.`id_estado` = `estados`.`id_estado`)) join `tipos_asen` on(`domicilio`.`tipo_asen` = `tipos_asen`.`id_tipo_asen`)) join `clientes` on(`domicilio`.`id_cliente` = `clientes`.`id_usuario`)) ;

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
  MODIFY `id_usuario` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `domicilio`
--
ALTER TABLE `domicilio`
  MODIFY `id_domicilio` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

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
  MODIFY `id_ocupacion` tinyint(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  MODIFY `id_prestamo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

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
