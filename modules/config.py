import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API configuration
API_KEY = os.getenv('BINANCE_API_KEY', '')
API_SECRET = os.getenv('BINANCE_API_SECRET', '')

# Testnet configuration
API_TESTNET = os.getenv('BINANCE_API_TESTNET', 'False').lower() == 'true'

# API URLs - Automatically determined based on testnet setting
if API_TESTNET:
    # Testnet URLs
    API_URL = 'https://testnet.binancefuture.com'
    WS_BASE_URL = 'wss://stream.binancefuture.com'
else:
    # Production URLs
    API_URL = os.getenv('BINANCE_API_URL', 'https://fapi.binance.com')
    WS_BASE_URL = 'wss://fstream.binance.com'

# API request settings
RECV_WINDOW = int(os.getenv('BINANCE_RECV_WINDOW', '10000'))

# Trading parameters
TRADING_SYMBOL = os.getenv('TRADING_SYMBOL', 'BTCUSDT')
TRADING_TYPE = 'FUTURES'  # Use futures trading
LEVERAGE = int(os.getenv('LEVERAGE', '30'))
MARGIN_TYPE = os.getenv('MARGIN_TYPE', 'CROSSED')  # ISOLATED or CROSSED
STRATEGY = os.getenv('STRATEGY', 'PurePriceActionStrategy')

# Position sizing - Enhanced risk management (aligned with SmartTrendCatcher)
INITIAL_BALANCE = float(os.getenv('INITIAL_BALANCE', '50.0'))
FIXED_TRADE_PERCENTAGE = float(os.getenv('FIXED_TRADE_PERCENTAGE', '0.45'))  # 45% to match strategy base_position_pct
MAX_OPEN_POSITIONS = int(os.getenv('MAX_OPEN_POSITIONS', '3'))  # Conservative for better risk management

# Margin safety settings - More conservative
MARGIN_SAFETY_FACTOR = float(os.getenv('MARGIN_SAFETY_FACTOR', '0.90'))  # Use at most 90% of available margin
MAX_POSITION_SIZE_PCT = float(os.getenv('MAX_POSITION_SIZE_PCT', '0.50'))  # Max 50% position size (matches strategy)
MIN_FREE_BALANCE_PCT = float(os.getenv('MIN_FREE_BALANCE_PCT', '0.10'))  # Keep at least 10% free

# Multi-instance configuration for running separate bot instances per trading pair
MULTI_INSTANCE_MODE = os.getenv('MULTI_INSTANCE_MODE', 'True').lower() == 'true'
MAX_POSITIONS_PER_SYMBOL = int(os.getenv('MAX_POSITIONS_PER_SYMBOL', '3'))  # Updated to match .env

# Auto-compounding settings - Enhanced with performance-based adjustments
AUTO_COMPOUND = os.getenv('AUTO_COMPOUND', 'True').lower() == 'true'
COMPOUND_REINVEST_PERCENT = float(os.getenv('COMPOUND_REINVEST_PERCENT', '0.75'))
COMPOUND_INTERVAL = os.getenv('COMPOUND_INTERVAL', 'DAILY')

# Dynamic compounding adjustments
COMPOUND_PERFORMANCE_WINDOW = int(os.getenv('COMPOUND_PERFORMANCE_WINDOW', '7'))  # Look back 7 days
COMPOUND_MIN_WIN_RATE = float(os.getenv('COMPOUND_MIN_WIN_RATE', '0.6'))  # Require 60% win rate
COMPOUND_MAX_DRAWDOWN = float(os.getenv('COMPOUND_MAX_DRAWDOWN', '0.15'))  # Pause if >15% drawdown
COMPOUND_SCALING_FACTOR = float(os.getenv('COMPOUND_SCALING_FACTOR', '0.5'))  # Reduce compounding if performance poor

# Pure Price Action Strategy Parameters - No Traditional Indicators

# Price action analysis parameters
PRICE_ACTION_LOOKBACK = int(os.getenv('PRICE_ACTION_LOOKBACK', '12'))    # Optimal for 5m BTC
BREAKOUT_THRESHOLD = float(os.getenv('BREAKOUT_THRESHOLD', '0.008'))     # 0.8% for 5m BTC moderate vol
VOLATILITY_WINDOW = int(os.getenv('VOLATILITY_WINDOW', '8'))            # Shorter for 5m
MOMENTUM_WINDOW = int(os.getenv('MOMENTUM_WINDOW', '6'))                 # Shorter for 5m
SUPPORT_RESISTANCE_STRENGTH = int(os.getenv('SUPPORT_RESISTANCE_STRENGTH', '2'))  # Reduced for 5m

