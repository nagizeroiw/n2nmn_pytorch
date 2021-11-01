python train_model/train_clevr_gt_layout.py \
    --gpu_id 2 \
    --exp_name fs_test \
    --model_type scratch \
    --data_dir ../n2nmn/n2nmn/exp_clevr/data \
    --image_feat_dir ../n2nmn/n2nmn/exp_clevr/data/vgg_pool5/train \
    --out_dir ./output
