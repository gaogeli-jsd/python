import logging

logging.basicConfig(level=logging.INFO)

def process_data(data):
    logging.info("Processing data...")
    try:
        # 何かしらの処理
        # ...
        c=7/0
        print("abc")
    except Exception as e:
        logging.error("Error occurred while processing data: %s", e)
        raise
    finally:
        logging.info("Data processing completed.")

process_data("Sample data")