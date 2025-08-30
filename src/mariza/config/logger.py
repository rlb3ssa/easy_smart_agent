import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),  # console
        # logging.FileHandler("logs/uLawyer.log")  # arquivo
    ]
)

def get_logger(name: str = __name__):
    return logging.getLogger(name)


# Como usar:
# from uLawyer.config import logger
# logger = logger.get_logger(__name__)
# logger.info(f"Mensagem de exemplo: {self.agents} | {var_qualquer}")
#
#
#
