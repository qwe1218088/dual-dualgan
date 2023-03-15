import os
cmd = 'python main.py --phase train --dataset_name sketch-photo --image_size 128 --lambda_A 1000.0 --lambda_B 1000.0 --epoch 1000'
os.system(cmd)
cmd = 'python main2.py --phase train --dataset_name sketch-photo --image_size 128 --lambda_B 1000.0 --lambda_C 1000.0 --epoch 1000'
os.system(cmd)