TIMEFRAME = os.getenv('TIMEFRAME', '5m')  # 5m for BTC scalping

# Risk management - Enhanced for BTC 5m trading (moderate volatility optimized)
USE_STOP_LOSS = os.getenv('USE_STOP_LOSS', 'True').lower() == 'true'
STOP_LOSS_PCT = float(os.getenv('STOP_LOSS_PCT', '0.008'))  # 0.8% stop loss for BTC moderate vol
TRAILING_STOP = os.getenv('TRAILING_STOP', 'True').lower() == 'true'
TRAILING_STOP_PCT = float(os.getenv('TRAILING_STOP_PCT', '0.006'))  # 0.6% trailing stop for moderate vol
UPDATE_TRAILING_ON_HOLD = os.getenv('UPDATE_TRAILING_ON_HOLD', 'True').lower() == 'true'

# Take profit settings - Optimized for BTC 5m moderate volatility trading
USE_TAKE_PROFIT = os.getenv('USE_TAKE_PROFIT', 'True').lower() == 'true'
TAKE_PROFIT_PCT = float(os.getenv('TAKE_PROFIT_PCT', '0.012'))  # 1.2% take profit for BTC moderate vol

# Enhanced backtesting parameters
BACKTEST_START_DATE = os.getenv('BACKTEST_START_DATE', '2023-01-01')
BACKTEST_END_DATE = os.getenv('BACKTEST_END_DATE', '')
BACKTEST_INITIAL_BALANCE = float(os.getenv('BACKTEST_INITIAL_BALANCE', '50.0'))
BACKTEST_COMMISSION = float(os.getenv('BACKTEST_COMMISSION', '0.0004'))
BACKTEST_USE_AUTO_COMPOUND = os.getenv('BACKTEST_USE_AUTO_COMPOUND', 'True').lower() == 'true'  # Enabled for enhanced auto-compounding test

# Enhanced validation requirements - Optimized for pure price action strategies
BACKTEST_BEFORE_LIVE = os.getenv('BACKTEST_BEFORE_LIVE', 'True').lower() == 'true'
BACKTEST_MIN_PROFIT_PCT = float(os.getenv('BACKTEST_MIN_PROFIT_PCT', '10.0'))  # Suitable for price action
BACKTEST_MIN_WIN_RATE = float(os.getenv('BACKTEST_MIN_WIN_RATE', '40.0'))  # Realistic for pure price action
BACKTEST_MAX_DRAWDOWN = float(os.getenv('BACKTEST_MAX_DRAWDOWN', '30.0'))  # Allow for volatility
BACKTEST_MIN_PROFIT_FACTOR = float(os.getenv('BACKTEST_MIN_PROFIT_FACTOR', '1.2'))  # Conservative
BACKTEST_PERIOD = os.getenv('BACKTEST_PERIOD', '90 days')  # Default to 90 days for comprehensive testing

# Logging and notifications
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
USE_TELEGRAM = os.getenv('USE_TELEGRAM', 'True').lower() == 'true'
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')
SEND_DAILY_REPORT = os.getenv('SEND_DAILY_REPORT', 'True').lower() == 'true'
DAILY_REPORT_TIME = os.getenv('DAILY_REPORT_TIME', '00:00')  # 24-hour format

# Other settings
RETRY_COUNT = int(os.getenv('RETRY_COUNT', '3'))
RETRY_DELAY = int(os.getenv('RETRY_DELAY', '5'))  # seconds

# Enhanced Price Action Pattern Configuration for BTC 5m (moderate volatility)
ZONE_WIDTH_PCT = float(os.getenv('ZONE_WIDTH_PCT', '0.006'))  # 0.6% zone width for BTC moderate volatility
MIN_ZONE_STRENGTH = int(os.getenv('MIN_ZONE_STRENGTH', '2'))  # Reduced for 5m opportunities
MIN_SIGNAL_STRENGTH = int(os.getenv('MIN_SIGNAL_STRENGTH', '3'))  # Reduced for 5m entries

