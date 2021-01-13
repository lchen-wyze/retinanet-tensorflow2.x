# RetinaNet

#### Supports
 - [x] Performs better than most of the implemetations
 - [x] Multiple ResNet Depths
 - [x] Train on Single/ Multiple GPUs
 - [x] Stable training with Automatic Mixed Precision (~2.5x quicker)
 - [x] Train on TPU/ TPU pods (slices)
 - [x] Export `saved_model`
 - [x] COCO mAP evaluation callback
 - [ ] Transfer learning/ Fine-tuning
 - [ ] Export TensorRT model
 - [ ] Batched inference



## Getting Started
### Training
 - Use `prepare_coco_dataset.sh` to download the COCO2017 dataset and create the tfrecords.
 - If you plan to train on **Google Cloud TPU**, upload the `coco_tfrecords` folder to your **Google Cloud Storage** bucket.
 - `USE_SYNC_BN="" TF_CPP_MIN_LOG_LEVEL="3" TPU_NAME="v3-8-3" python3 -m retinanet.main --config_path configs/retinanet-34-640-30x-64-tpu.json --log_dir logs --alsologtostderr` to train, you should now be able to see logs similar to this
```
I1026 09:23:09.476862 140424579548992 trainer.py:77] Setting up train dataset
I1026 09:23:09.533261 140424579548992 input_pipeline.py:30] Found 256 train tfrecords matching gs://tfrc_datasets/coco_tfrecords/train*
I1026 09:23:11.362147 140424579548992 trainer.py:92] Looking for existing checkpoints in gs://tfrc_datasets/model_files/retinanet-101-640-30x-64-tpu
I1026 09:23:11.468965 140424579548992 trainer.py:104] No existing checkpoints found in gs://tfrc_datasets/model_files/retinanet-101-640-30x-64-tpu, training from scratch!
I1026 09:23:11.488565 140424579548992 trainer.py:184] Starting training from step 0 for 675000 steps with 250 steps per execution
I1026 09:23:11.488853 140424579548992 trainer.py:186] Saving checkpoints every 50000 steps in gs://tfrc_datasets/model_files/retinanet-101-640-30x-64-tpu
I1026 09:23:11.489072 140424579548992 trainer.py:83] Setting up summary writer
I1026 09:23:11.491212 140424579548992 trainer.py:88] Writing summaries to gs://tfrc_datasets/tensorboard/retinanet-101-640-30x-64-tpu
I1026 09:23:12.733609 140424579548992 tpu.py:1238] Automatic outside compilation is enabled. Ops without XLA kernels will be automatically placed on CPU.
I1026 09:23:54.162838 140424579548992 tpu.py:1238] Automatic outside compilation is enabled. Ops without XLA kernels will be automatically placed on CPU.
I1026 09:24:38.644693 140424579548992 tpu.py:1238] Automatic outside compilation is enabled. Ops without XLA kernels will be automatically placed on CPU.
I1026 09:25:19.810285 140424579548992 tpu.py:1238] Automatic outside compilation is enabled. Ops without XLA kernels will be automatically placed on CPU.
I1026 09:30:40.215446 140424579548992 trainer.py:239] [global_step 250/675000] [ETA: 332:11:12] [36.11 imgs/s] {'box-loss': 0.01, 'class-loss': 1.128, 'weighted-loss': 1.634, 'l2-regularization': 2.772, 'total-loss': 4.406, 'gradient-norm': 0.414, 'execution-time': 443.08, 'learning-rate': 0.008}
I1026 09:31:33.522529 140424579548992 trainer.py:239] [global_step 500/675000] [ETA: 39:49:04] [301.15 imgs/s] {'box-loss': 0.01, 'class-loss': 1.008, 'weighted-loss': 1.499, 'l2-regularization': 2.762, 'total-loss': 4.261, 'gradient-norm': 0.388, 'execution-time': 53.13, 'learning-rate': 0.009}
I1026 09:32:26.712022 140424579548992 trainer.py:239] [global_step 750/675000] [ETA: 39:42:21] [301.89 imgs/s] {'box-loss': 0.01, 'class-loss': 0.981, 'weighted-loss': 1.471, 'l2-regularization': 2.749, 'total-loss': 4.22, 'gradient-norm': 0.35, 'execution-time': 53.0, 'learning-rate': 0.009}
I1026 09:33:19.951558 140424579548992 trainer.py:239] [global_step 1000/675000] [ETA: 39:44:36] [301.49 imgs/s] {'box-loss': 0.009, 'class-loss': 0.942, 'weighted-loss': 1.409, 'l2-regularization': 2.736, 'total-loss': 4.145, 'gradient-norm': 0.385, 'execution-time': 53.07, 'learning-rate': 0.01}
I1026 09:34:13.216273 140424579548992 trainer.py:239] [global_step 1250/675000] [ETA: 39:46:25] [301.15 imgs/s] {'box-loss': 0.009, 'class-loss': 0.934, 'weighted-loss': 1.39, 'l2-regularization': 2.722, 'total-loss': 4.111, 'gradient-norm': 0.411, 'execution-time': 53.13, 'learning-rate': 0.011}
I1026 09:35:06.289964 140424579548992 trainer.py:239] [global_step 1500/675000] [ETA: 39:37:27] [302.17 imgs/s] {'box-loss': 0.009, 'class-loss': 0.953, 'weighted-loss': 1.399, 'l2-regularization': 2.706, 'total-loss': 4.105, 'gradient-norm': 0.441, 'execution-time': 52.95, 'learning-rate': 0.012}
I1026 09:35:59.451853 140424579548992 trainer.py:239] [global_step 1750/675000] [ETA: 39:37:55] [302.00 imgs/s] {'box-loss': 0.009, 'class-loss': 0.91, 'weighted-loss': 1.351, 'l2-regularization': 2.689, 'total-loss': 4.041, 'gradient-norm': 0.399, 'execution-time': 52.98, 'learning-rate': 0.013}
I1026 09:36:52.646378 140424579548992 trainer.py:239] [global_step 2000/675000] [ETA: 39:40:10] [301.60 imgs/s] {'box-loss': 0.008, 'class-loss': 0.824, 'weighted-loss': 1.224, 'l2-regularization': 2.672, 'total-loss': 3.896, 'gradient-norm': 0.38, 'execution-time': 53.05, 'learning-rate': 0.014}
I1026 09:37:45.771663 140424579548992 trainer.py:239] [global_step 2250/675000] [ETA: 39:35:42] [302.06 imgs/s] {'box-loss': 0.008, 'class-loss': 0.904, 'weighted-loss': 1.306, 'l2-regularization': 2.653, 'total-loss': 3.959, 'gradient-norm': 0.428, 'execution-time': 52.97, 'learning-rate': 0.015}
I1026 09:38:39.022006 140424579548992 trainer.py:239] [global_step 2500/675000] [ETA: 39:40:39] [301.32 imgs/s] {'box-loss': 0.008, 'class-loss': 0.79, 'weighted-loss': 1.199, 'l2-regularization': 2.633, 'total-loss': 3.832, 'gradient-norm': 0.372, 'execution-time': 53.1, 'learning-rate': 0.016}

```
___
### Running Inference
```python
import json
from glob import glob
from time import time

import tensorflow as tf

from retinanet.image_utils import read_image, visualize_detections


image_dir = '~coco2017/val2017'
images = sorted(glob(image_dir + '/*'))
print('Found {} images in {}'.format(len(images), image_dir))

#  Load label mapping
with open('coco_label_map.json', 'r') as f:
    label_map = json.load(f)

#  Load `saved_model`
model = tf.saved_model.load('model_files/retinanet-1024-30x-64-tpu')
serving_fn = model.signatures['serving_default']

idx = 336
image = read_image(images[idx])

tik = time()
detections = serving_fn(image=image, image_id=tf.constant(idx))
toc = time()

valid_detections = detections['valid_detections'].numpy()
boxes = detections['boxes'][:valid_detections].numpy()
classes = [
    label_map[str(idx)]
    for idx in detections['class_ids'][:valid_detections].numpy()
]
scores = detections['scores'][:valid_detections].numpy()

#  Visualize detections
visualize_detections(image,
                     boxes,
                     classes,
                     scores,
                     title='Image: {}'.format(idx),
                     save=False,
                     filename='outputs/image_{}.png'.format(idx))

print('Inference time: {:.2f} ms'.format((toc - tik) * 1000))
```
___
### Visualizations

<table>
  <tr>
    <td valign="top"><img src="assets/image_3116.png"></td>
    <td valign="top"><img src="assets/image_1618.png"></td>
    <td valign="top"><img src="assets/image_4964.png"></td>
    <td valign="top"><img src="assets/image_4348.png"></td>
  </tr>
 </table>


___
### Tensorboard
![loss curves](assets/tensorboard.png)


___
#### To-Do
 - [x] Train on ResNet18, 34, 101
 - [x] Add models trained with 30x schedule, without imagenet pretrained weights
 - [x] Support Input Sharding for TPU Pod
 - [x] COCO mAP evaluation callback
 - [ ] Support fine tuning and training with other datasets
 - [ ] Add fine-tuning example
 - [ ] Add MobileNetV3 Backbone

```
@misc{1708.02002,
Author = {Tsung-Yi Lin and Priya Goyal and Ross Girshick and Kaiming He and Piotr Dollár},
Title = {Focal Loss for Dense Object Detection},
Year = {2017},
Eprint = {arXiv:1708.02002},
}
```
