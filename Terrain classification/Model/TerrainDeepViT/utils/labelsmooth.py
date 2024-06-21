import torch
from torch import nn

class LabelSmoothing(nn.Module):
    def __init__(self, size, smoothing=0.0):
        super(LabelSmoothing, self).__init__()
        self.criterion = nn.KLDivLoss(reduction='mean')
        self.Logsoftmax = nn.LogSoftmax(dim = 0)
        self.confidence = 1.0 - smoothing
        self.smoothing = smoothing
        self.size = size
        self.true_dist = None

    def forward(self, x, target):
        assert x.size(1) == self.size
        x = self.Logsoftmax(x)
        true_dist = x.data.clone()
        true_dist.fill_(self.smoothing / (self.size - 1))
        true_dist.scatter_(1, target.data.unsqueeze(1), self.confidence)
        self.true_dist = true_dist
        true_dist.requires_grad = False
        return self.criterion(x, true_dist)

def SmoothedLabel(true_labels, classes, smoothing=0.0):
    """
    if smoothing == 0, it's one-hot method
    if 0 < smoothing < 1, it's smooth method
    """
    assert 0 <= smoothing < 1
    confidence = 1.0 - smoothing
    label_shape = torch.Size((true_labels.size(0), classes))
    with torch.no_grad():
        true_dist = torch.empty(size=label_shape, device=true_labels.device)
        true_dist.fill_(smoothing / (classes - 1))
        true_dist.scatter_(1, true_labels.data.unsqueeze(1), confidence)
    return true_dist

class CrossEntropyLoss(nn.Module):
    def __init__(self, classes, smooth):
        super(CrossEntropyLoss, self).__init__()
        self.classes = classes
        self.smooth = smooth

    def forward(self, pred, labels):
        labels = SmoothedLabel(labels, self.classes, self.smooth)
        pred = pred.log_softmax(-1)
        return torch.mean(torch.sum(-labels * pred, dim = -1))



