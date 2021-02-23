# -*- coding: utf-8 -*-
import re

from .base import BaseConfig


class IAMConfig(BaseConfig):

    def __init__(
            self,
            data_dir,
            image_w=1024,
            image_h=128,
            dataset_name='iam',
            chars=' !"#&\'()*+,-./0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
            blank='ß',
            **kwargs,
    ):
        super().__init__(
            data_dir=data_dir,
            dataset_name=dataset_name,
            image_w=image_w,
            image_h=image_h,
            chars=chars,
            blank=blank,
            **kwargs,
        )

    def preprocess(self, text):
        """ preprocess only train text """
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def postprocess(self, text):
        """ postprocess output text """
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
