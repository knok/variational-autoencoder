# -*- coding: utf-8 -*-
from args import args
from vae import BernoulliVAE, GaussianVAE, Conf

conf = Conf()
conf.use_gpu = args.use_gpu
vae = GaussianVAE(conf, name="m1")