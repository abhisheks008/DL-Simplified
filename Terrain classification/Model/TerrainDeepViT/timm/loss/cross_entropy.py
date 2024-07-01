import torch
import torch.nn as nn
import torch.nn.functional as F


class LabelSmoothingCrossEntropy(nn.Module):
    """
    NLL loss with label smoothing.
    """
    def __init__(self, smoothing=0.1):
        """
        Constructor for the LabelSmoothing module.
        :param smoothing: label smoothing factor
        """
        super(LabelSmoothingCrossEntropy, self).__init__()
        assert smoothing < 1.0
        self.smoothing = smoothing
        self.confidence = 1. - smoothing

    def forward(self, x, target):
        logprobs = F.log_softmax(x, dim=-1)
        nll_loss = -logprobs.gather(dim=-1, index=target.unsqueeze(1))
        nll_loss = nll_loss.squeeze(1)
        smooth_loss = -logprobs.mean(dim=-1)
        loss = self.confidence * nll_loss + self.smoothing * smooth_loss
        return loss.mean()


class SoftTargetCrossEntropy(nn.Module):

    def __init__(self):
        super(SoftTargetCrossEntropy, self).__init__()

    def forward(self, x, target, atten=None):
        # import pdb;pdb.set_trace()
        loss = torch.sum(-target * F.log_softmax(x, dim=-1), dim=-1)
        return loss.mean()
class SoftTargetCrossEntropyCosReg(nn.Module):

    def __init__(self, n_comn=2):
        super(SoftTargetCrossEntropyCosReg, self).__init__()
        self.dis_fn = torch.nn.CosineSimilarity(dim=1)
        self.n_comn = n_comn

    def forward(self, x, target, atten=None):
        loss = torch.sum(-target * F.log_softmax(x, dim=-1), dim=-1)
        cos_loss = 0
        if atten is not None:
            for i in range(self.n_comn):
                cos_loss += self.dis_fn(atten[i], atten[i+1])
        # import pdb;pdb.set_trace()
        return loss.mean() + 0.1 * cos_loss.mean()/self.n_comn
