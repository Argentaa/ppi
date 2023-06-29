-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 29-Jun-2023 às 03:01
-- Versão do servidor: 8.0.32
-- versão do PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bd_progparcial`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `avaliacoes`
--

CREATE TABLE `avaliacoes` (
  `id` int NOT NULL,
  `requerimento_id` int NOT NULL,
  `criterio_id` int NOT NULL,
  `pontos_obtidos` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `categorias`
--

CREATE TABLE `categorias` (
  `id` int NOT NULL,
  `parte_id` int NOT NULL,
  `descricao` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `categorias`
--

INSERT INTO `categorias` (`id`, `parte_id`, `descricao`) VALUES
(18, 11, '1 - Número de Horas Aula'),
(19, 11, '2 - Desempenho didático avaliado pelo corpo docente'),
(20, 12, '14 - Cursos de nivel de graducao e pos graduacao');

-- --------------------------------------------------------

--
-- Estrutura da tabela `criterios`
--

CREATE TABLE `criterios` (
  `id` int NOT NULL,
  `categoria_id` int NOT NULL,
  `descricao` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pontos` int NOT NULL,
  `pontos_string` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `criterios`
--

INSERT INTO `criterios` (`id`, `categoria_id`, `descricao`, `pontos`, `pontos_string`) VALUES
(21, 18, 'Numero Semestres', 2, '02 pontos por Periodos de Aula'),
(22, 18, 'Numero Periodos de Aulas', 3, '03 pontos por atividade'),
(23, 19, 'Nnuerowmofw2', 3, '03 pontos por atividade');

-- --------------------------------------------------------

--
-- Estrutura da tabela `docente`
--

CREATE TABLE `docente` (
  `id` int NOT NULL,
  `CPF` varchar(255) NOT NULL,
  `SIAPE` varchar(255) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `CPPD` smallint NOT NULL,
  `foto` varchar(255) DEFAULT NULL,
  `escolaridade` varchar(255) DEFAULT NULL,
  `aperfeicoamento` varchar(255) DEFAULT NULL,
  `especializacao` varchar(255) DEFAULT NULL,
  `mestrado` smallint DEFAULT NULL,
  `doutorado` smallint DEFAULT NULL,
  `lotacao` varchar(255) DEFAULT NULL,
  `diretoria` varchar(255) DEFAULT NULL,
  `coordenacao` varchar(255) DEFAULT NULL,
  `cargo` varchar(255) DEFAULT NULL,
  `chefiaImediata` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `docente`
--

INSERT INTO `docente` (`id`, `CPF`, `SIAPE`, `nome`, `email`, `senha`, `CPPD`, `foto`, `escolaridade`, `aperfeicoamento`, `especializacao`, `mestrado`, `doutorado`, `lotacao`, `diretoria`, `coordenacao`, `cargo`, `chefiaImediata`) VALUES
(1, 'admin', 'admin', 'eduardo', 'admin', 'sha256$N0mQxQCz8NNBuwhr$ae63c083d11961a175235bbd2a1190df63dca2b3dcea92c7e9d868d9fc3c4e45', 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'argenta', 'argenta', 'Argenta', 'argenta', 'sha256$q82Mz8WS4PVDhIxD$be405551c81fbbbfa30b38aa3a74478bbec3dde370d926861830f7512056fb3b', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, '02333045094', '123456', 'Eduardo May Argenta', 'eduardoma890@gmail.com', 'sha256$5lgY7X2Ttv4OKjRW$360d148ae660b698a915ed13428500719a70d406b2fbc2f2c3330913b10d596a', 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `documentos`
--

CREATE TABLE `documentos` (
  `id` int NOT NULL,
  `avaliacao_id` int NOT NULL,
  `caminho` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `partes`
--

CREATE TABLE `partes` (
  `id` int NOT NULL,
  `descricao` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `partes`
--

INSERT INTO `partes` (`id`, `descricao`) VALUES
(11, 'Parte 1: Atividade Docente'),
(12, 'Parte 2: Horario Docente');

-- --------------------------------------------------------

--
-- Estrutura da tabela `requerimentos`
--

CREATE TABLE `requerimentos` (
  `id` int NOT NULL,
  `docente_id` int NOT NULL,
  `cppd_id` int DEFAULT NULL,
  `titulo` varchar(255) NOT NULL,
  `descricao` text,
  `status` enum('pendente','aprovado','reprovado') NOT NULL DEFAULT 'pendente',
  `data_criacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `nivelCapacitacao` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `avaliacoes`
--
ALTER TABLE `avaliacoes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `requerimento_id` (`requerimento_id`),
  ADD KEY `criterio_id` (`criterio_id`);

--
-- Índices para tabela `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id`),
  ADD KEY `parte_id` (`parte_id`);

--
-- Índices para tabela `criterios`
--
ALTER TABLE `criterios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `categoria_id` (`categoria_id`);

--
-- Índices para tabela `docente`
--
ALTER TABLE `docente`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `documentos`
--
ALTER TABLE `documentos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `avaliacao_id` (`avaliacao_id`);

--
-- Índices para tabela `partes`
--
ALTER TABLE `partes`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `requerimentos`
--
ALTER TABLE `requerimentos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`docente_id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `avaliacoes`
--
ALTER TABLE `avaliacoes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de tabela `criterios`
--
ALTER TABLE `criterios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de tabela `docente`
--
ALTER TABLE `docente`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `documentos`
--
ALTER TABLE `documentos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `partes`
--
ALTER TABLE `partes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de tabela `requerimentos`
--
ALTER TABLE `requerimentos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `avaliacoes`
--
ALTER TABLE `avaliacoes`
  ADD CONSTRAINT `avaliacoes_ibfk_1` FOREIGN KEY (`requerimento_id`) REFERENCES `requerimentos` (`id`),
  ADD CONSTRAINT `avaliacoes_ibfk_2` FOREIGN KEY (`criterio_id`) REFERENCES `criterios` (`id`);

--
-- Limitadores para a tabela `categorias`
--
ALTER TABLE `categorias`
  ADD CONSTRAINT `categorias_ibfk_1` FOREIGN KEY (`parte_id`) REFERENCES `partes` (`id`);

--
-- Limitadores para a tabela `criterios`
--
ALTER TABLE `criterios`
  ADD CONSTRAINT `criterios_ibfk_1` FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`id`);

--
-- Limitadores para a tabela `documentos`
--
ALTER TABLE `documentos`
  ADD CONSTRAINT `documentos_ibfk_1` FOREIGN KEY (`avaliacao_id`) REFERENCES `avaliacoes` (`id`);

--
-- Limitadores para a tabela `requerimentos`
--
ALTER TABLE `requerimentos`
  ADD CONSTRAINT `requerimentos_ibfk_1` FOREIGN KEY (`docente_id`) REFERENCES `docente` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
