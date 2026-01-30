import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def add(a, b):
    logging.info(f"Adding {a} and {b}")
    result = a + b
    logging.info(f"Result is {result}")
    return result

if __name__ == "__main__":
    logging.info("Application started")
    add(10, 20)
    logging.info("Application finished")
