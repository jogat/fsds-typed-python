from datetime import date
from decimal import Decimal

from app.analytics.renderers import render_markdown_report
from app.analytics.reports import build_bitcoin_analytics_report
from app.core.types.bitcoin import BitcoinDailyCandle


def _candle(
    d: date, close: Decimal, volume: Decimal = Decimal("1")
) -> BitcoinDailyCandle:
    return BitcoinDailyCandle(
        date=d,
        open=close,
        high=close,
        low=close,
        close=close,
        volume=volume,
    )


def test_build_bitcoin_analytics_report() -> None:
    candles = [
        _candle(date(2024, 1, 1), Decimal("100"), Decimal("10")),
        _candle(date(2024, 1, 2), Decimal("110"), Decimal("5")),
        _candle(date(2024, 1, 3), Decimal("121"), Decimal("2")),
    ]

    report = build_bitcoin_analytics_report(candles)

    assert report.start_date == date(2024, 1, 1)
    assert report.end_date == date(2024, 1, 3)
    assert report.volume.total_volume == Decimal("17")
    assert report.returns.observation_count == 2


def test_render_markdown_report_contains_key_sections() -> None:
    candles = [
        _candle(date(2024, 1, 1), Decimal("100")),
        _candle(date(2024, 1, 2), Decimal("110")),
    ]

    report = build_bitcoin_analytics_report(candles)
    markdown = render_markdown_report(report)

    assert "# 📊 Bitcoin Analytics Report" in markdown
    assert "## 💰 Price Summary" in markdown
    assert "## 📈 Returns" in markdown
