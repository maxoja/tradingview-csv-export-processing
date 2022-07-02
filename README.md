# tradingview-csv-export-processing
Utility Python scripts for processing exported CSV from a TradingView chart

- **identify_candles.py**
  - Prints datetime of candles that match a given simple condition
  - Example `python identify_candles.py file.csv "volume MA" "col > 500"`
  - The keyword `col` refers to the given column "volume MA"