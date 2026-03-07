"""Simple logging utility for Sentinel AI"""

import logging

logger = logging.getLogger("sentinel")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)


def log(message: str):
    logger.info(message)
