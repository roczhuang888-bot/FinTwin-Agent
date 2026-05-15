# FinTwin-Agent: Global Financial Digital Twin & Multi-Agent Evolution System

## 1. 项目解决的核心痛点
在复杂的二级市场分析中，传统的 AI 方案往往因上下文受限或缺乏博弈逻辑，难以量化宏观事件对微观交易实体的非线性传导。本项目解决了以下痛点：
* **信息截断与幻觉：** 传统 RAG 无法处理百万字级别的财报全量数据。
* **缺乏对抗性推演：** 市场是博弈的结果，单一 Agent 无法模拟多空双方的激烈对抗。
* **长链逻辑断裂：** 宏观政策到个股 EPS 的传导逻辑极其复杂，需要深度的递归推理。

## 2. 核心架构与逻辑流
本项目基于 **LangGraph** 与 **Multi-Agent Orchestration** 架构：
* **大规模并行仿真：** 系统同时调度 500+ 个具备独立记忆与风险偏好的专用 Agent（代表机构、散户、算法交易员）。
* **多智能体演化博弈：** 采用红蓝对抗机制（Bull vs Bear），针对财报数据进行多轮交叉质询。
* **蒙特卡洛搜索（MCTS）推理：** 针对重大波动执行数千次演化推演，每条路径包含 10 步以上的长链递归推理。

## 3. Token 消耗说明
由于涉及大规模并发 Agent 协作及长上下文（200k+）的频繁调用，单次压力测试涉及上万次 API 递归。目前每日稳定消耗约 **2 亿至 5 亿 Token**，极大提升了极端市场环境下风险穿透的准确度。

## 4. 技术栈
* **Framework:** LangGraph, PydanticAI
* **Reasoning:** Tree-of-Thought (ToT), Recursive ReAct
* **Vector DB:** Pinecone (High-throughput metadata filtering)
