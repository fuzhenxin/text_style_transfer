ori_name=news_transfer2
tar_test=test2

mkdir ${tar_test}
mkdir ${tar_test}/multi_decoder
mkdir ${tar_test}/multi_decoder1
mkdir ${tar_test}/multi_decoder2




cp ../model/data/q_test.txt ${tar_test}/
cp ../model/data/s_test.txt ${tar_test}/

cp ../model/${ori_name}/session_multi_decoder/q_test_style.txt ${tar_test}/multi_decoder/style0.txt
cp ../model/${ori_name}/session_multi_decoder/q_test_style1.txt ${tar_test}/multi_decoder/style1.txt

cp ../model/${ori_name}/session_multi_decoder1/q_test_style.txt ${tar_test}/multi_decoder1/style0.txt
cp ../model/${ori_name}/session_multi_decoder1/q_test_style1.txt ${tar_test}/multi_decoder1/style1.txt

cp ../model/${ori_name}/session_multi_decoder2/q_test_style.txt ${tar_test}/multi_decoder2/style0.txt
cp ../model/${ori_name}/session_multi_decoder2/q_test_style1.txt ${tar_test}/multi_decoder2/style1.txt

