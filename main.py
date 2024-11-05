import sys
from dotenv import load_dotenv
import logging
import os
import logging.config
import qrcode

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
        ]
    )

def configure_logging():
    logging_conf_path = 'logging.conf'
    if os.path.exists(logging_conf_path):
        logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Logging configured.")

setup_logging()
configure_logging()

logging.info("QR code generation began.")
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size = 20,
                   border = 2)

qr.add_data("https://github.com/rithika955")
qr.make(fit = True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("myqr.png")
logging.info("QR code generation succesful")
