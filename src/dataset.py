# -*- coding: utf-8 -*-
import cv2
import torch
import numpy as np
from torch.utils.data import Dataset


from .utils import resize_if_need, make_img_padding


class DatasetRetriever(Dataset):

    def __init__(self, df, config, converter):
        self.config = config
        self.converter = converter
        self.image_ids = df.index.values
        self.texts = df['text'].values
        self.paths = df['path'].values

    def __len__(self):
        return len(self.image_ids)

    def __getitem__(self, idx):
        image_id = self.image_ids[idx]
        image = self.load_image(idx)
        gt_text = self.texts[idx]
        encoded = self.converter.encode(gt_text)
        image = image.astype(np.float32) / 255.0
        image = torch.from_numpy(image).permute(2, 0, 1)
        return {
            'id': image_id,
            'image': image,
            'gt_text': gt_text,
            'encoded': torch.tensor(encoded, dtype=torch.int32),
        }

    def load_image(self, idx):
        image = cv2.imread(f'{self.config.data_dir}/{self.paths[idx]}')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = resize_if_need(image, self.config['image_h'], self.config['image_w'])
        image = make_img_padding(image, self.config['image_h'], self.config['image_w'])
        return image
