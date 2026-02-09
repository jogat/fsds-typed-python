from __future__ import annotations

from app.analytics.schemas import BitcoinAnalyticsReport


def render_markdown_report(report: BitcoinAnalyticsReport) -> str:
    return f"""
        # 📊 Bitcoin Analytics Report
    
        **Period:** {report.start_date} → {report.end_date}
    
        ---
    
        ## 💰 Price Summary
        - Average close: {report.price.average_close:.2f}
        - Min close: {report.price.min_close:.2f}
        - Max close: {report.price.max_close:.2f}
    
        ---
    
        ## 📦 Volume Summary
        - Total volume: {report.volume.total_volume}
        - Average daily volume: {report.volume.average_volume}
    
        ---
    
        ## 📈 Returns
        - Mean daily return: {report.returns.mean_daily_return:.2%}
        - Volatility: {report.returns.volatility:.2%}
        - Observations: {report.returns.observation_count}
        """.strip()
