from tensorflow.keras.layers import Activation, Conv2D, BatchNormalization, Add


def residual_block_basic(x, filters, kernel_size=3, strides=1):
    # Residual Path
    conv_1 = Conv2D(filters=filters, kernel_size=kernel_size, padding='same', strides=strides)(x)
    bn_1 = BatchNormalization(axis=-1)(conv_1)
    act_1 = Activation('relu')(bn_1)

    conv_2 = Conv2D(filters=filters, kernel_size=kernel_size, padding='same', strides=strides)(act_1)

    residual = BatchNormalization(axis=-1)(conv_2)

    # Shortcut Path:
    shortcut = x if strides == 1 else Conv2D(filters, kernel_size=1, padding='valid', strides=strides)(x)

    # Merge and return:

    return Activation('relu')(Add([shortcut, residual]))
