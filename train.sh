python train_model/train_clevr_gt_layout.py \
    --gpu_id 2 \
    --exp_name fs_test \
    --model_type scratch \
    --data_dir ./data/data \
    --image_feat_dir ./data/data/vgg_pool5/train \
    --out_dir ./output
