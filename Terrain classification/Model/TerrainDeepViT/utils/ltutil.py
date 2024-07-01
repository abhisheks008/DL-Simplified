import torch
import pickle
import numpy as np
import torch.nn.functional as F


def pnorm(weights, p):
    normB = torch.norm(weights, 2, 1)
    ws = weights.clone()
    for i in range(weights.size(0)):
        ws[i] = ws[i] / torch.pow(normB[i], p)
    return ws

class TauLayer(torch.nn.Module):
    def __init__(self, fc, tau=None):
        super(TauLayer, self).__init__()
        if tau is None:
            self.tau = np.linspace(0, 1, 11)
        elif isinstance(tau, (int, float)):
            self.tau = [tau]
        elif isinstance(tau, (list, np.array)):
            self.tau = tau
        else:
            raise NotImplementedError('tau type nog recognized')
    
        ws = []
        for t in self.tau:
            ws.append(pnorm(fc.weight.data, t))
        self.weight = torch.nn.Parameter(torch.cat(ws), requires_grad=False)
        self.register_parameter('bias', None)

    def forward(self, input):
        return F.linear(input, self.weight, self.bias)
    
    @property
    def num_tau(self):
        if isinstance(self.tau, (int, float)):
            return 1
        else:
            return len(self.tau)


class SoftCrossEntropyLoss(torch.nn.Module):
    def __init__(self):
        super(SoftCrossEntropyLoss, self).__init__()
    
    def forward(self, input, target):
        bs = input.shape[0]
        nlp = -F.log_softmax(input, dim=1)
        loss = torch.sum(nlp * target) / bs
        return loss

class SumCrossEntropyLoss(torch.nn.Module):
    def __init__(self, tgt_avg=False):
        super(SumCrossEntropyLoss, self).__init__()
        self.tgt_avg = tgt_avg
        print('=> target size averaging: ', self.tgt_avg)

    def forward(self, input, target):
        bs = input.shape[0]
        mask = (target>0).float()
        p = F.softmax(input, dim=1)
        psum = torch.sum(p*mask, dim=1)
        nlp = -torch.log(psum)
        if self.tgt_avg:
            return nlp / mask.sum()
        else:
            return nlp / bs
 

class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self, name, fmt=':f'):
        self.name = name
        self.fmt = fmt
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

    def __str__(self):
        fmtstr = '{name} {val' + self.fmt + '} ({avg' + self.fmt + '})'
        return fmtstr.format(**self.__dict__)


class AverageMeters(object):
    def __init__(self, size):
        self.meters = [AverageMeter(i) for i in range(size)]
    
    def update(self, idxs, vals):
        for i, v in zip(idxs, vals):
            self.meters[i].update(v)
    
    def get_avgs(self):
        return np.array([m.avg for m in self.meters])
    
    def get_sums(self):
        return np.array([m.sum for m in self.meters])
    
    def get_cnts(self):
        return np.array([m.count for m in self.meters])


class ProgressMeter(object):
    def __init__(self, num_batches, meters, prefix=""):
        self.batch_fmtstr = self._get_batch_fmtstr(num_batches)
        self.meters = meters
        self.prefix = prefix

    def display(self, batch):
        entries = [self.prefix + self.batch_fmtstr.format(batch)]
        entries += [str(meter) for meter in self.meters]
        print('\t'.join(entries))

    def _get_batch_fmtstr(self, num_batches):
        num_digits = len(str(num_batches // 1))
        fmt = '{:' + str(num_digits) + 'd}'
        return '[' + fmt + '/' + fmt.format(num_batches) + ']'


def accuracy(output, target, topk=(1,), detail=False):
    """Computes the accuracy over the k top predictions for the specified values of k"""
    with torch.no_grad():
        maxk = max(topk)
        batch_size = target.size(0)

        _, pred = output.topk(maxk, 1, True, True)
        pred = pred.t()
        correct = pred.eq(target.view(1, -1).expand_as(pred))

        res = []
        for k in topk:
            correct_k = correct[:k].view(-1).float().sum(0, keepdim=True)
            res.append(correct_k.mul_(100.0 / batch_size))
        if detail:
            return res, target.cpu().numpy(), correct[0].cpu().numpy()
        else:
            return res


def shot_acc(percls_acc, cls_cnts, shots=[20, 100]):
    assert len(percls_acc) == len(cls_cnts)
    shots = sorted(shots, reverse=True)
    accs = []
    reset = np.ones(len(percls_acc), dtype=bool)
    for s in shots:
        accs.append(np.mean(percls_acc[np.logical_and(reset, cls_cnts>s)]))
        reset = np.logical_and(reset, cls_cnts<=s)
    accs.append(np.mean(percls_acc[reset]))
    return accs


def save_obj(fname, obj):
    print('=> saving to {}'.format(fname))
    with open(fname, 'wb') as f:
        pickle.dump(obj, f)


def load_obj(fname):
    print('=> loading from {}'.format(fname))
    with open(fname, 'rb') as f:
        return pickle.load(f)
