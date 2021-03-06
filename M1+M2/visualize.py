# -*- coding: utf-8 -*-
import os, sys, time, pylab
import numpy as np
from chainer import cuda, Variable
import matplotlib.patches as mpatches
sys.path.append(os.path.split(os.getcwd())[0])
import util
from args import args
from model import conf1, vae1, conf2, vae2
from vae_m1 import GaussianM1VAE

try:
	os.mkdir(args.vis_dir)
except:
	pass

dist = "bernoulli"
if isinstance(vae1, GaussianM1VAE):
	dist = "gaussian"
dataset, labels = util.load_labeled_images(args.test_image_dir, dist=dist)

num_plot = 10000
x = util.sample_x_variable(num_plot, conf1.ndim_x, dataset, gpu_enabled=conf1.gpu_enabled)
z1 = vae1.encoder(x, test=True)
y = vae2.sample_x_y(z1, test=True)
z2 = vae2.encode_xy_z(z1, y, test=True)

_z1 = vae2.decode_zy_x(z2, y, test=True, apply_f=True)
_x = vae1.decoder(_z1, test=True)
if conf1.gpu_enabled:
	z2.to_cpu()
	_x.to_cpu()
_x = _x.data

util.visualize_x(_x, dir=args.vis_dir)
util.visualize_z(z2.data, dir=args.vis_dir)
util.visualize_labeled_z(z2.data, labels, dir=args.vis_dir)