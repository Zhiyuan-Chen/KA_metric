from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .cross_entropy_loss import CrossEntropyLabelSmooth
from .hard_mine_triplet_loss import TripletLoss
from .center_loss import CenterLoss
from .ring_loss import RingLoss
from .ka_loss import KALoss
from .batch_all_triplet_loss import BA_TripletLoss
from .lifted_loss import LiftedLoss


def DeepSupervision(criterion, xs, y):
    """
    Args:
    - criterion: loss function
    - xs: tuple of inputs
    - y: ground truth
    """
    loss = 0.
    for x in xs:
        loss += criterion(x, y)
    loss /= len(xs)
    return loss

def DeepSupervision_wcont(criterion, xs_batch1, xs_batch2, y_batch1, y_batch2):
    """
    Args:
    - criterion: loss function
    - xs: tuple of inputs
    - y: ground truth
    """
    loss = 0.
    for ind in len(xs_batch1):
        loss += criterion(xs_batch1, xs_batch2, y_batch1, y_batch2)
    loss /= len(xs)
    return loss