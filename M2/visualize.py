# -*- coding: utf-8 -*-
import os, sys, time, pylab
import numpy as np
from chainer import cuda, Variable
import matplotlib.patches as mpatches
sys.path.append(os.path.split(os.getcwd())[0])
import util
from args import args
from model import conf, vae

try:
	os.mkdir(args.visualization_dir)
except:
	pass

vae.load(args.model_dir)
dataset = util.load_images(args.test_image_dir)
num_images = 100
x = util.sample_x_variable(num_images, conf.ndim_x, dataset, use_gpu=conf.use_gpu)
z = vae.encode(x, test=True)
_x = vae.decode(z, test=True, output_pixel_value=True)
if conf.use_gpu:
	z.to_cpu()
	_x.to_cpu()
util.visualize_x(_x.data, dir=args.vis_dir)
util.visualize_z(z.data, dir=args.vis_dir)