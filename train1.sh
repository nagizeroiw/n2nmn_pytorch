python train_model/train_clevr_gt_layout.py \
    --gpu_id 1 \
    --exp_name gt_test \
    --model_type gt_layout \
    --data_dir ./data/data \
    --image_feat_dir ./data/data/vgg_pool5/train \
    --out_dir ./output
