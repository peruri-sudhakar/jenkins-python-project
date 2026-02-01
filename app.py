import logging
import socket

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Webhook test: new change pushed")

def add(a, b):
    logging.info(f"Adding {a} and {b}")
    return a + b

if __name__ == "__main__":
    add(10, 20)
