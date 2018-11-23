-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 2018-11-23 00:59:50
-- 服务器版本： 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `databases`
--

-- --------------------------------------------------------

--
-- 表的结构 `员工`
--

CREATE TABLE `员工` (
  `员工号` int(11) NOT NULL,
  `员工表员工号` int(11) NOT NULL,
  `姓名` char(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `性别` char(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `联系方式` char(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- 转存表中的数据 `员工`
--

INSERT INTO `员工` (`员工号`, `员工表员工号`, `姓名`, `性别`, `联系方式`) VALUES
(2, 12346, '王华', '男', '1230002'),
(3, 12347, '张悦', '女', '1230003');

-- --------------------------------------------------------

--
-- 表的结构 `客户`
--

CREATE TABLE `客户` (
  `客户号` int(11) NOT NULL,
  `客户表客户号` int(11) NOT NULL,
  `客户名` char(4) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `地址` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `联系方式` char(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- 转存表中的数据 `客户`
--

INSERT INTO `客户` (`客户号`, `客户表客户号`, `客户名`, `地址`, `联系方式`) VALUES
(1, 1, '张三', '市南区', '1000001'),
(2, 2, '李四', '东城区', '1000002'),
(3, 3, '王五', '黄岛区', '1000007'),
(4, 4, '赵兰', '崂山区', '1000004'),
(5, 5, '李青', '黄岛区', '1000009'),
(6, 6, '张倩', '市南区', '1000003');

-- --------------------------------------------------------

--
-- 表的结构 `收费登记`
--

CREATE TABLE `收费登记` (
  `客户号` int(11) NOT NULL,
  `客户表客户号` int(11) NOT NULL,
  `月份` date NOT NULL,
  `员工号` int(11) DEFAULT NULL,
  `应收费用` float(8,2) DEFAULT NULL,
  `实收费用` float(8,2) DEFAULT NULL,
  `结余费用` float(8,2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- 转存表中的数据 `收费登记`
--

INSERT INTO `收费登记` (`客户号`, `客户表客户号`, `月份`, `员工号`, `应收费用`, `实收费用`, `结余费用`) VALUES
(1, 1, '2018-09-06', 12345, 330.00, 330.00, 0.00),
(2, 1, '2018-10-11', 12346, 100.00, 50.00, 50.00),
(3, 2, '2018-11-08', 12347, 125.00, 100.00, 25.00),
(4, 3, '2018-09-12', 12345, 187.50, 187.50, 0.00),
(5, 4, '2018-10-09', 12346, 400.00, 200.00, 200.00),
(6, 5, '2018-10-04', 12347, 102.00, 102.00, 0.00),
(7, 6, '2018-10-23', 12347, 100.00, 50.00, 50.00);

-- --------------------------------------------------------

--
-- 表的结构 `用电信息`
--

CREATE TABLE `用电信息` (
  `客户号` int(11) NOT NULL,
  `客户表客户号` int(11) NOT NULL,
  `类别号` char(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `月份` date NOT NULL,
  `客户_客户号` int(11) DEFAULT NULL,
  `用电度数` char(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- 转存表中的数据 `用电信息`
--

INSERT INTO `用电信息` (`客户号`, `客户表客户号`, `类别号`, `月份`, `客户_客户号`, `用电度数`) VALUES
(1, 1, 'ABC', '2018-10-01', 1, '100'),
(2, 1, 'ABE', '2018-09-01', 1, '220'),
(3, 2, 'ABC', '2018-11-01', 2, '110'),
(4, 3, 'ABE', '2018-09-01', 3, '125'),
(5, 3, 'ABE', '2018-11-01', 3, '105'),
(6, 4, 'ABC', '2018-10-08', 4, '200'),
(7, 5, 'ABC', '2018-10-09', 5, '102'),
(8, 6, 'ABC', '2018-09-11', 6, '100');

-- --------------------------------------------------------

--
-- 表的结构 `用电类型`
--

CREATE TABLE `用电类型` (
  `类别号` int(11) NOT NULL,
  `客户表客户号` char(11) COLLATE utf8mb4_unicode_ci NOT NULL,
  `客户号` int(11) DEFAULT NULL,
  `类别名` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `电价` float(8,2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- 转存表中的数据 `用电类型`
--

INSERT INTO `用电类型` (`类别号`, `客户表客户号`, `客户号`, `类别名`, `电价`) VALUES
(1, 'ABC', NULL, '家庭', 1.00),
(2, 'ABD', NULL, '政府', 2.00),
(3, 'ABE', NULL, '工厂', 1.50),
(4, 'ABF', NULL, '学校', 2.50),
(5, 'ABG', NULL, '医院', 0.50);

-- --------------------------------------------------------

--
-- 表的结构 `费用管理`
--

CREATE TABLE `费用管理` (
  `客户号` int(11) NOT NULL,
  `客户表客户号` int(11) NOT NULL,
  `月份` date NOT NULL,
  `员工号` int(11) DEFAULT NULL,
  `费用` float(8,2) DEFAULT NULL,
  `收费标志` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT '未收费'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- 转存表中的数据 `费用管理`
--

INSERT INTO `费用管理` (`客户号`, `客户表客户号`, `月份`, `员工号`, `费用`, `收费标志`) VALUES
(1, 1, '2018-09-06', 12345, 330.00, '以收费'),
(2, 1, '2018-10-01', NULL, 100.00, '未收费'),
(3, 2, '2018-11-08', 12346, 100.00, '以收费'),
(4, 3, '2018-09-12', 12345, 125.00, '未交齐'),
(5, 4, '2018-10-09', 12346, 400.00, '未交齐'),
(6, 5, '2018-10-04', 12347, 102.00, '以收费'),
(7, 6, '2018-10-23', 12347, 100.00, '未交齐');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `员工`
--
ALTER TABLE `员工`
  ADD PRIMARY KEY (`员工号`);

--
-- Indexes for table `客户`
--
ALTER TABLE `客户`
  ADD PRIMARY KEY (`客户号`);

--
-- Indexes for table `收费登记`
--
ALTER TABLE `收费登记`
  ADD PRIMARY KEY (`客户号`,`月份`),
  ADD KEY `FK_登记` (`员工号`);

--
-- Indexes for table `用电信息`
--
ALTER TABLE `用电信息`
  ADD PRIMARY KEY (`客户号`,`类别号`,`月份`),
  ADD KEY `FK_使用` (`客户_客户号`),
  ADD KEY `类别号` (`类别号`);

--
-- Indexes for table `用电类型`
--
ALTER TABLE `用电类型`
  ADD PRIMARY KEY (`类别号`),
  ADD KEY `FK_使用` (`客户号`);

--
-- Indexes for table `费用管理`
--
ALTER TABLE `费用管理`
  ADD PRIMARY KEY (`客户号`,`月份`),
  ADD KEY `FK_管理` (`员工号`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `员工`
--
ALTER TABLE `员工`
  MODIFY `员工号` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- 使用表AUTO_INCREMENT `客户`
--
ALTER TABLE `客户`
  MODIFY `客户号` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- 使用表AUTO_INCREMENT `收费登记`
--
ALTER TABLE `收费登记`
  MODIFY `客户号` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- 使用表AUTO_INCREMENT `用电信息`
--
ALTER TABLE `用电信息`
  MODIFY `客户号` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- 使用表AUTO_INCREMENT `用电类型`
--
ALTER TABLE `用电类型`
  MODIFY `类别号` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- 使用表AUTO_INCREMENT `费用管理`
--
ALTER TABLE `费用管理`
  MODIFY `客户号` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
