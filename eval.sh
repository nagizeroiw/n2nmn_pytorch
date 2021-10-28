python eval_model/eval_layout_accuracy.py \
    --gpu_id 2 \
    --exp_name gt_rl_test \
    --snapshot_name 00080000 \
    --test_split val \
    --data_dir ./data/data \
    --image_dir ./data/data/vgg_pool5 \
    --model_dir ./output/tfmodel
