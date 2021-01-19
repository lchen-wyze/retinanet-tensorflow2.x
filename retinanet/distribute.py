import os

import tensorflow as tf
from absl import logging


def get_strategy(params):
    if params.type == 'gpu':
        logging.info('Creating GPU strategy')
        return tf.distribute.OneDeviceStrategy(device='/gpu:0')

    if params.type == 'cpu':
        logging.info('Creating CPU strategy')
        return tf.distribute.OneDeviceStrategy(device='/cpu:0')

    if params.type == 'multi_gpu':
        logging.info('Creating Multi GPU strategy')
        return tf.distribute.MirroredStrategy()

    if params.type == 'tpu':
        logging.info('Creating TPU strategy')

        tpu_name = params.name

        if tpu_name == '':
            if 'TPU_NAME' not in os.environ:
                raise AssertionError(
                    'Failed to fetch TPU name, please set ENV VAR \
                        `TPU_NAME` or specify TPU name in config ')

            tpu_name = os.environ['TPU_NAME']
            logging.warning(
                'Using {} as TPU name from ENV VAR `TPU_NAME`'.format(tpu_name))

        else:
            if 'TPU_NAME' in os.environ:
                tpu_name = os.environ['TPU_NAME']

                logging.warning(
                    'Changed TPU name from {} to {} \
                        (overided with ENV VAR `TPU_NAME`)'.format(
                        params.name, tpu_name))

        resolver = tf.distribute.cluster_resolver.TPUClusterResolver.connect(
            tpu_name)
        return tf.distribute.TPUStrategy(resolver)

    raise ValueError('Unsupported strategy requested')
