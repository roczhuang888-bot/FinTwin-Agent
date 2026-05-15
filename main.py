from agent_engine import FinancialEvolutionEngine
import logging

async def main():
    print("Initializing Global Financial Digital Twin...")
    engine = FinancialEvolutionEngine()
    
    # 模拟重大宏观事件：如美联储非农数据发布
    target_event = "Federal Reserve Non-farm Payrolls Analysis"
    
    # 启动大规模推演
    # 注意：此操作预计将产生单次千万级的 Token 吞吐
    report = await engine.run_evolution(target_event)
    
    print(f"推演完成。最终策略一致性得分: {report.confidence_score}")

if __name__ == "__main__":
    asyncio.run(main())
