# GZY-medical-AI

广州中医药大学 - 医学信息工程 - 我的代码生涯起点

> 🎯 目标：考研四川大学 → 头部医疗公司算法工程师
> 📅 起点：2026-09-11（大一上）
> 👤 GitHub：[@QJH20070830](https://github.com/QJH20070830)

## 仓库结构

| 目录 | 内容 |
|---|---|
| `01-C-Language/` | C 语言（大一上核心课，也是考研复试机试语言） |
| `02-DataStructures/` | 数据结构（408 中占 45 分，最重要的一门） |
| `03-Python/` | Python 与科学计算（医疗 AI 主力语言） |
| `04-MachineLearning/` | 机器学习（sklearn → 传统模型 → 医学数据建模） |
| `05-MedicalAI/` | 医学影像与深度学习（DICOM / SimpleITK / PyTorch） |
| `06-Kaoyan408/` | 考研 408 复习（数据结构 / 计组 / 操作系统 / 计网） |

## 开发环境

| 项目 | 版本 / 位置 |
|---|---|
| Python | 3.11.16（conda 环境 `medai`，位于 `D:\Dev\Miniconda3\envs\medai`） |
| 核心包 | numpy · pandas · scikit-learn · PyTorch(CPU) · pydicom · SimpleITK |
| C 编译器 | MinGW-w64 GCC 16.1.0 |
| 数据库 | MySQL 8.0.29（端口 3306，库 `medinfo`） |
| IDE | VS Code / PyCharm |

> ⚠️ 本机为 Intel Arc 核显，无 NVIDIA 显卡，PyTorch 是 CPU 版。
> 真正的模型训练走云端 GPU（AutoDL / Kaggle / 趋动云）。

## 每日习惯

写完代码就 `git add` → `git commit -m "..."` → `git push`，**每天至少 1 个绿点**。
这会成为考研复试前最值钱的成绩单。
