import sys
import os

from eval_model.layout_evaluator import run_eval

exp_name = 'gt_test'
dataSplitSet = 'val'
out_file = "./layout_learning_on_eval_dataset.txt"

eval_results = []

with open(out_file, 'w') as f:
    for i_iter in range(1,9):
        snapshot_name = '000%d0000' % i_iter
        snapshot_file = './output/tfmodel/%s/model_%s' % (exp_name, snapshot_name)
        if os.path.exists(snapshot_file):
            # def run_eval(exp_name, snapshot_name, tst_image_set, data_dir, image_feat_dir, tf_model_dir,print_log = False):

            # return layout_accuracy, layout_correct_total, num_questions_total, answer_accuracy
            layout_accuracy, layout_correct_total, num_questions_total, answer_accuracy = run_eval(exp_name, snapshot_name, dataSplitSet,
                './data/data', './data/data/vgg_pool5', './output/tfmodel')
            # eval_results.append((i_iter,accuracy,total))
            print("[eval] iter:", i_iter,"\tlayout_accuracy:", layout_accuracy, "\tcorrect_total:", layout_correct_total, "\tnum_questions_total", num_questions_total, "\tanswer_accuracy", answer_accuracy)
            # sys.stdout.flush()
            f.write(' '.join(["iter:", str(i_iter),"\tlayout_accuracy:", str(layout_accuracy), "\tcorrect_total:", str(layout_correct_total), "\tnum_questions_total", str(num_questions_total), "\tanswer_accuracy", str(answer_accuracy)]) + '\n')
