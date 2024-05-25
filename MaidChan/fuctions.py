import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from manga_ocr import MangaOcr
from transformers import T5Tokenizer, T5ForConditionalGeneration


class text:

    def start_hello(User):
        hello = f"Hello {User} ! I'm Maid-Chan your personal assistan"
        return hello

class OCR:

    def manga_ocr(img:str):
        mocr = MangaOcr()
        img = Image.open(img)
        text = mocr(img)

        return text

class translate:

    def translate(leng_int:str, leng_out:str, text:str):
        tokenizer = T5Tokenizer.from_pretrained("google-t5/t5-small")
        model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-small")

        input_ids = tokenizer(f"translate {leng_int} to {leng_out}: {text}", return_tensors="pt").input_ids
        outputs = model.generate(input_ids)

        return tokenizer.decode(outputs[0], skip_special_tokens=True)

