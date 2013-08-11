import numpy as np


def pformat(masked_array):
    rank = len(masked_array.shape)

    slices = tuple([slice(0, masked_array.shape[i]) for i in xrange(rank - 1)])

    digits = int(np.ceil(np.log10(masked_array.max())))

    f = '%%%dd' % digits
    line = ']\n' + ((rank - 1) * ' ') + '['

    formatted_masked = line.join([', '.join([f % block_id
                                             if not m else digits * '-'
                                             for block_id, m in zip(row,
                                                                    row.mask)])
                                  for row in masked_array[slices]])
    return rank * '[' + formatted_masked + rank * ']'
