ori_name=news_transfer3
tar_test=test3

mkdir ${tar_test}
mkdir ${tar_test}/auto_encoder
mkdir ${tar_test}/auto_encoder1
mkdir ${tar_test}/auto_encoder2


cp ../model/data/q_test.txt ${tar_test}/
cp ../model/data/s_test.txt ${tar_test}/

cp ../model/${ori_name}/session_auto_encoder/q_test_style.txt ${tar_test}/auto_encoder/style0.txt
cp ../model/${ori_name}/session_auto_encoder/q_test_style.txt ${tar_test}/auto_encoder/style1.txt

cp ../model/${ori_name}/session_auto_encoder1/q_test_style.txt ${tar_test}/auto_encoder1/style0.txt
cp ../model/${ori_name}/session_auto_encoder1/q_test_style.txt ${tar_test}/auto_encoder1/style1.txt

cp ../model/${ori_name}/session_auto_encoder2/q_test_style.txt ${tar_test}/auto_encoder2/style0.txt
cp ../model/${ori_name}/session_auto_encoder2/q_test_style.txt ${tar_test}/auto_encoder2/style1.txt