# Pattern Detection Parameters
ENABLE_MULTI_CANDLE_PATTERNS = os.getenv('ENABLE_MULTI_CANDLE_PATTERNS', 'True').lower() == 'true'
ENABLE_FLAG_PENNANT_DETECTION = os.getenv('ENABLE_FLAG_PENNANT_DETECTION', 'True').lower() == 'true'
MIN_FLAG_CONSOLIDATION_CANDLES = int(os.getenv('MIN_FLAG_CONSOLIDATION_CANDLES', '5'))
MIN_PENNANT_CONSOLIDATION_CANDLES = int(os.getenv('MIN_PENNANT_CONSOLIDATION_CANDLES', '6'))

# Pattern Quality Filters - Tighter for BTC 5m
MIN_PIN_BAR_SHADOW_RATIO = float(os.getenv('MIN_PIN_BAR_SHADOW_RATIO', '2.2'))  # Tighter for BTC
MIN_MARUBOZU_BODY_RATIO = float(os.getenv('MIN_MARUBOZU_BODY_RATIO', '0.87'))  # Tighter for BTC
MIN_DOJI_BODY_RATIO = float(os.getenv('MIN_DOJI_BODY_RATIO', '0.12'))  # Tighter for BTC
MIN_ENGULFING_SIZE_RATIO = float(os.getenv('MIN_ENGULFING_SIZE_RATIO', '1.08'))  # Tighter for BTC

# Volume Confirmation (when available) - Adjusted for BTC 5m
VOLUME_CONFIRMATION_MULTIPLIER = float(os.getenv('VOLUME_CONFIRMATION_MULTIPLIER', '1.4'))  # Tighter for BTC
ENABLE_VOLUME_CONFIRMATION = os.getenv('ENABLE_VOLUME_CONFIRMATION', 'True').lower() == 'true'

# Risk Management for Enhanced Patterns
PATTERN_BASED_POSITION_SIZING = os.getenv('PATTERN_BASED_POSITION_SIZING', 'True').lower() == 'true'
HIGH_CONFIDENCE_POSITION_MULTIPLIER = float(os.getenv('HIGH_CONFIDENCE_POSITION_MULTIPLIER', '1.2'))  # 20% larger for high confidence
LOW_CONFIDENCE_POSITION_MULTIPLIER = float(os.getenv('LOW_CONFIDENCE_POSITION_MULTIPLIER', '0.8'))  # 20% smaller for low confidence

# Pattern-Specific Risk Management
PATTERN_SPECIFIC_RISK = os.getenv('PATTERN_SPECIFIC_RISK', 'True').lower() == 'true'

# Different stop losses for different pattern types - BTC 5m moderate volatility optimized
REVERSAL_PATTERN_STOP_PCT = float(os.getenv('REVERSAL_PATTERN_STOP_PCT', '0.010'))   # 1.0% for BTC reversals
BREAKOUT_PATTERN_STOP_PCT = float(os.getenv('BREAKOUT_PATTERN_STOP_PCT', '0.008'))  # 0.8% for BTC breakouts
CONTINUATION_PATTERN_STOP_PCT = float(os.getenv('CONTINUATION_PATTERN_STOP_PCT', '0.006'))  # 0.6% for continuation

# Different take profits for pattern types - BTC 5m moderate volatility optimized
REVERSAL_PATTERN_TP_PCT = float(os.getenv('REVERSAL_PATTERN_TP_PCT', '0.018'))      # 1.8% for BTC reversals
BREAKOUT_PATTERN_TP_PCT = float(os.getenv('BREAKOUT_PATTERN_TP_PCT', '0.020'))       # 2.0% for BTC breakouts
CONTINUATION_PATTERN_TP_PCT = float(os.getenv('CONTINUATION_PATTERN_TP_PCT', '0.012'))  # 1.2% for continuation

# Signal confidence adjustments
HIGH_CONFIDENCE_PATTERNS = ['morning_star', 'evening_star', 'three_white_soldiers', 'three_black_crows', 
                           'marubozu_bullish', 'marubozu_bearish', 'bullish_breakout', 'bearish_breakout']
MEDIUM_CONFIDENCE_PATTERNS = ['engulfing_bullish', 'engulfing_bearish', 'pin_bar_bullish', 'pin_bar_bearish',
                             'tweezer_top', 'tweezer_bottom', 'bullish_flag', 'bearish_flag']
LOW_CONFIDENCE_PATTERNS = ['doji', 'spinning_top', 'spinning_bottom', 'inside_bar', 'outside_bar']