import torch
import torch.nn as nn
import torch.nn.functional as F

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
